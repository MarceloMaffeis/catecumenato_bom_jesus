# -*- coding: utf-8 -*-
"""
Módulo Oratório e Devocionário Católico & Franciscano
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
import database
from style import render_divider

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            🕊️ Oratório Litúrgico & Devocionário
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            Orações dos Santos, Espiritualidade Franciscana e Exame de Consciência
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_devocionario, tab_exame, tab_latim = st.tabs([
        "🙏 Devocionário do Catecúmeno",
        "⚖️ Guia de Exame de Consciência (Confissão)",
        "🏛️ Orações Clássicas em Latim & Português"
    ])

    # 1. Devocionário
    with tab_devocionario:
        categorias = ["Todas as Orações"] + database.get_categorias_oracoes()
        cat_escolhida = st.selectbox("Filtrar Orações por Categoria:", categorias)

        oracoes = database.get_oracoes(categoria=cat_escolhida)

        for o in oracoes:
            with st.expander(f"✨ {o['titulo']} ({o['categoria']})", expanded=(o['titulo'] == "Oração da Paz (Oração de São Francisco)")):
                st.markdown(f"""
                <div style="font-size: 0.95rem; color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.5rem;">
                    Origem / Autor: {o['origem_autor']}
                </div>
                """, unsafe_allow_html=True)

                # Formatar o texto com quebras suaves
                texto_formatado = o['texto'].replace('\n', '<br>')
                st.markdown(f"""
                <div class="pergaminho-card" style="font-size: 1.15rem; line-height: 1.8; color: #2C1810; font-style: italic;">
                    {texto_formatado}
                </div>
                """, unsafe_allow_html=True)

    # 2. Exame de Consciência
    with tab_exame:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            Guia Católico para a Santa Confissão (Sacramento da Reconciliação)
        </h4>
        <p style="font-size: 1.05rem; line-height: 1.6;">
            Antes de receber os sacramentos da Páscoa (ou para a confissão periódica), cada catecúmeno deve fazer 
            um exame de consciência sereno, sincero e sem desespero diante do amor misericordioso do Pai.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pergaminho-card">
            <h5 style="color: #781826; margin-top: 0; font-family: 'Cinzel', serif;">
                I. Meus deveres para com Deus (1º ao 3º Mandamento)
            </h5>
            <ul style="font-size: 1rem; line-height: 1.7;">
                <li>Coloquei coisas do mundo (dinheiro, vaidade, vícios, trabalho) acima de Deus?</li>
                <li>Consultei práticas contrárias à fé (astrologia, cartomancia, espiritismo, superstições)?</li>
                <li>Pronunciei o santo nome de Deus em vão, com blasfêmias ou em piadas desrespeitosas?</li>
                <li>Faltei deliberadamente à Santa Missa aos domingos ou festas de preceito por preguiça ou comodismo?</li>
                <li>Comunguei alguma vez sabendo que estava em pecado mortal grave sem ter me confessado?</li>
            </ul>

            <h5 style="color: #781826; margin-top: 1.2rem; font-family: 'Cinzel', serif;">
                II. Meus deveres para com o próximo (4º ao 8º Mandamento)
            </h5>
            <ul style="font-size: 1rem; line-height: 1.7;">
                <li>Fui desrespeitoso, agressivo ou negligente com meus pais, cônjuge ou filhos?</li>
                <li>Nutri ódio, mágoa, rancor ou recusei o perdão a alguém que me ofendeu?</li>
                <li>Causei escândalo ou induzi outros ao pecado através do meu exemplo ou conselho?</li>
                <li>Fui infiel em meu matrimônio ou consenti em pensamentos, palavras e atos impuros?</li>
                <li>Peguei coisas que não me pertenciam, fui desonesto nos negócios ou não paguei o que devia?</li>
                <li>Menti, caluniei, difamei ou fiz fofocas destruindo a honra de outras pessoas?</li>
            </ul>

            <h5 style="color: #781826; margin-top: 1.2rem; font-family: 'Cinzel', serif;">
                III. Meus deveres interiores e de vida cristã (9º e 10º Mandamento)
            </h5>
            <ul style="font-size: 1rem; line-height: 1.7;">
                <li>Alimentei inveja do bem, do sucesso ou da família dos outros?</li>
                <li>Fui egoísta, fechando os olhos às necessidades dos pobres, aflitos e necessitados?</li>
                <li>Vivo na soberba, desprezando as pessoas simples?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 Lembre-se: 'O padre no confessionário não é um juiz vingativo, mas o abraço do Pai misericordioso que espera o filho pródigo com amor'.")

    # 3. Latim & Português
    with tab_latim:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            As Grandes Orações da Igreja em sua Língua Mãe (Latim) e Português
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            O latim preserva a sacralidade universal e a unidade da Igreja em todos os séculos e nações.
        </p>
        """, unsafe_allow_html=True)

        col_lat1, col_lat2 = st.columns(2)
        with col_lat1:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">Pater Noster</h5>
                <p style="font-style: italic; line-height: 1.7;">
                    Pater noster, qui es in caelis,<br>
                    sanctificetur nomen tuum.<br>
                    Adveniat regnum tuum.<br>
                    Fiat voluntas tua,<br>
                    sicut in caelo et in terra.<br>
                    Panem nostrum quotidianum da nobis hodie,<br>
                    et dimitte nobis debita nostra,<br>
                    sicut et nos dimittimus debitoribus nostris.<br>
                    Et ne nos inducas in tentationem,<br>
                    sed libera nos a malo. Amen.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col_lat2:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">Ave Maria</h5>
                <p style="font-style: italic; line-height: 1.7;">
                    Ave Maria, gratia plena,<br>
                    Dominus tecum.<br>
                    Benedicta tu in mulieribus,<br>
                    et benedictus fructus ventris tui, Iesus.<br>
                    Sancta Maria, Mater Dei,<br>
                    ora pro nobis peccatoribus,<br>
                    nunc et in hora mortis nostrae. Amen.
                </p>
            </div>
            """, unsafe_allow_html=True)