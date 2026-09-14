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

    perfil = st.session_state.get("perfil_usuario", "visitante")
    cid_usuario = st.session_state.get("catecumeno_id", 0)
    nome_usuario = st.session_state.get("nome_usuario", "Irmão em Cristo")

    if perfil == "catequisando":
        # Painel Pessoal do Catequisando
        st.markdown(f"""
        <div class="pergaminho-card-franciscano">
            <h3 style="color: #5A3825; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span>☩</span> Paz e Bem, caríssimo(a) {nome_usuario}!
            </h3>
            <p style="font-size: 1.12rem; line-height: 1.6; margin-bottom: 0.3rem;">
                Seja bem-vindo ao seu espaço de formação na fé da <strong>Paróquia Bom Jesus dos Aflitos</strong>.
                Aqui você acompanha sua evolução espiritual, estuda os 40 encontros, realiza os exercícios de fixação e guarda suas reflexões para a vida eterna.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Métricas Pessoais de Progresso
        prog = database.get_progresso_catecumeno(cid_usuario)
        quiz_stats = database.get_estatisticas_quiz_catecumeno(cid_usuario)

        st.markdown("### 🕊️ Minha Jornada Espiritual no Catecumenato")
        
        # Barra de Progresso Visual
        progresso_decimal = min(prog["total_concluidos"] / 40.0, 1.0)
        st.progress(progresso_decimal, text=f"Progresso Geral da Formação: {prog['total_concluidos']} de 40 encontros concluídos ({prog['percentual']}%)")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Encontros Concluídos", value=f"{prog['total_concluidos']} / 40", delta=f"{prog['percentual']}%")
        with col2:
            st.metric(label="Encontros Restantes", value=f"{40 - prog['total_concluidos']}")
        with col3:
            st.metric(label="Questões de Fé Feitas", value=quiz_stats["total_respondidas"])
        with col4:
            st.metric(label="Taxa de Acertos no Quiz", value=f"{quiz_stats['taxa_acerto']}%", delta=f"{quiz_stats['total_acertos']} acertos")

        # Próximo Encontro Sugerido & Marco Espiritual
        proximo_enc_num = 1
        for num in range(1, 41):
            if num not in prog["lista_concluidos"]:
                proximo_enc_num = num
                break

        enc_prox = database.get_encontro_by_numero(proximo_enc_num)
        
        # Marco Espiritual Atual
        if prog["total_concluidos"] == 0:
            marco_titulo = "🌱 Início da Caminhada"
            marco_desc = "Você está prestes a dar os primeiros passos nesta linda jornada com Cristo Jesus!"
        elif prog["total_concluidos"] < 10:
            marco_titulo = "🌿 Semeador da Palavra"
            marco_desc = "Você já iniciou os estudos e a semente da fé está brotando no seu coração."
        elif prog["total_concluidos"] < 20:
            marco_titulo = "📜 Ouvinte Atento do Evangelho"
            marco_desc = "Você aprofundou a Palavra e o Magistério, construindo sua fé sobre a rocha firme."
        elif prog["total_concluidos"] < 30:
            marco_titulo = "✝️ Discípulo do Bom Jesus"
            marco_desc = "Você conhece a doutrina dos Sacramentos e vive a fraternidade franciscana."
        elif prog["total_concluidos"] < 40:
            marco_titulo = "⛪ Pilar Vivo da Comunidade"
            marco_desc = "Falta muito pouco para a conclusão total do itinerário de formação catequética!"
        else:
            marco_titulo = "🌟 Plena Prontidão Pascal"
            marco_desc = "Louvado seja Deus! Todos os 40 encontros concluídos. Você está pronto para os Santos Mistérios!"

        col_prox, col_marco = st.columns([1.3, 1])
        with col_prox:
            if enc_prox:
                st.markdown(f"""
                <div class="pergaminho-card-bordo">
                    <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                        🎯 Próximo Encontro da Sua Caminhada
                    </h4>
                    <p style="font-size: 1.15rem; font-weight: bold; color: #2B1810; margin-bottom: 0.3rem;">
                        Encontro {enc_prox['numero']:02d}: {enc_prox['titulo']}
                    </p>
                    <p style="font-size: 0.95rem; color: #5A3825; font-style: italic; margin-bottom: 0.8rem;">
                        Módulo: {enc_prox['bloco']}
                    </p>
                    <p style="font-size: 0.98rem; color: #3A2315; line-height: 1.5;">
                        {enc_prox['resumo'][:160]}...
                    </p>
                </div>
                """, unsafe_allow_html=True)
        with col_marco:
            st.markdown(f"""
            <div class="pilula-franciscana">
                <h4 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                    {marco_titulo}
                </h4>
                <p style="font-size: 1.05rem; line-height: 1.6; color: #2E1B10; font-style: italic;">
                    "{marco_desc}"
                </p>
                <div style="font-size: 0.88rem; color: #781826; font-weight: bold; margin-top: 0.5rem;">
                    Status: {prog['total_concluidos']} / 40 encontros concluídos
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Certificado Solene de Conclusão (quando atingir 40 encontros ou botão pastoral)
        if prog["total_concluidos"] >= 40:
            st.markdown("---")
            st.success("🎉 **Parabéns em Cristo! Você completou com louvor todos os 40 encontros do Catecumenato!**")
            from modules.certificado import render_certificado_html
            cert_html = render_certificado_html(nome_usuario)
            col_cert1, col_cert2 = st.columns([2.5, 1.5])
            with col_cert1:
                st.markdown("Seu **Certificado Solene de Formação Catequética** está emitido e pronto para ser impresso ou salvo em PDF.")
            with col_cert2:
                st.download_button(
                    label="🎓 Baixar / Imprimir Certificado",
                    data=cert_html.encode("utf-8"),
                    file_name=f"certificado_catecumenato_{nome_usuario.replace(' ', '_')}.html",
                    mime="text/html",
                    use_container_width=True
                )

        # Linha do Tempo Unificada do Diário Espiritual do Aluno
        st.markdown("---")
        with st.expander("📜 Meu Diário de Bordo Espiritual (Todas as Minhas Reflexões)", expanded=False):
            todas_anotacoes = database.get_todas_anotacoes_catecumeno(cid_usuario)
            if todas_anotacoes:
                st.markdown(f"**Total de reflexões e partilhas registradas ao longo do ano:** {len(todas_anotacoes)}")
                for a in todas_anotacoes:
                    st.markdown(f"""
                    <div style="background: #FAF8F5; border: 1px solid #D8C8B4; border-left: 4px solid #781826; padding: 0.8rem 1rem; border-radius: 6px; margin-bottom: 0.8rem;">
                        <div style="display: flex; justify-content: space-between; font-size: 0.88rem; color: #781826; font-weight: bold;">
                            <span>📖 Encontro {a['encontro_numero']:02d}: {a.get('titulo_encontro', 'Encontro')}</span>
                            <span>📅 {a['data_registro']}</span>
                        </div>
                        <p style="font-size: 1.02rem; margin: 0.5rem 0 0 0; color: #2B1810; line-height: 1.5;">
                            {a['texto']}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("Você ainda não registrou reflexões no diário. Ao estudar os encontros e responder aos quizzes, registre suas orações na aba 'Diário & Partilha'!")

    else:
        # Modo Catequista Administrador
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
        import os
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_cruz = os.path.join(base_dir, "assets", "images", "encontro_15.jpg")
        if not os.path.exists(caminho_cruz):
            caminho_cruz = os.path.join("assets", "images", "encontro_15.jpg")
        if os.path.exists(caminho_cruz):
            st.image(caminho_cruz, caption="O Santo Crucifixo de São Damião: 'Francisco, vai e restaura a Minha Igreja!'", use_container_width=True)

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
                ⚡ Pilares da Formação
            </h4>
            <p style="font-size: 0.98rem; margin-bottom: 0.8rem;">Dimensões organizadas no menu lateral:</p>
            <ul style="font-size: 0.96rem; line-height: 1.8; list-style-type: none; padding-left: 0;">
                <li>🎓 <strong>Curso & Formação:</strong> Encontros, Chamada e Vigília</li>
                <li>🏛️ <strong>Teologia & Doutrina:</strong> Tratados, Moral e Confissão</li>
                <li>⛪ <strong>Liturgia & Oração:</strong> Santa Missa, Terço e Tesouro Franciscano</li>
                <li>🔍 <strong>Pesquisa & Fontes:</strong> Biblioteca Sacra, CIC e Bíblia</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)