# -*- coding: utf-8 -*-
"""
Portal do Catecumenato de Adultos
Paróquia Bom Jesus dos Aflitos — Sorocaba / SP
Ordem dos Frades Menores (Franciscanos)
"""

import streamlit as st
import database
import style
from modules import (
    home, encontros, gestao_catequistas, biblioteca_sacra, oracoes_e_liturgia,
    santa_missa, santo_terco, tratados_teologicos, confissao_e_reconciliacao,
    tesouro_franciscano, vida_moral, vigilia_pascal
)

# Configuração da Página
st.set_page_config(
    page_title="Catecumenato de Adultos | Bom Jesus dos Aflitos",
    page_icon="☩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar estilos visuais sacros e litúrgicos
style.apply_sacred_style()

# Inicializar Banco de Dados
database.init_db()

# Inicializar estado da sessão
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "perfil_usuario" not in st.session_state:
    st.session_state.perfil_usuario = "visitante"
if "nome_usuario" not in st.session_state:
    st.session_state.nome_usuario = ""
if "catecumeno_id" not in st.session_state:
    st.session_state.catecumeno_id = 0

# TELA DE LOGIN SACRA (se não autenticado)
if not st.session_state.autenticado:
    style.render_header(
        titulo="PORTAL DO CATECUMENATO",
        subtitulo="Paróquia Bom Jesus dos Aflitos • Sorocaba / SP"
    )

    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h3 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.3rem;">
            ☩ Acesso à Formação na Fé Católica ☩
        </h3>
        <p style="font-size: 1.15rem; color: #5A3825; font-style: italic;">
            "O Senhor te dê a paz! Identifique-se para acessar o material de formação e acompanhamento."
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_vazia1, col_login, col_vazia2 = st.columns([1, 2, 1])

    with col_login:
        tab_aluno, tab_catequista = st.tabs([
            "📖 Acesso do Catequisando (Aluno)",
            "🔑 Acesso do Catequista (Administrador)"
        ])

        # 1. Acesso do Catequisando
        with tab_aluno:
            st.markdown("""
            <div class="pergaminho-card">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    Seja bem-vindo, catecúmeno!
                </h4>
                <p style="font-size: 1rem; line-height: 1.5; color: #3A2315;">
                    Selecione seu nome na lista da turma paroquial para acessar os 40 encontros, 
                    a Santa Missa, o Santo Terço e registrar suas anotações no diário espiritual.
                </p>
            </div>
            """, unsafe_allow_html=True)

            catecumenos_ativos = database.get_catecumenos(filtro_ativo=True)
            opcoes_alunos = {f"{c['nome']} (Turma Atual)": c for c in catecumenos_ativos}
            opcoes_alunos["Ouvinte / Visitante Convidado"] = {"id": 0, "nome": "Ouvinte Convidado"}

            aluno_escolhido_label = st.selectbox("Identifique seu nome:", list(opcoes_alunos.keys()))
            aluno_obj = opcoes_alunos[aluno_escolhido_label]

            if st.button("Entrar como Catequisando ☩", type="primary", use_container_width=True):
                st.session_state.autenticado = True
                st.session_state.perfil_usuario = "catequisando"
                st.session_state.nome_usuario = aluno_obj["nome"]
                st.session_state.catecumeno_id = aluno_obj["id"]
                st.rerun()

        # 2. Acesso do Catequista (Admin)
        with tab_catequista:
            st.markdown("""
            <div class="pergaminho-card-bordo">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    Acesso Pastoral Restrito
                </h4>
                <p style="font-size: 1rem; line-height: 1.5; color: #3A2315;">
                    Área exclusiva para os catequistas da Paróquia Bom Jesus dos Aflitos. 
                    Permite gestão de matrículas, controle de presença, relatórios e acompanhamento sacramental.
                </p>
            </div>
            """, unsafe_allow_html=True)

            with st.form("form_login_catequista"):
                senha_input = st.text_input("Senha do Catequista:", type="password", placeholder="Digite sua senha de acesso")
                btn_entrar_cat = st.form_submit_button("Entrar como Catequista Administrador ☩", type="primary", use_container_width=True)

                if btn_entrar_cat:
                    if database.verificar_senha_catequista(senha_input):
                        st.session_state.autenticado = True
                        st.session_state.perfil_usuario = "catequista"
                        st.session_state.nome_usuario = "Catequista Administrador"
                        st.session_state.catecumeno_id = 0
                        st.success("Acesso autorizado! Paz e Bem.")
                        st.rerun()
                    else:
                        st.error("Senha incorreta! Dica inicial padrão: pazebem")

    st.stop()

# USUÁRIO AUTENTICADO - NAVEGAÇÃO PRINCIPAL
with st.sidebar:
    # Cabeçalho Paroquial
    st.markdown("""
    <div style="text-align: center; padding: 0.8rem 0.5rem; background: #FAF5EB; border: 1px solid #D8C8B4; border-radius: 8px; margin-bottom: 1rem;">
        <div style="font-size: 2rem; color: #781826; line-height: 1;">☩</div>
        <div style="font-family: 'Cinzel', serif; font-weight: 700; font-size: 1.05rem; color: #781826; margin-top: 0.3rem;">
            BOM JESUS DOS AFLITOS
        </div>
        <div style="font-size: 0.82rem; color: #5A3825; font-family: 'Cinzel', serif; letter-spacing: 1px;">
            SOROCABA / SP • FRANCISCANOS
        </div>
        <div style="margin-top: 0.3rem; font-size: 0.78rem; background: #C5A059; color: #2B1810; display: inline-block; padding: 2px 8px; border-radius: 12px; font-weight: bold;">
            PAZ E BEM!
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Identificação do Usuário Conectado
    perfil = st.session_state.perfil_usuario
    nome = st.session_state.nome_usuario

    if perfil == "catequista":
        st.markdown(f"""
        <div style="background: #EEDCCE; border-left: 4px solid #781826; padding: 0.5rem 0.8rem; border-radius: 4px; font-size: 0.88rem; margin-bottom: 1rem;">
            <strong style="color: #781826;">🛡️ Modo: Catequista</strong><br>
            <span style="font-size: 0.82rem; color: #4A2E1B;">Acesso Completo de Gestão</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background: #E8F0E4; border-left: 4px solid #2E7D32; padding: 0.5rem 0.8rem; border-radius: 4px; font-size: 0.88rem; margin-bottom: 1rem;">
            <strong style="color: #1B5E20;">👤 Catequisando:</strong><br>
            <span style="font-weight: bold; color: #2E1B10;">{nome}</span>
        </div>
        """, unsafe_allow_html=True)

    # Definição das Dimensões / Pilares de Formação
    if perfil == "catequista":
        estrutura_menu = {
            "🎓 Curso & Formação": [
                "🏠 Início & Visão Pastoral",
                "📖 Os 40 Encontros",
                "👥 Gestão da Turma & Chamada",
                "🕯️ Vigília Pascal & Padrinhos"
            ],
            "🏛️ Teologia & Doutrina": [
                "🏛️ Tratados Teológicos",
                "📜 Vida Moral & Virtudes",
                "🕊️ Confissão & Exame de Consciência"
            ],
            "⛪ Liturgia & Oração": [
                "⛪ A Santa Missa Passo a Passo",
                "📿 O Santo Terço",
                "🌿 Tesouro Franciscano",
                "🕊️ Oratório & Devocionário"
            ],
            "🔍 Pesquisa & Fontes": [
                "📜 Biblioteca Sacra & Fontes"
            ]
        }
    else:
        estrutura_menu = {
            "🎓 Curso & Formação": [
                "🏠 Início & Minha Jornada",
                "📖 Os 40 Encontros",
                "🕯️ Vigília Pascal & Padrinhos"
            ],
            "🏛️ Teologia & Doutrina": [
                "🏛️ Tratados Teológicos",
                "📜 Vida Moral & Virtudes",
                "🕊️ Confissão & Exame de Consciência"
            ],
            "⛪ Liturgia & Oração": [
                "⛪ A Santa Missa Passo a Passo",
                "📿 O Santo Terço",
                "🌿 Tesouro Franciscano",
                "🕊️ Oratório & Devocionário"
            ],
            "🔍 Pesquisa & Fontes": [
                "📜 Biblioteca Sacra & Fontes"
            ]
        }

    st.markdown("""
    <div style="font-family: 'Cinzel', serif; font-size: 0.80rem; font-weight: bold; color: #781826; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.3rem;">
        ☩ Dimensão / Pilar:
    </div>
    """, unsafe_allow_html=True)

    lista_grupos = list(estrutura_menu.keys())

    if "pilar_ativo" not in st.session_state or st.session_state.pilar_ativo not in lista_grupos:
        st.session_state.pilar_ativo = lista_grupos[0]

    idx_grupo = lista_grupos.index(st.session_state.pilar_ativo)
    grupo_selecionado = st.selectbox(
        "Selecione o Pilar:",
        options=lista_grupos,
        index=idx_grupo,
        label_visibility="collapsed",
        key="select_pilar"
    )
    st.session_state.pilar_ativo = grupo_selecionado

    st.markdown("""
    <div style="font-family: 'Cinzel', serif; font-size: 0.80rem; font-weight: bold; color: #5A3825; text-transform: uppercase; letter-spacing: 1px; margin-top: 0.7rem; margin-bottom: 0.3rem;">
        📄 Conteúdos & Módulos:
    </div>
    """, unsafe_allow_html=True)

    opcoes_paginas = estrutura_menu[grupo_selecionado]
    pagina = st.radio(
        "Selecione o Conteúdo:",
        options=opcoes_paginas,
        label_visibility="collapsed",
        key=f"radio_pag_{grupo_selecionado}"
    )

    st.markdown("---")

    # Botão de Sair / Trocar Usuário
    if st.button("🚪 Sair / Trocar de Usuário", use_container_width=True):
        st.session_state.autenticado = False
        st.session_state.perfil_usuario = "visitante"
        st.session_state.nome_usuario = ""
        st.session_state.catecumeno_id = 0
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Itinerário Litúrgico
    st.markdown("""
    <div style="background: #F4EBE1; border-left: 3px solid #781826; padding: 0.7rem; border-radius: 4px; font-size: 0.85rem;">
        <strong style="color: #781826; font-family: 'Cinzel', serif;">Itinerário Litúrgico:</strong><br>
        • Apresentação: <em>4º Dom. Quaresma</em><br>
        • Sacramentos: <em>Vigília Pascal</em>
    </div>
    """, unsafe_allow_html=True)

    # Bênção de Frei Leão
    st.markdown("""
    <div style="text-align: center; font-size: 0.8rem; color: #5A3825; font-style: italic; border-top: 1px solid #D8C8B4; padding-top: 0.8rem; margin-top: 0.8rem;">
        "O Senhor te abençoe e te guarde.<br>Mostre-te a sua face e te dê a paz!" ☩
    </div>
    """, unsafe_allow_html=True)

# Cabeçalho Litúrgico de Navegação (Breadcrumb)
st.markdown(f"""
<div style="background: linear-gradient(90deg, #FDFBF7 0%, #F6EFE6 100%); 
            border: 1px solid #E2D5C3; 
            border-left: 4px solid #781826; 
            border-radius: 6px; 
            padding: 0.45rem 0.9rem; 
            margin-bottom: 1.2rem; 
            display: flex; 
            flex-wrap: wrap;
            gap: 0.4rem;
            align-items: center; 
            justify-content: space-between;">
    <div style="font-size: 0.88rem; color: #5A3825;">
        <span style="color: #781826; font-family: 'Cinzel', serif; font-weight: bold;">☩ {grupo_selecionado}</span> 
        <span style="color: #C5A059; margin: 0 0.4rem;">›</span> 
        <strong style="color: #2B1810;">{pagina}</strong>
    </div>
    <div style="font-size: 0.78rem; color: #8C7355; font-family: 'Cinzel', serif;">
        Paróquia Bom Jesus dos Aflitos • Sorocaba / SP
    </div>
</div>
""", unsafe_allow_html=True)

# Roteamento dos Módulos
if "🏠 Início" in pagina:
    home.render()
elif "📖 Os 40 Encontros" in pagina:
    encontros.render()
elif "👥 Gestão da Turma" in pagina:
    if perfil == "catequista":
        gestao_catequistas.render()
    else:
        st.warning("Acesso restrito ao catequista administrador.")
elif "🕊️ Confissão" in pagina:
    confissao_e_reconciliacao.render()
elif "🌿 Tesouro Franciscano" in pagina:
    tesouro_franciscano.render()
elif "📜 Vida Moral" in pagina:
    vida_moral.render()
elif "🕯️ Vigília Pascal" in pagina:
    vigilia_pascal.render()
elif "⛪ A Santa Missa" in pagina:
    santa_missa.render()
elif "📿 O Santo Terço" in pagina:
    santo_terco.render()
elif "🏛️ Tratados Teológicos" in pagina:
    tratados_teologicos.render()
elif "📜 Biblioteca Sacra" in pagina:
    biblioteca_sacra.render()
elif "🕊️ Oratório" in pagina:
    oracoes_e_liturgia.render()