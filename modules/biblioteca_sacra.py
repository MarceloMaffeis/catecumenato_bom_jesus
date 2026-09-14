# -*- coding: utf-8 -*-
"""
Módulo Biblioteca Sacra e Fontes da Fé Católica Ampliada
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
from style import render_divider

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            📜 Biblioteca Sacra & Fontes Autênticas da Fé
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            Sagrada Tradição, Sagrada Escritura, Concílios Ecumênicos, Encíclicas e Herança Franciscana
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_fundamentais, tab_concilio, tab_enciclicas, tab_licenca = st.tabs([
        "🏛️ Fontes Primordiais da Fé",
        "⛪ Documentos do Concílio Vaticano II",
        "📜 Grandes Encíclicas & Escritos dos Santos",
        "⚖️ Licença, Direitos Autorais & Arte Sacra"
    ])

    # 1. Fontes Primordiais
    with tab_fundamentais:
        # Fonte 1: Catecismo da Igreja Católica (CIC)
        st.markdown("""
        <div class="pergaminho-card-bordo">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="color: #781826; margin: 0; font-family: 'Cinzel', serif;">
                    🏛️ 1. Catecismo da Igreja Católica (CIC)
                </h4>
                <span style="background: #781826; color: white; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem; font-family: 'Cinzel', serif;">
                    Santa Sé • Vaticano
                </span>
            </div>
            <p style="font-size: 1.05rem; line-height: 1.6; margin-top: 0.8rem; color: #2D1B13;">
                Promulgado pelo Papa São João Paulo II através da Constituição Apostólica <em>Fidei Depositum</em> (1992), 
                o CIC é o compêndio seguro e autêntico de toda a sã doutrina católica.
            </p>
            <div style="background: #F3ECE2; padding: 0.8rem; border-radius: 4px; font-size: 0.95rem; margin-bottom: 0.8rem;">
                <strong>Estrutura fundamental nas 4 partes:</strong><br>
                1. A Profissão da Fé (O Credo) — CIC 26-1065<br>
                2. Os Sacramentos da Fé (A Liturgia) — CIC 1066-1690<br>
                3. A Vida na Fé (Os Mandamentos e a Moral) — CIC 1691-2557<br>
                4. A Oração na Fé (O Pai Nosso) — CIC 2558-2865
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(
            "🔗 Acessar Catecismo da Igreja Católica no Portal do Vaticano",
            "https://www.vatican.va/archive/cathechism_po/index_new/prima-pagina-cic_po.html"
        )

        render_divider("☩")

        # Fonte 2: Bíblia Católica
        st.markdown("""
        <div class="pergaminho-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="color: #781826; margin: 0; font-family: 'Cinzel', serif;">
                    📖 2. A Sagrada Escritura (Bíblia Católica)
                </h4>
                <span style="background: #C5A059; color: #2B1810; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem; font-family: 'Cinzel', serif; font-weight: bold;">
                    Edição Canônica (73 Livros)
                </span>
            </div>
            <p style="font-size: 1.05rem; line-height: 1.6; margin-top: 0.8rem; color: #2D1B13;">
                A Bíblia Católica completa preserva os 73 livros sagrados inspirados por Deus (46 no Antigo Testamento e 27 no Novo Testamento). 
                Disponibilizamos o leitor bíblico do apostolado do Pe. Paulo Ricardo com notas e comentários patrísticos.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(
            "🔗 Acessar Bíblia Católica Online (Padre Paulo Ricardo)",
            "https://padrepauloricardo.org/biblia"
        )

        render_divider("☩")

        # Fonte 3: CDC
        st.markdown("""
        <div class="pergaminho-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="color: #781826; margin: 0; font-family: 'Cinzel', serif;">
                    ⚖️ 3. Código de Direito Canônico (CDC)
                </h4>
                <span style="background: #781826; color: white; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem; font-family: 'Cinzel', serif;">
                    Legislação Eclesial
                </span>
            </div>
            <p style="font-size: 1.05rem; line-height: 1.6; margin-top: 0.8rem; color: #2D1B13;">
                As diretrizes canônicas que regem a Iniciação Cristã de Adultos: Cânones 851, 863, 865 e 866.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(
            "🔗 Acessar Código de Direito Canônico Oficial (Vaticano)",
            "https://www.vatican.va/archive/cdc/index_po.htm"
        )

        render_divider("☩")

        # Fonte 4: Didaqué
        st.markdown("""
        <div class="pergaminho-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="color: #781826; margin: 0; font-family: 'Cinzel', serif;">
                    🕯️ 4. A Didaqué (Doutrina dos Doze Apóstolos)
                </h4>
                <span style="background: #5A3825; color: white; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem; font-family: 'Cinzel', serif;">
                    Século I • Era Apostólica
                </span>
            </div>
            <p style="font-size: 1.05rem; line-height: 1.6; margin-top: 0.8rem; color: #2D1B13;">
                O catecismo mais antigo da Igreja cristã primitiva (ano 60-90 d.C.), ensinando o Caminho da Vida e da Morte.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(
            "🔗 Ler a Didaqué na Íntegra em Português",
            "https://www.monergismo.com/textos/credos/didaque.htm"
        )

        render_divider("☩")

        # Fonte 5: Suma Teológica
        st.markdown("""
        <div class="pergaminho-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="color: #781826; margin: 0; font-family: 'Cinzel', serif;">
                    🎓 5. Suma Teológica — Santo Tomás de Aquino
                </h4>
                <span style="background: #C5A059; color: #2B1810; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem; font-family: 'Cinzel', serif; font-weight: bold;">
                    Doutor Angélico
                </span>
            </div>
            <p style="font-size: 1.05rem; line-height: 1.6; margin-top: 0.8rem; color: #2D1B13;">
                A obra-prima do pensamento católico e da teologia dos sacramentos e da graça.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(
            "🔗 Baixar Suma Teológica Completa em PDF",
            "https://sumateologica.wordpress.com/wp-content/uploads/2017/04/suma-teolc3b3gica.pdf"
        )

        render_divider("☩")

        # Fonte 6: Franciscanos
        st.markdown("""
        <div class="pilula-franciscana">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="color: #5A3825; margin: 0; font-family: 'Cinzel', serif;">
                    🕊️ 6. Província Franciscana & Paróquia Bom Jesus dos Aflitos
                </h4>
                <span style="background: #5A3825; color: white; padding: 2px 10px; border-radius: 4px; font-size: 0.85rem; font-family: 'Cinzel', serif;">
                    Paz e Bem!
                </span>
            </div>
            <p style="font-size: 1.05rem; line-height: 1.6; margin-top: 0.8rem; color: #2D1B13;">
                A espiritualidade dos Frades Menores de São Francisco e Santa Clara de Assis no Brasil.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(
            "🔗 Portal Oficial dos Franciscanos no Brasil",
            "https://franciscanos.org.br/#gsc.tab=0"
        )

    # 2. Concílio Vaticano II
    with tab_concilio:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            As Grandes Constituições do Concílio Vaticano II (1962-1965)
        </h4>
        <p style="font-size: 1.05rem; line-height: 1.6;">
            O Concílio Ecumênico Vaticano II ofereceu documentos fundamentais para a catequese dos tempos modernos:
        </p>
        """, unsafe_allow_html=True)

        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">📜 Dei Verbum (A Palavra de Deus)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Constituição Dogmática sobre a Divina Revelação. Explica como Deus se revela à humanidade, 
                    a inspiração bíblica e a transmissão viva da fé pela Tradição e Magistério.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("🔗 Ler Dei Verbum no Vaticano", "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19651118_dei-verbum_po.html")

            st.markdown("""
            <div class="pergaminho-card" style="margin-top: 1rem;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">⛪ Sacrosanctum Concilium (A Liturgia)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Constituição sobre a Sagrada Liturgia. Define a Santa Missa e os sacramentos como fonte e ápice 
                    de toda a vida cristã e restaura o Catecumenato de Adultos (RICA).
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("🔗 Ler Sacrosanctum Concilium no Vaticano", "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19631204_sacrosanctum-concilium_po.html")

        with col_c2:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">🕊️ Lumen Gentium (A Luz dos Povos)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Constituição Dogmática sobre o mistério da Igreja como Povo de Deus, Corpo Místico de Cristo 
                    e a vocação universal de todos os cristãos à santidade no mundo.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("🔗 Ler Lumen Gentium no Vaticano", "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19641121_lumen-gentium_po.html")

            st.markdown("""
            <div class="pergaminho-card" style="margin-top: 1rem;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">🌍 Gaudium et Spes (A Igreja no Mundo)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Constituição Pastoral sobre a Igreja no mundo contemporâneo: família, trabalho, dignidade da pessoa humana, justiça e paz social.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("🔗 Ler Gaudium et Spes no Vaticano", "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19651207_gaudium-et-spes_po.html")

    # 3. Grandes Encíclicas
    with tab_enciclicas:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            Exortações Apostólicas, Encíclicas e Tratados dos Santos
        </h4>
        """, unsafe_allow_html=True)

        col_e1, col_e2 = st.columns(2)
        with col_e1:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">📖 Catechesi Tradendae — São João Paulo II (1979)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Exortação Apostólica fundamental sobre a catequese em nosso tempo: 'A finalidade definitiva da catequese 
                    é colocar a pessoa não apenas em contato, mas em comunhão, em intimidade com Jesus Cristo'.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("🔗 Acessar Catechesi Tradendae", "https://www.vatican.va/content/john-paul-ii/pt/apost_exhortations/documents/hf_jp-ii_exh_16101979_catechesi-tradendae.html")

            st.markdown("""
            <div class="pergaminho-card" style="margin-top: 1rem;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">👑 Tratado da Verdadeira Devoção à Santíssima Virgem</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Obra clássica de São Luís Maria Grignion de Montfort sobre a consagração total a Jesus por meio de Maria Santíssima.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col_e2:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">🔥 Evangelii Nuntiandi — São Paulo VI (1975)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Documento magno sobre a evangelização no mundo moderno: 'O homem contemporâneo escuta mais de bom grado 
                    as testemunhas do que os mestres, ou se escuta os mestres, é porque eles são testemunhas'.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("🔗 Acessar Evangelii Nuntiandi", "https://www.vatican.va/content/paul-vi/pt/apost_exhortations/documents/hf_p-vi_exh_19751208_evangelii-nuntiandi.html")

            st.markdown("""
            <div class="pilula-franciscana" style="margin-top: 1rem;">
                <h5 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">🌿 Laudato Si' — Papa Francisco (2015)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Inspirada no Cântico das Criaturas de São Francisco de Assis, esta encíclica aborda o cuidado 
                    da Casa Comum como compromisso autêntico da fé cristã com os mais pobres e com a criação de Deus.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("🔗 Acessar Laudato Si'", "https://www.vatican.va/content/francesco/pt/encyclicals/documents/papa-francesco_20150524_enciclica-laudato-si.html")

    # 4. Licença, Direitos Autorais & Arte Sacra
    with tab_licenca:
        st.markdown("""
        <div class="pergaminho-card-bordo">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                ⚖️ Licença de Software, Direitos Autorais & Arte Sacra
            </h4>
            <p style="font-size: 1.05rem; line-height: 1.7; color: #2D1B13; text-align: justify;">
                Este portal foi concebido com zelo apostólico e fidelidade à Santa Sé para apoiar a evangelização 
                e o catecumenato de adultos na <strong>Paróquia Bom Jesus dos Aflitos de Sorocaba/SP</strong> 
                (Frades Menores Franciscanos). Todos os direitos de propriedade intelectual, licenças e obras sacras 
                seguem rigorosamente os parâmetros éticos e legais vigentes:
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">💻 1. Licença MIT (Software Livre)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    O código-fonte do sistema está registrado no GitHub sob a <strong>Licença MIT</strong> (Copyright &copy; 2026 Marcelo Maffeis).
                </p>
                <ul style="font-size: 0.95rem; line-height: 1.6; padding-left: 1.2rem;">
                    <li><strong>Livre uso e modificação:</strong> Qualquer paróquia, diocese ou catequista tem permissão para utilizar, adaptar e executar a ferramenta.</li>
                    <li><strong>Sem fins comerciais:</strong> O projeto visa a caridade e o serviço ao Reino de Deus sem cobrança de taxas ou mensalidades.</li>
                    <li><strong>Transparência:</strong> O código completo está disponível publicamente para auditoria e melhorias contínuas da comunidade.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="pergaminho-card" style="margin-top: 1rem;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">🏛️ 3. Magistério e Textos Bíblicos</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    As citações bíblicas, orações tradicionais e parágrafos do <em>Catecismo da Igreja Católica (CIC)</em> 
                    pertencem ao patrimônio espiritual da Sé Apostólica e são utilizados sob o <strong>Direito de Citação</strong> 
                    (Lei nº 9.610/98, Art. 46, VIII), com indicação expressa dos livros e cânones canônicos para fins exclusivamente catequéticos.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col_l2:
            st.markdown("""
            <div class="pergaminho-card">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">🎨 2. Obras de Arte Sacra (Domínio Público)</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Todas as pinturas e afrescos sacros exibidos nos 40 encontros, na Santa Missa e no Santo Terço são obras-primas históricas 
                    produzidas entre os séculos XIII e XIX por gênios da cristandade (Michelangelo, Rafael, Caravaggio, Rembrandt, Fra Angelico, Giotto, Murillo, Perugino, etc.).
                </p>
                <ul style="font-size: 0.95rem; line-height: 1.6; padding-left: 1.2rem;">
                    <li><strong>Domínio Público Pleno:</strong> Obras criadas há séculos cujos direitos patrimoniais expiraram (Lei 9.610/98, Art. 41 e Convenção de Berna).</li>
                    <li><strong>Via Pulchritudinis:</strong> A beleza sacra como caminho pedagógico para elevar o coração a Deus.</li>
                    <li><strong>Proveniência:</strong> Wikimedia Commons / Museus Internacionais com identificação de título e autor.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="pilula-franciscana" style="margin-top: 1rem;">
                <h5 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">🕊️ 4. Carisma Franciscano & Paróquia</h5>
                <p style="font-size: 0.98rem; line-height: 1.6;">
                    Desenvolvido para a <strong>Paróquia Bom Jesus dos Aflitos de Sorocaba/SP</strong>, confiada aos cuidados da 
                    Ordem dos Frades Menores (OFM). Todas as referências às Fontes Franciscanas visam difundir o ideal de 
                    paz, fraternidade, amor aos pobres e cuidado com toda a criação. <em>Paz e Bem!</em>
                </p>
            </div>
            """, unsafe_allow_html=True)