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
    initial_sidebar_state="collapsed"
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
if "pagina_ativa" not in st.session_state:
    st.session_state.pagina_ativa = "hub"

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
# ==============================================================================
# USUÁRIO AUTENTICADO - EXPERIÊNCIA DE NAVEGAÇÃO MODERNA (HUB SACRO)
# ==============================================================================
perfil = st.session_state.perfil_usuario
nome = st.session_state.nome_usuario

# 1. CABEÇALHO SUPERIOR ELEGANTE COM IDENTIFICAÇÃO DO USUÁRIO & SAÍDA
if perfil == "catequista":
    badge_conteudo = """
    <div style="background: #FFFFFF; border: 1px solid #E2D7C7; border-left: 4px solid #781826; padding: 6px 12px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
            <span style="background: #F8EAE9; color: #781826; font-size: 0.70rem; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-family: 'Cinzel', serif;">🛡️ CATEQUISTA</span>
            <span style="font-size: 0.74rem; color: #781826; font-weight: bold;">COORDENAÇÃO</span>
        </div>
        <div style="font-weight: 700; color: #2E1B10; font-size: 0.88rem; margin-top: 2px;">Catequista Administrador</div>
    </div>
    """
elif perfil == "degustacao":
    badge_conteudo = """
    <div style="background: #FFFFFF; border: 1px solid #E8E0D2; border-left: 4px solid #C5A059; padding: 6px 12px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
            <span style="background: #FFF8E1; color: #8C6A1D; font-size: 0.70rem; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-family: 'Cinzel', serif;">🌟 DEGUSTAÇÃO</span>
            <span style="font-size: 0.74rem; color: #8C6A1D; font-weight: bold;">VISITANTE</span>
        </div>
        <div style="font-weight: 700; color: #2E1B10; font-size: 0.88rem; margin-top: 2px;">Navegação Aberta</div>
    </div>
    """
else:
    turma_nome_exib = st.session_state.get("turma_nome", "")
    turma_nivel_exib = st.session_state.get("turma_nivel", "")
    turma_rotulo = f"🏫 {turma_nome_exib} ({turma_nivel_exib})" if turma_nome_exib else "Turma Ativa"
    badge_conteudo = f"""
    <div style="background: #FFFFFF; border: 1px solid #D5E5D5; border-left: 4px solid #2E7D32; padding: 6px 12px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
            <span style="background: #E8F5E9; color: #2E7D32; font-size: 0.70rem; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-family: 'Cinzel', serif;">👤 CATEQUISANDO</span>
            <span style="font-size: 0.72rem; color: #2E7D32; font-weight: bold;">{turma_rotulo}</span>
        </div>
        <div style="font-weight: 700; color: #2E1B10; font-size: 0.88rem; margin-top: 2px;">{nome}</div>
    </div>
    """

col_top_logo, col_top_user, col_top_logout = st.columns([3.2, 1.8, 0.8])

with col_top_logo:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 14px; padding: 4px 0;">
        <span style="font-size: 2.2rem; color: #781826; line-height: 1;">☩</span>
        <div>
            <div style="font-family: 'Cinzel', serif; font-weight: 700; font-size: 1.15rem; color: #781826; letter-spacing: 0.5px; line-height: 1.2;">
                PARÓQUIA BOM JESUS DOS AFLITOS
            </div>
            <div style="font-size: 0.80rem; color: #5A3825; font-family: 'Cinzel', serif; letter-spacing: 1px; margin-top: 2px;">
                SOROCABA / SP &bull; FRANCISCANOS &bull; <strong style="color: #781826;">PAZ E BEM!</strong>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_top_user:
    st.markdown(badge_conteudo, unsafe_allow_html=True)

with col_top_logout:
    st.write("")
    if st.button("🚪 Sair", use_container_width=True, key="btn_logout_principal"):
        st.session_state.autenticado = False
        st.session_state.perfil_usuario = "visitante"
        st.session_state.nome_usuario = ""
        st.session_state.catecumeno_id = 0
        st.session_state.turma_id = 0
        st.session_state.turma_nome = ""
        st.session_state.turma_nivel = ""
        st.session_state.pagina_ativa = "hub"
        st.rerun()

st.markdown("""<div style="margin: 0.7rem 0 1.2rem 0; height: 1px; background: linear-gradient(to right, #781826, #C5A059, transparent);"></div>""", unsafe_allow_html=True)

# Mapa de metadados dos módulos para roteamento e atalhos rápidos
modulos_info = {
    "jornada": {"titulo": "Início & Minha Jornada", "setor": "Iniciação & Formação", "icone": "🏠"},
    "encontros": {"titulo": "Os 40 Encontros", "setor": "Iniciação & Formação", "icone": "📖"},
    "gestao": {"titulo": "Gestão da Turma & Chamada", "setor": "Iniciação & Formação", "icone": "👥"},
    "vigilia": {"titulo": "Vigília Pascal & Padrinhos", "setor": "Iniciação & Formação", "icone": "🕯️"},
    "tratados": {"titulo": "Tratados Teológicos", "setor": "Teologia & Doutrina", "icone": "🏛️"},
    "vida_moral": {"titulo": "Vida Moral & Virtudes", "setor": "Teologia & Doutrina", "icone": "📜"},
    "confissao": {"titulo": "Confissão & Reconciliação", "setor": "Teologia & Doutrina", "icone": "🕊️"},
    "santa_missa": {"titulo": "A Santa Missa Passo a Passo", "setor": "Liturgia & Oração", "icone": "⛪"},
    "santo_terco": {"titulo": "O Santo Terço", "setor": "Liturgia & Oração", "icone": "📿"},
    "tesouro": {"titulo": "Tesouro Franciscano", "setor": "Liturgia & Oração", "icone": "🌿"},
    "oratorio": {"titulo": "Oratório & Devocionário", "setor": "Liturgia & Oração", "icone": "🕊️"},
    "biblioteca": {"titulo": "Biblioteca Sacra & Fontes", "setor": "Pesquisa & Fontes", "icone": "📜"}
}

# ==============================================================================
# ESTADO A: O PORTAL HUB SACRO (VITRINE DE CARDS AGRUPADOS POR SETORES)
# ==============================================================================
if st.session_state.pagina_ativa == "hub":

    # 1. Mural Pastoral de Acolhida & Marco Litúrgico
    if perfil == "catequisando":
        cid_usuario = st.session_state.get("catecumeno_id", 0)
        prog = database.get_progresso_catecumeno(cid_usuario)
        pct = prog.get("percentual", 0)
        concluidos = prog.get("total_concluidos", 0)

        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #FAF8F5 0%, #F5ECE0 100%); border: 1px solid #D8C8B4; border-left: 6px solid #C5A059; border-radius: 12px; padding: 14px 20px; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(120,24,38,0.04);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div>
                    <h3 style="color: #781826; font-family: 'Cinzel', serif; margin: 0; font-size: 1.15rem;">
                        ☩ Paz e Bem, caríssimo(a) {nome}!
                    </h3>
                    <p style="color: #5A3825; font-size: 0.95rem; margin: 4px 0 0 0; font-style: italic;">
                        Sua caminhada rumo aos Santos Sacramentos da Iniciação Cristã na Paróquia Bom Jesus dos Aflitos.
                    </p>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #C5A059; padding: 6px 14px; border-radius: 20px; font-weight: bold; color: #781826; font-size: 0.85rem; font-family: 'Cinzel', serif;">
                    Progresso Geral: {concluidos} / 40 ({pct}%)
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    elif perfil == "catequista":
        catecumenos = database.get_catecumenos(filtro_ativo=True)
        total_cat = len(catecumenos)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #FAF8F5 0%, #F5ECE0 100%); border: 1px solid #D8C8B4; border-left: 6px solid #781826; border-radius: 12px; padding: 14px 20px; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(120,24,38,0.04);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div>
                    <h3 style="color: #781826; font-family: 'Cinzel', serif; margin: 0; font-size: 1.15rem;">
                        ☩ Bem-vindo ao Painel Pastoral do Catequista, Irmão em Cristo!
                    </h3>
                    <p style="color: #5A3825; font-size: 0.95rem; margin: 4px 0 0 0; font-style: italic;">
                        Coordenação e pastoreio da formação de adultos rumo à Vigília Pascal.
                    </p>
                </div>
                <div style="background: #FFFFFF; border: 1px solid #781826; padding: 6px 14px; border-radius: 20px; font-weight: bold; color: #781826; font-size: 0.85rem; font-family: 'Cinzel', serif;">
                    👥 {total_cat} Catecúmenos Acompanhados
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FAF8F5 0%, #F5ECE0 100%); border: 1px solid #D8C8B4; border-left: 6px solid #C5A059; border-radius: 12px; padding: 14px 20px; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(120,24,38,0.04);">
            <h3 style="color: #781826; font-family: 'Cinzel', serif; margin: 0; font-size: 1.15rem;">
                🌟 Bem-vindo ao Modo Degustação da Formação Católica!
            </h3>
            <p style="color: #5A3825; font-size: 0.95rem; margin: 4px 0 0 0; font-style: italic;">
                Todo o acervo doutrinal, os 40 encontros, tratados e orações estão abertos para seu estudo e contemplação.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: #5A3825; font-size: 1rem; margin: 10px 0 20px 0;'>✨ <strong>Clique em qualquer módulo abaixo</strong> para acessar diretamente o conteúdo formativo desejado:</p>", unsafe_allow_html=True)

    # ==========================================================================
    # SETOR 1: 🎓 INICIAÇÃO CRISTÃ & FORMAÇÃO
    # ==========================================================================
    style.render_sector_header("🎓", "Setor 1 — Iniciação Cristã & Formação", "A caminhada dos 40 encontros, a Vigília Pascal sacramental e o acompanhamento pastoral")

    if perfil == "catequista":
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            style.render_hub_card("🏠", "Minha Jornada", "Visão pastoral, marcos da catequese e histórico comunitário.", "accent-bordo")
            if st.button("Abrir Jornada 🏠", use_container_width=True, key="hub_jorn"):
                st.session_state.pagina_ativa = "jornada"
                st.rerun()

        with c2:
            style.render_hub_card("📖", "Os 40 Encontros", "Bíblia, Magistério, apostilas para download e testes de fé.", "accent-ouro")
            if st.button("Estudar Encontros 📖", use_container_width=True, key="hub_enc"):
                st.session_state.pagina_ativa = "encontros"
                st.rerun()

        with c3:
            style.render_hub_card("👥", "Gestão & Chamada", "Matrículas de alunos, lista de chamada e relatórios pastorais.", "accent-verde")
            if st.button("Gerenciar Turma 👥", use_container_width=True, key="hub_gest"):
                st.session_state.pagina_ativa = "gestao"
                st.rerun()

        with c4:
            style.render_hub_card("🕯️", "Vigília Pascal", "Rito de Batismo, Crisma, Eucaristia e requisitos de padrinhos.", "accent-franciscano")
            if st.button("Ver Vigília 🕯️", use_container_width=True, key="hub_vig"):
                st.session_state.pagina_ativa = "vigilia"
                st.rerun()
    else:
        c1, c2, c3 = st.columns(3)
        with c1:
            style.render_hub_card("🏠", "Minha Jornada", "Métricas espirituais, progresso pessoal e diário de bordo da fé.", "accent-bordo")
            if st.button("Minha Jornada 🏠", use_container_width=True, key="hub_jorn"):
                st.session_state.pagina_ativa = "jornada"
                st.rerun()

        with c2:
            style.render_hub_card("📖", "Os 40 Encontros", "Bíblia, Magistério, apostilas para download e quizzes formativos.", "accent-ouro")
            if st.button("Estudar Encontros 📖", use_container_width=True, key="hub_enc"):
                st.session_state.pagina_ativa = "encontros"
                st.rerun()

        with c3:
            style.render_hub_card("🕯️", "Vigília Pascal", "Rito dos sacramentos pascais, testemunho cristão e padrinhos.", "accent-franciscano")
            if st.button("Ver Vigília 🕯️", use_container_width=True, key="hub_vig"):
                st.session_state.pagina_ativa = "vigilia"
                st.rerun()

    # ==========================================================================
    # SETOR 2: 🏛️ TEOLOGIA & DOUTRINA CATÓLICA
    # ==========================================================================
    style.render_sector_header("🏛️", "Setor 2 — Teologia & Doutrina Católica", "Fundamentos dogmáticos, tratados dos mistérios divinos, moral cristã e reconciliação")

    c1, c2, c3 = st.columns(3)
    with c1:
        style.render_hub_card("🏛️", "Tratados Teológicos", "Mariologia, Cristologia, Santíssima Trindade, Igreja e Anjos.", "accent-ouro")
        if st.button("Consultar Tratados 🏛️", use_container_width=True, key="hub_trat"):
            st.session_state.pagina_ativa = "tratados"
            st.rerun()

    with c2:
        style.render_hub_card("📜", "Vida Moral & Virtudes", "Os 10 Mandamentos, bem-aventuranças e vida cristã prática.", "accent-bordo")
        if st.button("Estudar Vida Moral 📜", use_container_width=True, key="hub_moral"):
            st.session_state.pagina_ativa = "vida_moral"
            st.rerun()

    with c3:
        style.render_hub_card("🕊️", "Confissão & Penitência", "Exame de consciência profundo e rito do perdão dos pecados.", "accent-franciscano")
        if st.button("Preparar Confissão 🕊️", use_container_width=True, key="hub_conf"):
            st.session_state.pagina_ativa = "confissao"
            st.rerun()

    # ==========================================================================
    # SETOR 3: ⛪ LITURGIA & ORAÇÃO FRANCISCANA
    # ==========================================================================
    style.render_sector_header("⛪", "Setor 3 — Liturgia & Oração Franciscana", "A celebração eucarística, o Rosário contemplativo e a espiritualidade dos Santos de Assis")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        style.render_hub_card("⛪", "A Santa Missa", "Passo a passo dos ritos, paramentos, cores e mistério eucarístico.", "accent-bordo")
        if st.button("Conhecer a Missa ⛪", use_container_width=True, key="hub_missa"):
            st.session_state.pagina_ativa = "santa_missa"
            st.rerun()

    with c2:
        style.render_hub_card("📿", "O Santo Terço", "Mistérios do dia, meditações bíblicas e orações marianas.", "accent-ouro")
        if st.button("Rezar o Terço 📿", use_container_width=True, key="hub_terco"):
            st.session_state.pagina_ativa = "santo_terco"
            st.rerun()

    with c3:
        style.render_hub_card("🌿", "Tesouro Franciscano", "São Francisco e Santa Clara, o Cântico das Criaturas e orações.", "accent-franciscano")
        if st.button("Meditar Tesouro 🌿", use_container_width=True, key="hub_tesouro"):
            st.session_state.pagina_ativa = "tesouro"
            st.rerun()

    with c4:
        style.render_hub_card("🕊️", "Oratório & Devoção", "Devocionário tradicional, liturgia diária e salmos de louvor.", "accent-verde")
        if st.button("Abrir Oratório 🕊️", use_container_width=True, key="hub_orat"):
            st.session_state.pagina_ativa = "oratorio"
            st.rerun()

    # ==========================================================================
    # SETOR 4: 📜 PESQUISA & FONTES SACRAS + ITINERÁRIO
    # ==========================================================================
    style.render_sector_header("📜", "Setor 4 — Pesquisa & Fontes Sacras", "Acesso ao magistério da Igreja, Sagrada Escritura e Tradição Católica")

    c_bib, c_itin, c_benc = st.columns([1.2, 1.4, 1.4])
    with c_bib:
        style.render_hub_card("📜", "Biblioteca Sacra", "Catecismo da Igreja Católica (CIC), Bíblia Sagrada e Concílios.", "accent-bordo")
        if st.button("Acessar Biblioteca 📜", use_container_width=True, key="hub_biblio"):
            st.session_state.pagina_ativa = "biblioteca"
            st.rerun()

    with c_itin:
        st.markdown("""
        <div style="background: #FFFFFF; border: 1px solid #E2D7C7; border-top: 4px solid #781826; border-radius: 14px; padding: 14px 16px; height: 175px; box-shadow: 0 4px 14px rgba(0,0,0,0.03); display: flex; flex-direction: column; justify-content: space-between;">
            <div style="color: #781826; font-family: 'Cinzel', serif; font-weight: 700; font-size: 0.88rem; display: flex; align-items: center; gap: 6px;">
                <span>⏳</span> ITINERÁRIO LITÚRGICO
            </div>
            <div style="color: #4A2E1B; font-size: 0.84rem; line-height: 1.5;">
                • <strong>Apresentação à Comunidade:</strong><br><em>4º Domingo da Quaresma (Laetare)</em><br>
                • <strong>Sacramentos Pascais:</strong><br><em>Vigília Pascal (Sábado Santo)</em>
            </div>
            <div style="font-size: 0.76rem; color: #8C6A1D; font-style: italic;">
                Iniciação Cristã de Adultos
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_benc:
        st.markdown("""
        <div style="background: #FFFFFF; border: 1px solid #E2D7C7; border-top: 4px solid #C5A059; border-radius: 14px; padding: 14px 16px; height: 175px; box-shadow: 0 4px 14px rgba(0,0,0,0.03); display: flex; flex-direction: column; justify-content: space-between; text-align: center;">
            <div style="color: #8C6A1D; font-family: 'Cinzel', serif; font-weight: 700; font-size: 0.88rem;">
                🕊️ BÊNÇÃO DE FREI LEÃO
            </div>
            <div style="font-size: 0.86rem; color: #5A3825; font-style: italic; line-height: 1.45;">
                "O Senhor te abençoe e te guarde.<br>Mostre-te a sua face e te dê a paz!" ☩
            </div>
            <div style="font-size: 0.76rem; color: #781826; font-family: 'Cinzel', serif; font-weight: bold;">
                São Francisco de Assis
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# ESTADO B: DENTRO DE UM MÓDULO (BARRA DE TOPO COM RETORNO E ATALHOS RÁPIDOS)
# ==============================================================================
else:
    info_atual = modulos_info.get(st.session_state.pagina_ativa, {"titulo": "Módulo", "setor": "Catecumenato", "icone": "☩"})

    # Barra Superior de Navegação
    c_nav_voltar, c_nav_bread, c_nav_atalho = st.columns([1.3, 2.3, 1.4])
    with c_nav_voltar:
        if st.button("⬅️ Voltar ao Portal (Hub)", use_container_width=True, key="btn_voltar_hub_top"):
            st.session_state.pagina_ativa = "hub"
            st.rerun()

    with c_nav_bread:
        st.markdown(f"""
        <div style="background: #FAF8F5; border: 1px solid #E2D7C7; border-left: 4px solid #781826; border-radius: 8px; padding: 0 14px; font-size: 0.88rem; color: #5A3825; height: 42px; display: flex; align-items: center;">
            <span style="color: #781826; font-family: 'Cinzel', serif; font-weight: bold;">☩ {info_atual['setor']}</span> 
            <span style="color: #C5A059; margin: 0 0.4rem;">›</span> 
            <strong style="color: #2B1810;">{info_atual['icone']} {info_atual['titulo']}</strong>
        </div>
        """, unsafe_allow_html=True)

    with c_nav_atalho:
        # Seletor rápido para alternar para qualquer outro módulo
        opcoes_atalho = {f"{v['icone']} {v['titulo']}": k for k, v in modulos_info.items() if (k != "gestao" or perfil == "catequista")}
        label_atual = f"{info_atual['icone']} {info_atual['titulo']}"
        lista_labels = list(opcoes_atalho.keys())
        idx_sel = lista_labels.index(label_atual) if label_atual in lista_labels else 0

        escolha_atalho = st.selectbox(
            "Ir direto para:",
            options=lista_labels,
            index=idx_sel,
            label_visibility="collapsed",
            key="sel_atalho_rapido"
        )
        if opcoes_atalho[escolha_atalho] != st.session_state.pagina_ativa:
            st.session_state.pagina_ativa = opcoes_atalho[escolha_atalho]
            st.rerun()

    st.write("")

    # Renderização do Módulo Ativo
    pag = st.session_state.pagina_ativa
    if pag == "jornada":
        home.render()
    elif pag == "encontros":
        encontros.render()
    elif pag == "gestao":
        if perfil == "catequista":
            gestao_catequistas.render()
        else:
            st.warning("Acesso restrito ao catequista administrador.")
    elif pag == "vigilia":
        vigilia_pascal.render()
    elif pag == "tratados":
        tratados_teologicos.render()
    elif pag == "vida_moral":
        vida_moral.render()
    elif pag == "confissao":
        confissao_e_reconciliacao.render()
    elif pag == "santa_missa":
        santa_missa.render()
    elif pag == "santo_terco":
        santo_terco.render()
    elif pag == "tesouro":
        tesouro_franciscano.render()
    elif pag == "oratorio":
        oracoes_e_liturgia.render()
    elif pag == "biblioteca":
        biblioteca_sacra.render()

    # Botão Inferior de Retorno ao Hub
    st.markdown("---")
    c_bot1, c_bot2, c_bot3 = st.columns([1, 2, 1])
    with c_bot2:
        if st.button("⬅️ Retornar ao Portal Principal (Hub)", use_container_width=True, key="btn_voltar_hub_bottom"):
            st.session_state.pagina_ativa = "hub"
            st.rerun()