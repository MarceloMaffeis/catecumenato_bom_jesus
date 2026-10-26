# -*- coding: utf-8 -*-
"""
Catequese da Igreja Católica Apostólica Romana — Diretório de Sorocaba
Hub de Consulta, Formação Doutrinal, Liturgia e Sagrada Tradição
Acesso Aberto para Fiéis, Catequistas, Catequisandos e Estudantes da Fé
"""

import streamlit as st
import importlib
import database
importlib.reload(database)
import style
from modules import (
    home, encontros, biblioteca_sacra, oracoes_e_liturgia,
    santa_missa, santo_terco, tratados_teologicos, confissao_e_reconciliacao,
    tesouro_franciscano, vida_moral, vigilia_pascal
)

# Configuração da Página
st.set_page_config(
    page_title="Catequese da Igreja Católica Apostólica Romana | Diretório de Sorocaba",
    page_icon="assets/favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Aplicar estilos visuais sacros e litúrgicos
style.apply_sacred_style()

# Inicializar Banco de Dados (Leitura dos 40 encontros e acervo)
database.init_db()

# Inicializar estado da sessão
if "pagina_ativa" not in st.session_state:
    st.session_state.pagina_ativa = "hub"

# ==============================================================================
# CABEÇALHO SUPERIOR INSTITUCIONAL (DIRETÓRIO DE SOROCABA)
# ==============================================================================
col_top_logo, col_top_user = st.columns([3.5, 1.5])

with col_top_logo:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 14px; padding: 4px 0;">
        <span style="font-size: 2.3rem; color: #781826; line-height: 1;">☩</span>
        <div>
            <div style="font-family: 'Cinzel', serif; font-weight: 700; font-size: 1.15rem; color: #781826; letter-spacing: 0.5px; line-height: 1.2;">
                CATEQUESE DA IGREJA CATÓLICA APOSTÓLICA ROMANA
            </div>
            <div style="font-size: 0.82rem; color: #5A3825; font-family: 'Cinzel', serif; letter-spacing: 1px; margin-top: 2px;">
                DIRETÓRIO DE SOROCABA &bull; HUB DE CONSULTA ABERTA &bull; <strong style="color: #781826;">PAZ E BEM!</strong>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_top_user:
    st.markdown("""
    <div style="background: #FFFFFF; border: 1px solid #E8E0D2; border-left: 4px solid #C5A059; padding: 6px 12px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">
            <span style="background: #FFF8E1; color: #8C6A1D; font-size: 0.70rem; padding: 2px 6px; border-radius: 4px; font-weight: bold; font-family: 'Cinzel', serif;">📖 CONSULTA LIVRE</span>
            <span style="font-size: 0.74rem; color: #8C6A1D; font-weight: bold;">SOROCABA</span>
        </div>
        <div style="font-weight: 700; color: #2E1B10; font-size: 0.88rem; margin-top: 2px;">Diretório Catequético</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""<div style="margin: 0.7rem 0 1.2rem 0; height: 1px; background: linear-gradient(to right, #781826, #C5A059, transparent);"></div>""", unsafe_allow_html=True)

# Mapa de metadados dos módulos para roteamento e atalhos rápidos
modulos_info = {
    "jornada": {"titulo": "Guia & Itinerário", "setor": "Iniciação & Formação", "icone": "🏠"},
    "encontros": {"titulo": "Os 40 Encontros", "setor": "Iniciação & Formação", "icone": "📖"},
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

    # Banner de Acolhida & Apresentação
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FAF8F5 0%, #F5ECE0 100%); border: 1px solid #D8C8B4; border-left: 6px solid #C5A059; border-radius: 12px; padding: 14px 20px; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(120,24,38,0.04);">
        <h3 style="color: #781826; font-family: 'Cinzel', serif; margin: 0; font-size: 1.2rem;">
            ☩ Bem-vindo ao Hub de Consulta da Fé Católica — Diretório de Sorocaba
        </h3>
        <p style="color: #5A3825; font-size: 0.96rem; margin: 5px 0 0 0; font-style: italic;">
            Acervo doutrinal, bíblico, litúrgico e formativo para livre consulta de catequistas, catequisandos e fiéis. 
            Estude os encontros, realize avaliações com download em HTML e baixe suas reflexões com total privacidade.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: #5A3825; font-size: 1rem; margin: 10px 0 20px 0;'>✨ <strong>Selecione o módulo temático</strong> para iniciar sua consulta:</p>", unsafe_allow_html=True)

    # ==========================================================================
    # SETOR 1: 🎓 INICIAÇÃO CRISTÃ & FORMAÇÃO
    # ==========================================================================
    style.render_sector_header("🎓", "Setor 1 — Iniciação Cristã & Formação", "A caminhada dos 40 encontros, diretrizes da Igreja e a celebração dos Santos Sacramentos")

    c1, c2, c3 = st.columns(3)
    with c1:
        style.render_hub_card("🏠", "Guia & Itinerário", "Visão geral dos 40 encontros, os 7 blocos temáticos e diretrizes catequéticas.", "accent-bordo")
        if st.button("▶ ACESSAR: Guia & Itinerário 🏠", use_container_width=True, key="hub_jorn"):
            st.session_state.pagina_ativa = "jornada"
            st.rerun()

    with c2:
        style.render_hub_card("📖", "Os 40 Encontros", "Bíblia, Magistério, apostilas, anotações e testes com download em HTML.", "accent-ouro")
        if st.button("▶ ACESSAR: Os 40 Encontros 📖", use_container_width=True, key="hub_enc"):
            st.session_state.pagina_ativa = "encontros"
            st.rerun()

    with c3:
        style.render_hub_card("🕯️", "Vigília Pascal", "Rito dos sacramentos pascais, testemunho cristão e requisitos de padrinhos.", "accent-franciscano")
        if st.button("▶ ACESSAR: Vigília Pascal 🕯️", use_container_width=True, key="hub_vig"):
            st.session_state.pagina_ativa = "vigilia"
            st.rerun()

    # ==========================================================================
    # SETOR 2: 🏛️ TEOLOGIA & DOUTRINA CATÓLICA
    # ==========================================================================
    style.render_sector_header("🏛️", "Setor 2 — Teologia & Doutrina Católica", "Fundamentos dogmáticos, tratados dos mistérios divinos, moral cristã e reconciliação")

    c1, c2, c3 = st.columns(3)
    with c1:
        style.render_hub_card("🏛️", "Tratados Teológicos", "Mariologia, Cristologia, Santíssima Trindade, Igreja e Anjos.", "accent-ouro")
        if st.button("▶ ACESSAR: Tratados Teológicos 🏛️", use_container_width=True, key="hub_trat"):
            st.session_state.pagina_ativa = "tratados"
            st.rerun()

    with c2:
        style.render_hub_card("📜", "Vida Moral & Virtudes", "Os 10 Mandamentos, bem-aventuranças e vida cristã prática.", "accent-bordo")
        if st.button("▶ ACESSAR: Vida Moral & Virtudes 📜", use_container_width=True, key="hub_moral"):
            st.session_state.pagina_ativa = "vida_moral"
            st.rerun()

    with c3:
        style.render_hub_card("🕊️", "Confissão & Penitência", "Exame de consciência profundo e rito do perdão dos pecados.", "accent-franciscano")
        if st.button("▶ ACESSAR: Confissão & Penitência 🕊️", use_container_width=True, key="hub_conf"):
            st.session_state.pagina_ativa = "confissao"
            st.rerun()

    # ==========================================================================
    # SETOR 3: ⛪ LITURGIA & ORAÇÃO
    # ==========================================================================
    style.render_sector_header("⛪", "Setor 3 — Liturgia & Oração", "A celebração eucarística, o Rosário contemplativo e a espiritualidade dos Santos")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        style.render_hub_card("⛪", "A Santa Missa", "Passo a passo dos ritos, paramentos, cores e mistério eucarístico.", "accent-bordo")
        if st.button("▶ ACESSAR: A Santa Missa ⛪", use_container_width=True, key="hub_missa"):
            st.session_state.pagina_ativa = "santa_missa"
            st.rerun()

    with c2:
        style.render_hub_card("📿", "O Santo Terço", "Mistérios do dia, meditações bíblicas e orações marianas.", "accent-ouro")
        if st.button("▶ ACESSAR: O Santo Terço 📿", use_container_width=True, key="hub_terco"):
            st.session_state.pagina_ativa = "santo_terco"
            st.rerun()

    with c3:
        style.render_hub_card("🌿", "Tesouro Franciscano", "Cântico das Criaturas, orações de paz e testemunho dos santos.", "accent-franciscano")
        if st.button("▶ ACESSAR: Tesouro Franciscano 🌿", use_container_width=True, key="hub_tesouro"):
            st.session_state.pagina_ativa = "tesouro"
            st.rerun()

    with c4:
        style.render_hub_card("🕊️", "Oratório & Devoção", "Devocionário tradicional, liturgia diária e salmos de louvor.", "accent-verde")
        if st.button("▶ ACESSAR: Oratório & Devoção 🕊️", use_container_width=True, key="hub_orat"):
            st.session_state.pagina_ativa = "oratorio"
            st.rerun()

    # ==========================================================================
    # SETOR 4: 📜 PESQUISA & FONTES SACRAS
    # ==========================================================================
    style.render_sector_header("📜", "Setor 4 — Pesquisa & Fontes Sacras", "Acesso ao magistério da Igreja, Sagrada Escritura e Tradição Católica")

    c_bib1, c_bib2 = st.columns([1.5, 2.5])
    with c_bib1:
        style.render_hub_card("📜", "Biblioteca Sacra", "Catecismo da Igreja Católica (CIC), Bíblia Sagrada e Concílios.", "accent-bordo")
        if st.button("▶ ACESSAR: Biblioteca Sacra & Fontes 📜", use_container_width=True, key="hub_biblio"):
            st.session_state.pagina_ativa = "biblioteca"
            st.rerun()

    with c_bib2:
        st.markdown("""
        <div class="hub-card-static" style="display: flex; flex-direction: column; justify-content: center; height: 180px;">
            <div style="margin-bottom: 6px;">
                <span style="background: #FAF5EB; border: 1px solid #C5A059; color: #781826; padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-family: 'Cinzel', serif; font-weight: bold;">
                    🏛️ FONTES DA VERDADE CATÓLICA
                </span>
            </div>
            <div style="font-family: 'Cinzel', serif; color: #781826; font-size: 1.05rem; font-weight: bold;">
                O Depósito Sagrado da Fé ao Seu Alcance
            </div>
            <p style="font-size: 0.95rem; color: #5A3825; margin: 6px 0 0 0; line-height: 1.5;">
                Acesso direto e irrestrito ao <strong>Catecismo da Igreja Católica (CIC)</strong>, à <strong>Sagrada Bíblia Canônica</strong> de 73 livros, 
                aos <strong>Concílios Ecumênicos</strong> e aos escritos dos Santos Doutores da Igreja.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ==========================================================================
    # PAINÉIS INFORMATIVOS LITÚRGICOS (LEITURA E ESPIRITUALIDADE)
    # ==========================================================================
    style.render_sector_header("📌", "Diretório Litúrgico & Bênção Tradicional", "Orientações da Igreja Católica Apostólica Romana e oração de paz")

    c_itin, c_benc = st.columns(2)
    with c_itin:
        st.markdown("""
        <div class="hub-card-static">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="color: #781826; font-family: 'Cinzel', serif; font-weight: 700; font-size: 0.92rem;">
                    ⏳ DIRETÓRIO DE SOROCABA
                </span>
                <span style="background: #F4EAD4; color: #5A3825; padding: 2px 8px; border-radius: 4px; font-size: 0.70rem; font-weight: bold; font-family: 'Cinzel', serif;">
                    ℹ️ PAINEL INFORMATIVO
                </span>
            </div>
            <div style="color: #4A2E1B; font-size: 0.92rem; line-height: 1.6;">
                • <strong>Itinerário Catequético:</strong> 40 Encontros de Formação Integral da Fé.<br>
                • <strong>Apresentação à Comunidade:</strong> 4º Domingo da Quaresma (Domingo Laetare).<br>
                • <strong>Sacramentos Pascais:</strong> Batismo, Crisma e Eucaristia na Vigília Pascal.
            </div>
            <div style="font-size: 0.80rem; color: #8C6A1D; font-style: italic; margin-top: 8px;">
                Iniciação Cristã da Igreja Católica Apostólica Romana
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_benc:
        st.markdown("""
        <div class="hub-card-static" style="text-align: center;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="color: #8C6A1D; font-family: 'Cinzel', serif; font-weight: 700; font-size: 0.92rem;">
                    🕊️ BÊNÇÃO TRADICIONAL
                </span>
                <span style="background: #F4EAD4; color: #5A3825; padding: 2px 8px; border-radius: 4px; font-size: 0.70rem; font-weight: bold; font-family: 'Cinzel', serif;">
                    ℹ️ PAINEL INFORMATIVO
                </span>
            </div>
            <div style="font-size: 0.95rem; color: #5A3825; font-style: italic; line-height: 1.5; margin: 10px 0;">
                "O Senhor te abençoe e te guarde.<br>Mostre-te a sua face e te dê a paz!" ☩
            </div>
            <div style="font-size: 0.82rem; color: #781826; font-family: 'Cinzel', serif; font-weight: bold;">
                São Francisco de Assis • Paz e Bem!
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# ESTADO B: DENTRO DE UM MÓDULO (BARRA DE TOPO COM RETORNO E ATALHOS RÁPIDOS)
# ==============================================================================
else:
    info_atual = modulos_info.get(st.session_state.pagina_ativa, {"titulo": "Módulo", "setor": "Catequese", "icone": "☩"})

    # Barra Superior de Navegação
    c_nav_voltar, c_nav_bread, c_nav_atalho = st.columns([1.3, 2.3, 1.4])
    with c_nav_voltar:
        if st.button("⬅️ Voltar ao Hub Principal", use_container_width=True, key="btn_voltar_hub_top"):
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
        opcoes_atalho = {f"{v['icone']} {v['titulo']}": k for k, v in modulos_info.items()}
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
        if st.button("⬅️ Retornar ao Hub Principal", use_container_width=True, key="btn_voltar_hub_bottom"):
            st.session_state.pagina_ativa = "hub"
            st.rerun()