# -*- coding: utf-8 -*-
"""
Estilos e Identidade Visual Sacra & Franciscana
Cores litúrgicas, tipografia clássica e ornamentos reverentes
"""

SACRED_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --sacro-ouro: #C5A059;
    --sacro-ouro-claro: #E6CA85;
    --sacro-bordo: #781826;
    --sacro-bordo-escuro: #4E0D16;
    --sacro-franciscano: #5A3825;
    --sacro-marfim: #FAF8F5;
    --sacro-pergaminho: #F3ECE2;
    --sacro-texto: #242120;
    --sacro-cinza-suave: #ECE7E0;
    --sacro-borda: #D8C8B4;
}

/* Tipografia e Base */
html, body, [class*="css"] {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 18px;
    color: var(--sacro-texto);
}

h1, h2, h3, .sacro-title {
    font-family: 'Cinzel', serif !important;
    letter-spacing: 0.5px;
    font-weight: 700;
}

/* Cabeçalho Paroquial Sacro */
.parish-header {
    background: linear-gradient(135deg, #4E0D16 0%, #781826 60%, #5A3825 100%);
    color: #FAF8F5;
    padding: 2.2rem 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    border: 2px solid #C5A059;
    box-shadow: 0 10px 25px rgba(78, 13, 22, 0.25);
    text-align: center;
    position: relative;
}

.parish-header h1 {
    color: #F8E7BE !important;
    margin-bottom: 0.3rem;
    font-size: 2.3rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.parish-header .subtitulo {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.25rem;
    color: #E6CA85;
    letter-spacing: 1px;
}

.parish-header .tau-badge {
    display: inline-block;
    background: rgba(197, 160, 89, 0.25);
    border: 1px solid #C5A059;
    color: #F8E7BE;
    padding: 0.25rem 0.9rem;
    border-radius: 20px;
    font-family: 'Cinzel', serif;
    font-size: 0.9rem;
    margin-top: 0.6rem;
    letter-spacing: 2px;
}

/* Divisor Sacro */
.sacro-divider {
    display: flex;
    align-items: center;
    text-align: center;
    margin: 1.5rem 0;
    color: #C5A059;
}
.sacro-divider::before, .sacro-divider::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #D8C8B4;
}
.sacro-divider span {
    padding: 0 15px;
    font-size: 1.2rem;
    font-family: 'Cinzel', serif;
    color: #781826;
}

/* Cards em estilo Pergaminho */
.pergaminho-card {
    background: #FAF8F5;
    background-image: radial-gradient(#F3ECE2 1px, transparent 0);
    background-size: 24px 24px;
    border: 1px solid #D8C8B4;
    border-left: 5px solid #C5A059;
    border-radius: 8px;
    padding: 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}

.pergaminho-card-bordo {
    background: #FAF8F5;
    border: 1px solid #D8C8B4;
    border-left: 5px solid #781826;
    border-radius: 8px;
    padding: 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}

.pergaminho-card-franciscano {
    background: #F8F5F0;
    border: 1px solid #D8C8B4;
    border-left: 5px solid #5A3825;
    border-radius: 8px;
    padding: 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}

/* Citação Bíblica e Magistério */
.citacao-biblica {
    background: #F5EFEB;
    border-left: 4px solid #781826;
    padding: 1rem 1.4rem;
    font-style: italic;
    font-size: 1.15rem;
    color: #382418;
    margin: 1rem 0;
    border-radius: 0 8px 8px 0;
}
.citacao-biblica .referencia {
    display: block;
    text-align: right;
    font-style: normal;
    font-weight: 600;
    font-family: 'Cinzel', serif;
    color: #781826;
    margin-top: 0.5rem;
    font-size: 0.95rem;
}

/* Pílula Franciscana */
.pilula-franciscana {
    background: linear-gradient(135deg, #F9F5F0 0%, #EDE4D8 100%);
    border: 1px solid #C5A059;
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    margin: 1.2rem 0;
    position: relative;
}
.pilula-franciscana h4 {
    font-family: 'Cinzel', serif;
    color: #5A3825;
    margin-top: 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Badges Sacramentais */
.badge-sacramento-ok {
    background-color: #E2F0D9;
    color: #385723;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.85rem;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    border: 1px solid #A9D18E;
}
.badge-sacramento-pendente {
    background-color: #FCE4D6;
    color: #C65911;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.85rem;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    border: 1px solid #F4B084;
}

/* ==========================================================================
   Template Sacro para Botões (Área Principal)
   ========================================================================== */

/* Botões Padrão (Secundários / Navegação) */
.stButton > button {
    font-family: 'Cinzel', serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    background: #FFFFFF !important;
    color: #781826 !important;
    border: 1.5px solid #D8C8B4 !important;
    border-radius: 8px !important;
    padding: 0.55rem 1.3rem !important;
    box-shadow: 0 2px 6px rgba(90, 56, 37, 0.04) !important;
    transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.stButton > button:hover {
    background: #FAF2EB !important;
    border-color: #781826 !important;
    color: #781826 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 14px rgba(120, 24, 38, 0.18) !important;
}

/* Botões Primários (Ações Sagradas / Salvar / Concluir) */
.stButton > button[kind="primary"],
button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #781826 0%, #5A111C 100%) !important;
    color: #FAF8F5 !important;
    border: 1.5px solid #C5A059 !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    padding: 0.6rem 1.4rem !important;
    box-shadow: 0 4px 14px rgba(120, 24, 38, 0.28) !important;
}

.stButton > button[kind="primary"]:hover,
button[data-testid="baseButton-primary"]:hover {
    background: linear-gradient(135deg, #911F30 0%, #6E1623 100%) !important;
    border-color: #E6CA85 !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 18px rgba(120, 24, 38, 0.4) !important;
}

/* Botões de Download (CSV / Certificados) */
.stDownloadButton > button {
    background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%) !important;
    color: #FFFFFF !important;
    border: 1.5px solid #81C784 !important;
    border-radius: 8px !important;
    font-family: 'Cinzel', serif !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.3rem !important;
    box-shadow: 0 3px 10px rgba(46, 125, 50, 0.25) !important;
    transition: all 0.22s ease !important;
}

.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #388E3C 0%, #2E7D32 100%) !important;
    border-color: #A5D6A7 !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 16px rgba(46, 125, 50, 0.35) !important;
}

/* Botões de Link Externo */
.stLinkButton > a {
    background: #FFFFFF !important;
    color: #5A3825 !important;
    border: 1.5px solid #C5A059 !important;
    border-radius: 8px !important;
    font-family: 'Cinzel', serif !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.3rem !important;
    box-shadow: 0 2px 6px rgba(197, 160, 89, 0.1) !important;
    transition: all 0.2s ease !important;
}

.stLinkButton > a:hover {
    background: #FAF2EB !important;
    border-color: #781826 !important;
    color: #781826 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 12px rgba(120, 24, 38, 0.15) !important;
}

/* Campos de Formulário no Conteúdo Principal */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    border-radius: 8px !important;
    border: 1px solid #D8C8B4 !important;
    background: #FFFFFF !important;
    transition: all 0.2s ease !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #781826 !important;
    box-shadow: 0 0 0 2px rgba(120, 24, 38, 0.15) !important;
}

/* ==========================================================================
   Sidebar Customizada - Template Sacro & Espaçoso
   ========================================================================== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FBF9F5 0%, #F4EFE6 100%) !important;
    border-right: 1px solid #E2D7C7 !important;
    box-shadow: 2px 0 12px rgba(90, 56, 37, 0.05) !important;
}

[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    padding: 1.4rem 1.1rem 2rem 1.1rem !important;
}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: #781826 !important;
}

/* Espaçamento e Estilo do Seletor de Pilar (Selectbox) */
[data-testid="stSidebar"] [data-testid="stSelectbox"] {
    margin-bottom: 0.5rem !important;
}

[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div {
    background-color: #FFFFFF !important;
    border: 1px solid #D8C8B4 !important;
    border-radius: 8px !important;
    font-family: 'Cinzel', serif !important;
    font-weight: 600 !important;
    color: #781826 !important;
    padding: 2px 4px !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02) !important;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div:hover {
    border-color: #C5A059 !important;
    box-shadow: 0 2px 8px rgba(197, 160, 89, 0.15) !important;
}

/* ==========================================================================
   Itens do Menu Lateral (Cards de Navegação Interativos)
   ========================================================================== */
[data-testid="stSidebar"] [data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    margin-top: 4px !important;
}

/* Cada opção do menu como um Card Elegante */
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background-color: #FFFFFF !important;
    border: 1px solid #E2D7C7 !important;
    border-left: 4px solid #C5A059 !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    margin: 0 !important;
    cursor: pointer !important;
    transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1) !important;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    box-shadow: 0 2px 5px rgba(90, 56, 37, 0.03) !important;
}

/* Efeito Hover nos Cards do Menu */
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background-color: #FAF5EB !important;
    border-color: #C5A059 !important;
    border-left: 4px solid #781826 !important;
    transform: translateX(4px) !important;
    box-shadow: 0 4px 10px rgba(197, 160, 89, 0.18) !important;
}

/* Ocultar o círculo de rádio padrão para visual moderno de Menu de App */
[data-testid="stSidebar"] [data-testid="stRadio"] label > div:first-child {
    display: none !important;
}

/* Tipografia dos Itens de Menu Inativos */
[data-testid="stSidebar"] [data-testid="stRadio"] label p {
    font-family: 'Cinzel', serif !important;
    font-size: 0.90rem !important;
    font-weight: 600 !important;
    color: #4A2E1B !important;
    margin: 0 !important;
    line-height: 1.4 !important;
}

/* Card do Item ATIVO / SELECIONADO */
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
    background: linear-gradient(135deg, #781826 0%, #5E101D 100%) !important;
    border-color: #781826 !important;
    border-left: 4px solid #E6CA85 !important;
    box-shadow: 0 4px 12px rgba(120, 24, 38, 0.28) !important;
    transform: translateX(4px) !important;
}

/* Texto do Item ATIVO */
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) p {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
}

/* Botão Sair no Sidebar */
[data-testid="stSidebar"] .stButton > button {
    background: #FFFFFF !important;
    color: #781826 !important;
    border: 1px solid #D8C8B4 !important;
    border-radius: 8px !important;
    padding: 0.6rem 1rem !important;
    font-size: 0.88rem !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.03) !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: #FAF2EB !important;
    border-color: #781826 !important;
    color: #781826 !important;
    box-shadow: 0 4px 10px rgba(120, 24, 38, 0.12) !important;
    transform: translateY(-1px) !important;
}


/* Destaques e Métricas */
[data-testid="stMetricValue"] {
    font-family: 'Cinzel', serif !important;
    color: #781826 !important;
}

/* ==========================================================================
   Template Nobre para as Guias / Abas (Segmented Pill Cards)
   ========================================================================== */
.stTabs [data-baseweb="tab-list"] {
    background: #FAF5EB !important;
    border: 1px solid #E2D7C7 !important;
    border-radius: 12px !important;
    padding: 6px 8px !important;
    gap: 8px !important;
    box-shadow: inset 0 2px 4px rgba(90, 56, 37, 0.04) !important;
    margin-bottom: 1.5rem !important;
    overflow-x: auto !important;
    border-bottom: 1px solid #E2D7C7 !important;
}

/* Ocultar barra horizontal nativa do Streamlit */
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* Cada Guia / Aba como um Card Litúrgico */
.stTabs [data-baseweb="tab"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E6DCCD !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    font-family: 'Cinzel', serif !important;
    font-weight: 600 !important;
    font-size: 0.90rem !important;
    color: #5A3825 !important;
    transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02) !important;
    white-space: nowrap !important;
}

/* Hover na Guia */
.stTabs [data-baseweb="tab"]:hover {
    background-color: #FFFDF9 !important;
    border-color: #C5A059 !important;
    color: #781826 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 10px rgba(197, 160, 89, 0.18) !important;
}

/* Guia ATIVA / SELECIONADA */
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(135deg, #781826 0%, #5A111C 100%) !important;
    border: 1px solid #781826 !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 12px rgba(120, 24, 38, 0.3) !important;
    transform: translateY(-2px) !important;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] p,
.stTabs [data-baseweb="tab"][aria-selected="true"] span,
.stTabs [data-baseweb="tab"][aria-selected="true"] div {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}
</style>
"""

def apply_sacred_style():
    import streamlit as st
    st.markdown(SACRED_CSS, unsafe_allow_html=True)

def render_header(titulo="CATECUMENATO DE ADULTOS", subtitulo="Iniciação Cristã e Formação na Fé Católica"):
    import streamlit as st
    html = f"""
    <div class="parish-header">
        <div class="tau-badge">☩ PAZ E BEM! • SOROCABA / SP ☩</div>
        <h1>{titulo}</h1>
        <div class="subtitulo">{subtitulo}</div>
        <div style="font-size: 0.95rem; margin-top: 0.6rem; color: #E8D8B8; font-family: 'Cinzel', serif;">
            Paróquia Bom Jesus dos Aflitos • Frades Franciscanos Menores
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_divider(texto="✦ ☩ ✦"):
    import streamlit as st
    st.markdown(f'<div class="sacro-divider"><span>{texto}</span></div>', unsafe_allow_html=True)