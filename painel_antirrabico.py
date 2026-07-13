import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página para modo amplo
st.set_page_config(page_title="Painel Antirrábico - Busca Ativa", layout="wide")

# =========================================================================
# 1. SISTEMA DE LOGIN E SEGURANÇA
# =========================================================================
def sistema_login():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        st.markdown("<h2 style='text-align: center; color: #2E5B88;'>Vigilância Epidemiológica - Distrito VII</h2>", unsafe_allow_html=True)
        
        col_login, _ = st.columns([1, 2])
        with col_login:
            st.subheader("🔑 Acesso Restrito ao Painel")
            usuario = st.text_input("Usuário (E-mail)")
            senha = st.text_input("Senha", type="password")
            
            if st.button("Entrar no Painel"):
                if usuario == "vigilancia.ds7@recife.pe.gov.br" and senha == "Antirrabica2026":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos!")
        return False
    return True

# Executa a verificação de segurança
if sistema_login():

    # =========================================================================
    # 2. CARREGAMENTO E TRATAMENTO DOS DADOS DO SINAN
    # =========================================================================
    @st.cache_data
    def carregar_dados_sinan():
        df = pd.read_excel('Banco_Dados_Antirrabica.xlsx')
        
        # Limpando as siglas oficiais do SUS
        df.columns = [col.split(',')[0] for col in df.columns]
        
        # Formatando os telefones para facilitar a leitura visual
        df['NU_TELEFON'] = df['NU_TELEFON'].fillna('Não Cadastrado').astype(str).apply(
            lambda x: f"(81) {x[:-4]}-{x[-4:]}" if x.isdigit() and len(x) >= 8 else x
        )
        
        # Tratando endereços e numeração vazia
        df['NM_LOGRADO'] = df['NM_LOGRADO'].fillna('Sem Logradouro Informado').str.upper()
        df['NU_NUMERO'] = df['NU_NUMERO'].fillna('S/N').astype(str)
        df['NM_BAIRRO'] = df['NM_BAIRRO'].fillna('Bairro Não Informado').str.upper()
        
        # Mapeamento do tipo de animal agressor
        mapa_animais = {1: 'Cão', 2: 'Gato', 3: 'Bovino', 4: 'Eqüino', 5: 'Ovino/Caprino', 6: 'Morcego', 7: 'Outros'}
        df['ANIMAL_DESC'] = df['ANIMAL'].map(mapa_animais).fillna('Não Informado')
        
        return df

    df_completo = carregar_dados_sinan()

    # =========================================================================
    # 3. BARRA LATERAL - FILTROS POR UNIDADE E ANO
    # =========================================================================
    st.sidebar.markdown("<h2 style='color: #2E5B88;'>Filtros Epidemiológicos</h2>", unsafe_allow_html=True)
    
    lista_unidades = sorted(list(df_completo['ID_UNIDADE'].dropna().unique()))
    unidade_selecionada = st.sidebar.selectbox("🏥 Selecione a Unidade de Saúde (ID_UNIDADE)", lista_unidades)
    
    lista_anos = sorted(list(df_completo['NU_ANO'].unique()), reverse=True)
    ano_selecionado = st.sidebar.selectbox("📅 Selecione o Ano", lista_anos)

    df_filtrado = df_completo[(df_completo['ID_UNIDADE'] == unidade_selecionada) & (df_completo['NU_ANO'] == ano_selecionado)]

    # =========================================================================
    # 4. PAINEL PRINCIPAL
    # =========================================================================
    st.markdown(f"<h1 style='color: #1E3A5F;'>📊 Monitoramento Antirrábico - Unidade: {unidade_selecionada}</h1>", unsafe_allow_html=True)
    st.markdown(f"**Status:** Exibindo {len(df_filtrado)} notificações registradas no ano de {ano_selecionado}.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total de Casos na Unidade", len(df_filtrado))
    c2.metric("Casos por Cães", len(df_filtrado[df_filtrado['ANIMAL_DESC'] == 'Cão']))
    c3.metric("Casos por Gatos", len(df_filtrado[df_filtrado['ANIMAL_DESC'] == 'Gato']))
    bairro_top = df_filtrado['NM_BAIRRO'].value_counts().index[0] if not df_filtrado.empty else "Nenhum"
    c4.metric("Foco de Maior Incidência", bairro_top)

    st.write("---")

    # =========================================================================
    # 5. 🎯 CENTRAL DE BUSCA ATIVA INTELEGENTE
    # =========================================================================
    st.markdown("<h3 style='color: #D9534F;'>📞 Central de Busca Ativa - Lista de Pacientes para Contato Obrigatório</h3>", unsafe_allow_html=True)
    st.markdown("Use o campo abaixo para localizar o paciente digitando o **Nome** ou o **Número da Notificação (SINAN)**.")

    termo_busca = st.text_input("🔍 Digite o Nome do Paciente ou o Número do SINAN:")
    
    df_busca_ativa = df_filtrado[[
        'NU_NOTIFIC', 'NM_PACIENT', 'NU_TELEFON', 'NM_LOGRADO', 'NU_NUMERO', 'NM_BAIRRO', 'DT_NOTIFIC', 'ANIMAL_DESC'
    ]].rename(columns={
        'NU_NOTIFIC': 'Nº SINAN / Notificação',
        'NM_PACIENT': 'Nome do Paciente',
        'NU_TELEFON': 'Telefone de Contato',
        'NM_LOGRADO': 'Endereço / Rua',
        'NU_NUMERO': 'Número',
        'NM_BAIRRO': 'Bairro',
        'DT_NOTIFIC': 'Data Notificação',
        'ANIMAL_DESC': 'Animal Agressor'
    })

    if termo_busca:
        condicao_nome = df_busca_ativa['Nome do Paciente'].str.contains(termo_busca, case=False, na=False)
        condicao_sinan = df_busca_ativa['Nº SINAN / Notificação'].astype(str).str.contains(termo_busca, na=False)
        df_busca_ativa = df_busca_ativa[condicao_nome | condicao_sinan]

    st.dataframe(df_busca_ativa, use_container_width=True, hide_index=True)

    st.write("---")

    # =========================================================================
    # 6. RELATÓRIOS E GRÁFICOS
    # =========================================================================
    st.markdown("### 📈 Perfil Epidemiológico da Unidade Selecionada")
    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.markdown("**Casos por Bairro de Residência**")
        if not df_filtrado.empty:
            df_bairros_unidade = df_filtrado['NM_BAIRRO'].value_counts().head(5).reset_index()
            fig_b_unidade = px.bar(df_bairros_unidade, x='count', y='NM_BAIRRO', orientation='h',
                                   labels={'count': 'Nº de Casos', 'NM_BAIRRO': 'Bairro'},
                                   color='count', color_continuous_scale='Blues')
            st.plotly_chart(fig_b_unidade, use_container_width=True)
        else:
            st.info("Sem dados suficientes para este período.")

    with col_g2:
        st.markdown("**Distribuição por Sexo dos Pacientes**")
        if not df_filtrado.empty:
            fig_sexo = px.pie(df_filtrado, names='CS_SEXO', hole=0.4, color_discrete_sequence=px.colors.qualitative.Safe)
            st.plotly_chart(fig_sexo, use_container_width=True)
        else:
            st.info("Sem dados suficientes para este período.")