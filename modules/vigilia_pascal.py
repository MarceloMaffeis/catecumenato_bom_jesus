# -*- coding: utf-8 -*-
"""
Módulo Pastoral: A Vigília Pascal & Guia dos Padrinhos e Madrinhas
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            🕯️ A Vigília Pascal & O Guia dos Padrinhos
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            "Esta é a noite em que Cristo rompeu as cadeias da morte e triunfante ressurgiu dos infernos!" • A Mãe de Todas as Vigílias
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_vigilia, tab_padrinhos, tab_rituais = st.tabs([
        "🕯️ As 4 Partes da Vigília Pascal",
        "🤝 Guia dos Padrinhos & Madrinhas",
        "🌊 O Rito da Iniciação dos Adultos"
    ])

    # 1. As 4 Partes
    with tab_vigilia:
        st.markdown("""
        <div class="pergaminho-card-franciscano">
            <h3 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                ☩ A Mãe de Todas as Santas Vigílias (Santo Agostinho)
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                A celebração da Noite Santa da Páscoa é a celebração litúrgica mais importante de todo o ano católico. 
                É nela que os catecúmenos adultos recebem os Sacramentos da Iniciação Cristã (Batismo, Crisma e Primeira Comunhão).
                A celebração desenvolve-se em quatro momentos sublimes:
            </p>
        </div>
        """, unsafe_allow_html=True)

        partes = [
            ("1ª Parte: O Lucernário (A Bênção do Fogo Novo e o Círio Pascal)", "A igreja está completamente às escuras. No exterior, acende-se uma fogueira (o Fogo Novo). O sacerdote abençoa o Círio Pascal, cravando nele grãos de incenso e dizendo: 'Cristo ontem e hoje, Princípio e Fim, Alfa e Ômega!'. O Círio entra na nave escura enquanto o diácono entoa por três vezes: 'Eis a Luz de Cristo!'. As velas de todos os fiéis são acesas nessa mesma chama. Em seguida, proclama-se o Exsultet (o hino triunfal da Proclamação da Páscoa)."),
            ("2ª Parte: A Liturgia da Palavra (O Percurso da Salvação)", "Medita-se através das Escrituras todas as maravilhas que Deus realizou desde a Criação, passando pelo sacrifício de Abraão e a travessia do Mar Vermelho, até culminar nas promessas dos Profetas. Ao término, os sinos da igreja tocam solenemente e entoa-se festivamente o hino do Glória e o canto pascal do Aleluia!"),
            ("3ª Parte: A Liturgia Batismal e Crismal", "Momento central para os nossos catecúmenos! Entoa-se a Ladainha de Todos os Santos. O sacerdote abençoa a água batismal mergulhando o Círio Pascal nela. Os catecúmenos fazem a renúncia a Satanás e a profissão de fé. São batizados, ungidos com o Santo Crisma e revestidos com a veste branca da pureza pascal."),
            ("4ª Parte: A Liturgia Eucarística Pascal", "Pela primeira vez em suas vidas, os novos cristãos (neófitos) participam da mesa do Senhor, recebendo o Corpo e o Sangue de Nosso Senhor Jesus Cristo sob as duas espécies sagradas.")
        ]

        for tit, desc in partes:
            st.markdown(f"""
            <div class="pergaminho-card" style="margin-bottom: 0.8rem; border-left: 4px solid #781826;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin: 0 0 0.3rem 0;">
                    {tit}
                </h4>
                <p style="font-size: 1.02rem; line-height: 1.6; color: #2B1810; margin: 0;">
                    {desc}
                </p>
            </div>
            """, unsafe_allow_html=True)

    # 2. Guia dos Padrinhos
    with tab_padrinhos:
        st.markdown("""
        <div class="pergaminho-card-bordo">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                🤝 O que Significa ser Padrinho ou Madrinha no Catecumenato?
            </h4>
            <p style="font-size: 1.02rem; line-height: 1.6; color: #2B1810;">
                Ser padrinho ou madrinha não é um título social, nem um favor de amizade ou parentesco. 
                É um <strong>ministério espiritual sagrado</strong> assumido perante Deus e a Sua Igreja. 
                O padrinho torna-se fiador da fé do catecúmeno e se compromete a acompanhá-lo por toda a vida terrena com orações e testemunho vivo.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_req1, col_req2 = st.columns(2)
        with col_req1:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    📜 Requisitos Canônicos (Código de Direito Canônico)
                </h5>
                <ul style="font-size: 0.98rem; line-height: 1.7; color: #2B1810;">
                    <li>Ter no mínimo 16 anos de idade completos;</li>
                    <li>Ser católico batizado, crismado e que já tenha feito a Primeira Comunhão;</li>
                    <li>Levar uma vida de acordo com a fé católica (participar da Missa, confessar-se, viver o matrimônio se casado for na Igreja);</li>
                    <li>Não estar impedido por nenhuma pena canônica legitimamente imposta;</li>
                    <li>Não ser o pai ou a mãe do catecúmeno (o padrinho representa a Igreja).</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col_req2:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🕊️ A Missão do Padrinho no Dia a Dia
                </h5>
                <ul style="font-size: 0.98rem; line-height: 1.7; color: #2B1810;">
                    <li><strong>Orar constantemente:</strong> Colocar o afilhado diariamente nas intenções do Terço e da Santa Missa;</li>
                    <li><strong>Dar bom testemunho:</strong> O afilhado aprende muito mais pelo exemplo cristão do padrinho do que por meras palavras;</li>
                    <li><strong>Apoiar nos momentos de crise:</strong> Ajudar o afilhado a não se afastar da Igreja e dos Sacramentos diante das tentações do mundo;</li>
                    <li><strong>Presença constante:</strong> Fazer-se presente nas datas litúrgicas importantes e celebrar o aniversário do Batismo.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # 3. Ritos e Símbolos
    with tab_rituais:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            🌊 Os Santos Símbolos da Iniciação Cristã
        </h4>
        """, unsafe_allow_html=True)

        simbolos = [
            ("A Água Batismal", "Símbolo de purificação e nova vida. Pelo Batismo, o catecúmeno é sepultado com Cristo na Sua morte para ressurgir com Ele como criatura nova, filho amado de Deus e templo vivo do Espírito Santo."),
            ("O Santo Óleo do Crisma", "Azeite perfumado com bálsamo, consagrado solene pelo Bispo na Quinta-feira Santa. A unção na fronte imprime na alma o caráter indelével (o selo) do Espírito Santo, transformando o crismado em apóstolo corajoso e soldado de Cristo."),
            ("A Veste Branca", "Simboliza que o novo cristão foi purificado de todo pecado (original e pessoal) e 'revestiu-se de Cristo'. O sacerdote diz: 'Recebe esta veste branca e leva-a sem mancha até o tribunal de Nosso Senhor Jesus Cristo!"),
            ("A Vela Acesa no Círio Pascal", "O neófito acende sua vela diretamente da chama do Círio Pascal. Simboliza que agora ele possui a Luz de Cristo viva no seu coração e é chamado a ser luz do mundo pelo seu testemunho de vida.")
        ]

        for s, d in simbolos:
            st.markdown(f"""
            <div class="pergaminho-card" style="margin-bottom: 0.7rem; border-left: 4px solid #781826;">
                <strong style="color: #781826; font-size: 1.05rem;">{s}</strong>
                <p style="margin: 0.3rem 0 0 0; font-size: 0.98rem; color: #2B1810; line-height: 1.5;">{d}</p>
            </div>
            """, unsafe_allow_html=True)
