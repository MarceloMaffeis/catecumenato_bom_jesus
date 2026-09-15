# -*- coding: utf-8 -*-
"""
Portal do Catecumenato de Adultos
Paróquia Bom Jesus dos Aflitos — Sorocaba / SP
Ordem dos Frades Menores (Franciscanos)
"""

import streamlit as st
import importlib
import database
importlib.reload(database)
import style
from modules import (
    home, encontros, gestao_catequistas, biblioteca_sacra, oracoes_e_liturgia,
    santa_missa, santo_terco, tratados_teologicos, confissao_e_reconciliacao,
    tesouro_franciscano, vida_moral, vigilia_pascal
)

# Configuração da Página
st.set_page_config(
    page_title="Catecumenato de Adultos | Bom Jesus dos Aflitos",
    page_icon="assets/favicon.png",
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
if "turma_id" not in st.session_state:
    st.session_state.turma_id = 1
if "turma_nome" not in st.session_state:
    st.session_state.turma_nome = ""
if "turma_nivel" not in st.session_state:
    st.session_state.turma_nivel = ""

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

    col_vazia1, col_login, col_vazia2 = st.columns([1, 2.2, 1])

    with col_login:
        tab_aluno, tab_degustacao, tab_catequista = st.tabs([
            "📖 Acesso do Aluno (Por Turma)",
            "🌟 Acesso Degustação (Visitante)",
            "🔑 Acesso do Catequista (Admin)"
        ])

        # 1. Acesso do Catequisando por Turma
        with tab_aluno:
            st.markdown("""
            <div class="pergaminho-card">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    Seja bem-vindo, catecúmeno!
                </h4>
                <p style="font-size: 0.98rem; line-height: 1.5; color: #3A2315; margin-bottom: 0;">
                    Selecione a sua <strong>Turma</strong>, identifique seu <strong>Nome</strong> e insira sua senha de acesso.
                </p>
            </div>
            """, unsafe_allow_html=True)

            turmas_ativas = database.get_turmas(apenas_ativas=True)
            if not turmas_ativas:
                turmas_ativas = [{"id": 1, "nome": "Turma Bom Jesus 2026", "nivel": "Catecumenato de Adultos"}]

            opcoes_turmas = {f"🏫 {t['nome']} — {t['nivel']}": t for t in turmas_ativas}
            turma_label_sel = st.selectbox("1. Selecione a sua Turma:", list(opcoes_turmas.keys()), key="login_sel_turma")
            turma_obj = opcoes_turmas[turma_label_sel]

            alunos_turma = database.get_catecumenos(filtro_ativo=True, turma_id=turma_obj["id"])
            if not alunos_turma:
                st.warning(f"Ainda não há catequisandos cadastrados na {turma_obj['nome']}. O catequista pode cadastrar os alunos no painel administrativo.")
            else:
                opcoes_alunos = {f"👤 {c['nome']}": c for c in alunos_turma}
                aluno_escolhido_label = st.selectbox("2. Identifique seu Nome:", list(opcoes_alunos.keys()), key="login_sel_aluno")
                aluno_obj = opcoes_alunos[aluno_escolhido_label]

                with st.form("form_login_catequisando"):
                    senha_aluno = st.text_input(
                        "3. Sua Senha de Acesso:",
                        type="password",
                        placeholder="Digite sua senha (padrão inicial: pazebem)",
                        help="Senha inicial padrão: pazebem. Você pode alterá-la no painel após entrar."
                    )
                    st.caption("🔒 *Dica:* A senha inicial de todos os catecúmenos é **`pazebem`**.")

                    btn_entrar_aluno = st.form_submit_button("Entrar como Catequisando ☩", type="primary", use_container_width=True)

                    if btn_entrar_aluno:
                        acesso_permitido = False
                        if hasattr(database, "verificar_senha_catecumeno"):
                            acesso_permitido = database.verificar_senha_catecumeno(aluno_obj["id"], senha_aluno)
                        else:
                            cat = database.get_catecumeno(aluno_obj["id"])
                            senha_salva = (cat.get("senha") if cat else None) or "pazebem"
                            acesso_permitido = senha_aluno.strip().lower() == senha_salva.strip().lower()

                        if acesso_permitido:
                            st.session_state.autenticado = True
                            st.session_state.perfil_usuario = "catequisando"
                            st.session_state.nome_usuario = aluno_obj["nome"]
                            st.session_state.catecumeno_id = aluno_obj["id"]
                            st.session_state.turma_id = turma_obj["id"]
                            st.session_state.turma_nome = turma_obj["nome"]
                            st.session_state.turma_nivel = turma_obj["nivel"]
                            st.rerun()
                        else:
                            st.error("Senha incorreta! A senha inicial padrão é 'pazebem'. Se você alterou e esqueceu, solicite ao catequista para redefini-la.")

        # 2. Acesso de Degustação (Visitante Aberto)
        with tab_degustacao:
            st.markdown("""
            <div class="pergaminho-card-franciscano">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🌟 Degustação da Formação Católica
                </h4>
                <p style="font-size: 1.02rem; line-height: 1.6; color: #2E1B10; text-align: justify; margin-bottom: 0.5rem;">
                    Paz e Bem! Criamos este acesso aberto para que qualquer pessoa possa <strong>conhecer, ler e estudar</strong> 
                    todo o tesouro da fé católica da Paróquia Bom Jesus dos Aflitos: os 40 encontros, os tratados de teologia, 
                    a Santa Missa, o Santo Terço e as orações dos santos franciscanos.
                </p>
                <div style="background: #FDFBF7; border-left: 4px solid #C5A059; padding: 0.7rem 0.9rem; border-radius: 4px; font-size: 0.92rem; color: #5A3825; margin: 0.8rem 0;">
                    <strong>ℹ️ Como funciona este modo:</strong> Você pode ler todos os materiais e realizar os testes da fé. 
                    Como é um acesso de visitante, <em>nenhuma informação de presença, nota ou diário pessoal é gravada no servidor</em>.
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Entrar no Modo Degustação ☩", type="primary", use_container_width=True, key="btn_entrar_degustacao"):
                st.session_state.autenticado = True
                st.session_state.perfil_usuario = "degustacao"
                st.session_state.nome_usuario = "Visitante em Degustação"
                st.session_state.catecumeno_id = 0
                st.session_state.turma_id = 0
                st.session_state.turma_nome = "Acesso Geral Aberto"
                st.session_state.turma_nivel = "Visitante"
                st.rerun()

        # 3. Acesso do Catequista (Admin)
        with tab_catequista:
            st.markdown("""
            <div class="pergaminho-card-bordo">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    Acesso Pastoral Restrito
                </h4>
                <p style="font-size: 1rem; line-height: 1.5; color: #3A2315;">
                    Área exclusiva para os catequistas da Paróquia Bom Jesus dos Aflitos. 
                    Permite gestão de turmas, matrículas, controle de presença, relatórios e acompanhamento sacramental.
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
                        st.session_state.turma_id = 0
                        st.session_state.turma_nome = "Todas as Turmas"
                        st.session_state.turma_nivel = "Coordenação"
                        st.success("Acesso autorizado! Paz e Bem.")
                        st.rerun()
                    else:
                        st.error("Senha incorreta! Dica inicial padrão: pazebem")

    st.stop()

# USUÁRIO AUTENTICADO - NAVEGAÇÃO PRINCIPAL
with st.sidebar:
    # Cabeçalho Paroquial Nobre
    st.markdown("""
    <div style="text-align: center; padding: 1.1rem 0.8rem; background: #FFFFFF; border: 1px solid #E2D7C7; border-top: 4px solid #781826; border-radius: 12px; box-shadow: 0 4px 14px rgba(120, 24, 38, 0.05); margin-bottom: 1.2rem;">
        <div style="font-size: 1.8rem; color: #781826; line-height: 1; margin-bottom: 0.2rem;">☩</div>
        <div style="font-family: 'Cinzel', serif; font-weight: 700; font-size: 1.05rem; color: #781826; letter-spacing: 0.5px;">
            BOM JESUS DOS AFLITOS
        </div>
        <div style="font-size: 0.78rem; color: #5A3825; font-family: 'Cinzel', serif; letter-spacing: 1.5px; margin-top: 0.2rem;">
            SOROCABA / SP • FRANCISCANOS
        </div>
        <div style="margin-top: 0.55rem;">
            <span style="font-size: 0.76rem; background: #FAF2E2; border: 1px solid #C5A059; color: #5A3825; padding: 3px 12px; border-radius: 16px; font-weight: 700; font-family: 'Cinzel', serif; letter-spacing: 1px;">
                PAZ E BEM!
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Identificação do Usuário Conectado (Card de Credencial)
    perfil = st.session_state.perfil_usuario
    nome = st.session_state.nome_usuario

    if perfil == "catequista":
        st.markdown("""
        <div style="background: #FFFFFF; border: 1px solid #E2D7C7; border-left: 4px solid #781826; padding: 0.75rem 0.9rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); margin-bottom: 1.3rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #781826; font-family: 'Cinzel', serif; font-size: 0.82rem; font-weight: 700;">🛡️ MODO PASTORAL</span>
                <span style="background: #F8EAE9; color: #781826; font-size: 0.70rem; padding: 2px 6px; border-radius: 4px; font-weight: bold; letter-spacing: 0.5px;">CATEQUISTA</span>
            </div>
            <div style="font-weight: 700; color: #2E1B10; font-size: 0.95rem; margin-top: 0.25rem;">Catequista / Coordenação</div>
            <div style="font-size: 0.78rem; color: #6D4C41; margin-top: 2px;">Acesso Completo de Gestão</div>
        </div>
        """, unsafe_allow_html=True)
    elif perfil == "degustacao":
        st.markdown("""
        <div style="background: #FFFFFF; border: 1px solid #E8E0D2; border-left: 4px solid #C5A059; padding: 0.75rem 0.9rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); margin-bottom: 1.3rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #8C6A1D; font-family: 'Cinzel', serif; font-size: 0.82rem; font-weight: 700;">🌟 CONVIDADO</span>
                <span style="background: #FFF8E1; color: #8C6A1D; font-size: 0.70rem; padding: 2px 6px; border-radius: 4px; font-weight: bold; letter-spacing: 0.5px;">DEGUSTAÇÃO</span>
            </div>
            <div style="font-weight: 700; color: #2E1B10; font-size: 0.95rem; margin-top: 0.25rem;">Visitante Convidado</div>
            <div style="font-size: 0.78rem; color: #6D4C41; margin-top: 2px;">Navegação aberta sem gravação</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        turma_nome_exib = st.session_state.get("turma_nome", "")
        turma_nivel_exib = st.session_state.get("turma_nivel", "")
        turma_info_html = f"<div style='font-size: 0.78rem; color: #2E7D32; margin-top: 2px; font-weight: 500;'>🏫 {turma_nome_exib} ({turma_nivel_exib})</div>" if turma_nome_exib else ""
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid #D5E5D5; border-left: 4px solid #2E7D32; padding: 0.75rem 0.9rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); margin-bottom: 1.3rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #2E7D32; font-family: 'Cinzel', serif; font-size: 0.82rem; font-weight: 700;">👤 CATEQUISANDO</span>
                <span style="background: #E8F5E9; color: #2E7D32; font-size: 0.70rem; padding: 2px 6px; border-radius: 4px; font-weight: bold; letter-spacing: 0.5px;">ALUNO</span>
            </div>
            <div style="font-weight: 700; color: #2E1B10; font-size: 0.95rem; margin-top: 0.25rem;">{nome}</div>
            {turma_info_html}
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
    <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 0.45rem;">
        <span style="color: #781826; font-size: 0.95rem;">☩</span>
        <span style="font-family: 'Cinzel', serif; font-size: 0.80rem; font-weight: 700; color: #781826; text-transform: uppercase; letter-spacing: 1px;">
            Dimensão Formativa:
        </span>
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
    <div style="display: flex; align-items: center; gap: 6px; margin-top: 1.3rem; margin-bottom: 0.55rem;">
        <span style="color: #5A3825; font-size: 0.85rem;">✦</span>
        <span style="font-family: 'Cinzel', serif; font-size: 0.80rem; font-weight: 700; color: #5A3825; text-transform: uppercase; letter-spacing: 1px;">
            Módulos & Conteúdos:
        </span>
    </div>
    """, unsafe_allow_html=True)

    opcoes_paginas = estrutura_menu[grupo_selecionado]
    pagina = st.radio(
        "Selecione o Conteúdo:",
        options=opcoes_paginas,
        label_visibility="collapsed",
        key=f"radio_pag_{grupo_selecionado}"
    )

    st.markdown("""
    <div style="margin: 1.4rem 0 1.1rem 0; height: 1px; background: linear-gradient(to right, transparent, #D8C8B4, transparent);"></div>
    """, unsafe_allow_html=True)

    # Botão de Sair / Trocar Usuário
    if st.button("🚪 Sair / Trocar de Usuário", use_container_width=True):
        st.session_state.autenticado = False
        st.session_state.perfil_usuario = "visitante"
        st.session_state.nome_usuario = ""
        st.session_state.catecumeno_id = 0
        st.session_state.turma_id = 0
        st.session_state.turma_nome = ""
        st.session_state.turma_nivel = ""
        st.rerun()

    # Itinerário Litúrgico
    st.markdown("""
    <div style="background: #FFFFFF; border: 1px solid #E2D7C7; border-left: 3px solid #781826; padding: 0.8rem; border-radius: 8px; font-size: 0.84rem; margin-top: 1.2rem; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div style="color: #781826; font-family: 'Cinzel', serif; font-weight: 700; font-size: 0.82rem; margin-bottom: 0.3rem;">
            ⏳ ITINERÁRIO LITÚRGICO
        </div>
        <div style="color: #4A2E1B; line-height: 1.45;">
            • Apresentação: <em>4º Dom. Quaresma</em><br>
            • Sacramentos: <em>Vigília Pascal</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Bênção de Frei Leão
    st.markdown("""
    <div style="text-align: center; font-size: 0.82rem; color: #5A3825; font-style: italic; border-top: 1px solid #E2D7C7; padding-top: 0.9rem; margin-top: 1.2rem; line-height: 1.4;">
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