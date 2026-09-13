# -*- coding: utf-8 -*-
"""
Módulo Principal: Página Inicial e Visão Geral Pastoral
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
import database
from style import render_header, render_divider

def render():
    render_header(
        titulo="CATECUMENATO DE ADULTOS",
        subtitulo="Iniciação Cristã • Encontro Pessoal com Jesus Cristo"
    )

    # Saudação Franciscana e Acolhida
    st.markdown("""
    <div class="pergaminho-card-franciscano">
        <h3 style="color: #5A3825; margin-top: 0; display: flex; align-items: center; gap: 8px;">
            <span>☩</span> Paz e Bem, caríssimo catequista e irmão em Cristo!
        </h3>
        <p style="font-size: 1.15rem; line-height: 1.6; margin-bottom: 0.5rem;">
            Seja bem-vindo ao portal de formação catequética e gestão pastoral da 
            <strong>Paróquia Bom Jesus dos Aflitos de Sorocaba/SP</strong>, confiada ao pastoreio dos 
            <strong>Frades Menores Franciscanos</strong>. 
            Este espaço foi concebido com zelo divino e reverência católica para orientar a caminhada de fé dos adultos 
            rumo aos sacramentos da Iniciação Cristã: <em>Batismo, Crisma e Santíssima Eucaristia</em>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Métricas Pastorais Dinâmicas
    st.markdown("### 📊 Panorama da Turma Paroquial")
    catecumenos = database.get_catecumenos(filtro_ativo=True)
    total_cat = len(catecumenos)

    precisam_batismo = sum(1 for c in catecumenos if c["batizado"] == 0)
    precisam_eucaristia = sum(1 for c in catecumenos if c["primeira_eucaristia"] == 0)
    precisam_crisma = sum(1 for c in catecumenos if c["crismado"] == 0)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Catecúmenos Inscritos", value=total_cat, help="Adultos em acompanhamento ativo na turma")
    with col2:
        st.metric(label="Rumo ao Batismo", value=precisam_batismo, delta="Vigília Pascal", delta_color="normal")
    with col3:
        st.metric(label="Rumo à 1ª Eucaristia", value=precisam_eucaristia)
    with col4:
        st.metric(label="Rumo à Crisma", value=precisam_crisma)

    render_divider("☩ AS DIRETRIZES DA CATEQUESE DE ADULTOS ☩")

    col_esq, col_dir = st.columns([1.4, 1])

    with col_esq:
        st.markdown("""
        <div class="pergaminho-card">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                📜 Objetivo e Missão do Catecumenato
            </h4>
            <p style="font-size: 1.05rem; text-align: justify; line-height: 1.6;">
                A catequese de adultos é um dos maiores desafios e bênçãos da Igreja. Os catequistas devem estar 
                profundamente preparados para transmitir com segurança o <strong>depósito sagrado da fé</strong> e, 
                acima de tudo, proporcionar aos catecúmenos uma experiência real de <strong>encontro pessoal com Cristo</strong>.
            </p>
            <p style="font-size: 1.05rem; text-align: justify; line-height: 1.6;">
                Nossa missão vai além da sala de aula: busca despertar o compromisso dos catecúmenos com o Evangelho 
                no mundo do trabalho (testemunho), na comunidade eclesial (participação nas pastorais) e na missão 
                como discípulos missionários.
            </p>
            <div style="background: #F2E8DC; border-left: 4px solid #781826; padding: 0.8rem 1rem; border-radius: 4px; font-size: 0.98rem; font-style: italic;">
                <strong>Atenção pastoral crucial:</strong> Deve-se combater com carinho qualquer mentalidade 
                meramente sacramentalista. O Catecumenato não é um cursinho para receber um diploma, mas a gestação de uma vida nova em Cristo.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pergaminho-card-bordo">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                🕊️ O Rito Litúrgico Tradicional
            </h4>
            <ul style="font-size: 1.05rem; line-height: 1.7; padding-left: 1.2rem;">
                <li><strong>Apresentação à Comunidade:</strong> Conforme antiga Tradição da Igreja desde o século II, os catecúmenos são apresentados solenemente no <em>4º Domingo da Quaresma (Domingo Laetare)</em>.</li>
                <li><strong>Recepção dos Divinos Mistérios:</strong> O Batismo, a Crisma e a Eucaristia são celebrados na solene <em>Vigília Pascal (Sábado Santo)</em>.</li>
                <li><strong>O Querigma e o Retiro Quaresmal:</strong> O anúncio primordial do amor salvífico de Cristo permeia todo o ano e culmina no Retiro Espiritual da Quaresma.</li>
                <li><strong>Jovens de 15 anos:</strong> Realizam 1 ano de Pré-Catecumenato com acompanhamento e retiros. A partir de 16 anos, integram-se diretamente com os demais adultos.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_dir:
        st.markdown("""
        <div class="pilula-franciscana">
            <h4 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                🌿 Sabedoria Franciscana
            </h4>
            <p style="font-style: italic; font-size: 1.1rem; line-height: 1.6; color: #3A2315;">
                "Comece fazendo o que é necessário, depois o que é possível, e de repente você estará fazendo o impossível."
            </p>
            <div style="text-align: right; font-weight: bold; font-size: 0.95rem; color: #5A3825;">
                — São Francisco de Assis
            </div>
            <hr style="border: 0; border-top: 1px solid #D8C8B4; margin: 1rem 0;">
            <p style="font-size: 0.95rem; color: #4A3525;">
                <strong>Oração do Catequista:</strong> Coloque aos pés do Bom Jesus dos Aflitos cada catecúmeno pelo nome antes de ministrar os encontros semanais.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pergaminho-card">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                ⚡ Atalhos Rápidos
            </h4>
            <p style="font-size: 0.98rem; margin-bottom: 0.8rem;">Acesse diretamente as seções do portal:</p>
            <ul style="font-size: 1rem; line-height: 1.8; list-style-type: none; padding-left: 0;">
                <li>📖 <strong>40 Encontros:</strong> Consulta integral do currículo</li>
                <li>👥 <strong>Chamada e Catecúmenos:</strong> Gestão da turma e frequência</li>
                <li>📜 <strong>Biblioteca Sacra:</strong> CIC, Bíblia e Magistério</li>
                <li>🕊️ <strong>Oratório:</strong> Orações católicas e franciscanas</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)