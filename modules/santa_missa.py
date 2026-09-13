# -*- coding: utf-8 -*-
"""
Módulo de Formação Litúrgica: A Santa Missa Passo a Passo
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
from style import render_divider

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            ⛪ A Santa Missa Passo a Passo & Alfabetização Litúrgica
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            O Santo Sacrifício do Altar, Ritos Sagrados, Alfaias, Vestes e Símbolos da Fé
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pergaminho-card-bordo">
        <p style="font-size: 1.15rem; line-height: 1.6; margin: 0; color: #2D1B13;">
            "A Santa Missa é o ato mais sublime e sagrado que pode acontecer sobre a terra: nela se renova o Sacrifício da Cruz 
            e o próprio Deus se faz presente em Corpo, Sangue, Alma e Divindade para nos alimentar e salvar."
        </p>
        <div style="text-align: right; font-family: 'Cinzel', serif; color: #781826; font-weight: bold; margin-top: 0.4rem;">
            — Sagrado Magistério da Igreja
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab_ritos, tab_alfaias, tab_vestes, tab_cores, tab_espaco = st.tabs([
        "📜 A Missa Parte por Parte",
        "🏺 Alfaias e Vasos Sagrados",
        "👘 Vestes Litúrgicas do Sacerdote",
        "🎨 As Cores Litúrgicas",
        "⛪ O Templo & Posturas Corporais"
    ])

    # 1. Ritos da Missa
    with tab_ritos:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            As Quatro Grandes Partes da Celebração Eucarística
        </h4>
        """, unsafe_allow_html=True)

        with st.expander("1. Ritos Iniciais (Preparar o coração e formar a assembleia)", expanded=True):
            st.markdown("""
            - **Canto e Procissão de Entrada:** O povo de Deus se reúne em marcha jubilosa; o sacerdote beija o Altar com reverência profunda (o altar representa o próprio Cristo).
            - **Saudação Trinitária:** 'Em nome do Pai e do Filho e do Espírito Santo' — a assembleia se coloca sob a bênção da Santíssima Trindade.
            - **Ato Penitencial:** Reconhecemos nossas fraquezas e pecados diante de Deus e dos irmãos ('Confesso a Deus Todo-Poderoso...'). Pedimos misericórdia: 'Senhor, tende piedade de nós!'.
            - **Hino do Glória (Gloria in Excelsis Deo):** Cântico dos Santos Anjos em Belém; louvor triunfante à Trindade (omitido no Advento e na Quaresma).
            - **Oração Coleta:** O sacerdote diz 'Oremos', faz um momento de silêncio para recolher as preces de cada coração e recita a oração que sintetiza a liturgia do dia.
            """)

        with st.expander("2. Liturgia da Palavra (Deus fala ao Seu povo)", expanded=False):
            st.markdown("""
            - **Primeira Leitura:** Geralmente extraída do Antigo Testamento, mostrando a fidelidade de Deus na História da Salvação (no Tempo Pascal, lê-se os Atos dos Apóstolos).
            - **Salmo Responsorial:** O povo responde à Palavra de Deus com a própria Palavra de Deus cantada ou recitada em tom orante.
            - **Segunda Leitura:** Aos domingos e solenidades, tirada das cartas dos Santos Apóstolos (São Paulo, São Pedro, São João, Tiago) ou do Apocalipse.
            - **Aclamação ao Evangelho (Aleluia):** Todos se colocam em pé com veneração para acolher as palavras do Senhor Jesus (o 'Aleluia' não é cantado na Quaresma).
            - **O Santo Evangelho:** O sacerdote ou diácono traça o sinal da cruz na fronte, nos lábios e no peito (pedindo a Cristo que esteja em nossos pensamentos, palavras e coração) e proclama o texto sagrado.
            - **Homilia:** O sacerdote atualiza a Palavra para o cotidiano da comunidade, exortando à conversão e santidade.
            - **Profissão de Fé (O Creio):** A assembleia proclama solenemente o resumo da fé católica recebida dos Apóstolos.
            - **Oração Universal dos Fiéis:** Preces pela Santa Igreja, pelo Papa, pelos governantes, pelos doentes, aflitos e pelas necessidades locais.
            """)

        with st.expander("3. Liturgia Eucarística (O Ápice do Sacrifício da Cruz)", expanded=False):
            st.markdown("""
            - **Apresentação das Oferendas (Ofertório):** O pão e o vinho são levados ao altar com a generosidade do dízimo e das ofertas dos fiéis. O sacerdote oferece a Deus o 'fruto da terra e do trabalho humano'.
            - **Oração sobre as Oferendas:** Prece pedindo que Deus acolha o sacrifício de nossas mãos.
            - **O Prefácio e o Sanctus (Santo, Santo, Santo):** Unimo-nos aos coros dos anjos e querubins celestiais cantando louvores ao Senhor dos Exércitos.
            - **A Oração Eucarística (Cânon Romano):**
              - *Epiclese:* O padre estende as mãos sobre o pão e o vinho, implorando a descida do Espírito Santo.
              - *Consagração e Transubstanciação:* Repetindo as palavras eternas de Cristo na Última Ceia ('Isto é o Meu Corpo... Este é o cálice do Meu Sangue'), o pão e o vinho deixam de ser pão e vinho e se tornam real e substancialmente o Corpo e o Sangue do Redentor.
              - *Elevação:* O padre ergue a Hóstia Consagrada e o Cálice para a solene adoração dos fiéis de joelhos.
              - *Anamnese e Doxologia Maior:* 'Eis o mistério da fé!' — culminando na grande louvação: *'Por Cristo, com Cristo, em Cristo, a Vós, Deus Pai Todo-Poderoso, na unidade do Espírito Santo, toda a honra e toda a glória, agora e para sempre. Amém!'*.
            """)

        with st.expander("4. Rito da Comunhão & Ritos Finais", expanded=False):
            st.markdown("""
            - **Pai Nosso:** A oração que o próprio Jesus nos ensinou, rezada em filial união.
            - **Rito da Paz:** Desejo fraterno de paz e reconciliação com o próximo antes da comunhão.
            - **Fração do Pão e Agnus Dei (Cordeiro de Deus):** O sacerdote parte a Hóstia Santa e coloca uma pequena partícula no cálice, simbolizando a união inseparável do Corpo e do Sangue de Cristo na Ressurreição.
            - **A Sagrada Comunhão:** 'Senhor, eu não sou digno de que entreis em minha morada, mas dizei uma palavra e serei salvo'. Os fiéis em estado de graça aproximam-se reverentemente para comungar o Santíssimo Corpo do Senhor.
            - **Ação de Graças:** Momento de silêncio sagrado para conversar intimamente com Jesus no coração.
            - **Oração pós-comunhão:** Prece pedindo os frutos do sacramento na vida prática.
            - **Bênção Final e Envio Missionário:** O padre abençoa a todos em nome da Trindade e nos envia: *'Ide em paz e o Senhor vos acompanhe — Graças a Deus!'*.
            """)

    # 2. Alfaias e Vasos Sagrados
    with tab_alfaias:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            Vasos e Alfaias Sagradas do Altar
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            Os objetos utilizados no altar são consagrados exclusivamente ao culto divino e tratados com suprema reverência.
        </p>
        """, unsafe_allow_html=True)

        col_a1, col_a2 = st.columns(2)
        with col_a1:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">🏆 Cálice</h5>
                <p>O vaso sagrado por excelência. Confeccionado em metal nobre ou dourado por dentro, onde o vinho é consagrado no Sangue precioso de Cristo.</p>
                <hr style="border: 0; border-top: 1px solid #D8C8B4;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">📀 Patena</h5>
                <p>Prato de metal nobre dourado que repousa sobre o cálice e onde se coloca a Hóstia grande que o sacerdote consagra e parte na Missa.</p>
                <hr style="border: 0; border-top: 1px solid #D8C8B4;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">🏺 Âmbula (ou Cibório)</h5>
                <p>Vaso semelhante a um cálice com tampa, usado para distribuir a comunhão e para reservar as Hóstias consagradas dentro do Sacrário.</p>
                <hr style="border: 0; border-top: 1px solid #D8C8B4;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">☀️ Ostensório (ou Custódia)</h5>
                <p>Peça rica com raios que simbolizam o sol, com um suporte de vidro (lúnula), usada para expor solenemente o Santíssimo Sacramento à adoração pública e em procissões.</p>
            </div>
            """, unsafe_allow_html=True)

        with col_a2:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">⬜ Corporal</h5>
                <p>Pano quadrado de linho branco com uma cruz no centro. É estendido no altar para que sobre ele sejam colocados o cálice e a patena, aparando qualquer fragmento da Hóstia.</p>
                <hr style="border: 0; border-top: 1px solid #D8C8B4;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">🧣 Sanguíneo e Pala</h5>
                <p><strong>Sanguíneo:</strong> Pano de linho estreito para purificar o cálice e a patena.<br>
                <strong>Pala:</strong> Quadrado rígido forrado de linho que se coloca sobre o cálice para evitar poeira.</p>
                <hr style="border: 0; border-top: 1px solid #D8C8B4;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">🍶 Galhetas e Manustérgio</h5>
                <p><strong>Galhetas:</strong> Duas jarras pequenas contendo a água e o vinho.<br>
                <strong>Manustérgio:</strong> Toalhinha para enxugar as mãos do padre no rito do Lavabo.</p>
                <hr style="border: 0; border-top: 1px solid #D8C8B4;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">💨 Turíbulo e Naveta</h5>
                <p>O <strong>turíbulo</strong> contém as brasas para queimar o incenso, e a <strong>naveta</strong> guarda o incenso em grãos. A fumaça perfumada simboliza a oração que sobe ao céu e a sacralidade das coisas de Deus.</p>
            </div>
            """, unsafe_allow_html=True)

    # 3. Vestes Litúrgicas
    with tab_vestes:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            As Vestes Sagradas do Sacerdote e seus Significados Espirituais
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            Ao se paramentar, o sacerdote deixa sua própria individualidade para revestir-se de Cristo Cabeça (*In Persona Christi*).
        </p>
        """, unsafe_allow_html=True)

        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">1. Alva (ou Túnica)</h5>
                <p>Túnica longa branca que cobre todo o corpo do sacerdote. Recorda a túnica alva do Batismo, a ressurreição e a pureza que se deve ter para celebrar os santos mistérios (Ap 7,14).</p>
                <hr style="border: 0; border-top: 1px solid #D8C8B4;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">2. Cíngulo</h5>
                <p>Cordão que amarra a túnica na cintura. Simboliza a virtude da pureza, a castidade sacerdotal e a prontidão no serviço de Deus.</p>
            </div>
            """, unsafe_allow_html=True)

        with col_v2:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">3. Estola</h5>
                <p>Faixa de tecido na cor litúrgica do dia. O bispo e os padres usam pendurada sobre os dois ombros caindo pelo peito; os diáconos a usam transversalmente (a tiracolo). É o distintivo da autoridade do sacramento da Ordem.</p>
                <hr style="border: 0; border-top: 1px solid #D8C8B4;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">4. Casula & Pluvial</h5>
                <p><strong>Casula:</strong> A veste superior ampla usada na celebração da Santa Missa. Simboliza o jugo suave de Cristo e a sublime virtude da caridade que cobre todas as imperfeições.<br>
                <strong>Pluvial:</strong> Capa solene aberta na frente, usada em procissões e bênçãos do Santíssimo.</p>
            </div>
            """, unsafe_allow_html=True)

    # 4. Cores Litúrgicas
    with tab_cores:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            O Significado das Cores Litúrgicas
        </h4>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
            <div style="background: #FFFDF8; border: 2px solid #C5A059; border-radius: 8px; padding: 1rem;">
                <h5 style="color: #8C6F2D; margin-top: 0; font-family: 'Cinzel', serif;">⚪ Branco / Dourado</h5>
                <p style="font-size: 0.95rem; line-height: 1.5;"><strong>Significado:</strong> Glória, alegria, vitória pascal, pureza e luz.<br>
                <strong>Usado em:</strong> Tempo do Natal, Tempo da Páscoa, festas de Cristo, da Santíssima Virgem Maria e dos Santos não-mártires.</p>
            </div>
            <div style="background: #F4FAF4; border: 2px solid #2E7D32; border-radius: 8px; padding: 1rem;">
                <h5 style="color: #1B5E20; margin-top: 0; font-family: 'Cinzel', serif;">🟢 Verde</h5>
                <p style="font-size: 0.95rem; line-height: 1.5;"><strong>Significado:</strong> Esperança, crescimento espiritual e perseverança na fé.<br>
                <strong>Usado em:</strong> Tempo Comum (ao longo de 33 ou 34 semanas do ano litúrgico).</p>
            </div>
            <div style="background: #FCF4F4; border: 2px solid #C62828; border-radius: 8px; padding: 1rem;">
                <h5 style="color: #B71C1C; margin-top: 0; font-family: 'Cinzel', serif;">🔴 Vermelho</h5>
                <p style="font-size: 0.95rem; line-height: 1.5;"><strong>Significado:</strong> O fogo ardente do Espírito Santo e o sangue redentor dos mártires.<br>
                <strong>Usado em:</strong> Domingo de Ramos, Sexta-feira da Paixão, Pentecostes, festas dos Santos Apóstolos e Mártires.</p>
            </div>
            <div style="background: #F8F4FA; border: 2px solid #6A1B9A; border-radius: 8px; padding: 1rem;">
                <h5 style="color: #4A148C; margin-top: 0; font-family: 'Cinzel', serif;">🟣 Roxo</h5>
                <p style="font-size: 0.95rem; line-height: 1.5;"><strong>Significado:</strong> Penitência, sobriedade, oração e conversão sincera do coração.<br>
                <strong>Usado em:</strong> Tempo do Advento e Tempo da Quaresma; também na liturgia dos fiéis defuntos.</p>
            </div>
            <div style="background: #FDF4F8; border: 2px solid #D81B60; border-radius: 8px; padding: 1rem;">
                <h5 style="color: #880E4F; margin-top: 0; font-family: 'Cinzel', serif;">🌸 Rosa</h5>
                <p style="font-size: 0.95rem; line-height: 1.5;"><strong>Significado:</strong> Alegria antecipada no meio do tempo de penitência.<br>
                <strong>Usado em:</strong> Apenas dois domingos no ano: 3º Domingo do Advento (<em>Gaudete</em>) e 4º Domingo da Quaresma (<em>Laetare</em> — dia da apresentação dos catecúmenos!).</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 5. O Templo e Posturas
    with tab_espaco:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            O Templo Católico & Nossas Posturas Corporais
        </h4>
        """, unsafe_allow_html=True)

        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">Os Lugares Sagrados da Igreja</h5>
                <ul style="line-height: 1.7; font-size: 1rem;">
                    <li><strong>Presbitério:</strong> Espaço elevado onde se encontram o Altar, a mesa da Palavra e a cadeira do celebrante.</li>
                    <li><strong>Altar:</strong> O centro da igreja, onde se renova o Sacrifício de Cristo. Merece a reverência e o beijo litúrgico.</li>
                    <li><strong>Ambão:</strong> A mesa sagrada de onde é proclamada a Palavra de Deus.</li>
                    <li><strong>Sacrário (Tabernáculo):</strong> O cofre santo onde repousa Jesus Sacramentado sob a espécie do pão consagrado. A luz vermelha acesa indica Sua Presença Real perpétua.</li>
                    <li><strong>Pia Batismal:</strong> A fonte sagrada de onde renascemos para a vida de filhos de Deus.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col_t2:
            st.markdown("""
            <div class="pergaminho-card-franciscano">
                <h5 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">O Sentido das Posturas Corporais</h5>
                <ul style="line-height: 1.7; font-size: 1rem;">
                    <li><strong>Em Pé:</strong> Demonstra dignidade de filhos de Deus ressuscitados com Cristo, vigilância atenta e respeito solene. Usamos nos ritos iniciais, na proclamação do Evangelho e nas orações do presidente.</li>
                    <li><strong>Sentados:</strong> Postura de discípulo que acolhe o ensinamento com tranquilidade no coração. Usamos nas leituras, no salmo, na homilia e na preparação das oferendas.</li>
                    <li><strong>De Joelhos:</strong> A mais humilde e nobre adoração perante a majestade de Deus. Usamos durante a consagração na Oração Eucarística e após comungar.</li>
                    <li><strong>Genuflexão:</strong> Tocar o joelho direito no solo perante o Santíssimo Sacramento ao entrar e sair da nave da igreja.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)