# -*- coding: utf-8 -*-
"""
Módulo do Santo Terço e da Devoção Mariana
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
from datetime import datetime
from style import render_divider

DIAS_SEMANA_NOMES = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

MISTERIOS_DATA = {
    "Mistérios Gozosos": {
        "dias": "Segundas-feiras e Sábados",
        "cor": "#C5A059",
        "tema": "A Infância de Jesus e a Alegria da Encarnação",
        "dezenas": [
            ("1ª Dezena", "A Anunciação do Arcanjo Gabriel à Virgem Maria (Lc 1,26-38)", "Fruto da contemplação: A virtude da Humildade e a docilidade ao plano de Deus."),
            ("2ª Dezena", "A Visitação de Nossa Senhora à sua prima Santa Isabel (Lc 1,39-56)", "Fruto da contemplação: O amor fraterno e o serviço diligente aos necessitados."),
            ("3ª Dezena", "O Nascimento de Nosso Senhor Jesus Cristo na gruta de Belém (Lc 2,1-20)", "Fruto da contemplação: O desapego das coisas do mundo e a santa pobreza de coração."),
            ("4ª Dezena", "A Apresentação do Menino Jesus no Templo de Jerusalém (Lc 2,21-38)", "Fruto da contemplação: A pureza de corpo e alma e a santa obediência."),
            ("5ª Dezena", "A Perda e o Encontro de Jesus no Templo entre os doutores da Lei (Lc 2,41-52)", "Fruto da contemplação: O zelo pelas coisas de Deus e a perseverança em procurar a Cristo.")
        ]
    },
    "Mistérios Luminosos": {
        "dias": "Quintas-feiras",
        "cor": "#8A6B2D",
        "tema": "A Vida Pública de Jesus e a Luz do Evangelho",
        "dezenas": [
            ("1ª Dezena", "O Batismo de Jesus no Rio Jordão pela mão de João Batista (Mt 3,13-17)", "Fruto da contemplação: A fidelidade às promessas batismais e a docilidade ao Espírito Santo."),
            ("2ª Dezena", "A Auto-revelação de Jesus e o primeiro milagre nas Bodas de Caná (Jo 2,1-11)", "Fruto da contemplação: A confiança cega na intercessão de Maria ('Fazei tudo o que Ele vos disser')."),
            ("3ª Dezena", "O Anúncio do Reino de Deus e o chamado urgente à Conversão (Mc 1,14-15)", "Fruto da contemplação: O arrependimento sincero dos pecados e a vida de penitência cristã."),
            ("4ª Dezena", "A Gloriosa Transfiguração de Jesus no Monte Tabor (Lc 9,28-36)", "Fruto da contemplação: O desejo da oração contemplativa e a busca pela santidade."),
            ("5ª Dezena", "A Instituição da Santíssima Eucaristia na Última Ceia (Mt 26,26-29)", "Fruto da contemplação: A devoção fervorosa à Sagrada Comunhão e a reverência diante do Altar.")
        ]
    },
    "Mistérios Dolorosos": {
        "dias": "Terças e Sextas-feiras",
        "cor": "#781826",
        "tema": "A Sagrada Paixão e Morte Redentora de Cristo",
        "dezenas": [
            ("1ª Dezena", "A Agonia mortal de Jesus no Horto das Oliveiras / Getsêmani (Lc 22,39-46)", "Fruto da contemplação: A contrição perfeita de nossos pecados e a submissão à vontade do Pai."),
            ("2ª Dezena", "A Sangrenta Flagelação de Jesus atado à coluna de pedra (Jo 19,1)", "Fruto da contemplação: A mortificação dos sentidos e a pureza corporal."),
            ("3ª Dezena", "A Coroação de Espinhos e as zombarias feitas ao Rei dos Reis (Mt 27,27-31)", "Fruto da contemplação: A vitória sobre o orgulho e o desprezo das glórias passageiras do mundo."),
            ("4ª Dezena", "Jesus carrega a pesada Cruz a caminho do Monte Calvário (Jo 19,16-17)", "Fruto da contemplação: A paciência cristã nas tribulações e nas cruzes de cada dia."),
            ("5ª Dezena", "A Crucificação e Morte de Nosso Senhor Jesus Cristo na Cruz (Jo 19,18-30)", "Fruto da contemplação: O perdão generoso aos inimigos e o amor heroico pelas almas.")
        ]
    },
    "Mistérios Gloriosos": {
        "dias": "Quartas-feiras e Domingos",
        "cor": "#C5A059",
        "tema": "A Triunfante Ressurreição e a Glória Eterna",
        "dezenas": [
            ("1ª Dezena", "A Triunfante Ressurreição de Jesus dentre os mortos ao terceiro dia (Mt 28,1-10)", "Fruto da contemplação: Uma fé viva, inabalável e a alegria pascal no coração."),
            ("2ª Dezena", "A Gloriosa Ascensão de Jesus aos Céus diante de Seus discípulos (At 1,6-11)", "Fruto da contemplação: A santa esperança e o anseio da Pátria Celeste definitiva."),
            ("3ª Dezena", "A Descida prodigiosa do Espírito Santo em Pentecostes sobre a Virgem e os Apóstolos (At 2,1-4)", "Fruto da contemplação: O zelo apostólico e o amor ardente de caridade pelas almas."),
            ("4ª Dezena", "A Bem-Aventurada Assunção de Nossa Senhora em corpo e alma aos Céus (Ap 12,1)", "Fruto da contemplação: A união perpétua com Deus e a graça de uma boa e santa morte."),
            ("5ª Dezena", "A Solene Coroação de Maria Santíssima como Rainha do Céu e da Terra (Ap 12,1-17)", "Fruto da contemplação: A confiança filial inabalável na proteção maternal da Virgem Maria.")
        ]
    }
}

def get_misterio_do_dia(weekday_idx):
    # weekday: 0=Seg, 1=Ter, 2=Qua, 3=Qui, 4=Sex, 5=Sab, 6=Dom
    if weekday_idx in [0, 5]: # Seg, Sab
        return "Mistérios Gozosos"
    elif weekday_idx in [1, 4]: # Ter, Sex
        return "Mistérios Dolorosos"
    elif weekday_idx == 3: # Qui
        return "Mistérios Luminosos"
    else: # Qua (2) e Dom (6)
        return "Mistérios Gloriosos"

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            📿 O Santo Terço Passo a Passo
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            Contemplando os Mistérios de Jesus com os Olhos e o Coração de Maria
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Identificação do dia atual
    hoje = datetime.now()
    dia_semana_num = hoje.weekday()
    dia_semana_nome = DIAS_SEMANA_NOMES[dia_semana_num]
    misterio_hoje = get_misterio_do_dia(dia_semana_num)

    col_img_terco, col_txt_terco = st.columns([1, 1.8])
    with col_img_terco:
        import os
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_maria = os.path.join(base_dir, "assets", "images", "encontro_40.jpg")
        if not os.path.exists(caminho_maria):
            caminho_maria = os.path.join("assets", "images", "encontro_40.jpg")
        if os.path.exists(caminho_maria):
            st.image(caminho_maria, caption="Nossa Senhora, Rainha do Santo Rosário — Murillo", use_container_width=True)
    with col_txt_terco:
        st.markdown(f"""
        <div class="pergaminho-card-bordo" style="height: 100%;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <span style="font-family: 'Cinzel', serif; color: #781826; font-weight: bold; font-size: 1.15rem;">
                    📅 Hoje é {dia_semana_nome}
                </span>
                <span style="background: #781826; color: white; padding: 3px 12px; border-radius: 12px; font-family: 'Cinzel', serif; font-size: 0.9rem;">
                    MISTÉRIO DO DIA: {misterio_hoje.upper()}
                </span>
            </div>
            <p style="font-size: 1.05rem; margin-top: 0.6rem; color: #3A2315;">
                {MISTERIOS_DATA[misterio_hoje]['tema']}. 
                A oração diária do Terço é a arma espiritual mais poderosa legada por Nossa Senhora para a paz na família e no mundo.
            </p>
        </div>
        """, unsafe_allow_html=True)

    tab_passos, tab_misterios, tab_promessas = st.tabs([
        "📖 Como Rezar o Terço (Esquema das Contas)",
        "✨ Meditação dos 4 Mistérios",
        "📜 As 15 Promessas de Nossa Senhora"
    ])

    # 1. Esquema das Contas
    with tab_passos:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            Roteiro de Oração nas Contas do Terço
        </h4>
        """, unsafe_allow_html=True)

        col_p1, col_p2 = st.columns([1.1, 1])
        with col_p1:
            st.markdown("""
            <div class="pergaminho-card">
                <ol style="line-height: 1.8; font-size: 1.05rem; padding-left: 1.2rem;">
                    <li><strong>Na Cruz:</strong> Sinal da Cruz + Símbolo dos Apóstolos (<em>Creio</em>).</li>
                    <li><strong>Na 1ª Conta Grande:</strong> Um <em>Pai Nosso</em> em louvor a Deus Pai.</li>
                    <li><strong>Nas 3 Primeiras Contas Pequenas:</strong> Três <em>Ave Marias</em>, pedindo o aumento das virtudes teologais:
                        <br>• 1ª Ave Maria: em honra a Deus Pai (pedindo o aumento da Fé).
                        <br>• 2ª Ave Maria: em honra a Deus Filho (pedindo a firmeza da Esperança).
                        <br>• 3ª Ave Maria: em honra ao Espírito Santo (pedindo a plenitude da Caridade).
                    </li>
                    <li><strong>No Espaço seguinte:</strong> Um <em>Glória ao Pai</em> e a <em>Jaculatória de Fátima</em>:
                        <br><em>"Ó meu Jesus, perdoai-nos, livrai-nos do fogo do inferno, levai as almas todas para o Céu e socorrei principalmente as que mais precisarem da Vossa misericórdia."</em>
                    </li>
                    <li><strong>Nas 5 Dezenas:</strong> Em cada dezena:
                        <br>• Anuncia-se o Mistério bíblico correspondente;
                        <br>• Reza-se 1 <em>Pai Nosso</em> na conta isolada;
                        <br>• Rezam-se 10 <em>Ave Marias</em> nas contas menores;
                        <br>• Reza-se 1 <em>Glória ao Pai</em> + a <em>Jaculatória de Fátima</em>.
                    </li>
                    <li><strong>No Encerramento:</strong> Oração de Agradecimento e a solene <em>Salve Rainha</em>.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col_p2:
            st.markdown("""
            <div class="pilula-franciscana">
                <h4 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                    🕊️ A Coroa Franciscana (As Sete Alegrias de Maria)
                </h4>
                <p style="font-size: 1rem; line-height: 1.6; color: #2E1B10;">
                    A Ordem Franciscana possui também sua coroa tradicional de sete dezenas, 
                    composta no ano de 1422 por um noviço franciscano sob a inspiração de Nossa Senhora. 
                    Nela se meditam as <strong>Sete Alegrias da Virgem Maria</strong>:
                </p>
                <ul style="font-size: 0.95rem; line-height: 1.6; color: #3A2315;">
                    <li>1ª Alegria: A Anunciação</li>
                    <li>2ª Alegria: A Visitação</li>
                    <li>3ª Alegria: O Nascimento de Jesus</li>
                    <li>4ª Alegria: A Adoração dos Magos</li>
                    <li>5ª Alegria: O Encontro de Jesus no Templo</li>
                    <li>6ª Alegria: A Ressurreição do Senhor</li>
                    <li>7ª Alegria: A Assunção e Coroação de Maria</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # 2. Meditação dos Mistérios
    with tab_misterios:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            Contemplação Bíblica dos Vinte Mistérios do Rosário
        </h4>
        """, unsafe_allow_html=True)

        misterio_selecionado = st.selectbox(
            "Selecione o grupo de mistérios para meditar:",
            list(MISTERIOS_DATA.keys()),
            index=list(MISTERIOS_DATA.keys()).index(misterio_hoje)
        )

        dados_m = MISTERIOS_DATA[misterio_selecionado]
        st.markdown(f"""
        <div style="background: #F3ECE2; border-left: 4px solid {dados_m['cor']}; padding: 0.8rem 1.2rem; border-radius: 4px; margin-bottom: 1.2rem;">
            <strong style="color: #781826; font-family: 'Cinzel', serif; font-size: 1.1rem;">{misterio_selecionado}</strong> — <em>{dados_m['dias']}</em><br>
            <span style="font-size: 1rem; color: #3A2315;">{dados_m['tema']}</span>
        </div>
        """, unsafe_allow_html=True)

        for nome_dez, passagem, fruto in dados_m["dezenas"]:
            with st.expander(f"📿 {nome_dez}: {passagem}", expanded=True):
                st.markdown(f"""
                <p style="font-size: 1.05rem; line-height: 1.6; margin: 0; color: #2D1B13;">
                    <strong>Passagem Sagrada:</strong> {passagem}<br>
                    <strong>Fruto Espiritual da Dezena:</strong> <em>{fruto}</em>
                </p>
                <div style="margin-top: 0.6rem; font-size: 0.95rem; color: #781826; font-style: italic;">
                    (Reza-se: 1 Pai Nosso, 10 Ave Marias, 1 Glória ao Pai e a Jaculatória de Fátima)
                </div>
                """, unsafe_allow_html=True)

    # 3. As 15 Promessas
    with tab_promessas:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            As 15 Promessas de Nossa Senhora aos que Rezarem o Terço
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            Promessas maternais reveladas pela Mãe de Deus a São Domingos de Gusmão e ao Beato Alano de la Roche:
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pergaminho-card">
            <ol style="line-height: 1.8; font-size: 1rem; padding-left: 1.2rem;">
                <li>A todos aqueles que rezarem devotamente o meu Rosário, prometo minha especial proteção e grandes graças.</li>
                <li>Aquele que perseverar na oração do meu Rosário receberá graças assinaladas.</li>
                <li>O Rosário será uma armadura poderosíssima contra o inferno; destruirá os vícios, desarmará o pecado e dissipará as heresias.</li>
                <li>O Rosário fará florescer as virtudes e as obras boas; obterá para as almas as mais abundantes misericórdias divinas.</li>
                <li>A alma que a mim se confiar por meio do Rosário não perecerá.</li>
                <li>Todo aquele que rezar devotamente o Rosário, contemplando os santos mistérios, não será oprimido pelas desventuras nem morrerá de morte imprevista; converter-se-á, se for pecador, e perseverará na graça se for justo.</li>
                <li>Os verdadeiros devotos do meu Rosário não morrerão sem os sacramentos da Santa Igreja.</li>
                <li>Aqueles que rezarem o meu Rosário encontrarão durante a vida e na hora da morte a luz de Deus e a plenitude de suas graças.</li>
                <li>Livrarei prontamente do Purgatório as almas devotas ao meu Rosário.</li>
                <li>Os verdadeiros filhos do meu Rosário gozarão de grande glória no Céu.</li>
                <li>Tudo o que pedirdes por meio do meu Rosário, vós o alcançareis.</li>
                <li>Socorrerei em todas as suas necessidades aqueles que propagarem o meu Rosário.</li>
                <li>Obtive de meu Divino Filho que todos os membros da Confraria do Rosário tenham por intercessores em vida e na morte toda a corte celestial.</li>
                <li>Aqueles que rezam o meu Rosário fielmente são todos meus filhos amados, irmãos e irmãs de Jesus Cristo.</li>
                <li>A devoção ao meu Rosário é um grande sinal de predestinação para a glória eterna.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)