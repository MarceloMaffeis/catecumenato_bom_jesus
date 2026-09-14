# -*- coding: utf-8 -*-
"""
Módulo de Tratados Teológicos Aprofundados: Cátedra de Teologia Sagrada
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
Doutrina Dogmática, Patrística, Conciliar e Mística Franciscana
"""

import os
import streamlit as st
from style import render_header, render_divider

def render_imagem_sacra(caminho_relativo, legenda):
    """Auxiliar para carregar com total segurança as imagens sacras locais."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidatos = [
        os.path.join(base_dir, caminho_relativo),
        caminho_relativo,
        os.path.abspath(caminho_relativo)
    ]
    for c in candidatos:
        if os.path.exists(c) and os.path.isfile(c):
            st.image(c, caption=legenda, use_container_width=True)
            return
    st.info(f"🎨 {legenda}")

def render():
    render_header(
        titulo="CÁTEDRA DE TEOLOGIA SACRA",
        subtitulo="Mariologia • Cristologia • Angelologia • Pneumatologia • Eclesiologia • Escatologia • Trindade"
    )

    st.markdown("""
    <div class="pergaminho-card-bordo">
        <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
            🏛️ Aprofundamento Dogmático da Sã Doutrina Católica
        </h4>
        <p style="font-size: 1.1rem; line-height: 1.7; color: #2D1B13; margin-bottom: 0;">
            "A fé procura a inteligência (<em>Fides quaerens intellectum</em>)". Como nos ensina Santo Anselmo e São Boaventura, 
            a teologia não é mero exercício intelectual, mas o amor que deseja conhecer mais profundamente a Verdade Divina 
            revelada para melhor amar, adorar e anunciar a Deus. Este espaço destina-se a catequistas e catecúmenos que desejam 
            beber nas fontes cristalinas dos <strong>Grandes Tratados da Igreja</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_maria, tab_cristo, tab_anjos, tab_espirito, tab_igreja, tab_escatologia, tab_trindade = st.tabs([
        "🌸 1. Mariologia",
        "✝️ 2. Cristologia",
        "👼 3. Angelologia",
        "🕊️ 4. Pneumatologia",
        "⛪ 5. Eclesiologia",
        "⏳ 6. Escatologia",
        "👑 7. Santíssima Trindade"
    ])

    # ==========================================
    # 1. MARIOLOGIA
    # ==========================================
    with tab_maria:
        col_m_img, col_m_txt = st.columns([1, 1.8])
        with col_m_img:
            render_imagem_sacra("assets/images/encontro_40.jpg", "A Imaculada Conceição — Bartolomé Esteban Murillo")
        with col_m_txt:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🌸 Tratado da Bem-Aventurada Virgem Maria
                </h4>
                <p style="font-size: 1.05rem; line-height: 1.6; color: #3A2315;">
                    A Mariologia é o ramo da teologia que contempla o mistério da Mãe de Deus na história da salvação. 
                    Como ensinava São Bernardo de Claraval: <em>"De Maria numquam satis"</em> (Sobre Maria nunca se dirá o suficiente). 
                    A verdadeira devoção a Nossa Senhora é sempre puramente cristocêntrica: conduz a Jesus e tem por lema 
                    as últimas palavras registradas da Virgem no Evangelho: <strong>"Fazei tudo o que Ele vos disser"</strong> (Jo 2,5).
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 📜 Os Quatro Dogmas Marianos da Fé Católica:")
        
        with st.expander("1. A Maternidade Divina de Maria (Theotókos — Concílio de Éfeso, 431)", expanded=True):
            st.markdown("""
            - **Definição Solene:** Maria é verdadeiramente a **Mãe de Deus (Theotókos)**, porque gerou segundo a carne a Pessoa Divina do Verbo Encarnado, a Segunda Pessoa da Santíssima Trindade.
            - **Fundamento Bíblico:** *"Eis que conceberás e darás à luz um filho, e Lhe porás o nome de Jesus. Ele será grande e será chamado Filho do Altíssimo"* (Lc 1,31-32); *"Donde me vem que a Mãe do meu Senhor venha a mim?"* (Lc 1,43).
            - **Erro combatido:** O nestorianismo, que afirmava que Maria era apenas mãe do homem Jesus e não do Deus-Filho, dividindo Cristo em duas pessoas.
            - **Magistério:** CIC 495: *"Aqule que Ela concebeu como homem pelo Espírito Santo, e que se tornou verdadeiramente seu Filho segundo a carne, não é outro senão o Filho Eterno do Pai"*.
            """)

        with st.expander("2. A Virgindade Perpétua (Semper Virgo — Concílio de Latrão, 649)", expanded=False):
            st.markdown("""
            - **Definição Solene:** Maria é virgem *ante partum* (antes do parto), *in partu* (durante o parto, sem violação da integridade física) e *post partum* (perpetuamente virgem após o parto).
            - **Esclarecimento Bíblico:** Na Bíblia semítica, a palavra "irmãos de Jesus" (Mt 13,55) designa parentes próximos, primos carnais (como Tiago e José, filhos de outra Maria em Mt 27,56). Na Cruz, Jesus entrega Sua Mãe aos cuidados do apóstolo João (Jo 19,26-27), o que não ocorreria se Ela tivesse outros filhos carnais.
            - **Significado Espiritual:** A virgindade de Maria é sinal do seu dom esponsal indiviso a Deus e da iniciativa absoluta de Deus na Encarnação salvífica. (CIC 496-507).
            """)

        with st.expander("3. A Imaculada Conceição (Bula Ineffabilis Deus — Papa Pio IX, 1854)", expanded=False):
            st.markdown("""
            - **Definição Solene:** *"A Bem-Aventurada Virgem Maria foi, no primeiro instante de sua conceição, por singular graça e privilégio de Deus onipotente, em vista dos méritos de Jesus Cristo Salvador, preservada imune de toda mancha da culpa original"*.
            - **A Glória Teológica Franciscana — Beato John Duns Scotus:** Quando muitos teólogos hesitavam sobre como Maria poderia ser preservada sem ferir a universalidade da Redenção de Cristo, o frei franciscano **Duns Scotus** formulou a célebre solução da *Redenção Preventiva*: *"Cristo é o mais perfeito Redentor; logo, convém que exerça o ato mais perfeito de mediação salvando alguém antecipadamente antes de cair no abismo do pecado. Potuit, decuit, ergo fecit (Deus podia, convinha que fizesse, logo fez!)"*.
            - **Saudação Bíblica:** O Arcanjo Gabriel não a chama pelo nome civil, mas pelo título divino: *"Alegra-te, ó Cheia de Graça (Kecharitomene)"* (Lc 1,28), cheia da presença divina desde sempre. (CIC 490-493).
            """)

        with st.expander("4. A Gloriosa Assunção aos Céus em Corpo e Alma (Munificentissimus Deus — Papa Pio XII, 1950)", expanded=False):
            st.markdown("""
            - **Definição Solene:** *"A Imaculada Mãe de Deus, a sempre Virgem Maria, terminado o curso de sua vida terrena, foi elevada em corpo e alma à glória celestial"*.
            - **Sentido Escatológico:** Maria é a primeira criatura humana redimida a participar plenamente dos frutos da Ressurreição de Jesus. Seu corpo virginal, que foi sacrário vivo do Deus encarnado, não conheceu a corrupção do sepulcro.
            - **Esperança da Igreja:** A Assunção é a garantia consoladora de que o nosso corpo mortal também ressuscitará no último dia para a glória eterna (Ap 12,1; CIC 966).
            """)

        st.markdown("""
        <div class="pilula-franciscana" style="margin-top: 1rem;">
            <h5 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                🕊️ Distinção Teológica Fundamental do Culto Católico:
            </h5>
            <ul style="font-size: 1rem; line-height: 1.7; color: #2B1810; margin-bottom: 0;">
                <li><strong>Latria (Adoração):</strong> Prestada única e exclusivamente à Santíssima Trindade (Pai, Filho e Espírito Santo). Adorar qualquer criatura é pecado gravíssimo de idolatria.</li>
                <li><strong>Dulia (Veneração):</strong> Prestada aos Santos e Santos Anjos, como amigos de Deus e modelos de virtude.</li>
                <li><strong>Hiperdulia (Veneração Eminente):</strong> Prestada com amor filial singular e incomparável à Virgem Maria, por sua altíssima dignidade de Mãe de Deus e Rainha dos Anjos, sem jamais adorá-la como deusa.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # ==========================================
    # 2. CRISTOLOGIA
    # ==========================================
    with tab_cristo:
        col_c_img, col_c_txt = st.columns([1, 1.8])
        with col_c_img:
            render_imagem_sacra("assets/images/encontro_18.jpg", "Cristo Glorioso Edifica e Sustenta a Santa Igreja — Fra Angelico")
        with col_c_txt:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    ✝️ Tratado de Nosso Senhor Jesus Cristo
                </h4>
                <p style="font-size: 1.05rem; line-height: 1.6; color: #3A2315;">
                    A Cristologia é o coração pulsante da teologia católica. Como declarou solenemente São Pedro sob inspiração do Pai: 
                    <strong>"Tu és o Cristo, o Filho do Deus vivo!"</strong> (Mt 16,16). 
                    Nele, <em>"habita corporalmente toda a plenitude da divindade"</em> (Cl 2,9). 
                    Jesus não é um simples mestre moral ou líder social: Ele é o próprio Deus feito homem para nossa redenção.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 📜 Pilares da Doutrina Cristológica:")

        with st.expander("1. O Dogma da União Hipostática (Concílio de Calcedônia, 451)", expanded=True):
            st.markdown("""
            - **Definição Máxima da Fé:** Em Jesus Cristo há **uma única Pessoa Divina** (a Segunda Pessoa da Trindade) que subsiste em **duas naturezas perfeitas**: a natureza divina e a natureza humana.
            - **Sem confusão nem divisão:** As duas naturezas permanecem intactas, unidas sem confusão, sem mudança, sem divisão e sem separação.
            - **Consequências teológicas:** 
              - Jesus é verdadeiro Deus: Onipotente, Eterno, Criador com o Pai.
              - Jesus é verdadeiro Homem: Teve alma humana, corpo real, inteligência humana, vontade humana e sentimentos humanos (chorou a morte de Lázaro, sentiu fome, sede e cansaço).
              - *Communication idiomatum:* Tudo o que a humanidade de Jesus operou pertence à Pessoa divina do Verbo (CIC 464-469).
            """)

        with st.expander("2. Os Três Múnus Messiânicos de Jesus Cristo", expanded=False):
            st.markdown("""
            - **Cristo como Sacerdote Eterno:** Ofereceu o Sacrifício perfeito e definitivo na Cruz, sendo Ele próprio o Sacerdote e a Vítima imaculada que reconciliou o homem com o Pai (Hb 7,24-27).
            - **Cristo como Profeta da Verdade:** É a própria Palavra Viva de Deus que nos revelou plenamente o Pai: *"Quem Me vê, vê o Pai"* (Jo 14,9).
            - **Cristo como Rei do Universo:** Seu Reino não é deste mundo, mas é eterno e universal: reino de verdade, justiça, amor e paz (CIC 436-440).
            """)

        with st.expander("3. O Mistério Pascal: Paixão, Morte e Ressurreição Gloriosa", expanded=False):
            st.markdown("""
            - **A Morte na Cruz:** Não foi um acidente político, mas o ato supremo de entrega redentora: *"Ninguém Me tira a vida, sou Eu que a dou livremente"* (Jo 10,18). Ele carregou em Seu Corpo sobre o madeiro as nossas culpas (1Pd 2,24).
            - **A Descida à Mansão dos Mortos (Sheol):** Jesus desceu aos infernos (limbo dos justos) para libertar as almas dos santos que esperavam a Redenção (como Adão, Moisés e Davi) e abrir-lhes as portas do Céu (CIC 632-635).
            - **A Ressurreição Corpórea:** Acontecimento histórico e transcendente atestado pelas testemunhas oculares. O sepulcro vazio e as aparições aos discípulos provam que a Morte foi vencida para sempre (1Cor 15,14; CIC 638-655).
            """)

    # ==========================================
    # 3. ANGELOLOGIA
    # ==========================================
    with tab_anjos:
        col_a_img, col_a_txt = st.columns([1, 1.8])
        with col_a_img:
            render_imagem_sacra("assets/images/encontro_05.jpg", "São Miguel Arcanjo derrota o Maligno — Guido Reni")
        with col_a_txt:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    👼 Tratado dos Santos Anjos (Angelologia)
                </h4>
                <p style="font-size: 1.05rem; line-height: 1.6; color: #3A2315;">
                    A Angelologia estuda a natureza, a missão e a hierarquia dos Santos Anjos segundo a Sagrada Escritura 
                    e a Tradição viva da Igreja. 
                    Conforme o Catecismo da Igreja Católica (CIC 328), a existência dos anjos é uma verdade incontestável de fé: 
                    são servos e mensageiros de Deus, contemplam incessantemente a face do Pai e atuam poderosamente 
                    em socorro da humanidade no combate espiritual contra as forças do mal.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 📜 A Doutrina Angélica:")

        with st.expander("1. A Natureza dos Anjos (CIC 328-330)", expanded=True):
            st.markdown("""
            - **Puro Espírito:** Não possuem corpo físico, nem sexo, nem composição material.
            - **Pessoais e Imortais:** São pessoas espirituais dotadas de inteligência luminosa e vontade livre inabalável.
            - **Superiores ao Homem por Natureza:** Excedem em perfeição a todas as criaturas visíveis pelo esplendor de sua glória e poder conferido por Deus.
            - **Aviso Doutrinal Crucial:** Seres humanos **NUNCA** se transformam em anjos após a morte. O homem ressuscitará com corpo e alma humanos glorificados.
            """)

        with st.expander("2. As Nove Ordens / Coros Angélicos na Tradição de São Dionísio e São Tomás de Aquino", expanded=False):
            st.markdown("""
            Na Tradição da Igreja (tratado de São Dionísio Areopagita e *Suma Teológica* I, q. 108), os anjos distribuem-se em três hierarquias de três coros cada:
            
            1. **Primeira Hierarquia (Adoram a Deus Face a Face):**
               - **Serafins:** Os mais próximos do trono; ardem no fogo vivo da suprema Caridade e Amor divino (Is 6,2).
               - **Querubins:** Resplandecem na plenitude da Ciência e Sabedoria divina (Gn 3,24).
               - **Tronos:** Portadores da majestade de Deus; representam a santa firmeza da Justiça divina.
            
            2. **Segunda Hierarquia (Governam o Cosmos e as Potências):**
               - **Dominações:** Transmitem as ordens de Deus e governam os coros inferiores com soberania espiritual.
               - **Virtudes:** Responsáveis pela ordem física dos astros e pela realização de milagres e prodígios na criação.
               - **Potestades:** Combatem diretamente as forças demoníacas e refreiam o poder das trevas para proteger as almas.
            
            3. **Terceira Hierarquia (Mais Próximos dos Homens e das Nações):**
               - **Principados:** Guardiões protetores dos povos, dioceses, cidades e comunidades eclesiais.
               - **Arcanjos:** Mensageiros celestes das revelações mais sublimes e chefes das milícias de Deus (Miguel, Gabriel, Rafael).
               - **Anjos:** Guardiões individuais da humanidade (nossos Santos Anjos da Guarda).
            """)

        with st.expander("3. Os Três Santos Arcanjos Canônicos", expanded=False):
            st.markdown("""
            - **São Miguel Arcanjo ("Quem como Deus?"):** O chefe Supremo da Milícia Celeste que expulsou o dragão soberbo do Céu (Ap 12,7-9). Defensor do Povo de Deus, terror dos espíritos malignos e protetor da Santa Igreja Católica.
            - **São Gabriel Arcanjo ("Fortaleza de Deus"):** O mensageiro divino da Encarnação do Verbo que proclamou a Anunciação à Virgem Maria (Lc 1,26) e fortaleceu o profeta Daniel (Dn 8,16).
            - **São Rafael Arcanjo ("Medicina de Deus"):** O guia providencial do jovem Tobias, curador da cegueira e libertador das aflições espirituais e conjugais (Tb 12,15).
            """)

        with st.expander("4. O Santo Anjo da Guarda e o Combate Espiritual (CIC 336)", expanded=False):
            st.markdown("""
            - **Dogma do Anjo da Guarda:** Cada ser humano possui desde a concepção um Santo Anjo pessoal designado por Deus para iluminar, defender e conduzir sua alma ao Paraíso.
            - **O Combate Espiritual (Efésios 6,12):** *"Pois não é contra homens de carne e sangue que temos de lutar, mas contra os principados e potestades, contra os príncipes deste mundo tenebroso, contra as forças espirituais do mal"*.
            - **Oração de Leão XIII:** Aconselha-se rezar diariamente ao fim da Missa e nas famílias a oração a São Miguel Arcanjo contra as ciladas do demônio.
            """)

    # ==========================================
    # 4. PNEUMATOLOGIA
    # ==========================================
    with tab_espirito:
        col_p_img, col_p_txt = st.columns([1, 1.8])
        with col_p_img:
            render_imagem_sacra("assets/images/encontro_16.jpg", "A Efusão do Espírito Santo no Cenáculo — El Greco")
        with col_p_txt:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🕊️ Tratado do Espírito Santo (Pneumatologia)
                </h4>
                <p style="font-size: 1.05rem; line-height: 1.6; color: #3A2315;">
                    A Pneumatologia contempla a Terceira Pessoa da Santíssima Trindade: o Espírito Santo, Senhor que dá a vida, 
                    o Amor consubstancial do Pai e do Filho. 
                    Ele é a alma da Igreja, o Consolador (*Paráclito*) prometido por Jesus que nos conduz a toda a verdade (Jo 16,13) 
                    e habita em cada coração em estado de graça como em um templo sagrado (1Cor 6,19).
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 📜 Dons e Frutos da Graça:")

        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">🌿 Os 7 Dons do Espírito Santo (Is 11,2)</h5>
                <ol style="font-size: 0.98rem; line-height: 1.7; padding-left: 1.2rem;">
                    <li><strong>Sabedoria:</strong> Saborear as coisas divinas acima das terrenas.</li>
                    <li><strong>Entendimento:</strong> Compreender a fundo as verdades da fé.</li>
                    <li><strong>Conselho:</strong> Discernir o caminho certo nos momentos difíceis.</li>
                    <li><strong>Fortaleza:</strong> Coragem heróica para vencer o pecado e sofrer por Cristo.</li>
                    <li><strong>Ciência:</strong> Ver a assinatura de Deus em toda a criação.</li>
                    <li><strong>Piedade:</strong> Amor filial e doce ternura de coração com Deus e os irmãos.</li>
                    <li><strong>Santo Temor de Deus:</strong> Medo amoroso de ofender o Deus que tanto nos ama.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col_d2:
            st.markdown("""
            <div class="pilula-franciscana">
                <h5 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">🍇 Os 12 Frutos da Graça (Gl 5,22 / CIC 1832)</h5>
                <p style="font-size: 0.98rem; line-height: 1.7;">
                    1. Caridade (Amor)<br>
                    2. Alegria espiritual<br>
                    3. Paz interior<br>
                    4. Paciência cristã<br>
                    5. Benignidade<br>
                    6. Bondade fraterna<br>
                    7. Longanimidade (constância)<br>
                    8. Mansidão<br>
                    9. Fé e Fidelidade<br>
                    10. Modéstia no porte<br>
                    11. Continência<br>
                    12. Castidade de coração e corpo
                </p>
            </div>
            """, unsafe_allow_html=True)

    # ==========================================
    # 5. ECLESIOLOGIA
    # ==========================================
    with tab_igreja:
        col_i_img, col_i_txt = st.columns([1, 1.8])
        with col_i_img:
            render_imagem_sacra("assets/images/encontro_02.jpg", "Cristo entrega as Chaves a São Pedro — Pietro Perugino (Capela Sistina)")
        with col_i_txt:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    ⛪ Tratado da Santa Igreja Católica (Eclesiologia)
                </h4>
                <p style="font-size: 1.05rem; line-height: 1.6; color: #3A2315;">
                    A Eclesiologia reflete sobre o mistério da Santa Igreja como Sociedade Visível e Corpo Místico de Cristo. 
                    Fundada sobre Pedro e os Doze Apóstolos, a Igreja não é criação humana, mas instituição divina permanente: 
                    ela é a barca da salvação que atravessa os séculos conduzindo os fiéis pelo oceano do mundo até a Pátria Celeste.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 📜 A Comunhão dos Santos nos Três Estados da Igreja:")

        col_st1, col_st2, col_st3 = st.columns(3)
        with col_st1:
            st.markdown("""
            <div class="pergaminho-card" style="text-align: center; height: 100%;">
                <h5 style="color: #C5A059; font-family: 'Cinzel', serif;">👑 Igreja Triunfante</h5>
                <p style="font-size: 0.95rem; line-height: 1.6;">
                    Composta por todos os Santos e Anjos que já contemplam a Deus face a face na glória do Céu. 
                    Eles intercedem continuamente por nós junto ao Cordeiro.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col_st2:
            st.markdown("""
            <div class="pergaminho-card-bordo" style="text-align: center; height: 100%;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif;">🔥 Igreja Padecente</h5>
                <p style="font-size: 0.95rem; line-height: 1.6;">
                    Composta pelas almas benditas que passam pela purificação do amor no Purgatório. 
                    Nós as socorremos com a Santa Missa, esmolas, orações e sufrágios.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col_st3:
            st.markdown("""
            <div class="pilula-franciscana" style="text-align: center; height: 100%;">
                <h5 style="color: #5A3825; font-family: 'Cinzel', serif;">⚔️ Igreja Militante</h5>
                <p style="font-size: 0.95rem; line-height: 1.6;">
                    Composta por nós, os batizados que peregrinamos sobre a terra, combatendo o bom combate da fé 
                    contra as tentações do demônio, do mundo e da carne.
                </p>
            </div>
            """, unsafe_allow_html=True)

    # ==========================================
    # 6. ESCATOLOGIA
    # ==========================================
    with tab_escatologia:
        col_e_img, col_e_txt = st.columns([1, 1.8])
        with col_e_img:
            render_imagem_sacra("assets/images/encontro_38.jpg", "O Juízo Universal — Michelangelo Buonarroti (Capela Sistina)")
        with col_e_txt:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    ⏳ Tratado dos Novíssimos (Escatologia)
                </h4>
                <p style="font-size: 1.05rem; line-height: 1.6; color: #3A2315;">
                    A Escatologia estuda as realidades últimas e definitivas da história e de cada ser humano. 
                    A Sagrada Escritura exorta no livro do Eclesiástico (7,36): 
                    <em>"Em todas as tuas obras, lembra-te dos teus novíssimos, e jamais pecarás"</em>. 
                    Os Quatro Novíssimos do homem são: <strong>Morte, Juízo, Inferno e Paraíso</strong>.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        with st.expander("1. A Morte Física e o Juízo Particular (Hb 9,27 / CIC 1021-1022)", expanded=True):
            st.markdown("""
            - A morte é a separação da alma e do corpo. O tempo de merecer encerra-se com o último suspiro terrestre.
            - Imediatamente após a morte, a alma imortal comparece diante de Jesus Cristo para o **Juízo Particular**, onde todas as suas obras e segredos são iluminados pela luz da Verdade.
            - A sentença é irrevogável: ou a comunhão eterna no Céu (direta ou pelo Purgatório) ou a condenação eterna no Inferno.
            """)

        with st.expander("2. O Purgatório: Purificação do Amor (2Mac 12,46 / CIC 1030-1032)", expanded=False):
            st.markdown("""
            - O Purgatório não é um inferno temporário, mas o vestíbulo glorioso do Céu: todas as almas que nele entram já estão eternamente salvas.
            - É o fogo do amor de Deus que queima as escórias do apego venial para que a alma atinja a santidade pura exigida para a visão beatífica (*"Nada de impuro entrará nela"*, Ap 21,27).
            - É santa e piedosa obrigação rezar pelas almas do purgatório e mandar celebrar a Santa Missa por elas.
            """)

        with st.expander("3. O Inferno: A Dor da Eterna Perdição (Mt 25,41 / CIC 1033-1037)", expanded=False):
            st.markdown("""
            - O Inferno é o estado de autoexclusão definitiva da comunhão com Deus e com os bem-aventurados.
            - Destina-se àqueles que morrem livremente em pecado mortal sem arrependimento até o fim.
            - A dor principal é a *poena damni* (a perda eterna de Deus, para Quem fomos criados e fora de Quem a alma é torturada pelo desespero).
            """)

        with st.expander("4. O Céu, a Parusia e a Ressurreição dos Corpos (1Cor 15 / CIC 1023-1029)", expanded=False):
            st.markdown("""
            - O Céu é a vida eterna com a Santíssima Trindade, a Virgem Maria, os Anjos e todos os Santos na felicidade infinita da Visão Beatífica.
            - No Fim dos Tempos, Jesus voltará em glória na Sua **Parusia**.
            - Todos os seres humanos ressuscitarão com seus próprios corpos físicos: os santos com corpos gloriosos, incorruptíveis e luminosos como o de Cristo ressuscitado.
            """)

    # ==========================================
    # 7. TEOLOGIA TRINITÁRIA
    # ==========================================
    with tab_trindade:
        col_t_img, col_t_txt = st.columns([1, 1.8])
        with col_t_img:
            render_imagem_sacra("assets/images/encontro_36.jpg", "O Sagrado Ícone da Santíssima Trindade — Santo Andrei Rublev")
        with col_t_txt:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    👑 Tratado da Santíssima Trindade
                </h4>
                <p style="font-size: 1.05rem; line-height: 1.6; color: #3A2315;">
                    O mistério da Santíssima Trindade é o mistério central da fé e da vida cristã católica (CIC 232). 
                    É o mistério de Deus em Si mesmo. 
                    Toda a história da salvação não é outra coisa senão a história do caminho e dos meios pelos quais 
                    o único Deus verdadeiro — Pai, Filho e Espírito Santo — Se revela, Se reconcilia e Se une aos seres humanos 
                    para torná-los participantes de Sua comunhão eterna de Amor.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("""
        <div class="pergaminho-card-bordo">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                📜 Síntese do Dogma Trinitário (Símbolo Atanasiano / Quicumque):
            </h4>
            <ul style="font-size: 1.05rem; line-height: 1.8; color: #2D1B13;">
                <li><strong>A Trindade é Una:</strong> Não confessamos três deuses, mas um só Deus em três Pessoas: a Trindade consubstancial (<em>homooúsios</em>).</li>
                <li><strong>As Pessoas Divinas são realmente distintas entre si:</strong> O Pai não é o Filho, o Filho não é o Pai, e o Espírito Santo não é nem o Pai nem o Filho. São distintas por suas relações de origem.</li>
                <li><strong>O Pai engendra o Filho:</strong> O Filho é eternamente gerado pelo Pai (*"Deus de Deus, Luz da Luz, Deus verdadeiro de Deus verdadeiro"*).</li>
                <li><strong>O Espírito Santo procede do Pai e do Filho:</strong> Como de um único princípio e por uma única espiração de amor infinito.</li>
                <li><strong>Circumincessão / Pericorese:</strong> Cada uma das Três Pessoas habita inteiramente nas outras duas em comunhão perfeitíssima e eterna.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
