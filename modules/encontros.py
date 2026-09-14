# -*- coding: utf-8 -*-
"""
Módulo dos 40 Encontros do Catecumenato com Arte Sacra Católica
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
import database
from style import render_divider

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            ☩ Os 40 Encontros do Catecumenato ☩
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            Sequência completa de formação doutrinal, bíblica, espiritual e litúrgica
        </p>
    </div>
    """, unsafe_allow_html=True)

    blocos = ["Todos os Blocos"] + database.get_blocos()

    col_filtro1, col_filtro2 = st.columns([1.2, 1.8])
    with col_filtro1:
        bloco_selecionado = st.selectbox("Filtrar por Módulo Temático:", blocos)
    with col_filtro2:
        termo_busca = st.text_input("Buscar por tema, passagem bíblica ou palavra-chave:", placeholder="Ex: Batismo, Is 53, Tradição, Missa...")

    encontros = database.get_encontros(bloco=bloco_selecionado, termo_busca=termo_busca)

    if not encontros:
        st.warning("Nenhum encontro encontrado com os filtros selecionados.")
        return

    # Recuperar progresso do catecúmeno para exibir badges
    cid_usuario = st.session_state.get("catecumeno_id", 0)
    progresso_info = database.get_progresso_catecumeno(cid_usuario) if cid_usuario else {"lista_concluidos": set()}
    concluidos_set = progresso_info.get("lista_concluidos", set())

    # Seletor do Encontro
    opcoes_encontros = {}
    for e in encontros:
        badge = " ✅" if e["numero"] in concluidos_set else ""
        opcoes_encontros[f"Encontro {e['numero']:02d}: {e['titulo']}{badge}"] = e["numero"]
    
    if "encontro_atual_num" not in st.session_state:
        st.session_state.encontro_atual_num = encontros[0]["numero"]

    nums_filtrados = [e["numero"] for e in encontros]
    if st.session_state.encontro_atual_num not in nums_filtrados:
        st.session_state.encontro_atual_num = nums_filtrados[0]

    opcoes_keys = list(opcoes_encontros.keys())
    idx_atual = 0
    for idx, k in enumerate(opcoes_keys):
        if opcoes_encontros[k] == st.session_state.encontro_atual_num:
            idx_atual = idx
            break

    col_nav1, col_nav2, col_nav3 = st.columns([1, 4, 1])
    with col_nav1:
        if st.button("⬅️ Anterior", disabled=(idx_atual == 0)):
            st.session_state.encontro_atual_num = opcoes_encontros[opcoes_keys[idx_atual - 1]]
            st.rerun()
    with col_nav3:
        if st.button("Próximo ➡️", disabled=(idx_atual >= len(opcoes_keys) - 1)):
            st.session_state.encontro_atual_num = opcoes_encontros[opcoes_keys[idx_atual + 1]]
            st.rerun()
    with col_nav2:
        escolha = st.selectbox("Selecione o Encontro para Estudo e Aula:", opcoes_keys, index=idx_atual)
        st.session_state.encontro_atual_num = opcoes_encontros[escolha]

    encontro = database.get_encontro_by_numero(st.session_state.encontro_atual_num)
    if not encontro:
        return

    # Painel do Encontro com Obra de Arte Sacra
    col_banner_img, col_banner_txt = st.columns([1, 1.6])
    with col_banner_img:
        import os
        num_enc = encontro.get("numero", 1)
        legenda = encontro.get("imagem_legenda", "")
        img_ref = encontro.get("imagem_url")
        
        # Diretório base do repositório
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Candidatos prioritários de arquivos locais
        candidatos = [
            os.path.join(base_dir, "assets", "images", f"encontro_{num_enc:02d}.jpg"),
            os.path.join("assets", "images", f"encontro_{num_enc:02d}.jpg"),
            os.path.abspath(os.path.join("assets", "images", f"encontro_{num_enc:02d}.jpg"))
        ]
        
        # Adicionar o img_ref se fornecido e for caminho de arquivo
        if img_ref and not img_ref.startswith("http://") and not img_ref.startswith("https://"):
            candidatos.insert(0, os.path.join(base_dir, img_ref) if not os.path.isabs(img_ref) else img_ref)
            candidatos.insert(1, img_ref)
        
        caminho_final = None
        for cand in candidatos:
            if cand and os.path.exists(cand) and os.path.isfile(cand):
                caminho_final = cand
                break
        
        if caminho_final:
            try:
                st.image(caminho_final, caption=legenda, use_container_width=True)
            except Exception as e:
                st.info(f"🎨 {legenda}")
        elif img_ref and (img_ref.startswith("http://") or img_ref.startswith("https://")):
            try:
                st.image(img_ref, caption=legenda, use_container_width=True)
            except Exception:
                st.info(f"🎨 {legenda}")
        else:
            st.info(f"🎨 {legenda}")
        status_html = ""
        if cid_usuario:
            info_c = database.is_encontro_concluido(cid_usuario, encontro['numero'])
            if info_c:
                status_html = f"""
                <div style="margin-top: 0.6rem; background: #E8F5E9; border: 1px solid #81C784; padding: 6px 12px; border-radius: 6px; display: inline-flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.1rem;">✅</span>
                    <strong style="color: #2E7D32; font-size: 0.92rem;">Estudo Concluído em {info_c['data_conclusao']}</strong>
                </div>
                """
            else:
                status_html = """
                <div style="margin-top: 0.6rem; background: #FFF8E1; border: 1px solid #FFE082; padding: 6px 12px; border-radius: 6px; display: inline-flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.1rem;">📖</span>
                    <span style="color: #795548; font-size: 0.92rem; font-weight: 500;">Encontro em andamento</span>
                </div>
                """

        st.markdown(f"""
        <div class="pergaminho-card-bordo" style="height: 100%;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <span style="background: #781826; color: #FAF8F5; padding: 4px 12px; border-radius: 4px; font-family: 'Cinzel', serif; font-size: 0.9rem;">
                    Módulo: {encontro['bloco']}
                </span>
                <span style="font-family: 'Cinzel', serif; font-weight: bold; color: #781826; font-size: 1.1rem;">
                    Encontro {encontro['numero']} de 40
                </span>
            </div>
            <h2 style="color: #781826; margin: 0.6rem 0 0.4rem 0; font-family: 'Cinzel', serif; font-size: 1.6rem;">
                {encontro['titulo']}
            </h2>
            <p style="font-size: 1.1rem; color: #3A2315; font-style: italic; margin-bottom: 0.4rem; line-height: 1.5;">
                {encontro['resumo']}
            </p>
            {status_html}
        </div>
        """, unsafe_allow_html=True)

    # Abas com conteúdo aprofundado
    tab_roteiro, tab_biblia, tab_magisterio, tab_franciscano, tab_diario, tab_impressao, tab_quiz, tab_anexos = st.tabs([
        "📋 Roteiro da Aula",
        "📖 Sagrada Escritura",
        "🏛️ Sagrado Magistério & CIC",
        "🕊️ Pílula Franciscana",
        "✍️ Diário & Partilha",
        "🖨️ Ficha de Impressão",
        "🎯 Quiz da Fé & Reflexão",
        "📎 Materiais & Anexos"
    ])

    # 1. Roteiro do Catequista
    with tab_roteiro:
        col_r1, col_r2 = st.columns([1.2, 1])
        with col_r1:
            st.markdown("""
            <h4 style="color: #781826; font-family: 'Cinzel', serif;">
                📌 Subtemas do Currículo Oficial
            </h4>
            """, unsafe_allow_html=True)
            subtemas_formatados = encontro['subtemas'].replace('\n', '<br>')
            st.markdown(f"""
            <div class="pergaminho-card">
                <div style="font-size: 1.05rem; line-height: 1.7; color: #2B1810;">
                    {subtemas_formatados}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_r2:
            st.markdown("""
            <h4 style="color: #5A3825; font-family: 'Cinzel', serif;">
                ⏱️ Passo a Passo da Aula (60 a 90 min)
            </h4>
            """, unsafe_allow_html=True)
            roteiro_formatado = encontro['roteiro_encontro'].replace('\n', '<br>')
            st.markdown(f"""
            <div class="pergaminho-card-franciscano">
                <div style="font-size: 1rem; line-height: 1.6; color: #3A2315;">
                    {roteiro_formatado}
                </div>
            </div>
            """, unsafe_allow_html=True)

        render_divider("ORAÇÃO FINAL DO ENCONTRO")
        st.markdown(f"""
        <div class="citacao-biblica" style="border-left-color: #C5A059; background: #FAF5EB;">
            <p style="margin: 0; font-size: 1.15rem; color: #4A2E1B;">
                "{encontro['oracao_final']}"
            </p>
            <span class="referencia">— Oração Conclusiva Litúrgica</span>
        </div>
        """, unsafe_allow_html=True)

    # 2. Sagrada Escritura
    with tab_biblia:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            📜 Fundamentação Bíblica do Encontro
        </h4>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="citacao-biblica">
            <p style="margin: 0; font-size: 1.2rem;">
                <strong>Passagens sagradas para proclamação e meditação:</strong><br>
                {encontro['referencias_biblicas']}
            </p>
            <span class="referencia">Sagrada Bíblia Católica • Palavra do Senhor</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="font-size: 1.05rem; line-height: 1.6;">
            A Palavra de Deus proclamada na catequese não é mero texto histórico, mas o próprio Cristo que fala aos nossos corações. 
            Recomenda-se realizar a <strong>Lectio Divina</strong> (Leitura Orante) destas passagens:
        </p>
        <ol style="font-size: 1.05rem; line-height: 1.8;">
            <li><strong>Leitura (Lectio):</strong> O que o texto sagrado diz em si mesmo?</li>
            <li><strong>Meditação (Meditatio):</strong> O que o Senhor diz para a minha vida através deste texto?</li>
            <li><strong>Oração (Oratio):</strong> O que respondo a Deus a partir do que Ele me falou?</li>
            <li><strong>Contemplação (Contemplatio):</strong> Que transformação de olhar e atitude Deus opera em mim?</li>
        </ol>
        """, unsafe_allow_html=True)

        st.link_button(
            "🔗 Abrir Bíblia Católica Online (Padre Paulo Ricardo / Edição Canônica)",
            "https://padrepauloricardo.org/biblia",
            help="Acesso ao texto bíblico integral com notas e comentários católicos"
        )

    # 3. Sagrado Magistério & CIC
    with tab_magisterio:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            🏛️ O Depósito da Fé: Catecismo da Igreja Católica & Magistério
        </h4>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="pergaminho-card">
            <h5 style="color: #781826; margin-top: 0; font-family: 'Cinzel', serif;">
                Catecismo da Igreja Católica (CIC) & Documentos Eclesiais
            </h5>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                <strong>Parágrafos e Decretos citados:</strong><br>
                {encontro['referencias_magisterio']}
            </p>
            <hr style="border: 0; border-top: 1px solid #D8C8B4; margin: 1rem 0;">
            <h5 style="color: #781826; margin-top: 0; font-family: 'Cinzel', serif;">
                Fontes Patrísticas, Didaqué e Doutores da Igreja
            </h5>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                {encontro['fontes_complementares']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.link_button(
                "🔗 Consultar CIC no Site Oficial da Santa Sé (Vaticano)",
                "https://www.vatican.va/archive/cathechism_po/index_new/prima-pagina-cic_po.html"
            )
        with col_l2:
            st.link_button(
                "🔗 Código de Direito Canônico (CDC - Vaticano)",
                "https://www.vatican.va/archive/cdc/index_po.htm"
            )

    # 4. Pílula Franciscana
    with tab_franciscano:
        st.markdown("""
        <h4 style="color: #5A3825; font-family: 'Cinzel', serif;">
            🌿 Espiritualidade Franciscana e o Bom Jesus dos Aflitos
        </h4>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="pilula-franciscana">
            <h4>☩ O Testemunho do Irmão Menor</h4>
            <p style="font-size: 1.15rem; line-height: 1.7; color: #2E1B10;">
                {encontro['reflexao_franciscana']}
            </p>
            <div style="margin-top: 1rem; font-size: 0.95rem; color: #5A3825; font-style: italic;">
                "Paz e Bem em todas as coisas!" • Paróquia Bom Jesus dos Aflitos de Sorocaba
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "🔗 Conhecer mais na Província Franciscana do Brasil",
            "https://franciscanos.org.br/#gsc.tab=0"
        )

    # 5. Diário & Partilha
    with tab_diario:
        perfil_usuario = st.session_state.get("perfil_usuario", "catequista")
        nome_usuario = st.session_state.get("nome_usuario", "Catequista")
        cid_usuario = st.session_state.get("catecumeno_id", 0)

        st.markdown(f"""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ✍️ Diário Espiritual & Partilha da Turma
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            Espaço sagrado para registrar orações, dúvidas que surgiram e propósitos de vida cristã.
        </p>
        """, unsafe_allow_html=True)

        with st.form(f"form_anotacao_{encontro['numero']}", clear_on_submit=True):
            if perfil_usuario == "catequista":
                catecumenos_lista = database.get_catecumenos(filtro_ativo=True)
                opcoes_autor = ["Catequista / Registro Geral"] + [f"{c['nome']} (Catecúmeno)" for c in catecumenos_lista]
                autor_selecionado = st.selectbox("Autor da Anotação:", opcoes_autor)
                cat_id = 0
                autor_nome = "Catequista"
                if " (Catecúmeno)" in autor_selecionado:
                    nome_puro = autor_selecionado.replace(" (Catecúmeno)", "")
                    autor_nome = nome_puro
                    for c in catecumenos_lista:
                        if c["nome"] == nome_puro:
                            cat_id = c["id"]
                            break
            else:
                autor_nome = nome_usuario
                cat_id = cid_usuario
                st.info(f"Registrando reflexão como: **{autor_nome}**")

            texto_anotacao = st.text_area("Reflexão espiritual ou apontamento da aula:", placeholder="Escreva aqui a síntese da partilha, o que mais tocou seu coração neste encontro...")
            btn_salvar = st.form_submit_button("Salvar Reflexão no Diário ☩")

            if btn_salvar:
                if texto_anotacao.strip():
                    database.add_anotacao(cat_id, encontro['numero'], autor_nome, texto_anotacao.strip())
                    st.success("Reflexão gravada com sucesso no diário!")
                    st.rerun()
                else:
                    st.warning("Por favor, digite o texto da reflexão.")

        # Histórico de anotações
        if perfil_usuario == "catequista":
            anotacoes = database.get_anotacoes(encontro['numero'])
        else:
            anotacoes = database.get_anotacoes(encontro['numero'], catecumeno_id=cid_usuario)

        if anotacoes:
            st.markdown("##### 📜 Registros Deste Encontro:")
            for a in anotacoes:
                st.markdown(f"""
                <div style="background: #FAF8F5; border: 1px solid #D8C8B4; border-left: 4px solid #781826; padding: 0.8rem 1rem; border-radius: 6px; margin-bottom: 0.8rem;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.88rem; color: #781826; font-weight: bold;">
                        <span>👤 {a['autor']}</span>
                        <span>📅 {a['data_registro']}</span>
                    </div>
                    <p style="font-size: 1.05rem; margin: 0.5rem 0 0 0; color: #2B1810; line-height: 1.5;">
                        {a['texto']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Nenhuma reflexão registrada ainda para este encontro.")

    # 6. Ficha de Impressão
    with tab_impressao:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            🖨️ Ficha Resumo do Encontro para Levar à Paróquia
        </h4>
        <p style="font-size: 0.95rem;">
            Você pode copiar este resumo limpo para imprimir ou enviar aos catecúmenos via WhatsApp/E-mail.
        </p>
        """, unsafe_allow_html=True)

        resumo_texto = f"""PARÓQUIA BOM JESUS DOS AFLITOS - SOROCABA/SP (FRANCISCANOS)
CATECUMENATO DE ADULTOS — ENCONTRO {encontro['numero']:02d} / 40
TEMA: {encontro['titulo'].upper()}
MÓDULO: {encontro['bloco']}

OBJETIVO E RESUMO:
{encontro['resumo']}

SUBTEMAS ABORDADOS:
{encontro['subtemas']}

PASSAGENS BÍBLICAS PARA LEITURA DURANTE A SEMANA:
{encontro['referencias_biblicas']}

CATECISMO DA IGREJA CATÓLICA:
{encontro['referencias_magisterio']}

ESPIRITUALIDADE FRANCISCANA:
{encontro['reflexao_franciscana']}

ORAÇÃO FINAL DO ENCONTRO:
"{encontro['oracao_final']}"

Paz e Bem!"""

        st.text_area("Texto formatado para cópia/impressão:", value=resumo_texto, height=350)

    # 7. Quiz da Fé & Reflexão Pessoal
    with tab_quiz:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1.2rem;">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
                🎯 Exercício de Fixação da Fé & Meditação Pessoal
            </h4>
            <p style="font-size: 1.05rem; color: #5A3825; font-style: italic;">
                Teste sua compreensão da sã doutrina católica com feedback imediato e reflita sobre sua caminhada cristã
            </p>
        </div>
        """, unsafe_allow_html=True)

        from data.quizzes_encontros import get_quiz_for_encontro
        dados_quiz = get_quiz_for_encontro(encontro['numero'])
        perguntas = dados_quiz.get("perguntas", [])
        reflexao_tema = dados_quiz.get("reflexao", "")

        # Respostas salvas anteriormente no banco para o catecúmeno logado
        respostas_salvas_db = database.get_respostas_quiz(cid_usuario, encontro['numero']) if cid_usuario else {}

        # Seção 1: Questões de Escolha Única
        if perguntas:
            st.markdown("##### 📝 Questões de Escolha Única:")
            for idx_p, p in enumerate(perguntas):
                chave_pergunta = f"quiz_{encontro['numero']}_{idx_p}"
                chave_respondido = f"resp_{encontro['numero']}_{idx_p}"

                salvo = respostas_salvas_db.get(idx_p)
                idx_padrao = salvo["opcao_escolhida"] if salvo else None

                # Se já estava salvo no banco e ainda não está na sessão, preenche a sessão
                if chave_respondido not in st.session_state and salvo:
                    exp_salva = p['explicacao_acerto'] if salvo["acertou"] else p['explicacao_erro']
                    st.session_state[chave_respondido] = (salvo["acertou"], f"{exp_salva}\n\n*(Registrado no histórico em {salvo['data_resposta']})*")

                st.markdown(f"""
                <div class="pergaminho-card" style="margin-bottom: 0.6rem; border-left: 4px solid #781826;">
                    <strong style="color: #781826; font-size: 1.05rem;">
                        Questão {idx_p + 1}:
                    </strong>
                    <span style="font-size: 1.05rem; font-weight: 600; color: #2D1B13;">
                        {p['enunciado']}
                    </span>
                </div>
                """, unsafe_allow_html=True)

                escolha = st.radio(
                    f"Selecione a alternativa para a questão {idx_p + 1}:",
                    p['opcoes'],
                    key=f"radio_{chave_pergunta}",
                    index=idx_padrao,
                    label_visibility="collapsed"
                )

                col_btn, col_espaco = st.columns([1.2, 2])
                with col_btn:
                    btn_verificar = st.button(
                        f"Confirmar Resposta {idx_p + 1} ☩",
                        key=f"btn_{chave_pergunta}",
                        type="primary"
                    )

                if btn_verificar:
                    if escolha is None:
                        st.warning("Selecione uma das alternativas acima antes de confirmar.")
                    else:
                        idx_escolhido = p['opcoes'].index(escolha)
                        acertou = (idx_escolhido == p['correta'])
                        explicacao = p['explicacao_acerto'] if acertou else p['explicacao_erro']
                        st.session_state[chave_respondido] = (acertou, explicacao)
                        
                        # Salvar no banco SQLite de forma permanente
                        if cid_usuario:
                            database.salvar_resposta_quiz(cid_usuario, encontro['numero'], idx_p, idx_escolhido, acertou)
                            st.toast("Resposta gravada no seu histórico de fé! ☩", icon="✅")

                if chave_respondido in st.session_state:
                    acertou, explicacao = st.session_state[chave_respondido]
                    if acertou:
                        st.success(f"✅ **RESPOSTA CORRETA!**\n\n{explicacao}")
                    else:
                        st.error(f"❌ **RESPOSTA INCORRETA**\n\n{explicacao}")

                st.markdown("<hr style='border: 0; border-top: 1px dashed #D8C8B4; margin: 1rem 0 1.5rem 0;'>", unsafe_allow_html=True)

        # Seção 2: Meditação Espiritual & Partilha
        if reflexao_tema:
            st.markdown("##### 🕊️ Meditação Espiritual & Exame do Coração:")
            st.markdown(f"""
            <div class="pilula-franciscana">
                <h5 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                    🌿 Pergunta para Meditação Pessoal:
                </h5>
                <p style="font-size: 1.1rem; line-height: 1.6; color: #2E1B10; font-style: italic; margin-bottom: 0;">
                    "{reflexao_tema}"
                </p>
            </div>
            """, unsafe_allow_html=True)

            with st.form(f"form_reflexao_quiz_{encontro['numero']}"):
                texto_refl = st.text_area(
                    "Sua oração ou compromisso de vida diante desta meditação:",
                    placeholder="Escreva sua oração sincera a Deus ou como você pretende viver este ensinamento em sua vida prática...",
                    key=f"txt_refl_{encontro['numero']}"
                )
                btn_salvar_refl = st.form_submit_button("Gravar no Meu Diário Espiritual ☩")
                if btn_salvar_refl:
                    if texto_refl.strip():
                        database.add_anotacao(
                            st.session_state.get("catecumeno_id", 0),
                            encontro['numero'],
                            st.session_state.get("nome_usuario", "Catequisando"),
                            f"[Reflexão do Quiz] {texto_refl.strip()}"
                        )
                        st.success("Sua reflexão foi gravada com sucesso no diário espiritual!")
                        st.rerun()
                    else:
                        st.warning("Por favor, digite sua meditação antes de gravar.")

    # 8. Materiais e Anexos da Aula
    with tab_anexos:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1.2rem;">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
                📎 Materiais Complementares & Anexos do Encontro
            </h4>
            <p style="font-size: 1.05rem; color: #5A3825; font-style: italic;">
                Arquivos pastorais, roteiros de leitura, apresentações e textos de apoio disponibilizados pelo catequista
            </p>
        </div>
        """, unsafe_allow_html=True)

        materiais = database.get_materiais_encontro(encontro['numero'])
        perfil_usuario = st.session_state.get("perfil_usuario", "visitante")

        # Se for catequista, exibe formulário de upload
        if perfil_usuario == "catequista":
            st.markdown("##### 📤 Disponibilizar Novo Material para a Turma:")
            with st.form(f"form_upload_material_{encontro['numero']}", clear_on_submit=True):
                arquivo_enviado = st.file_uploader(
                    "Selecione o arquivo pastoral (PDF, slides, documento, imagem, áudio):",
                    type=["pdf", "docx", "pptx", "txt", "png", "jpg", "jpeg", "mp3"],
                    key=f"file_upload_{encontro['numero']}"
                )
                desc_material = st.text_input(
                    "Descrição breve do material (opcional):",
                    placeholder="Ex: Slides da aula ministrada no sábado / Roteiro impresso para leitura em família",
                    key=f"desc_upload_{encontro['numero']}"
                )
                btn_enviar = st.form_submit_button("Publicar Anexo para os Catequisandos ☩", type="primary")

                if btn_enviar:
                    if arquivo_enviado is not None:
                        conteudo_bytes = arquivo_enviado.read()
                        database.adicionar_material_encontro(
                            encontro['numero'],
                            arquivo_enviado.name,
                            conteudo_bytes,
                            desc_material
                        )
                        st.success(f"Arquivo '{arquivo_enviado.name}' publicado com sucesso para este encontro!")
                        st.rerun()
                    else:
                        st.warning("Por favor, selecione um arquivo para enviar.")

            st.markdown("---")

        # Lista de materiais para download (visível para catequisandos e catequistas)
        if materiais:
            st.markdown(f"##### 📥 Materiais Disponíveis para Download ({len(materiais)}):")
            for mat in materiais:
                tamanho_kb = round(mat["tamanho_bytes"] / 1024.0, 1)
                
                col_m1, col_m2 = st.columns([3, 1.2])
                with col_m1:
                    st.markdown(f"""
                    <div style="background: #FAF8F5; border: 1px solid #D8C8B4; border-left: 4px solid #781826; padding: 0.8rem 1rem; border-radius: 6px; margin-bottom: 0.6rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <strong style="color: #781826; font-size: 1.05rem;">📄 {mat['nome_arquivo']}</strong>
                            <span style="font-size: 0.85rem; color: #5A3825;">📅 {mat['data_upload']} • {tamanho_kb} KB</span>
                        </div>
                        <p style="margin: 0.4rem 0 0 0; font-size: 0.95rem; color: #3A2315; font-style: italic;">
                            {mat['descricao'] or 'Sem descrição adicional.'}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                with col_m2:
                    caminho_f = mat["caminho_arquivo"]
                    if os.path.exists(caminho_f):
                        with open(caminho_f, "rb") as f_down:
                            bytes_arq = f_down.read()
                        st.download_button(
                            label="📥 Baixar Arquivo",
                            data=bytes_arq,
                            file_name=mat['nome_arquivo'],
                            key=f"down_mat_{mat['id']}",
                            use_container_width=True
                        )
                    else:
                        st.error("Arquivo não encontrado no servidor.")

                    if perfil_usuario == "catequista":
                        if st.button("🗑️ Remover", key=f"del_mat_{mat['id']}", use_container_width=True):
                            database.remover_material_encontro(mat["id"])
                            st.warning("Material removido.")
                            st.rerun()
        else:
            st.info("O catequista ainda não disponibilizou materiais complementares para download neste encontro.")

    # Ação de Conclusão do Encontro (para o Catequisando)
    if cid_usuario:
        st.markdown("<br>", unsafe_allow_html=True)
        info_concl = database.is_encontro_concluido(cid_usuario, encontro['numero'])
        
        st.markdown("""
        <div style="border-top: 1px solid #D8C8B4; margin-top: 1rem; padding-top: 1rem;"></div>
        """, unsafe_allow_html=True)
        
        col_c1, col_c2 = st.columns([2.5, 1.5])
        with col_c1:
            if info_concl:
                st.markdown(f"""
                <div style="background: #E8F5E9; border-left: 4px solid #2E7D32; padding: 0.8rem 1rem; border-radius: 4px;">
                    <strong style="color: #1B5E20; font-size: 1.05rem;">🎉 Encontro Concluído!</strong><br>
                    <span style="color: #2E1B10; font-size: 0.95rem;">
                        Você registrou a conclusão dos estudos deste encontro em <strong>{info_concl['data_conclusao']}</strong>.
                    </span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="background: #FAF8F5; border-left: 4px solid #781826; padding: 0.8rem 1rem; border-radius: 4px;">
                    <strong style="color: #781826; font-size: 1.05rem;">☩ Conclusão dos Estudos</strong><br>
                    <span style="color: #5A3825; font-size: 0.95rem;">
                        Terminou de estudar o roteiro, as leituras e realizar o quiz? Marque como concluído para atualizar seu avanço na jornada de fé.
                    </span>
                </div>
                """, unsafe_allow_html=True)
        with col_c2:
            if info_concl:
                if st.button("↩️ Desmarcar Conclusão", key=f"btn_unmark_{encontro['numero']}", use_container_width=True):
                    database.desmarcar_encontro_concluido(cid_usuario, encontro['numero'])
                    st.rerun()
            else:
                if st.button("☩ Marcar como Concluído ☩", key=f"btn_mark_{encontro['numero']}", type="primary", use_container_width=True):
                    database.marcar_encontro_concluido(cid_usuario, encontro['numero'])
                    st.balloons()
                    st.success("Encontro marcado como concluído com sucesso!")
                    st.rerun()