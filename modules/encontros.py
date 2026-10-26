# -*- coding: utf-8 -*-
"""
Módulo dos 40 Encontros da Catequese com Arte Sacra Católica
Catequese da Igreja Católica Apostólica Romana — Diretório de Sorocaba
Hub de Consulta, Formação Doutrinal e Testes com Download em HTML
"""

import os
import streamlit as st
import database
from style import render_divider
from data.quizzes_encontros import get_quiz_for_encontro
from modules.export_html import gerar_html_anotacoes, gerar_html_quiz

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            ☩ Os 40 Encontros da Catequese ☩
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            Diretório de Sorocaba • Sequência completa de formação doutrinal, bíblica, espiritual e litúrgica
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

    # Seletor do Encontro
    opcoes_encontros = {}
    for e in encontros:
        opcoes_encontros[f"Encontro {e['numero']:02d}: {e['titulo']}"] = e["numero"]
    
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
        escolha = st.selectbox("Selecione o Encontro para Consulta e Estudo:", opcoes_keys, index=idx_atual)
        st.session_state.encontro_atual_num = opcoes_encontros[escolha]

    encontro = database.get_encontro_by_numero(st.session_state.encontro_atual_num)
    if not encontro:
        return

    # Painel do Encontro com Obra de Arte Sacra
    col_banner_img, col_banner_txt = st.columns([1, 1.6])
    with col_banner_img:
        num_enc = encontro.get("numero", 1)
        legenda = encontro.get("imagem_legenda", "")
        img_ref = encontro.get("imagem_url")
        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        candidatos = [
            os.path.join(base_dir, "assets", "images", f"encontro_{num_enc:02d}.jpg"),
            os.path.join("assets", "images", f"encontro_{num_enc:02d}.jpg"),
            os.path.abspath(os.path.join("assets", "images", f"encontro_{num_enc:02d}.jpg"))
        ]
        
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
            except Exception:
                st.info(f"🎨 {legenda}")
        elif img_ref and (img_ref.startswith("http://") or img_ref.startswith("https://")):
            try:
                st.image(img_ref, caption=legenda, use_container_width=True)
            except Exception:
                st.info(f"🎨 {legenda}")
        else:
            st.info(f"🎨 {legenda}")

    with col_banner_txt:
        card_html = (
            f'<div class="pergaminho-card-bordo" style="height: 100%;">'
            f'<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">'
            f'<span style="background: #781826; color: #FAF8F5; padding: 4px 12px; border-radius: 4px; font-family: \'Cinzel\', serif; font-size: 0.9rem;">'
            f'Módulo: {encontro["bloco"]}'
            f'</span>'
            f'<span style="font-family: \'Cinzel\', serif; font-weight: bold; color: #781826; font-size: 1.1rem;">'
            f'Encontro {encontro["numero"]} de 40'
            f'</span>'
            f'</div>'
            f'<h2 style="color: #781826; margin: 0.6rem 0 0.4rem 0; font-family: \'Cinzel\', serif; font-size: 1.6rem;">'
            f'{encontro["titulo"]}'
            f'</h2>'
            f'<p style="font-size: 1.05rem; color: #3A2315; font-style: italic; margin-bottom: 0.4rem; line-height: 1.5;">'
            f'{encontro["resumo"]}'
            f'</p>'
            f'<div style="margin-top: 0.6rem; background: #FAF5EB; border: 1px solid #C5A059; padding: 6px 12px; border-radius: 6px; display: inline-flex; align-items: center; gap: 8px;">'
            f'<span style="font-size: 1.1rem;">☩</span>'
            f'<span style="color: #5A3825; font-size: 0.92rem; font-weight: 600;">Diretório de Sorocaba • Hub de Consulta Livre</span>'
            f'</div>'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    # Abas com conteúdo aprofundado
    tab_roteiro, tab_biblia, tab_magisterio, tab_franciscano, tab_diario, tab_quiz, tab_impressao, tab_anexos = st.tabs([
        "📋 Roteiro da Aula",
        "📖 Sagrada Escritura",
        "🏛️ Sagrado Magistério & CIC",
        "🕊️ Espiritualidade",
        "✍️ Anotações (Download HTML)",
        "🎯 Teste da Fé (Download HTML)",
        "🖨️ Ficha de Impressão",
        "📎 Materiais & Anexos"
    ])

    # 1. Roteiro do Catequista / Aula
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
            "🔗 Abrir Bíblia Católica Online (Edição Canônica)",
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

    # 4. Pílula Franciscana / Espiritualidade
    with tab_franciscano:
        st.markdown("""
        <h4 style="color: #5A3825; font-family: 'Cinzel', serif;">
            🌿 Espiritualidade e Reflexão Espiritual
        </h4>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="pilula-franciscana">
            <h4>☩ Testemunho & Vivência Cristã</h4>
            <p style="font-size: 1.15rem; line-height: 1.7; color: #2E1B10;">
                {encontro['reflexao_franciscana']}
            </p>
            <div style="margin-top: 1rem; font-size: 0.95rem; color: #5A3825; font-style: italic;">
                "Paz e Bem em todas as coisas!" • Diretório de Sorocaba
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "🔗 Conhecer mais na Província Franciscana do Brasil",
            "https://franciscanos.org.br/#gsc.tab=0"
        )

    # 5. Anotações & Estudo Pessoal (Download em HTML)
    with tab_diario:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ✍️ Anotações Pessoais & Diário de Estudo
        </h4>
        <p style="font-size: 1rem; color: #5A3825;">
            Espaço para redigir seus apontamentos da aula, orações pessoais ou sínteses doutrinais. 
            Você pode gerar e baixar um arquivo formatado em <strong>HTML</strong> pronto para guardar ou imprimir.
        </p>
        """, unsafe_allow_html=True)

        nome_autor = st.text_input(
            "Seu Nome (opcional para constar no cabeçalho do documento):",
            placeholder="Ex: João da Silva / Catequisando",
            key=f"autor_anot_{encontro['numero']}"
        )

        texto_anotacao = st.text_area(
            "Suas anotações, síntese do encontro ou oração pessoal:",
            placeholder="Escreva aqui o que mais tocou seu coração neste encontro, dúvidas esclarecidas ou propósitos práticos de vida cristã...",
            height=220,
            key=f"texto_anot_{encontro['numero']}"
        )

        col_d1, col_d2 = st.columns([1.5, 2])
        with col_d1:
            if texto_anotacao.strip():
                html_gerado = gerar_html_anotacoes(encontro, texto_anotacao.strip(), nome_autor.strip())
                st.download_button(
                    label="📥 Baixar Minhas Anotações em HTML",
                    data=html_gerado.encode("utf-8"),
                    file_name=f"Anotacoes_Encontro_{encontro['numero']:02d}.html",
                    mime="text/html",
                    type="primary",
                    use_container_width=True,
                    key=f"btn_down_anot_{encontro['numero']}"
                )
            else:
                st.button(
                    "📥 Baixar Minhas Anotações em HTML",
                    disabled=True,
                    help="Digite suas anotações no campo acima para habilitar o download.",
                    use_container_width=True
                )

        st.markdown("""
        <div style="background: #FAF8F5; border: 1px dashed #C5A059; border-radius: 6px; padding: 0.8rem 1rem; margin-top: 1rem; font-size: 0.92rem; color: #5A3825;">
            💡 <strong>Privacidade Total:</strong> Suas anotações não são gravadas em nenhum banco de dados ou servidor externo. O arquivo <code>.html</code> baixado é totalmente autônomo, formatado com tipografia sacra e pronto para ser visualizado em qualquer navegador ou impresso diretamente em PDF (A4).
        </div>
        """, unsafe_allow_html=True)

    # 6. Teste da Fé & Avaliação Doutrinal (Download em HTML)
    with tab_quiz:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1.2rem;">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
                🎯 Teste de Fixação da Fé & Doutrina Católica
            </h4>
            <p style="font-size: 1.05rem; color: #5A3825; font-style: italic;">
                Avalie seus conhecimentos da sã doutrina católica, receba sua nota instantânea e baixe o relatório completo em HTML
            </p>
        </div>
        """, unsafe_allow_html=True)

        dados_quiz = get_quiz_for_encontro(encontro['numero'])
        perguntas = dados_quiz.get("perguntas", [])
        reflexao_tema = dados_quiz.get("reflexao", "")

        nome_estudante_quiz = st.text_input(
            "Seu Nome (opcional para constar no relatório da avaliação):",
            placeholder="Ex: Maria de Nazaré / Estudante",
            key=f"nome_quiz_{encontro['numero']}"
        )

        respostas_usuario = {}
        if perguntas:
            st.markdown("##### 📝 Questões de Múltipla Escolha:")
            for idx_p, p in enumerate(perguntas):
                chave_pergunta = f"quiz_sel_{encontro['numero']}_{idx_p}"

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
                    f"Questão {idx_p + 1}",
                    options=p['opcoes'],
                    key=chave_pergunta,
                    index=None,
                    label_visibility="collapsed"
                )
                if escolha is not None:
                    respostas_usuario[idx_p] = p['opcoes'].index(escolha)

        # Reflexão / Meditação Opcional
        texto_meditacao = ""
        if reflexao_tema:
            st.markdown("##### 🕊️ Meditação & Exame do Coração:")
            st.markdown(f"""
            <div class="pilula-franciscana">
                <h5 style="color: #5A3825; font-family: 'Cinzel', serif; margin-top: 0;">
                    🌿 Questão para Meditação Pessoal:
                </h5>
                <p style="font-size: 1.1rem; line-height: 1.6; color: #2E1B10; font-style: italic; margin-bottom: 0;">
                    "{reflexao_tema}"
                </p>
            </div>
            """, unsafe_allow_html=True)

            texto_meditacao = st.text_area(
                "Sua oração ou compromisso espiritual diante desta meditação (opcional):",
                placeholder="Escreva sua oração ou como pretende viver este ensinamento...",
                key=f"txt_meditacao_quiz_{encontro['numero']}"
            )

        col_q1, col_q2 = st.columns([1.5, 2])
        with col_q1:
            btn_avaliar = st.button("Avaliar Teste & Calcular Nota ☩", type="primary", use_container_width=True, key=f"btn_avaliar_{encontro['numero']}")

        chave_resultado = f"resultado_quiz_{encontro['numero']}"
        if btn_avaliar:
            if len(respostas_usuario) < len(perguntas):
                st.warning(f"Por favor, responda a todas as {len(perguntas)} questões antes de calcular sua nota.")
            else:
                acertos = sum(1 for idx, p in enumerate(perguntas) if respostas_usuario.get(idx) == p['correta'])
                total = len(perguntas)
                pct = int(round((acertos / total) * 100)) if total > 0 else 0
                st.session_state[chave_resultado] = {
                    "acertos": acertos,
                    "total": total,
                    "percentual": pct,
                    "respostas": respostas_usuario,
                    "meditacao": texto_meditacao,
                    "nome": nome_estudante_quiz
                }
                st.rerun()

        # Exibição do Resultado se já avaliado
        if chave_resultado in st.session_state:
            res = st.session_state[chave_resultado]
            acertos = res["acertos"]
            total = res["total"]
            pct = res["percentual"]

            render_divider("RESULTADO DO SEU TESTE DA FÉ")
            
            cor_box = "#2E7D32" if pct >= 70 else "#C62828"
            st.markdown(f"""
            <div style="background: #FFFFFF; border: 2px solid {cor_box}; border-radius: 10px; padding: 1.2rem; text-align: center; margin-bottom: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                <div style="font-family: 'Cinzel', serif; font-size: 1.1rem; color: #5A3825; font-weight: bold;">
                    RELATÓRIO DE AVALIAÇÃO DA SÃ DOUTRINA
                </div>
                <div style="font-family: 'Cinzel', serif; font-size: 2.5rem; font-weight: 900; color: {cor_box}; margin: 0.3rem 0;">
                    Nota: {acertos} / {total}
                </div>
                <div style="font-size: 1.2rem; font-weight: 600; color: #2B1810;">
                    Aproveitamento: {pct}%
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Detalhes e feedback de cada questão
            for idx, p in enumerate(perguntas):
                resp_dada = res["respostas"].get(idx)
                acertou = (resp_dada == p['correta'])
                explicacao = p['explicacao_acerto'] if acertou else p['explicacao_erro']

                if acertou:
                    st.success(f"✅ **Questão {idx + 1}: Resposta Correta!**\n\n{explicacao}")
                else:
                    st.error(f"❌ **Questão {idx + 1}: Resposta Incorreta**\n\n*Resposta correta:* **{p['opcoes'][p['correta']]}**\n\n{explicacao}")

            # Botão de Download do Teste em HTML
            html_teste = gerar_html_quiz(
                encontro=encontro,
                perguntas=perguntas,
                respostas_usuario=res["respostas"],
                nota=acertos,
                total=total,
                percentual=pct,
                reflexao_texto=res.get("meditacao", ""),
                nome_autor=res.get("nome", "")
            )

            st.markdown("<br>", unsafe_allow_html=True)
            col_down1, col_down2 = st.columns([1.5, 2])
            with col_down1:
                st.download_button(
                    label="📥 Baixar Teste Concluído em HTML",
                    data=html_teste.encode("utf-8"),
                    file_name=f"Teste_Encontro_{encontro['numero']:02d}.html",
                    mime="text/html",
                    type="primary",
                    use_container_width=True,
                    key=f"btn_down_quiz_{encontro['numero']}"
                )

            st.caption("📄 *O arquivo HTML baixado inclui todas as questões, suas respostas, o gabarito oficial com a fundamentação do Catecismo e a sua nota.*")

    # 7. Ficha de Impressão
    with tab_impressao:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            🖨️ Ficha Resumo do Encontro para Estudo
        </h4>
        <p style="font-size: 0.95rem;">
            Texto sumarizado com todos os tópicos, fundamentações e oração deste encontro para cópia rápida.
        </p>
        """, unsafe_allow_html=True)

        resumo_texto = f"""CATEQUESE DA IGREJA CATÓLICA APOSTÓLICA ROMANA — DIRETÓRIO DE SOROCABA
ENCONTRO {encontro['numero']:02d} / 40: {encontro['titulo'].upper()}
MÓDULO: {encontro['bloco']}

OBJETIVO E RESUMO:
{encontro['resumo']}

SUBTEMAS ABORDADOS:
{encontro['subtemas']}

PASSAGENS BÍBLICAS PARA LEITURA DURANTE A SEMANA:
{encontro['referencias_biblicas']}

CATECISMO DA IGREJA CATÓLICA (CIC):
{encontro['referencias_magisterio']}

FONTES COMPLEMENTARES:
{encontro['fontes_complementares']}

ESPIRITUALIDADE:
{encontro['reflexao_franciscana']}

ORAÇÃO FINAL DO ENCONTRO:
"{encontro['oracao_final']}"

Paz e Bem! — Diretório de Sorocaba"""

        st.text_area("Texto formatado para cópia/impressão:", value=resumo_texto, height=350)

    # 8. Materiais e Anexos da Aula
    with tab_anexos:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 1.2rem;">
            <h4 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
                📎 Materiais Complementares & Anexos do Encontro
            </h4>
            <p style="font-size: 1.05rem; color: #5A3825; font-style: italic;">
                Arquivos, roteiros de leitura e textos de apoio disponibilizados para este encontro
            </p>
        </div>
        """, unsafe_allow_html=True)

        materiais = database.get_materiais_encontro(encontro['numero'])
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
        else:
            st.info("Não há arquivos externos anexados para este encontro. O conteúdo formativo está integralmente disponível nas abas acima.")