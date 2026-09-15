# -*- coding: utf-8 -*-
"""
Módulo de Gestão Pastoral e Multi-Turmas Catequéticas
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import database
from style import render_divider

def render():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <h2 style="color: #781826; font-family: 'Cinzel', serif; margin-bottom: 0.2rem;">
            👥 Gestão Pastoral e Multi-Turmas
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            Controle de turmas formativas, matrículas, presenças e acompanhamento sacramental
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_turmas, tab_lista, tab_chamada, tab_relatorio, tab_engajamento, tab_novo, tab_config = st.tabs([
        "🏫 Gestão de Turmas",
        "📋 Lista de Catecúmenos",
        "✅ Registro de Chamada",
        "📊 Frequência Presencial",
        "📈 Estudos Online & Quizzes",
        "➕ Cadastrar Novo Catecúmeno",
        "🎓 Certificados & Senha"
    ])

    # ==============================================================================
    # 1. Gestão de Turmas (Níveis Catequéticos)
    # ==============================================================================
    with tab_turmas:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            🏫 Turmas e Etapas da Catequese Paroquial
        </h4>
        <p style="font-size: 0.95rem; color: #5A3825;">
            Ambiente preparado para as diversas etapas catequéticas (Pré-Catequese, Catequese Anos 1 a 3, Crisma 1 a 3 e Catecumenato de Adultos).
        </p>
        """, unsafe_allow_html=True)

        col_t_lista, col_t_nova = st.columns([1.7, 1.3])

        with col_t_lista:
            mostrar_inativas = st.checkbox("Exibir também turmas arquivadas / inativas", value=False, key="chk_turmas_inativas")
            turmas = database.get_turmas(apenas_ativas=not mostrar_inativas)

            if not turmas:
                st.info("Nenhuma turma cadastrada. Utilize o formulário ao lado para cadastrar a primeira turma.")
            else:
                st.markdown(f"**Total de Turmas:** {len(turmas)}")
                for t in turmas:
                    status_badge = "🟢 Ativa" if t["ativa"] == 1 else "🔴 Inativa"
                    total_alunos = t.get("total_alunos", 0)

                    with st.expander(f"🏫 {t['nome']} — {t['nivel']} ({status_badge})", expanded=False):
                        st.markdown(f"""
                        - **Nível Formativo:** `{t['nivel']}`
                        - **Ano Letivo:** {t['ano']} | **Horário dos Encontros:** {t['horario'] or 'A definir'}
                        - **Catequista Responsável:** {t['catequista_responsavel'] or 'Não informado'}
                        - **Alunos Ativos Matriculados:** **{total_alunos}** aluno(s)
                        - **Data de Criação:** {t.get('data_criacao', 'Não informada')}
                        """)

                        col_act1, col_act2 = st.columns([1, 1.5])
                        with col_act1:
                            novo_status = 0 if t["ativa"] == 1 else 1
                            lbl_status = "Desativar Turma" if t["ativa"] == 1 else "Reativar Turma"
                            if st.button(lbl_status, key=f"btn_toggle_turma_{t['id']}"):
                                database.update_turma(
                                    t["id"], t["nome"], t["nivel"], t["ano"],
                                    t["horario"], t["catequista_responsavel"], novo_status
                                )
                                st.success(f"Status da turma '{t['nome']}' atualizado!")
                                st.rerun()

                        with col_act2:
                            with st.popover("✏️ Editar Detalhes da Turma"):
                                with st.form(f"form_edit_turma_{t['id']}"):
                                    ed_nome = st.text_input("Nome da Turma:", value=t["nome"])
                                    idx_nivel = database.NIVEIS_CATEQUESE.index(t["nivel"]) if t["nivel"] in database.NIVEIS_CATEQUESE else 0
                                    ed_nivel = st.selectbox("Nível Catequético:", database.NIVEIS_CATEQUESE, index=idx_nivel)
                                    ed_ano = st.text_input("Ano Letivo:", value=t["ano"] or "2026")
                                    ed_horario = st.text_input("Horário dos Encontros:", value=t["horario"] or "")
                                    ed_resp = st.text_input("Catequista Responsável:", value=t["catequista_responsavel"] or "")
                                    if st.form_submit_button("Salvar Modificações ☩", use_container_width=True):
                                        if ed_nome.strip():
                                            database.update_turma(t["id"], ed_nome, ed_nivel, ed_ano, ed_horario, ed_resp, t["ativa"])
                                            st.success("Dados da turma atualizados com sucesso!")
                                            st.rerun()
                                        else:
                                            st.warning("O nome da turma não pode ficar vazio.")

        with col_t_nova:
            st.markdown("""
            <div class="pergaminho-card" style="padding: 1.2rem;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    ➕ Cadastrar Nova Turma
                </h5>
                <p style="font-size: 0.9rem; color: #4A2810;">
                    Cadastre uma nova turma pastoral para acolher os fiéis nos diversos graus de maturidade na fé.
                </p>
            """, unsafe_allow_html=True)

            with st.form("form_cadastrar_nova_turma", clear_on_submit=True):
                novo_turma_nome = st.text_input("Nome da Turma *:", placeholder="Ex: Turma São Francisco 2026")
                novo_turma_nivel = st.selectbox(
                    "Nível Catequético *:",
                    database.NIVEIS_CATEQUESE,
                    index=len(database.NIVEIS_CATEQUESE) - 1,
                    help="Selecione o grau correspondente conforme as diretrizes pastorais da CNBB."
                )
                novo_turma_ano = st.text_input("Ano Letivo:", value="2026")
                novo_turma_horario = st.text_input("Dia e Horário:", placeholder="Ex: Sábados às 15h00")
                novo_turma_resp = st.text_input("Catequista Responsável:", placeholder="Ex: Frei / Marcelo Maffeis")

                btn_criar_turma = st.form_submit_button("Cadastrar Turma ☩", type="primary", use_container_width=True)
                if btn_criar_turma:
                    if not novo_turma_nome.strip():
                        st.error("Informe o nome da turma!")
                    else:
                        database.add_turma(
                            nome=novo_turma_nome.strip(),
                            nivel=novo_turma_nivel,
                            ano=novo_turma_ano.strip() or "2026",
                            horario=novo_turma_horario.strip(),
                            catequista_responsavel=novo_turma_resp.strip() or "Catequista"
                        )
                        st.success(f"Turma '{novo_turma_nome}' cadastrada com sucesso!")
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    # ==============================================================================
    # 2. Lista de Catecúmenos
    # ==============================================================================
    with tab_lista:
        turmas_ativas = database.get_turmas(apenas_ativas=True)
        opcoes_filtro = {0: "🏫 Todas as Turmas"}
        for t in turmas_ativas:
            opcoes_filtro[t["id"]] = f"{t['nome']} ({t['nivel']})"

        col_lf1, col_lf2 = st.columns([2, 1])
        with col_lf1:
            turma_sel_lista = st.selectbox(
                "Filtrar por Turma:",
                options=list(opcoes_filtro.keys()),
                format_func=lambda x: opcoes_filtro[x],
                key="sel_filtro_turma_lista"
            )
        with col_lf2:
            exibir_inativos = st.checkbox("Exibir alunos inativos / desistentes", value=False, key="chk_inativos_lista")

        catecumenos = database.get_catecumenos(
            filtro_ativo=not exibir_inativos,
            turma_id=turma_sel_lista if turma_sel_lista > 0 else None
        )

        if not catecumenos:
            st.info("Nenhum catecúmeno encontrado para o filtro selecionado.")
        else:
            st.markdown(f"**Total de Catecúmenos listados:** {len(catecumenos)}")

            for cat in catecumenos:
                status_bat = "✅ Batizado" if cat["batizado"] == 1 else "⏳ Precisa de Batismo"
                status_euc = "✅ 1ª Eucaristia" if cat["primeira_eucaristia"] == 1 else "⏳ Precisa de 1ª Eucaristia"
                status_cris = "✅ Crismado" if cat["crismado"] == 1 else "⏳ Precisa de Crisma"
                status_ativo = "Ativo" if cat["ativo"] == 1 else "Inativo"
                turma_label = f"{cat.get('turma_nome') or 'Sem Turma'} ({cat.get('turma_nivel') or 'Geral'})"

                with st.expander(f"👤 {cat['nome']} — 🏫 {turma_label} [{status_ativo}]", expanded=False):
                    col_info1, col_info2, col_info3 = st.columns([1.2, 1.2, 1.1])
                    with col_info1:
                        st.write(f"**Turma:** {turma_label}")
                        st.write(f"**E-mail:** {cat['email'] or 'Não informado'}")
                        st.write(f"**Telefone/WhatsApp:** {cat['telefone'] or 'Não informado'}")
                        st.write(f"**Nascimento:** {cat['data_nascimento'] or 'Não informado'}")
                        st.write(f"**Estado Civil:** {cat['estado_civil'] or 'Não informado'}")
                    with col_info2:
                        st.write("**Situação Sacramental:**")
                        st.markdown(f"- {status_bat}")
                        st.markdown(f"- {status_euc}")
                        st.markdown(f"- {status_cris}")
                        st.write(f"**Padrinhos/Madrinhas:** {cat['padrinho_madrinha'] or 'A definir'}")
                    with col_info3:
                        st.write(f"**Cadastrado em:** {cat['data_cadastro']}")
                        st.write(f"🔑 **Senha de Acesso:** `{cat.get('senha') or 'pazebem'}`")
                        st.write(f"**Observações:** {cat['observacoes'] or 'Sem observações'}")

                    # Ações pastorais
                    col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([1, 1.2, 1.2, 0.8])
                    with col_btn1:
                        novo_status = 0 if cat["ativo"] == 1 else 1
                        label_status = "Desativar" if cat["ativo"] == 1 else "Reativar"
                        if st.button(label_status, key=f"btn_toggle_cat_{cat['id']}"):
                            database.update_catecumeno(
                                cat['id'], cat['nome'], cat['email'], cat['telefone'],
                                cat['data_nascimento'], cat['estado_civil'], cat['batizado'],
                                cat['primeira_eucaristia'], cat['crismado'], cat['padrinho_madrinha'],
                                cat['observacoes'], novo_status
                            )
                            st.success(f"Situação de {cat['nome']} atualizada!")
                            st.rerun()

                    with col_btn2:
                        with st.popover("🏫 Mudar Turma"):
                            st.write(f"Transferir **{cat['nome']}** para outra turma:")
                            todas_turmas_transfer = database.get_turmas(apenas_ativas=True)
                            if todas_turmas_transfer:
                                id_turma_atual = cat.get("turma_id", 1)
                                idx_padrao = 0
                                for i, t_op in enumerate(todas_turmas_transfer):
                                    if t_op["id"] == id_turma_atual:
                                        idx_padrao = i
                                        break

                                nova_turma_sel = st.selectbox(
                                    "Nova Turma:",
                                    options=[t["id"] for t in todas_turmas_transfer],
                                    format_func=lambda x: next((f"{t['nome']} ({t['nivel']})" for t in todas_turmas_transfer if t["id"] == x), ""),
                                    index=idx_padrao,
                                    key=f"sel_transf_{cat['id']}"
                                )
                                if st.button("Confirmar Transferência", key=f"btn_salvar_transf_{cat['id']}"):
                                    database.update_catecumeno(
                                        cat['id'], cat['nome'], cat['email'], cat['telefone'],
                                        cat['data_nascimento'], cat['estado_civil'], cat['batizado'],
                                        cat['primeira_eucaristia'], cat['crismado'], cat['padrinho_madrinha'],
                                        cat['observacoes'], cat['ativo'], turma_id=nova_turma_sel
                                    )
                                    st.success(f"Aluno {cat['nome']} transferido com sucesso!")
                                    st.rerun()

                    with col_btn3:
                        with st.popover("🔑 Redefinir Senha"):
                            nova_senha_input = st.text_input(f"Nova senha para {cat['nome']}:", key=f"senha_input_{cat['id']}")
                            if st.button("Confirmar Nova Senha", key=f"btn_salvar_senha_{cat['id']}"):
                                if nova_senha_input.strip():
                                    database.alterar_senha_catecumeno(cat['id'], nova_senha_input.strip())
                                    st.success("Senha alterada com sucesso!")
                                    st.rerun()
                                else:
                                    st.warning("Digite uma senha válida.")

                    with col_btn4:
                        if st.button("🗑️ Excluir", key=f"btn_del_{cat['id']}"):
                            database.delete_catecumeno(cat['id'])
                            st.warning(f"Registro de {cat['nome']} excluído permanentemente.")
                            st.rerun()

    # ==============================================================================
    # 3. Registro de Chamada (Por Turma)
    # ==============================================================================
    with tab_chamada:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ✅ Chamada e Registro de Presença por Turma e Encontro
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            Selecione a turma correspondente, o número do encontro e marque a presença dos catecúmenos.
        </p>
        """, unsafe_allow_html=True)

        turmas_ativas_chamada = database.get_turmas(apenas_ativas=True)
        if not turmas_ativas_chamada:
            st.warning("Não há turmas ativas cadastradas. Crie uma turma primeiro na aba 'Gestão de Turmas'.")
        else:
            col_ch_t, col_ch1, col_ch2 = st.columns([1.6, 1, 1])
            with col_ch_t:
                turma_chamada_id = st.selectbox(
                    "Selecione a Turma para a Chamada:",
                    options=[t["id"] for t in turmas_ativas_chamada],
                    format_func=lambda x: next((f"{t['nome']} ({t['nivel']})" for t in turmas_ativas_chamada if t["id"] == x), ""),
                    key="sel_turma_chamada"
                )
            with col_ch1:
                encontro_chamada = st.number_input("Número do Encontro (1 a 40):", min_value=1, max_value=40, value=st.session_state.get("encontro_atual_num", 1))
            with col_ch2:
                data_chamada = st.date_input("Data da Realização do Encontro:", value=datetime.now())

            enc_info = database.get_encontro_by_numero(encontro_chamada)
            if enc_info:
                st.info(f"**Encontro {encontro_chamada:02d}:** {enc_info['titulo']} (Módulo: {enc_info['bloco']})")

            catecumenos_ativos = database.get_catecumenos(filtro_ativo=True, turma_id=turma_chamada_id)
            if not catecumenos_ativos:
                st.warning("Não há catecúmenos ativos matriculados nesta turma para realizar a chamada.")
            else:
                presencas_salvas = database.get_presencas_encontro(encontro_chamada)

                st.markdown(f"##### Marque a Presença dos Alunos ({len(catecumenos_ativos)} matriculados):")
                novo_registro = {}
                for cat in catecumenos_ativos:
                    cid = cat["id"]
                    valor_inicial = presencas_salvas.get(cid, False)
                    novo_registro[cid] = st.checkbox(f"**{cat['nome']}**", value=valor_inicial, key=f"chamada_{turma_chamada_id}_{encontro_chamada}_{cid}")

                if st.button("💾 Salvar Chamada do Encontro ☩", type="primary", key="btn_salvar_chamada_turma"):
                    database.salvar_presencas_encontro(encontro_chamada, str(data_chamada), novo_registro)
                    total_presentes = sum(1 for p in novo_registro.values() if p)
                    st.success(f"Chamada do Encontro {encontro_chamada} gravada com sucesso! {total_presentes} presentes de {len(catecumenos_ativos)} catecúmenos.")

    # ==============================================================================
    # 4. Relatório de Frequência & Prontidão
    # ==============================================================================
    with tab_relatorio:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            📊 Acompanhamento de Assiduidade e Prontidão Pascal
        </h4>
        <p style="font-size: 0.98rem;">
            Apresentação conforme as diretrizes do Catecumenato: os catecúmenos são apresentados à comunidade no 
            4º Domingo da Quaresma para receberem os sacramentos na Vigília Pascal.
        </p>
        """, unsafe_allow_html=True)

        turmas_todas = database.get_turmas(apenas_ativas=True)
        opcoes_filtro_freq = {0: "🏫 Todas as Turmas"}
        for t in turmas_todas:
            opcoes_filtro_freq[t["id"]] = f"{t['nome']} ({t['nivel']})"

        turma_sel_freq = st.selectbox(
            "Filtrar Relatório por Turma:",
            options=list(opcoes_filtro_freq.keys()),
            format_func=lambda x: opcoes_filtro_freq[x],
            key="sel_filtro_turma_freq"
        )

        stats = database.get_estatisticas_frequencia(turma_id=turma_sel_freq if turma_sel_freq > 0 else None)

        if stats:
            dados_tabela = []
            for s in stats:
                freq_pct = (s["total_presencas"] / 40.0) * 100.0 if s["total_presencas"] else 0.0
                
                # Prontidão espiritual e canônica
                sacramentos_pendentes = []
                if s["batizado"] == 0:
                    sacramentos_pendentes.append("Batismo")
                if s["primeira_eucaristia"] == 0:
                    sacramentos_pendentes.append("1ª Comunhão")
                if s["crismado"] == 0:
                    sacramentos_pendentes.append("Crisma")

                sacramentos_str = ", ".join(sacramentos_pendentes) if sacramentos_pendentes else "Iniciação Completa"
                status_apto = "✅ Apto para os Sacramentos" if freq_pct >= 75 else "⚠️ Atenção na Frequência"

                item = {
                    "Nome do Catecúmeno": s["nome"],
                    "Turma": f"{s.get('turma_nome') or 'Sem Turma'} ({s.get('turma_nivel') or 'Geral'})",
                    "Presenças Confirmadas": f"{s['total_presencas']} / 40",
                    "Frequência (%)": f"{freq_pct:.1f}%",
                    "Sacramentos a Receber na Páscoa": sacramentos_str,
                    "Avaliação Pastoral": status_apto
                }
                dados_tabela.append(item)

            df = pd.DataFrame(dados_tabela)
            st.dataframe(df, use_container_width=True, hide_index=True)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Exportar Relatório de Frequência (CSV / Excel)",
                data=csv,
                file_name=f"relatorio_frequencia_turma_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.info("Nenhum dado de frequência registrado para o filtro selecionado.")

    # ==============================================================================
    # 5. Estudos Online & Quizzes
    # ==============================================================================
    with tab_engajamento:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            📈 Acompanhamento do Estudo Individual e Quizzes da Fé
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            Monitore em tempo real o avanço dos catecúmenos na plataforma: encontros estudados em casa, acertos nos quizzes e anotações espirituais.
        </p>
        """, unsafe_allow_html=True)

        turmas_eng = database.get_turmas(apenas_ativas=True)
        opcoes_filtro_eng = {0: "🏫 Todas as Turmas"}
        for t in turmas_eng:
            opcoes_filtro_eng[t["id"]] = f"{t['nome']} ({t['nivel']})"

        turma_sel_eng = st.selectbox(
            "Filtrar Estudos por Turma:",
            options=list(opcoes_filtro_eng.keys()),
            format_func=lambda x: opcoes_filtro_eng[x],
            key="sel_filtro_turma_eng"
        )

        relatorio_online = database.get_relatorio_engajamento_turma(turma_id=turma_sel_eng if turma_sel_eng > 0 else None)

        if relatorio_online:
            total_alunos = len(relatorio_online)
            total_encontros_concluidos_geral = sum(r["encontros_concluidos"] for r in relatorio_online)
            media_conclusao = round(sum(r["pct_conclusao"] for r in relatorio_online) / total_alunos, 1) if total_alunos > 0 else 0
            total_quizzes_geral = sum(r["quizzes_respondidos"] for r in relatorio_online)
            total_acertos_geral = sum(r["quizzes_acertos"] for r in relatorio_online)
            taxa_acerto_geral = round((total_acertos_geral / total_quizzes_geral) * 100.0, 1) if total_quizzes_geral > 0 else 0.0

            col_m1, col_m2, col_m3, col_m4 = st.columns(4)
            with col_m1:
                st.metric("Alunos Monitorados", total_alunos)
            with col_m2:
                st.metric("Média de Conclusão", f"{media_conclusao}%", delta="dos 40 encontros")
            with col_m3:
                st.metric("Exercícios Feitos", total_quizzes_geral)
            with col_m4:
                st.metric("Índice de Acertos", f"{taxa_acerto_geral}%", delta=f"{total_acertos_geral} acertos")

            st.markdown("---")

            dados_engajamento = []
            for r in relatorio_online:
                if r["pct_conclusao"] >= 75:
                    status_ritmo = "🌟 Excelente Ritmo"
                elif r["pct_conclusao"] >= 40:
                    status_ritmo = "📖 Em Bom Andamento"
                elif r["pct_conclusao"] > 0:
                    status_ritmo = "🌱 Iniciando Estudos"
                else:
                    status_ritmo = "⏳ Sem Acessos Registrados"

                dados_engajamento.append({
                    "Catecúmeno": r["nome"],
                    "Turma": f"{r.get('turma_nome') or 'Geral'}",
                    "Encontros Estudados": f"{r['encontros_concluidos']} / 40",
                    "Progresso (%)": f"{r['pct_conclusao']}%",
                    "Quizzes Feitos": r["quizzes_respondidos"],
                    "Acertos no Quiz": f"{r['taxa_acerto_quiz']}% ({r['quizzes_acertos']})",
                    "Reflexões no Diário": r["total_reflexoes"],
                    "Última Atividade": r["ultima_atividade"],
                    "Avaliação do Catequista": status_ritmo
                })

            df_eng = pd.DataFrame(dados_engajamento)
            st.dataframe(df_eng, use_container_width=True, hide_index=True)

            csv_eng = df_eng.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Exportar Relatório de Engajamento Online (Excel/CSV)",
                data=csv_eng,
                file_name=f"relatorio_engajamento_online_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.info("Nenhum catecúmeno ativo registrado para o filtro de turma selecionado.")

    # ==============================================================================
    # 6. Cadastrar Novo Catecúmeno (Com Seleção de Turma)
    # ==============================================================================
    with tab_novo:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ➕ Ficha de Inscrição e Matrícula Pastoral
        </h4>
        <p style="font-size: 0.95rem; color: #5A3825;">
            Preencha os dados do novo catecúmeno e associe-o à sua turma correspondente.
        </p>
        """, unsafe_allow_html=True)

        turmas_cad = database.get_turmas(apenas_ativas=True)
        if not turmas_cad:
            st.warning("⚠️ Atenção: Não há turmas ativas cadastradas. Crie uma turma primeiro na aba 'Gestão de Turmas' para poder matricular catecúmenos.")
        else:
            with st.form("form_novo_catecumeno", clear_on_submit=True):
                col_f1, col_f2 = st.columns(2)
                with col_f1:
                    nome_novo = st.text_input("Nome Completo do Catecúmeno *:")
                    
                    turma_novo_id = st.selectbox(
                        "Turma de Matrícula *:",
                        options=[t["id"] for t in turmas_cad],
                        format_func=lambda x: next((f"{t['nome']} — {t['nivel']}" for t in turmas_cad if t["id"] == x), ""),
                        help="Selecione a turma à qual o catecúmeno pertencerá."
                    )
                    
                    email_novo = st.text_input("E-mail para contato:")
                    telefone_novo = st.text_input("Telefone / WhatsApp (com DDD):")
                    data_nasc_novo = st.text_input("Data de Nascimento (AAAA-MM-DD):", placeholder="Ex: 1990-08-15")
                    senha_novo = st.text_input("Senha Inicial de Acesso (padrão: pazebem):", value="pazebem", help="Senha que o catecúmeno usará para acessar o portal.")
                with col_f2:
                    estado_civil_novo = st.selectbox("Estado Civil:", [
                        "Solteiro(a)", "Casado(a) na Igreja Católica", "Casado(a) apenas no Civil",
                        "Viúvo(a)", "União Estável", "Divorciado(a)"
                    ])
                    st.write("**Sacramentos que JÁ RECEBEU anteriormente:**")
                    batizado_novo = st.checkbox("Já é Batizado na Igreja Católica?")
                    eucaristia_novo = st.checkbox("Já fez a Primeira Comunhão (Eucaristia)?")
                    crisma_novo = st.checkbox("Já recebeu a Crisma (Confirmação)?")
                    padrinhos_novo = st.text_input("Nome do Padrinho / Madrinha (se houver):")

                obs_novo = st.text_area("Observações Pastorais (motivação, acolhida, necessidades especiais):")

                btn_cadastrar = st.form_submit_button("Cadastrar Catecúmeno no Sistema ☩", type="primary")

                if btn_cadastrar:
                    if not nome_novo.strip():
                        st.error("O campo 'Nome Completo' é obrigatório!")
                    else:
                        database.add_catecumeno(
                            nome=nome_novo.strip(),
                            email=email_novo.strip(),
                            telefone=telefone_novo.strip(),
                            data_nasc=data_nasc_novo.strip(),
                            estado_civil=estado_civil_novo,
                            batizado=1 if batizado_novo else 0,
                            eucaristia=1 if eucaristia_novo else 0,
                            crismado=1 if crisma_novo else 0,
                            padrinhos=padrinhos_novo.strip(),
                            obs=obs_novo.strip(),
                            senha=senha_novo.strip() if senha_novo.strip() else "pazebem",
                            turma_id=turma_novo_id
                        )
                        st.success(f"Catecúmeno(a) {nome_novo} matriculado(a) com louvor na turma selecionada!")
                        st.rerun()

    # ==============================================================================
    # 7. Certificados & Senha do Catequista
    # ==============================================================================
    with tab_config:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            🎓 Emissão de Certificados & Segurança Pastoral
        </h4>
        """, unsafe_allow_html=True)

        col_cert, col_senha = st.columns(2)

        # Emissão de Certificado
        with col_cert:
            st.markdown("""
            <div class="pergaminho-card" style="height: 100%;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🎓 Emitir Certificado Paroquial
                </h5>
                <p style="font-size: 0.95rem; color: #3A2315;">
                    Selecione um catecúmeno para gerar e imprimir o Certificado de Formação Catequética formatado em pergaminho sagrado.
                </p>
            """, unsafe_allow_html=True)

            alunos_lista = database.get_catecumenos(filtro_ativo=True)
            if alunos_lista:
                aluno_selecionado = st.selectbox(
                    "Selecione o Catecúmeno:",
                    [f"{a['nome']} — {a.get('turma_nome') or 'Turma Geral'}" for a in alunos_lista],
                    key="sel_cert_aluno"
                )
                nome_puro = aluno_selecionado.split(" — ")[0]
                from modules.certificado import render_certificado_html
                cert_html = render_certificado_html(nome_puro)
                
                st.download_button(
                    label=f"📥 Gerar Certificado de {nome_puro.split()[0]} (HTML/PDF)",
                    data=cert_html.encode("utf-8"),
                    file_name=f"certificado_{nome_puro.replace(' ', '_')}.html",
                    mime="text/html",
                    type="primary",
                    use_container_width=True
                )
            else:
                st.info("Nenhum catecúmeno ativo cadastrado.")

            st.markdown("</div>", unsafe_allow_html=True)

        # Alteração de Senha Administrativa
        with col_senha:
            st.markdown("""
            <div class="pergaminho-card-bordo" style="height: 100%;">
                <h5 style="color: #781826; font-family: 'Cinzel', serif; margin-top: 0;">
                    🔑 Alterar Senha de Acesso do Catequista
                </h5>
                <p style="font-size: 0.95rem; color: #3A2315;">
                    Atualize a senha de acesso administrativo à Gestão Pastoral.
                </p>
            """, unsafe_allow_html=True)

            with st.form("form_troca_senha"):
                senha_atual = st.text_input("Senha Atual do Catequista:", type="password")
                nova_senha = st.text_input("Nova Senha:", type="password")
                confirma_senha = st.text_input("Confirmar Nova Senha:", type="password")
                btn_alterar_senha = st.form_submit_button("Alterar Senha de Acesso ☩", use_container_width=True)

                if btn_alterar_senha:
                    if not database.verificar_senha_catequista(senha_atual):
                        st.error("A senha atual informada está incorreta!")
                    elif len(nova_senha) < 4:
                        st.warning("A nova senha deve ter pelo menos 4 caracteres.")
                    elif nova_senha != confirma_senha:
                        st.error("A nova senha e a confirmação não conferem!")
                    else:
                        database.alterar_senha_catequista(nova_senha)
                        st.success("Senha do Catequista alterada com sucesso!")
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)
