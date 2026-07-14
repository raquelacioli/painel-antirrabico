import base64
import io
import os
import urllib.parse
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv

# Configuração da página DEVE ser o primeiro comando Streamlit executado
st.set_page_config(page_title="Painel Antirrábico - Busca Ativa", layout="wide")

# Carrega variáveis de ambiente a partir de um arquivo .env local
load_dotenv()

# 1. Primeiro, tenta carregar do arquivo .env local
VALID_USER = os.getenv("PANEL_USER")
VALID_PASS = os.getenv("PANEL_PASS")

# 2. Se não encontrar no .env, busca no st.secrets
if not VALID_USER or not VALID_PASS:
    try:
        if hasattr(st, "secrets") and len(st.secrets) > 0:
            VALID_USER = st.secrets.get("PANEL_USER")
            VALID_PASS = st.secrets.get("PANEL_PASS")
    except Exception:
        pass

# 3. Fallback definitivo se nada acima estiver configurado
if not VALID_USER or not VALID_PASS:
    VALID_USER = "vigilanciaepidemiologicadsvii@gmail.com"
    VALID_PASS = "antirrabica"
    USE_FALLBACK_CREDENTIALS = True
else:
    USE_FALLBACK_CREDENTIALS = False


def get_login_background_base64():
    root = Path(__file__).parent
    image_names = [
        "Painel VigiRaiva DSVII – Fundo.png",
        "Painel VigiRaiva DSVII - Fundo.png",
        "vagiraiva_dsvii_bg.png",
        "vagiraiva_dsvii_bg.jpg",
        "vagiraiva_dsvii_bg.jpeg",
        "vagiraiva_dsvii_fundo.png",
        "vagiraiva_dsvii_fundo.jpg",
        "vagiraiva_dsvii_fundo.jpeg",
        "vigi_raiva_dsvii.png",
        "vigi_raiva_dsvii.jpg",
        "vigi_raiva_dsvii.jpeg"
    ]
    for name in image_names:
        path = root / name
        if path.exists():
            suffix = path.suffix.lower()
            mime_type = "image/png" if suffix == ".png" else "image/jpeg"
            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
                return f"data:{mime_type};base64,{encoded}"
    return None


def set_login_background():
    img_b64 = get_login_background_base64()
    if img_b64:
        st.markdown(
            """
            <style>
            /* Oculta o cabeçalho padrão e a faixa branca do Streamlit */
            header {
                visibility: hidden !important;
                height: 0px !important;
            }
            .stAppDeployButton {
                display: none !important;
            }
            
            /* Plano de fundo com a imagem e overlay escuro */
            .stApp {
                background-image: url('""" + img_b64 + """');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            .stApp::before {
                content: "";
                position: fixed;
                inset: 0;
                background: rgba(10, 25, 47, 0.55); /* Escurece um pouco mais para dar leitura aos textos */
                z-index: 0;
            }
            
            /* Centraliza e estiliza os blocos de texto e inputs */
            [data-testid="stHeader"] {
                background: transparent;
            }
            
            /* Estilização dos inputs para ficarem bonitos e legíveis sobre o fundo escuro */
            .stTextInput>div>div>input {
                border-radius: 12px !important;
                background-color: rgba(255, 255, 255, 0.9) !important;
                color: #1E3A5F !important;
                font-weight: 500;
            }
            .stTextInput>div>label {
                color: #FFFFFF !important;
                font-weight: 600 !important;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
            }
            
            /* Estilização do Botão de Entrar */
            .stButton>button {
                width: 100% !important;
                border-radius: 12px !important;
                background-color: #1E3A5F !important;
                color: white !important;
                font-weight: bold !important;
                border: none !important;
                padding: 0.75rem 1rem !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
                transition: background-color 0.3s;
            }
            .stButton>button:hover {
                background-color: #2E5B88 !important;
                color: white !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            header {
                visibility: hidden !important;
                height: 0px !important;
            }
            .stAppDeployButton {
                display: none !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )


# =========================================================================
# 1. SISTEMA DE LOGIN E SEGURANÇA (SEM DIVS QUE QUEBRAM O LAYOUT)
# =========================================================================
def sistema_login():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        set_login_background()
        
        # Estrutura de colunas invisível apenas para centralizar o formulário na tela
        col_esq, col_centro, col_dir = st.columns([1, 2, 1])
        
        with col_centro:
            # Espaçador para empurrar o conteúdo um pouco para baixo
            st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
            
            # Títulos principais com sombra no texto para leitura perfeita no fundo
            st.markdown("<h1 style='text-align: center; color: #FFFFFF; font-weight: 800; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); margin-bottom: 5px;'>Painel Antirrábico</h1>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: #E0E0E0; font-weight: 500; text-shadow: 1px 1px 3px rgba(0,0,0,0.8); margin-top: 0; margin-bottom: 5px;'>Busca Ativa</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #D1D5DB; margin-top: 0; margin-bottom: 30px; font-size: 1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);'>Vigilância Epidemiológica — Distrito VII</p>", unsafe_allow_html=True)
            
            st.markdown("<h4 style='text-align: center; margin-top: 0; margin-bottom: 20px; color: #F3F4F6; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);'>🔑 Acesso Restrito</h4>", unsafe_allow_html=True)
            
            usuario = st.text_input("Usuário (E-mail)", key="input_user")
            senha = st.text_input("Senha", type="password", key="input_pass")
            
            if not VALID_USER or not VALID_PASS:
                st.warning("As credenciais não estão definidas no arquivo .env.")
            
            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
            
            if st.button("Entrar no Painel"):
                if usuario == VALID_USER and senha == VALID_PASS:
                    st.session_state["autenticado"] = True
                    try:
                        st.rerun()
                    except AttributeError:
                        st.experimental_rerun()
                else:
                    st.error("Usuário ou senha incorretos!")
            
            # Créditos no rodapé da página de login
            st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 0.85rem; margin-top: 40px; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);'>Produzido por Raquel Acioli</p>", unsafe_allow_html=True)
                    
        return False
    return True
# =========================================================================
# EXECUÇÃO DO APLICATIVO
# =========================================================================
if sistema_login():

    # =========================================================================
    # 2. CARREGAMENTO E TRATAMENTO DOS DADOS DO SINAN
    # =========================================================================
    @st.cache_data
    def carregar_dados_sinan(file_bytes):
        df = pd.read_excel(io.BytesIO(file_bytes))
        
        df.columns = [col.split(',')[0] for col in df.columns]
        
        df['NU_TELEFON'] = df['NU_TELEFON'].fillna('Não Cadastrado').astype(str).apply(
            lambda x: f"(81) {x[:-4]}-{x[-4:]}" if x.isdigit() and len(x) >= 8 else x
        )
        
        df['NM_LOGRADO'] = df['NM_LOGRADO'].fillna('Sem Logradouro Informado').str.upper()
        df['NU_NUMERO'] = df['NU_NUMERO'].fillna('S/N').astype(str)
        df['NM_BAIRRO'] = df['NM_BAIRRO'].fillna('Bairro Não Informado').str.upper()
        
        mapa_animais = {1: 'Cão', 2: 'Gato', 3: 'Bovino', 4: 'Eqüino', 5: 'Ovino/Caprino', 6: 'Morcego', 7: 'Outros'}
        df['ANIMAL_DESC'] = df['ANIMAL'].map(mapa_animais).fillna('Não Informado')
        
        return df

    st.sidebar.markdown("<h2 style='color: #2E5B88;'>Dados</h2>", unsafe_allow_html=True)
    arquivo_enviado = st.sidebar.file_uploader("Upload do Banco de Dados (Excel)", type=['xlsx'])
    if arquivo_enviado is None:
        st.sidebar.warning("Faça upload do arquivo Excel para carregar os dados.")
        st.stop()

    # Passamos os bytes para a função cacheada
    file_bytes = arquivo_enviado.getvalue()
    st.sidebar.success("Arquivo carregado com sucesso. O painel será atualizado.")

    try:
        df_completo = carregar_dados_sinan(file_bytes)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        st.stop()

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
    
    # Tratamento seguro para evitar quebras se a contagem estiver zerada
    bairros_counts = df_filtrado['NM_BAIRRO'].value_counts()
    bairro_top = bairros_counts.index[0] if not bairros_counts.empty else "Nenhum"
    c4.metric("Foco de Maior Incidência", bairro_top)

    st.write("---")

    # =========================================================================
    # 5. 🎯 CENTRAL DE BUSCA ATIVA INTELIGENTE
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

    if not df_busca_ativa.empty:
        paciente_selecionado = st.selectbox(
            "🔎 Selecione o paciente para ver o endereço no mapa:",
            df_busca_ativa['Nome do Paciente'].unique()
        )
        endereco = df_busca_ativa.loc[df_busca_ativa['Nome do Paciente'] == paciente_selecionado].iloc[0]
        endereco_completo = f"{endereco['Endereço / Rua']}, {endereco['Número']}, {endereco['Bairro']}, Recife, PE, Brasil"
        endereco_query = urllib.parse.quote_plus(endereco_completo)
        mapa_embed = f"https://maps.google.com/maps?q={endereco_query}&t=&z=15&ie=UTF8&iwloc=&output=embed"

        st.markdown(f"**Endereço selecionado:** {endereco_completo}")
        st.markdown(f"[Abrir no Google Maps](https://www.google.com/maps/search/?api=1&query={endereco_query})")
        st.components.v1.html(
            f'<iframe src="{mapa_embed}" width="100%" height="450" style="border:0;"></iframe>',
            height=470,
            scrolling=False,
        )

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
            # Força o nome das colunas para evitar incompatibilidade entre versões antigas e novas do pandas
            df_bairros_unidade.columns = ['Bairro', 'Casos']
            fig_b_unidade = px.bar(df_bairros_unidade, x='Casos', y='Bairro', orientation='h',
                                   labels={'Casos': 'Nº de Casos', 'Bairro': 'Bairro'},
                                   color='Casos', color_continuous_scale='Blues')
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