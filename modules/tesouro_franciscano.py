# -*- coding: utf-8 -*-
"""
Módulo Pastoral: Tesouro Franciscano — O Carisma dos Filhos de São Francisco
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
import os

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            🌿 Tesouro Franciscano: O Carisma dos Filhos de São Francisco
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            "Paz e Bem!" • A espiritualidade da minoridade, da fraternidade e do louvor à Criação
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_coroa, tab_cantico, tab_cruz, tab_santos = st.tabs([
        "📿 A Coroa Franciscana (Sete Alegrias)",
        "☀️ O Cântico das Criaturas",
        "✝️ O Santo Crucifixo de São Damião",
        "🌿 Os Santos da Família Franciscana"
    ])

    # 1. A Coroa Franciscana
    with tab_coroa:
        st.markdown("""
        <div class="pergaminho-card-franciscano">
            <h3 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                ☩ A Origem da Coroa Franciscana (Rosário Seráfico)
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                No ano de 1422, um jovem piedoso entrou para a Ordem dos Frades Menores Franciscanos. 
                Antes de ingressar, ele tinha o doce costume de tecer diariamente uma coroa de flores frescas para coroar a imagem da Virgem Maria. 
                Porém, no noviciado, sem tempo livre para colher flores no campo, entristeceu-se a ponto de pensar em abandonar o claustro.
            </p>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                A Santíssima Virgem Maria apareceu-lhe maternalmente e disse-lhe: 
                <em>"Não te entristeças, meu filho! Eu te ensinarei a trançar uma coroa muito mais perfumada e preciosa, que nunca murchará: 
                reza para mim sete dezenas de Ave Marias, meditando as Sete Maiores Alegrias que inundaram o meu coração nesta vida."</em>
                Assim nasceu a <strong>Coroa Franciscana das Sete Alegrias de Nossa Senhora</strong>, rezada em todo o mundo franciscano!
            </p>
        </div>
        """, unsafe_allow_html=True)

        alegrias = [
            ("1ª Alegria: A Anunciação do Arcanjo Gabriel e a Encarnação do Verbo", "Lucas 1, 26-38", "Maria alegrou-se intensamente ao ser escolhida para ser a Mãe do Filho do Altíssimo, pronunciando com amor virginal o seu sublime Fiat: 'Eis aqui a serva do Senhor; faça-se em mim segundo a tua palavra.'"),
            ("2ª Alegria: A Visitação a Santa Isabel e a Santificação de São João Batista", "Lucas 1, 39-56", "Maria viajou pelas montanhas para servir sua prima Isabel. Ao som de sua saudação, o Menino João estremeceu de alegria no seio materno e Maria entoou o cântico imortal do Magnificat."),
            ("3ª Alegria: O Santo Nascimento de Jesus no Presépio de Belém", "Lucas 2, 1-20", "A alegria infinita de contemplar o Filho de Deus feito homem, envolto em faixas e deitado sobre a palha na pobreza humilde de Belém, adorado por Maria, José e os pastores."),
            ("4ª Alegria: A Adoração dos Magos do Oriente (Epifania)", "Mateus 2, 1-12", "A manifestação da glória do Menino Jesus a todos os povos e nações, quando os reis magos se prostraram com ouro (realeza), incenso (divindade) e mirra (redenção)."),
            ("5ª Alegria: O Encontro do Menino Jesus no Templo de Jerusalém", "Lucas 2, 41-52", "Após três dias de angústia e busca dolorosa, a indizível alegria de encontrar o Menino entre os doutores da Lei, ouvindo-os e interrogando-os sobre as coisas de Seu Pai."),
            ("6ª Alegria: A Gloriosa Ressurreição de Jesus Cristo", "Mateus 28, 1-10", "A vitória definitiva de Cristo sobre o pecado e a morte na manhã da Páscoa! Segundo a piedosa tradição franciscana, o Senhor ressuscitado apareceu primeiro à Sua Mãe Santíssima para consolá-la."),
            ("7ª Alegria: A Assunção e Coroação de Maria como Rainha do Céu e da Terra", "Apocalipse 12, 1", "A elevação de Maria em corpo e alma à glória celeste, sendo coroada pela Santíssima Trindade como Rainha dos Anjos e dos Santos, nossa Mãe e Advogada perpétua.")
        ]

        st.markdown("##### 🌸 As Sete Dezenas da Coroa Seráfica:")
        for titulo, ref, med in alegrias:
            with st.expander(f"☩ {titulo}", expanded=False):
                st.markdown(f"**Passagem Bíblica:** *{ref}*")
                st.markdown(f"<p style='font-size: 1.05rem; line-height: 1.6; color: #2B1810;'>{med}</p>", unsafe_allow_html=True)
                st.info("Reza-se: 1 Pai Nosso, 10 Ave Marias e 1 Glória ao Pai.")

        st.markdown("""
        <div class="pergaminho-card">
            <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                O Fechamento Tradicional da Coroa Seráfica:
            </h5>
            <p style="font-size: 1rem; line-height: 1.6; color: #2B1810;">
                Após as 7 dezenas (completando 70 Ave Marias), <strong>acrescentam-se 2 Ave Marias</strong> 
                para totalizar as <strong>72 Ave Marias</strong>, em veneração aos 72 anos que a piedosa tradição atribui à vida terrena de Nossa Senhora.<br>
                Finaliza-se com <strong>1 Pai Nosso e 1 Ave Maria</strong> pelas intenções do Santo Padre, o Papa, para receber as indulgências franciscanas.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 2. O Cântico das Criaturas
    with tab_cantico:
        st.markdown("""
        <div class="pergaminho-card-franciscano">
            <h3 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                ☀️ O Cântico do Irmão Sol (Composto por São Francisco em 1225 em São Damião)
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                Composto nos últimos anos de sua vida, quando estava enfermo e quase cego, o Cântico das Criaturas 
                é o primeiro grande monumento literário da língua italiana e o hino supremo de reconciliação de toda a Criação em Deus.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pergaminho-card" style="font-style: italic; font-size: 1.08rem; line-height: 1.8; color: #2B1810; text-align: center; padding: 1.5rem 2rem;">
            Altíssimo, onipotente, bom Senhor,<br>
            Teus são o louvor, a glória, a honra e toda a bênção.<br>
            A Ti somente, Altíssimo, eles convêm,<br>
            e homem algum é digno de Te nomear.<br><br>
            
            <strong>Louvado sejas, meu Senhor, com todas as Tuas criaturas,</strong><br>
            especialmente o senhor irmão Sol,<br>
            que clareia o dia e por ele nos iluminas.<br>
            E ele é belo e radiante com grande esplendor:<br>
            de Ti, Altíssimo, nos traz a semelhança.<br><br>
            
            <strong>Louvado sejas, meu Senhor, pela irmã Lua e pelas Estrelas:</strong><br>
            no céu as formaste claras, preciosas e belas.<br><br>
            
            <strong>Louvado sejas, meu Senhor, pelo irmão Vento,</strong><br>
            e pelo ar, e pelas nuvens, e pelo sereno, e por todo o tempo,<br>
            pelo qual às Tuas criaturas dás sustento.<br><br>
            
            <strong>Louvado sejas, meu Senhor, pela irmã Água,</strong><br>
            que é tão útil e humilde, e preciosa e casta.<br><br>
            
            <strong>Louvado sejas, meu Senhor, pelo irmão Fogo,</strong><br>
            pelo qual iluminas a noite:<br>
            e ele é belo, jucundo, robusto e forte.<br><br>
            
            <strong>Louvado sejas, meu Senhor, por nossa irmã, a mãe Terra,</strong><br>
            que nos sustenta e governa,<br>
            e produz diversos frutos com coloridas flores e ervas.<br><br>
            
            <strong>Louvado sejas, meu Senhor, por aqueles que perdoam por Teu amor</strong><br>
            e suportam enfermidades e tribulações.<br>
            Bem-aventurados aqueles que as suportarem em paz,<br>
            porque por Ti, Altíssimo, serão coroados.<br><br>
            
            <strong>Louvado sejas, meu Senhor, por nossa irmã a Morte corporal,</strong><br>
            da qual homem algum vivente pode escapar.<br>
            Ai daqueles que morrerem em pecado mortal!<br>
            Bem-aventurados os que ela encontrar na Tua santíssima vontade,<br>
            porque a segunda morte não lhes fará mal.<br><br>
            
            Louvai e bendizei a meu Senhor, e dai-Lhe graças,<br>
            e servi-O com grande humildade!<br>
            <strong>Amém! ☩</strong>
        </div>
        """, unsafe_allow_html=True)

    # 3. O Santo Crucifixo de São Damião
    with tab_cruz:
        col_img, col_txt = st.columns([1, 1.4])
        with col_img:
            base_d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            caminho_cruz = os.path.join(base_d, "assets", "images", "encontro_15.jpg")
            if os.path.exists(caminho_cruz):
                st.image(caminho_cruz, caption="O Sagrado Ícone do Crucifixo de São Damião", use_container_width=True)
            else:
                st.info("🎨 Ícone do Crucifixo de São Damião")
        with col_txt:
            st.markdown("""
            <div class="pergaminho-card-bordo">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    A Teologia do Ícone que Falou a São Francisco (1206)
                </h4>
                <p style="font-size: 1.02rem; line-height: 1.6; color: #2B1810;">
                    Em 1206, ajoelhado em oração diante deste crucifixo na ermida de São Damião, Francisco ouviu por três vezes 
                    a voz viva de Cristo vinda da cruz:<br>
                    <strong style="color: #781826;">'Francisco, vai e restaura a Minha Igreja que, como vês, está toda em ruínas!'</strong>
                </p>
                <ul style="font-size: 0.98rem; line-height: 1.7; color: #2B1810;">
                    <li><strong>Cristo Glorioso:</strong> Não está morto nem derrotado, mas ereto e luminoso, vencedor da morte. Seus olhos abertos fitam a humanidade com misericórdia infinita.</li>
                    <li><strong>A Veste Sacerdotal:</strong> O perizoma de linho dourado recorda a túnica dos sacerdotes da Antiga Aliança (Cristo é o Eterno Sumo Sacerdote).</li>
                    <li><strong>As Testemunhas Maiores:</strong> Ao lado esquerdo de Cristo estão a Virgem Maria e São João Evangelista; ao lado direito, Maria Madalena, Maria de Cléofas e o Centurião romano que proclamou: <em>'Verdadeiramente este homem era o Filho de Deus!'</em></li>
                    <li><strong>O Sangue Redentor:</strong> Das chagas sagradas brota o sangue que banha as testemunhas e a Igreja inteira.</li>
                    <li><strong>A Mão do Pai Celestial:</strong> No topo da cruz, Cristo sobe triunfante ao Céu segurando a cruz como cetro, e a Mão direita de Deus Pai acolhe o Filho amado na glória!</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # 4. Os Grandes Santos Franciscanos
    with tab_santos:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            🌿 A Comunhão dos Santos da Família Franciscana
        </h4>
        """, unsafe_allow_html=True)

        santos = [
            ("São Francisco de Assis (1182 - 1226)", "O Pai Seráfico e fundador da Ordem dos Frades Menores. Despojou-se de todas as riquezas paternas para abraçar a 'Dama Pobreza' e configurar-se perfeitamente a Cristo Crucificado, recebendo os santos estigmas no Monte Alverne."),
            ("Santa Clara de Assis (1194 - 1253)", "A primeira mulher a redigir uma Regra de vida religiosa aprovada pelo Papa. Fundadora da Ordem das Pobres Damas (Clarissas), viveu a pobreza radical e salvou o convento de São Damião erguendo a custódia com o Santíssimo Sacramento perante os invasores."),
            ("Santo Antônio de Pádua e Lisboa (1195 - 1231)", "Nascido em Lisboa, tornou-se Frade Menor franciscano após contemplar o martírio dos primeiros franciscanos em Marrocos. Conhecido como o 'Doutor Evangélico' e o 'Martelo dos Hereges', pregava com sabedoria bíblica prodigiosa e profunda caridade para com os pobres."),
            ("São Boaventura de Bagnoregio (1221 - 1274)", "O 'Doutor Seráfico', Cardeal e Ministro Geral da Ordem. Foi o grande filósofo e místico que sistematizou a teologia franciscana (Itinerário da Mente para Deus) e reconciliou a alta erudição com a simplicidade seráfica."),
            ("Beato João Duns Scotus (1266 - 1308)", "O 'Doutor Sutil', mestre nas Universidades de Oxford e Paris. Foi o heróico teólogo franciscano que defendeu brilhantemente o privilégio da Imaculada Conceição de Maria, formulando a teologia da Redenção Preventiva."),
            ("São Maximiliano Maria Kolbe (1894 - 1941)", "Frade Franciscano Menor Conventual polonês, fundador da Milícia da Imaculada. Ofereceu espontaneamente sua própria vida para morrer de fome no bunker de Auschwitz em substituição a um pai de família, testemunhando que o Amor é mais forte que a morte.")
        ]

        for nome, bio in santos:
            with st.expander(f"☩ {nome}", expanded=False):
                st.markdown(f"<p style='font-size: 1.05rem; line-height: 1.6; color: #2B1810;'>{bio}</p>", unsafe_allow_html=True)
