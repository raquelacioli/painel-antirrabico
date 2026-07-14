import base64
import io
import os
import urllib.parse
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv


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


def get_login_logo_base64():
    root = Path(__file__).parent
    logo_names = [
        "logo.png",
        "logo.jpg",
        "logo.jpeg",
        "vagiraiva_logo.png",
        "vagiraiva_logo.jpg",
        "vagiraiva_logo.jpeg",
        "logo_vagi_raiva.png",
        "logo_vagi_raiva.jpg",
        "logo_vagi_raiva.jpeg",
        "logo.svg",
        "vagiraiva_logo.svg",
        "logo_vagi_raiva.svg"
    ]
    for name in logo_names:
        path = root / name
        if path.exists():
            suffix = path.suffix.lower()
            if suffix == ".svg":
                mime_type = "image/svg+xml"
            elif suffix == ".png":
                mime_type = "image/png"
            else:
                mime_type = "image/jpeg"
            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
                return f"data:{mime_type};base64,{encoded}"
    return None


def get_login_brand_html():
    return "<div class='brand-logo'>DSVII</div>"


def set_login_background():
    img_b64 = get_login_background_base64()
    if img_b64:
        st.markdown(
            """
            <style>
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
                background: rgba(10, 25, 47, 0.44);
                z-index: 0;
            }
            .login-box {
                position: relative;
                z-index: 1;
                background: rgba(255, 255, 255, 0.94);
                padding: 32px 36px;
                border-radius: 28px;
                box-shadow: 0 28px 80px rgba(0, 0, 0, 0.16);
                max-width: 620px;
                width: min(95%, 620px);
                margin: 72px auto 48px auto;
                border: 1px solid rgba(255, 255, 255, 0.72);
                backdrop-filter: blur(16px);
            }
            .login-box .brand-header {
                display: flex;
                align-items: center;
                gap: 16px;
                margin-bottom: 18px;
                justify-content: center;
            }
            .login-box .stTextInput,
            .login-box .stButton {
                width: 100% !important;
                max-width: 560px;
                margin: 0 auto;
            }
            @media screen and (max-width: 768px) {
                .login-box {
                    padding: 24px 20px;
                    margin: 42px auto 32px auto;
                }
                .login-box .brand-header {
                    flex-direction: column;
                    align-items: center;
                }
                .login-box .brand-logo, .login-box .brand-logo-img {
                    width: 48px;
                    height: 48px;
                }
                .login-box h2 {
                    font-size: 1.75rem;
                }
                .login-box .stButton button {
                    font-size: 0.95rem;
                }
            }
            .login-box .brand-logo, .login-box .brand-logo-img {
                width: 56px;
                height: 56px;
                border-radius: 18px;
                display: grid;
                place-items: center;
                font-weight: 700;
                font-size: 1.15rem;
                letter-spacing: 0.08em;
            }
            .login-box .brand-logo {
                background: #2E5B88;
                color: white;
            }
            .login-box .brand-logo-img {
                object-fit: contain;
                background: white;
                padding: 6px;
                border: 1px solid rgba(46, 91, 136, 0.18);
            }
            .login-box .brand-text {
                line-height: 1.2;
            }
            .login-box .brand-text strong {
                display: block;
                color: #1E3A5F;
                font-size: 1rem;
            }
            .login-box .brand-text span {
                color: #4a4a4a;
                font-size: 0.94rem;
            }
            .login-box h2 {
                margin-bottom: 8px;
                font-size: 2.1rem;
                letter-spacing: 0.04em;
            }
            .login-box .stButton button {
                width: 100%;
                padding: 0.95rem 1rem;
                font-size: 1rem;
            }
            .login-box .stTextInput>div>div>input {
                border-radius: 12px;
            }
            .login-box .stTextInput>div>label {
                font-weight: 600;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            .login-box {
                position: relative;
                z-index: 1;
                background: rgba(255, 255, 255, 0.96);
                padding: 32px 36px;
                border-radius: 28px;
                box-shadow: 0 28px 80px rgba(0, 0, 0, 0.16);
                max-width: 620px;
                width: min(95%, 620px);
                margin: 72px auto 48px auto;
                border: 1px solid rgba(230, 230, 230, 0.9);
                backdrop-filter: blur(16px);
            }
            .login-box .brand-header {
                display: flex;
                align-items: center;
                gap: 16px;
                margin-bottom: 18px;
                justify-content: center;
            }
            .login-box .stTextInput,
            .login-box .stButton {
                width: 100% !important;
                max-width: 560px;
                margin: 0 auto;
            }
            @media screen and (max-width: 768px) {
                .login-box {
                    padding: 24px 20px;
                    margin: 42px auto 32px auto;
                }
                .login-box .brand-header {
                    flex-direction: column;
                    align-items: center;
                }
                .login-box .brand-logo {
                    width: 48px;
                    height: 48px;
                }
                .login-box h2 {
                    font-size: 1.75rem;
                }
                .login-box .stButton button {
                    font-size: 0.95rem;
                }
            }
            .login-box .brand-logo {
                width: 56px;
                height: 56px;
                border-radius: 18px;
                background: #2E5B88;
                color: white;
                display: grid;
                place-items: center;
                font-weight: 700;
                font-size: 1.15rem;
                letter-spacing: 0.08em;
            }
            .login-box .brand-text {
                line-height: 1.2;
            }
            .login-box .brand-text strong {
                display: block;
                color: #1E3A5F;
                font-size: 1rem;
            }
            .login-box .brand-text span {
                color: #4a4a4a;
                font-size: 0.94rem;
            }
            .login-box h2 {
                margin-bottom: 8px;
                font-size: 2.1rem;
                letter-spacing: 0.04em;
            }
            .login-box .stButton button {
                width: 100%;
                padding: 0.95rem 1rem;
                font-size: 1rem;
            }
            .login-box .stTextInput>div>div>input {
                border-radius: 12px;
            }
            .login-box .stTextInput>div>label {
                font-weight: 600;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Carrega variáveis de ambiente a partir de um arquivo .env local
load_dotenv()

# 1. Primeiro, tenta carregar do arquivo .env local (evita que o Streamlit quebre na sua máquina)
VALID_USER = os.getenv("PANEL_USER")
VALID_PASS = os.getenv("PANEL_PASS")

# 2. Se não encontrar no .env (como no servidor de produção online), tenta buscar no st.secrets com tratamento de erro
if not VALID_USER or not VALID_PASS:
    try:
        if hasattr(st, "secrets") and len(st.secrets) > 0:
            VALID_USER = st.secrets.get("PANEL_USER")
            VALID_PASS = st.secrets.get("PANEL_PASS")
    except Exception:
        # Se der erro de "secrets não encontrado", simplesmente ignora para rodar o fallback abaixo
        pass

# 3. Fallback definitivo se nada acima estiver configurado
if not VALID_USER or not VALID_PASS:
    VALID_USER = "vigilanciaepidemiologicadsvii@gmail.com"
    VALID_PASS = "antirrabica"
    USE_FALLBACK_CREDENTIALS = True
else:
    USE_FALLBACK_CREDENTIALS = False

# =========================================================================
# 1. SISTEMA DE LOGIN E SEGURANÇA
# =========================================================================
def sistema_login():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        set_login_background()
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        st.markdown(
            "<div class='brand-header'>"
            f"{get_login_brand_html()}"
            "<div class='brand-text'><strong>Vigilância Epidemiológica</strong><span>Distrito VII</span></div>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown("<h2 style='text-align: center; color: #2E5B88; margin-bottom: 6px;'>Painel Antirrábico - Busca Ativa</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #4a4a4a; margin-top: 0; margin-bottom: 22px; font-size: 1rem;'>Acesso restrito ao painel de vigilância antirrábica</p>", unsafe_allow_html=True)
        
        col1, col_login, col2 = st.columns([1, 2, 1])
        with col_login:
            st.subheader("🔑 Acesso Restrito ao Painel")
            usuario = st.text_input("Usuário (E-mail)")
            senha = st.text_input("Senha", type="password")
            
            if not VALID_USER or not VALID_PASS:
                st.warning("As credenciais não estão definidas. Crie um arquivo .env com PANEL_USER e PANEL_PASS.")

            if st.button("Entrar no Painel"):
                if usuario == VALID_USER and senha == VALID_PASS:
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos!")
        st.markdown("</div>", unsafe_allow_html=True)
        return False
    return True

# Executa a verificação de segurança
if sistema_login():

    # =========================================================================
    # 2. CARREGAMENTO E TRATAMENTO DOS DADOS DO SINAN
    # =========================================================================
    @st.cache_data
    def carregar_dados_sinan(file_bytes):
        df = pd.read_excel(io.BytesIO(file_bytes))
        
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

    st.sidebar.markdown("<h2 style='color: #2E5B88;'>Dados</h2>", unsafe_allow_html=True)
    arquivo_enviado = st.sidebar.file_uploader("Upload do Banco de Dados (Excel)", type=['xlsx'])
    if arquivo_enviado is None:
        st.sidebar.warning("Faça upload do arquivo Excel para carregar os dados.")
        st.stop()

    file_bytes = arquivo_enviado.read()
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