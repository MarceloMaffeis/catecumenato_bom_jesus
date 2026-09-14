# -*- coding: utf-8 -*-
"""
Módulo Pastoral: A Vida Moral em Cristo — Mandamentos, Virtudes e Graça
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            📜 A Vida Moral em Cristo: Mandamentos & Virtudes
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            "Se me amais, guardareis os meus mandamentos" (Jo 14, 15) • O caminho da bem-aventurança e santidade
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_decalogo, tab_virtudes, tab_pecados, tab_misericordia, tab_igreja = st.tabs([
        "📜 Os Dez Mandamentos (CIC)",
        "💎 As Sete Virtudes Cristãs",
        "⚔️ Os Pecados Capitais & Remédios",
        "🤝 As 14 Obras de Misericórdia",
        "⛪ Os 5 Preceitos da Igreja"
    ])

    # 1. Os Dez Mandamentos
    with tab_decalogo:
        st.markdown("""
        <div class="pergaminho-card-franciscano">
            <h3 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                ☩ A Lei Antiga Aperfeiçoada por Jesus Cristo
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                Os Dez Mandamentos (o Decálogo) foram entregues por Deus a Moisés no Monte Sinai e aperfeiçoados 
                por Nosso Senhor Jesus Cristo no Sermão da Montanha. Não são restrições que tiram a liberdade humana, 
                mas a verdadeira bússola da vida e o mapa do Amor autêntico.
            </p>
        </div>
        """, unsafe_allow_html=True)

        decalogo = [
            ("1º Mandamento: Amar a Deus sobre todas as coisas", "Êxodo 20, 2-5", "Ordena: A adoração exclusiva ao único Deus verdadeiro, a prática das virtudes teologais (Fé, Esperança e Caridade) e a oração perseverante.\nProíbe: A idolatria, a superstição, o espiritismo, o ateísmo prático, o sacrilégio e a desconfiança em Deus."),
            ("2º Mandamento: Não tomar seu santo Nome em vão", "Êxodo 20, 7", "Ordena: O respeito absoluto e o louvor ao Nome de Deus, de Jesus Cristo, da Virgem Maria e dos Santos.\nProíbe: A blasfêmia, a imprecação, o juramento falso e o uso leviano do sagrado."),
            ("3º Mandamento: Guardar domingos e festas de preceito", "Êxodo 20, 8-11", "Ordena: A santificação do Dia do Senhor (Domingo, dia da Ressurreição) com a participação plena na Santa Missa, as obras de caridade e o descanso da alma.\nProíbe: A falta voluntária à Missa dominical e os trabalhos servis desnecessários que impeçam o culto divino."),
            ("4º Mandamento: Honrar pai e mãe", "Êxodo 20, 12", "Ordena: O amor, o respeito, a gratidão e a obediência aos pais e autoridades legítimas, e o amparo filial na velhice e enfermidade.\nProíbe: O desprezo, a ingratidão, a desobediência filial e a negligência dos pais na educação cristã dos filhos."),
            ("5º Mandamento: Não matar", "Êxodo 20, 13", "Ordena: O respeito sagrado à vida humana desde a concepção até a morte natural, a defesa dos vulneráveis e a saúde corporal.\nProíbe: O homicídio, o aborto provocado, a eutanásia, o suicídio, a violência, o ódio, o rancor e os escândalos que conduzem outros ao pecado."),
            ("6º Mandamento: Não pecar contra a castidade", "Êxodo 20, 14", "Ordena: A pureza de vida, a castidade segundo o próprio estado (solteiro, casado, consagrado) e a fidelidade conjugal no santo Matrimônio.\nProíbe: O adultério, a fornicação, a pornografia, a masturbação, os atos homossexuais e a prostituição."),
            ("7º Mandamento: Não furtar", "Êxodo 20, 15", "Ordena: A justiça nas relações comerciais, o respeito ao patrimônio alheio, a caridade para com os pobres e o pagamento de salários justos.\nProíbe: O roubo, a fraude, o suborno, a usura, o desperdício egoísta e o prejuízo injusto aos bens do próximo."),
            ("8º Mandamento: Não levantar falso testemunho", "Êxodo 20, 16", "Ordena: A sinceridade, o testemunho da Verdade em Cristo e a defesa da boa reputação dos irmãos.\nProíbe: A mentira, a calúnia, a difamação (fofoca), o falso testemunho em juízo e os juízos temerários."),
            ("9º Mandamento: Não desejar a mulher do próximo", "Êxodo 20, 17", "Ordena: A pureza do coração e dos pensamentos, o pudor cristão no vestir e no agir e a modéstia dos sentimentos.\nProíbe: A cobiça desordenada dos desejos carnais, a lascívia mental e a cumplicidade com os olhares impuros."),
            ("10º Mandamento: Não cobiçar as coisas alheias", "Êxodo 20, 17", "Ordena: A pobreza de espírito franciscana, o desapego dos bens terrenos e a santa alegria pelo bem do irmão.\nProíbe: A inveja dos bens ou do sucesso do próximo, a avareza e a ganância desmedida.")
        ]

        for titulo, ref, texto in decalogo:
            with st.expander(f"☩ {titulo}", expanded=False):
                st.markdown(f"**Referência:** *{ref}*")
                partes = texto.split("\n")
                for p in partes:
                    st.markdown(f"- {p}")

    # 2. As Sete Virtudes
    with tab_virtudes:
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🕊️ As 3 Virtudes Teologais
                </h4>
                <p style="font-size: 0.95rem; color: #5A3825; font-style: italic;">
                    Infundidas diretamente por Deus na alma através da graça do Santo Batismo (CIC 1812-1829):
                </p>
                <p style="font-size: 1.02rem; line-height: 1.6; color: #2B1810;">
                    <strong>1. Fé:</strong> A virtude pela qual cremos firmemente em Deus e em tudo o que Ele revelou e a Santa Igreja nos propõe a crer.<br><br>
                    <strong>2. Esperança:</strong> A virtude pela qual desejamos e esperamos com inabalável confiança a vida eterna e a graça de perseverar até o fim.<br><br>
                    <strong>3. Caridade (Amor):</strong> A maior de todas as virtudes! Pela qual amamos a Deus sobre todas as coisas e ao próximo como a nós mesmos por amor a Deus.
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col_v2:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🛡️ As 4 Virtudes Cardeais
                </h4>
                <p style="font-size: 0.95rem; color: #5A3825; font-style: italic;">
                    Os quatro pilares (charneiras) em torno dos quais giram todas as demais virtudes humanas:
                </p>
                <p style="font-size: 1.02rem; line-height: 1.6; color: #2B1810;">
                    <strong>1. Prudência:</strong> Dispõe a razão prática a discernir em qualquer circunstância o nosso verdadeiro bem e escolher os meios justos de realizá-lo.<br><br>
                    <strong>2. Justiça:</strong> A constante e firme vontade de dar a Deus e ao próximo o que lhes é de direito.<br><br>
                    <strong>3. Fortaleza:</strong> Assegura a firmeza e a coragem nas dificuldades, e a constância na busca do bem, mesmo diante da perseguição e da morte.<br><br>
                    <strong>4. Temperança:</strong> Modera a atração dos prazeres e assegura o equilíbrio no uso dos bens criados, dominando as paixões da carne.
                </p>
            </div>
            """, unsafe_allow_html=True)

    # 3. Pecados Capitais e Remédios
    with tab_pecados:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ⚔️ O Bom Combate: Vícios Capitais vs. Remédios da Graça
        </h4>
        <p style="font-size: 0.98rem; color: #3A2315;">
            Os pecados capitais são raízes de todos os demais vícios na alma humana. A vida espiritual é a arte de substituí-los pela virtude contrária:
        </p>
        """, unsafe_allow_html=True)

        combate = [
            ("Soberba (Orgulho e vanglória)", "Humildade Franciscana", "A soberba faz o homem colocar-se no lugar de Deus. O remédio é a humildade: reconhecer que tudo o que temos de bom vem da graça divina."),
            ("Avareza (Amor desregrado ao dinheiro)", "Generosidade e Desapego", "O remédio é a partilha de bens, a esmola evangélica e a confiança na Divina Providência que cuida dos lírios do campo."),
            ("Luxúria (Apetite carnal desordenado)", "Pureza e Castidade", "O remédio é a mortificação dos sentidos, a fuga das ocasiões perigosas, a modéstia no olhar e a frequência aos Santos Sacramentos."),
            ("Ira (Cólera e ímpeto de vingança)", "Paciência e Mansidão", "O remédio é imitar a doçura de Cristo na Paixão: 'Aprendei de mim, que sou manso e humilde de coração' (Mt 11, 29)."),
            ("Gula (Excesso no comer e beber)", "Sobriedade e Jejum Litúrgico", "O remédio é a temperança, agradecendo o alimento sem fazer dele o senhor dos nossos instintos."),
            ("Inveja (Tristeza com o bem do irmão)", "Caridade Fraterna", "O remédio é alegrar-se verdadeiramente com as bênçãos e dons concedidos aos outros, sabendo que somos todos membros do mesmo Corpo Místico."),
            ("Preguiça Espiritual (Acídia)", "Fervor e Diligência na Oração", "O desânimo nas coisas de Deus. O remédio é a constância heroica nos deveres cotidianos e na vida de piedade.")
        ]

        for vicio, virtude, desc in combate:
            st.markdown(f"""
            <div class="pergaminho-card" style="margin-bottom: 0.6rem; border-left: 4px solid #781826;">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <span style="color: #A31D1D; font-weight: bold; font-size: 1.05rem;">❌ {vicio}</span>
                    <span style="color: #2E7D32; font-weight: bold; font-size: 1.05rem;">✅ {virtude}</span>
                </div>
                <p style="margin: 0.4rem 0 0 0; font-size: 0.98rem; color: #2B1810; line-height: 1.5;">
                    {desc}
                </p>
            </div>
            """, unsafe_allow_html=True)

    # 4. As 14 Obras de Misericórdia
    with tab_misericordia:
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("""
            <div class="pergaminho-card">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🥖 7 Obras de Misericórdia Corporais
                </h4>
                <ol style="font-size: 1.02rem; line-height: 1.8; color: #2B1810;">
                    <li>Dar de comer aos famintos.</li>
                    <li>Dar de beber a quem tem sede.</li>
                    <li>Vestir os nus.</li>
                    <li>Acolher os peregrinos e sem-teto.</li>
                    <li>Visitar e cuidar dos enfermos.</li>
                    <li>Visitar os presos.</li>
                    <li>Sepultar os mortos com dignidade.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        with col_m2:
            st.markdown("""
            <div class="pergaminho-card">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🕊️ 7 Obras de Misericórdia Espirituais
                </h4>
                <ol style="font-size: 1.02rem; line-height: 1.8; color: #2B1810;">
                    <li>Dar bom conselho a quem precisa.</li>
                    <li>Ensinar os que não sabem (catequese!).</li>
                    <li>Corrigir os que erram com caridade.</li>
                    <li>Consolar os aflitos e tristes.</li>
                    <li>Perdoar de coração as ofensas.</li>
                    <li>Suportar pacientemente as fraquezas alheias.</li>
                    <li>Rezar a Deus pelos vivos e pelos falecidos.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

    # 5. Os Cinco Mandamentos da Igreja
    with tab_igreja:
        st.markdown("""
        <div class="pergaminho-card-franciscano">
            <h3 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                ⛪ Os Cinco Preceitos da Santa Igreja Católica (CIC 2041-2043)
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                Assim como uma mãe zela pela saúde mínima dos seus filhos, a Santa Igreja estabelece 
                cinco mandamentos práticos indispensáveis para garantir a salvação das nossas almas:
            </p>
        </div>
        """, unsafe_allow_html=True)

        preceitos = [
            ("1º Preceito: Participar da Missa inteira nos domingos e festas de guarda", "Garante que o católico cultue a Deus no dia da Ressurreição do Senhor e nas grandes solenidades litúrgicas da Igreja."),
            ("2º Preceito: Confessar-se ao menos uma vez a cada ano", "Prepara a alma para o encontro com Cristo e assegura a remissão dos pecados graves cometidos após o Batismo."),
            ("3º Preceito: Comungar ao menos pela Páscoa da Ressurreição", "Garante a união mínima com o Corpo e Sangue de Cristo no ápice do Ano Litúrgico."),
            ("4º Preceito: Jejuar e abster-se de carne quando manda a Santa Igreja", "Determinado para a Quarta-feira de Cinzas e a Sexta-feira Santa; além de penitência nas sextas-feiras do ano para mortificação das paixões carnais."),
            ("5º Preceito: Ajudar a Igreja em suas necessidades materiais", "Contribuir generosamente com o Dízimo e as ofertas para a manutenção do culto divino, o sustento dos sacerdotes e a assistência aos pobres.")
        ]

        for p, d in preceitos:
            st.markdown(f"""
            <div class="pergaminho-card" style="margin-bottom: 0.8rem; border-left: 4px solid #781826;">
                <strong style="color: #781826; font-size: 1.05rem;">{p}</strong>
                <p style="margin: 0.3rem 0 0 0; font-size: 1rem; color: #2B1810; line-height: 1.5;">{d}</p>
            </div>
            """, unsafe_allow_html=True)
