# -*- coding: utf-8 -*-
"""
Módulo Principal: Página Inicial e Visão Geral Pastoral
Catequese da Igreja Católica Apostólica Romana — Diretório de Sorocaba
Hub de Consulta e Formação Doutrinal Aberta
"""

import streamlit as st
import database
from style import render_header, render_divider, render_hub_card, render_sector_header

def render():
    render_header(
        titulo="CATEQUESE DA IGREJA CATÓLICA APOSTÓLICA ROMANA",
        subtitulo="Diretório de Sorocaba • Hub de Consulta, Formação & Doutrina"
    )

    # Painel Acolhedor de Abertura do Hub
    st.markdown("""
    <div class="pergaminho-card-franciscano">
        <h3 style="color: #781826; margin-top: 0; display: flex; align-items: center; gap: 8px;">
            <span>☩</span> Paz e Bem! Seja bem-vindo ao Hub de Consulta da Catequese
        </h3>
        <p style="font-size: 1.15rem; line-height: 1.6; margin-bottom: 0.5rem; text-align: justify;">
            Este portal reúne o <strong>itinerário formativo completo da fé católica</strong> organizado pelo 
            <strong>Diretório de Sorocaba da Igreja Católica Apostólica Romana</strong>. 
            Desenvolvido como um <strong>espaço de livre consulta e estudo</strong>, aqui catequistas, catequisandos, 
            estudantes de teologia e qualquer fiel católico têm acesso direto e irrestrito ao acervo dos 
            <strong>40 Encontros</strong>, aos <strong>Tratados Teológicos</strong>, à <strong>Sagrada Liturgia</strong> e às 
            <strong>Fontes do Magistério da Igreja</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Guia Rápido de Utilização do Hub
    st.markdown("""
    <div class="pergaminho-card" style="border-left: 4px solid #C5A059; margin-top: 1rem;">
        <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
            🌟 Como utilizar este Hub de Consulta:
        </h4>
        <ul style="font-size: 1.05rem; line-height: 1.8; padding-left: 1.2rem; color: #2E1B10;">
            <li>📖 <strong>Os 40 Encontros:</strong> Acesse cada aula com fundamentação bíblica, Catecismo da Igreja Católica (CIC), roteiro detalhado, arte sacra e espiritualidade.</li>
            <li>🎯 <strong>Testes da Fé com Download em HTML:</strong> Responda às questões doutrinais de cada encontro, receba a nota instantânea com fundamentação teológica e <strong>baixe o teste completo em HTML</strong> para seu computador ou celular.</li>
            <li>✍️ <strong>Anotações Pessoais em HTML:</strong> Faça suas reflexões, anotações de estudo ou orações e <strong>baixe um arquivo HTML formatado</strong> (sem nada ser armazenado no servidor, com total privacidade).</li>
            <li>🏛️ <strong>Tratados & Doutrina:</strong> Estude aprofundadamente Mariologia, Cristologia, Santíssima Trindade, Vida Moral e o Sacramento da Reconciliação.</li>
            <li>⛪ <strong>Liturgia Viva:</strong> Contemple o passo a passo da Santa Missa, os Mistérios do Santo Terço e as orações do Tesouro Franciscano.</li>
        </ul>
        <div style="background: #FAF5EB; border: 1px dashed #C5A059; padding: 0.8rem 1rem; border-radius: 6px; font-size: 0.95rem; color: #5A3825; margin-top: 0.8rem;">
            🔒 <strong>Privacidade Total & Sem Necessidade de Cadastro:</strong> Não é preciso fazer login nem cadastrar senhas. O portal é 100% aberto para consulta imediata. Suas anotações e testes podem ser salvos diretamente em seus arquivos pessoais através do download em formato HTML.
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_divider("☩ OS 7 MÓDULOS TEMÁTICOS DA FORMAÇÃO CATEQUÉTICA ☩")

    # Panorama dos 7 Blocos Formativos dos 40 Encontros
    blocos_dados = [
        {
            "bloco": "Módulo 1: O Anúncio e o Encontro com a Palavra",
            "encontros": "Encontros 01 a 05",
            "desc": "A Bíblia Sagrada (Dei Verbum), o Magistério, a Tradição, a Criação do Mundo e o Plano de Salvação de Deus.",
            "icone": "📜",
            "accent": "accent-bordo"
        },
        {
            "bloco": "Módulo 2: A História da Salvação e as Alianças",
            "encontros": "Encontros 06 a 11",
            "desc": "De Abraão aos Profetas: a preparação da humanidade para a vinda do Salvador prometido.",
            "icone": "⛺",
            "accent": "accent-ouro"
        },
        {
            "bloco": "Módulo 3: Jesus Cristo, Verdadeiro Deus e Verdadeiro Homem",
            "encontros": "Encontros 12 a 18",
            "desc": "A Encarnação, Vida Pública, o Sermão da Montanha, a Paixão, Morte e a Ressurreição gloriosa do Senhor.",
            "icone": "✝️",
            "accent": "accent-bordo"
        },
        {
            "bloco": "Módulo 4: O Espírito Santo e a Santa Igreja Católica",
            "encontros": "Encontros 19 a 24",
            "desc": "Pentecostes, a fundação da Igreja por Cristo, as 4 marcas da Igreja, o Primado de Pedro e a Comunhão dos Santos.",
            "icone": "🕊️",
            "accent": "accent-franciscano"
        },
        {
            "bloco": "Módulo 5: Os Sete Sacramentos da Vida Cristã",
            "encontros": "Encontros 25 a 31",
            "desc": "Batismo, Crisma, Santíssima Eucaristia, Penitência, Unção dos Enfermos, Ordem e Matrimônio.",
            "icone": "⛪",
            "accent": "accent-ouro"
        },
        {
            "bloco": "Módulo 6: A Vida Moral em Cristo & Mandamentos",
            "encontros": "Encontros 32 a 36",
            "desc": "A Lei de Deus, a Consciência Moral, o Decálogo, as Bem-Aventuranças e o combate contra o pecado.",
            "icone": "⚖️",
            "accent": "accent-bordo"
        },
        {
            "bloco": "Módulo 7: A Oração do Cristão & Vigília Pascal",
            "encontros": "Encontros 37 a 40",
            "desc": "A Oração do Pai-Nosso, a Mãe Santíssima, a contemplação cristã e a celebração culminante da Noite Pascal.",
            "icone": "🕯️",
            "accent": "accent-ouro"
        }
    ]

    col_b1, col_b2 = st.columns(2)
    for idx, b in enumerate(blocos_dados):
        col_atual = col_b1 if idx % 2 == 0 else col_b2
        with col_atual:
            st.markdown(f"""
            <div class="pergaminho-card" style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
                    <span style="font-family: 'Cinzel', serif; font-weight: bold; color: #781826; font-size: 1.05rem;">
                        {b['icone']} {b['bloco']}
                    </span>
                    <span style="background: #F4EAD4; color: #5A3825; padding: 2px 8px; border-radius: 4px; font-size: 0.82rem; font-weight: bold;">
                        {b['encontros']}
                    </span>
                </div>
                <p style="font-size: 0.98rem; color: #3A2315; margin: 0; line-height: 1.5;">
                    {b['desc']}
                </p>
            </div>
            """, unsafe_allow_html=True)

    # Botão de Ação Rápida para Estudar
    c_ir1, c_ir2, c_ir3 = st.columns([1, 2, 1])
    with c_ir2:
        if st.button("📖 Acessar Diretamente os 40 Encontros 📖", type="primary", use_container_width=True, key="btn_home_to_enc"):
            st.session_state.pagina_ativa = "encontros"
            st.rerun()

    render_divider("☩ DIRETRIZES DO DIRETÓRIO DE SOROCABA ☩")

    col_esq, col_dir = st.columns([1.4, 1])

    with col_esq:
        st.markdown("""
        <div class="pergaminho-card">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                📜 Fidelidade ao Depósito da Fé (Depositum Fidei)
            </h4>
            <p style="font-size: 1.05rem; text-align: justify; line-height: 1.6;">
                A catequese da Igreja Católica não ensina opiniões humanas passageiras, mas transmite com fidelidade 
                o <strong>depósito sagrado da fé</strong> confiado aos Apóstolos. O tripé que sustenta toda a formação é composto por:
            </p>
            <ul style="font-size: 1.02rem; line-height: 1.7; padding-left: 1.2rem; color: #2E1B10;">
                <li><strong>Sagrada Escritura:</strong> A Palavra de Deus escrita sob a inspiração do Espírito Santo.</li>
                <li><strong>Sagrada Tradição:</strong> A transmissão viva da Palavra confiada à Igreja ao longo dos séculos.</li>
                <li><strong>Sagrado Magistério:</strong> A autoridade de ensinar em nome de Cristo exercida pelo Papa e pelos Bispos em comunhão com ele.</li>
            </ul>
            <div style="background: #F2E8DC; border-left: 4px solid #781826; padding: 0.8rem 1rem; border-radius: 4px; font-size: 0.98rem; font-style: italic; margin-top: 0.8rem;">
                <em>"Ide por todo o mundo e pregai o Evangelho a toda criatura. Quem crer e for batizado será salvo."</em> (Mc 16,15-16)
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pergaminho-card-bordo">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                🕊️ O Itinerário da Iniciação Cristã de Adultos (RICA)
            </h4>
            <ul style="font-size: 1.05rem; line-height: 1.7; padding-left: 1.2rem;">
                <li><strong>Pré-Catecumenato:</strong> Primeiro anúncio (Querigma) e acolhimento dos que buscam a fé.</li>
                <li><strong>Catecumenato:</strong> Período prolongado de catequese integral, oração e vivência comunitária (os 40 encontros).</li>
                <li><strong>Purificação e Iluminação:</strong> Tempo quaresmal de retiro e escrutínios espirituais.</li>
                <li><strong>Mistagogia:</strong> Aprofundamento pós-sacramental após a recepção dos sacramentos na solene Vigília Pascal.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_dir:
        import os
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_cruz = os.path.join(base_dir, "assets", "images", "encontro_15.jpg")
        if not os.path.exists(caminho_cruz):
            caminho_cruz = os.path.join("assets", "images", "encontro_15.jpg")
        if os.path.exists(caminho_cruz):
            st.image(caminho_cruz, caption="O Santo Crucifixo: 'Vai e restaura a Minha Igreja!'", use_container_width=True)

        st.markdown("""
        <div class="pilula-franciscana">
            <h4 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                🌿 Paz e Bem!
            </h4>
            <p style="font-style: italic; font-size: 1.1rem; line-height: 1.6; color: #3A2315;">
                "Senhor, fazei-me instrumento de vossa paz. Onde houver ódio, que eu leve o amor; onde houver erro, que eu leve a verdade."
            </p>
            <div style="text-align: right; font-weight: bold; font-size: 0.95rem; color: #5A3825;">
                — Oração da Paz
            </div>
            <hr style="border: 0; border-top: 1px solid #D8C8B4; margin: 0.8rem 0;">
            <p style="font-size: 0.95rem; color: #4A3525; margin: 0;">
                <strong>Diretório de Sorocaba:</strong> Que a luz do Evangelho ilumine cada coração na busca dos Santos Sacramentos.
            </p>
        </div>
        """, unsafe_allow_html=True)