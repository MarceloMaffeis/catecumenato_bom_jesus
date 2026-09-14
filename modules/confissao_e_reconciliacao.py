# -*- coding: utf-8 -*-
"""
Módulo Pastoral: O Sacramento da Reconciliação & Santa Confissão
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            🕊️ O Sacramento da Reconciliação & Santa Confissão
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            "A quem perdoardes os pecados, ser-lhes-ão perdoados" (Jo 20, 23) • O abraço misericordioso do Pai
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_passos, tab_exame, tab_roteiro, tab_oracoes, tab_duvidas = st.tabs([
        "🕊️ Os 5 Passos da Boa Confissão",
        "🔍 Exame de Consciência Interativo",
        "⛪ Roteiro Prático no Confessionário",
        "📜 Fórmulas & Orações Penitenciais",
        "❓ Dúvidas & Escrupulosidades"
    ])

    # 1. Os 5 Passos
    with tab_passos:
        st.markdown("""
        <div class="pergaminho-card-franciscano">
            <h3 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                ☩ As Cinco Condições para uma Confissão Frutuosa
            </h3>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                A Igreja Católica ensina, com base na Sagrada Tradição e no Catecismo (CIC 1450-1460), 
                que o penitente precisa percorrer cinco etapas para receber dignamente a absolvição dos seus pecados:
            </p>
        </div>
        """, unsafe_allow_html=True)

        passos = [
            ("1. Exame de Consciência", "Relembrar diante de Deus, com sinceridade e sob a luz do Espírito Santo, todos os pecados cometidos por pensamentos, palavras, atos e omissões desde a última confissão bem feita."),
            ("2. Dor ou Contrição do Coração", "É o pesar da alma e a aversão ao pecado cometido, com a convicção de que ele ofendeu a Deus, que é infinitamente bom, e feriu a comunhão com os irmãos. A contrição perfeita nasce do amor a Deus; a imperfeita (atrição) nasce do temor do castigo eterno."),
            ("3. Firme Propósito de Emenda", "A decisão sincera e inabalável da vontade de não mais pecar e de evitar as ocasiões próximas de pecado. Não significa que você nunca mais terá tentações ou fraquezas, mas que está disposto a lutar com a graça divina."),
            ("4. Confissão Íntegra ao Sacerdote", "Acusar todos os pecados graves (mortais) conhecidos em espécie (o que foi feito) e número (quantas vezes, ainda que aproximado) ao sacerdote católico, que age in Persona Christi. Ocultar conscientemente um pecado grave torna a confissão inválida e comete-se sacrilégio."),
            ("5. Cumprimento da Penitência (Satisfação)", "Realizar com devoção a oração, obra de caridade ou sacrifício imposto pelo sacerdote para reparar os danos temporais do pecado e reeducar a alma na virtude.")
        ]

        for titulo, desc in passos:
            st.markdown(f"""
            <div class="pergaminho-card" style="margin-bottom: 0.8rem; border-left: 4px solid #781826;">
                <h4 style="color: #781826; font-family: 'Cinzel', serif; margin: 0 0 0.3rem 0;">
                    {titulo}
                </h4>
                <p style="font-size: 1.02rem; line-height: 1.6; color: #2B1810; margin: 0;">
                    {desc}
                </p>
            </div>
            """, unsafe_allow_html=True)

    # 2. Exame de Consciência Interativo
    with tab_exame:
        st.markdown("""
        <div style="background: #FAF5EB; border: 1px solid #D8C8B4; padding: 1rem; border-radius: 8px; margin-bottom: 1.2rem;">
            <strong style="color: #781826; font-family: 'Cinzel', serif; font-size: 1.05rem;">
                🔒 Sigilo Sagrado e Intimidade da Alma
            </strong>
            <p style="font-size: 0.95rem; color: #4A2E1B; margin: 0.3rem 0 0 0;">
                Este exame de consciência é estritamente íntimo entre você e Deus. 
                <strong>Nenhuma das suas marcações é salva em nosso banco de dados</strong> ou transmitida pela internet. 
                Use os botões de recolhimento para preparar tranquilamente o seu coração antes de se confessar.
            </p>
        </div>
        """, unsafe_allow_html=True)

        mandamentos_exame = [
            ("1º Mandamento: Amar a Deus sobre todas as coisas", [
                "Neguei ou duvidei voluntariamente de alguma verdade de fé católica revelada por Deus?",
                "Envolvi-me com superstições, astrologia, cartomancia, espiritismo, curandeirismo ou ocultismo?",
                "Deixei de rezar por preguiça ou indiferença prolongada?",
                "Cometi sacrilégio, recebendo a Sagrada Eucaristia em estado de pecado grave?"
            ]),
            ("2º Mandamento: Não tomar seu santo Nome em vão", [
                "Pronunciei o santo Nome de Deus, de Jesus Cristo, da Virgem Maria ou dos Santos com raiva, leviandade ou zombaria?",
                "Jurei em falso, invocando o Nome divino como testemunha de uma mentira?",
                "Deixei de cumprir promessas ou votos feitos a Deus?"
            ]),
            ("3º Mandamento: Guardar domingos e festas de preceito", [
                "Faltei deliberadamente à Santa Missa aos domingos ou dias de preceito por culpa própria e sem motivo grave (doença/impossibilidade real)?",
                "Trabalhei ou obriguei outros a realizarem trabalhos servis desnecessários aos domingos, impedindo o devido culto a Deus e o descanso da alma?"
            ]),
            ("4º Mandamento: Honrar pai e mãe", [
                "Fui desrespeitoso, desobediente ou ingrato com meus pais ou superiores legítimos?",
                "Negligenciei o auxílio material, afetivo e espiritual aos meus pais na velhice ou enfermidade?",
                "(Para pais): Negligenciei a educação cristã, a oração e o exemplo católico de meus filhos?"
            ]),
            ("5º Mandamento: Não matar", [
                "Alimentei sentimentos de ódio, vingança, rancor ou recusei o perdão a quem me ofendeu?",
                "Cometi, colaborei, aconselhei ou apoiei o pecado gravíssimo do aborto provocado?",
                "Prejudiquei minha saúde ou meu corpo com embriaguez, drogas ou excessos?",
                "Matei a reputação de alguém pela violência, pela ira descontrolada ou pelo ódio?"
            ]),
            ("6º e 9º Mandamentos: Guardar a castidade e pureza", [
                "Consenti em pensamentos, desejos impuros ou fantasias lascivas deliberadas?",
                "Consumi pornografia (vídeos, revistas, internet) ou cometi atos impuros solitários (masturbação)?",
                "Cometi atos sexuais fora do santo sacramento do Matrimônio (fornicação, adultério)?",
                "Fui ocasião de escândalo pela imodéstia no vestir, no falar ou nas conversas licenciosas?"
            ]),
            ("7º e 10º Mandamentos: Não furtar e não cobiçar os bens alheios", [
                "Tomei algo que pertencia a outra pessoa ou causei prejuízo ao patrimônio alheio?",
                "Enganei alguém nos negócios, no peso, no troco ou no pagamento de dívidas e salários justos?",
                "Soneguei impostos justos ou cometi fraude?",
                "Alimentei inveja doentia do sucesso, dos bens ou das graças concedidas aos irmãos?"
            ]),
            ("8º Mandamento: Não levantar falso testemunho", [
                "Disse mentiras deliberadas para me defender ou para prejudicar alguém?",
                "Cometi calúnia (atribuir a alguém um mal que ele não fez) ou difamação/maledicência (espalhar defeitos reais dos outros sem justa causa)?",
                "Fiz juízos temerários e suspeitas injustas sobre o próximo?"
            ])
        ]

        for mand, perguntas in mandamentos_exame:
            with st.expander(f"☩ {mand}", expanded=False):
                for p in perguntas:
                    st.checkbox(p, key=f"exame_{hash(p)}")

    # 3. Roteiro no Confessionário
    with tab_roteiro:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ⛪ Roteiro Passo a Passo Diante do Sacerdote
        </h4>
        <p style="font-size: 1rem; color: #2B1810; line-height: 1.6;">
            Não tenha medo nem vergonha! O sacerdote acolhe você no confessionário como o Pai acolheu o Filho Pródigo. 
            Ele está sob o <strong>sigilo sacramental absoluto</strong> (segredo inviolável de confissão, sob pena de excomunhão).
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pergaminho-card">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                1. Chegada e Saudação Inicial
            </h4>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                Ajoelhe-se ou sente-se diante do sacerdote. Faça o Sinal da Cruz:<br>
                <strong>Você:</strong> <em>"Em nome do Pai, do Filho e do Espírito Santo. Amém. Abençoai-me, Padre, porque pequei."</em><br>
                <strong>Você complementa:</strong> <em>"Minha última confissão bem feita foi há (diga quanto tempo, ou: 'Esta é a minha primeira confissão no Catecumenato de Adultos')."</em>
            </p>
            <hr style="border: 0; border-top: 1px dashed #D8C8B4; margin: 1rem 0;">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                2. A Acusação Clara dos Pecados
            </h4>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                Diga seus pecados de forma simples, direta e sem rodeios. Não invente desculpas nem conte histórias longas sobre terceiros. Acuse seus próprios atos.<br>
                <em>"Padre, eu me acuso de ter cometido... (diga os pecados e aproximadamente quantas vezes)."</em><br>
                Ao final, diga: <em>"Padre, peço perdão destes pecados e de todos aqueles de que não me recordo no momento."</em>
            </p>
            <hr style="border: 0; border-top: 1px dashed #D8C8B4; margin: 1rem 0;">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                3. Conselho Espiritual e Imposição da Penitência
            </h4>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                O sacerdote lhe dará um conselho paternal para sua cura espiritual e indicará a penitência (ex: rezar um Salmo, meditar o Terço, fazer uma obra de caridade).
            </p>
            <hr style="border: 0; border-top: 1px dashed #D8C8B4; margin: 1rem 0;">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                4. O Ato de Contrição
            </h4>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                O padre pedirá que você reze o Ato de Contrição em voz alta.
            </p>
            <hr style="border: 0; border-top: 1px dashed #D8C8B4; margin: 1rem 0;">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                5. A Sagrada Absolvição
            </h4>
            <p style="font-size: 1.05rem; line-height: 1.6; color: #2B1810;">
                O padre estende as mãos sobre sua cabeça e pronuncia as palavras de Cristo:<br>
                <em>"...E eu te absolvo dos teus pecados em nome do Pai e do Filho e do Espírito Santo."</em><br>
                <strong>Você responde:</strong> <em>"Amém!"</em><br>
                <strong>Padre:</strong> <em>"Ide em paz e o Senhor vos acompanhe."</em><br>
                <strong>Você:</strong> <em>"Graças a Deus!"</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 4. Fórmulas e Orações
    with tab_oracoes:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            📜 Orações Tradicionais do Penitente
        </h4>
        """, unsafe_allow_html=True)

        col_or1, col_or2 = st.columns(2)
        with col_or1:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    ☩ Ato de Contrição Tradicional
                </h5>
                <p style="font-size: 1.05rem; line-height: 1.7; color: #2B1810; font-style: italic;">
                    "Senhor meu Jesus Cristo, Deus e Homem verdadeiro, Criador e Redentor meu,
                    por serdes Vós quem sois, sumamente bom e digno de ser amado sobre todas as coisas,
                    e porque Vos amo e estimo, pesa-me, Senhor, de todo o meu coração de Vos ter ofendido;
                    pesa-me também de ter perdido o Céu e merecido o Inferno;
                    e proponho firmemente, ajudado com os auxílios da Vossa divina graça,
                    emendar-me e nunca mais Vos tornar a ofender.
                    Espero alcançar o perdão de minhas culpas pela Vossa infinita misericórdia.
                    Amém."
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col_or2:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    ☩ Ato de Contrição Bíblico (Mais Breve)
                </h5>
                <p style="font-size: 1.05rem; line-height: 1.7; color: #2B1810; font-style: italic;">
                    "Meu Deus, eu me arrependo de todo o coração de Vos ter ofendido, 
                    porque sois tão bom e amável. 
                    Prometo, com a Vossa graça, nunca mais pecar e evitar as ocasiões de pecado. 
                    Meu Jesus, misericórdia!"
                </p>
                <hr style="border: 0; border-top: 1px dashed #D8C8B4; margin: 1rem 0;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    ☩ Oração Antes da Confissão
                </h5>
                <p style="font-size: 0.98rem; line-height: 1.6; color: #3A2315;">
                    <em>"Vinde, Espírito Santo, iluminai a minha inteligência para que eu conheça os meus pecados; 
                    tocai o meu coração para que eu me arrependa deles com sincera dor; 
                    fortalecei a minha vontade para que eu os confesse com humildade e não torne a cair. 
                    Maria, Refúgio dos Pecadores, rogai por mim!"</em>
                </p>
            </div>
            """, unsafe_allow_html=True)

    # 5. Dúvidas Frequentes
    with tab_duvidas:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ❓ Dúvidas e Consolo Pastoral
        </h4>
        """, unsafe_allow_html=True)

        duvidas = [
            ("E se eu esquecer algum pecado sem querer?", "Se você não se lembrou de um pecado grave durante a confissão (esquecimento involuntário, sem má fé), a sua confissão é plenamente válida e aquele pecado foi perdoado! Porém, quando você se lembrar dele no futuro, deverá mencioná-lo na sua próxima confissão ordinária."),
            ("O padre pode contar meus pecados para alguém?", "JAMAIS! O sacerdote está obrigado ao 'Sigilo Sacramental' (Sigillum Confessionis). A Igreja estabelece pena de excomunhão automática reservada à Santa Sé para o padre que violar o sigilo de qualquer confissão, sob qualquer pretexto, até mesmo para salvar a própria vida."),
            ("Por que não posso me confessar direto com Deus?", "Deus certamente ouve nosso arrependimento sincero, mas foi o próprio Jesus Cristo quem quis e instituiu o sacramento visível ao dizer aos Seus Apóstolos: 'Aqueles a quem perdoardes os pecados, ser-lhes-ão perdoados' (Jo 20, 23). O ser humano precisa ouvir a certeza audível do perdão ('Eu te absolvo') pela autoridade conferida à Sua Santa Igreja."),
            ("Tenho muita vergonha de confessar certos pecados. O que fazer?", "A vergonha é a consequência do pecado, mas lembre-se: o padre já ouviu todo tipo de fraqueza humana ao longo dos anos. Ele não está ali para julgar, mas para ser o médico das almas em nome de Cristo. Quanto mais humilde for sua confissão, maior será a paz que invadirá o seu coração!")
        ]

        for p, r in duvidas:
            with st.expander(f"📌 {p}", expanded=False):
                st.markdown(f"<p style='font-size: 1.05rem; line-height: 1.6; color: #2B1810;'>{r}</p>", unsafe_allow_html=True)
