# -*- coding: utf-8 -*-
"""
Módulo de Gestão Pastoral e Controle de Catecúmenos
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
            👥 Gestão Pastoral do Catecumenato
        </h2>
        <p style="font-size: 1.1rem; color: #5A3825; font-style: italic;">
            Controle de matrículas, acompanhamento sacramental e registro de presenças
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_turma, tab_chamada, tab_relatorio, tab_engajamento, tab_novo = st.tabs([
        "📋 Lista da Turma",
        "✅ Registro de Chamada",
        "📊 Frequência Presencial",
        "📈 Estudos Online & Quizzes",
        "➕ Cadastrar Novo Catecúmeno"
    ])

    # 1. Lista da Turma
    with tab_turma:
        catecumenos = database.get_catecumenos(filtro_ativo=False)

        if not catecumenos:
            st.info("Nenhum catecúmeno cadastrado ainda. Utilize a aba 'Cadastrar Novo Catecúmeno' para iniciar.")
        else:
            st.markdown(f"**Total de Catecúmenos cadastrados:** {len(catecumenos)}")

            # Visualização em cartões pastorais elegantes
            for cat in catecumenos:
                status_bat = "✅ Batizado" if cat["batizado"] == 1 else "⏳ Precisa de Batismo"
                status_euc = "✅ 1ª Eucaristia" if cat["primeira_eucaristia"] == 1 else "⏳ Precisa de 1ª Eucaristia"
                status_cris = "✅ Crismado" if cat["crismado"] == 1 else "⏳ Precisa de Crisma"
                status_ativo = "Ativo na Turma" if cat["ativo"] == 1 else "Inativo / Desistente"

                cor_borda = "#781826" if cat["ativo"] == 1 else "#A0A0A0"

                with st.expander(f"👤 {cat['nome']} — {status_ativo}", expanded=False):
                    col_info1, col_info2, col_info3 = st.columns([1.2, 1.2, 1])
                    with col_info1:
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
                        st.write(f"**Observações:** {cat['observacoes'] or 'Sem observações'}")

                    # Ações rápidas de edição ou exclusão
                    col_btn1, col_btn2 = st.columns(2)
                    with col_btn1:
                        novo_status = 0 if cat["ativo"] == 1 else 1
                        label_status = "Desativar da Turma" if cat["ativo"] == 1 else "Reativar na Turma"
                        if st.button(label_status, key=f"btn_toggle_{cat['id']}"):
                            database.update_catecumeno(
                                cat['id'], cat['nome'], cat['email'], cat['telefone'],
                                cat['data_nascimento'], cat['estado_civil'], cat['batizado'],
                                cat['primeira_eucaristia'], cat['crismado'], cat['padrinho_madrinha'],
                                cat['observacoes'], novo_status
                            )
                            st.success(f"Situação de {cat['nome']} atualizada!")
                            st.rerun()
                    with col_btn2:
                        if st.button("🗑️ Excluir Registro", key=f"btn_del_{cat['id']}"):
                            database.delete_catecumeno(cat['id'])
                            st.warning(f"Registro de {cat['nome']} excluído permanentemente.")
                            st.rerun()

    # 2. Registro de Chamada
    with tab_chamada:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ✅ Chamada e Registro de Presença por Encontro
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            Selecione o número do encontro e marque os catecúmenos presentes.
        </p>
        """, unsafe_allow_html=True)

        col_ch1, col_ch2 = st.columns(2)
        with col_ch1:
            encontro_chamada = st.number_input("Número do Encontro (1 a 40):", min_value=1, max_value=40, value=st.session_state.get("encontro_atual_num", 1))
        with col_ch2:
            data_chamada = st.date_input("Data da Realização do Encontro:", value=datetime.now())

        enc_info = database.get_encontro_by_numero(encontro_chamada)
        if enc_info:
            st.info(f"**Encontro {encontro_chamada:02d}:** {enc_info['titulo']} (Módulo: {enc_info['bloco']})")

        catecumenos_ativos = database.get_catecumenos(filtro_ativo=True)
        if not catecumenos_ativos:
            st.warning("Não há catecúmenos ativos para realizar a chamada.")
        else:
            presencas_salvas = database.get_presencas_encontro(encontro_chamada)

            st.markdown("##### Marque a Presença dos Alunos:")
            novo_registro = {}
            for cat in catecumenos_ativos:
                cid = cat["id"]
                valor_inicial = presencas_salvas.get(cid, False)
                novo_registro[cid] = st.checkbox(f"**{cat['nome']}**", value=valor_inicial, key=f"chamada_{encontro_chamada}_{cid}")

            if st.button("💾 Salvar Chamada do Encontro ☩", type="primary"):
                database.salvar_presencas_encontro(encontro_chamada, str(data_chamada), novo_registro)
                total_presentes = sum(1 for p in novo_registro.values() if p)
                st.success(f"Chamada do Encontro {encontro_chamada} gravada com sucesso! {total_presentes} presentes de {len(catecumenos_ativos)} catecúmenos.")

    # 3. Relatório de Frequência & Prontidão
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

        stats = database.get_estatisticas_frequencia()

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

                dados_tabela.append({
                    "Nome do Catecúmeno": s["nome"],
                    "Presenças Confirmadas": f"{s['total_presencas']} / 40",
                    "Frequência (%)": f"{freq_pct:.1f}%",
                    "Sacramentos a Receber na Páscoa": sacramentos_str,
                    "Avaliação Pastoral": status_apto
                })

            df = pd.DataFrame(dados_tabela)
            st.dataframe(df, use_container_width=True, hide_index=True)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Exportar Relatório em CSV (Excel)",
                data=csv,
                file_name=f"relatorio_catecumenato_bom_jesus_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.info("Nenhum dado de frequência registrado ainda.")

    # 4. Estudos Online & Quizzes
    with tab_engajamento:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            📈 Acompanhamento do Estudo Individual e Quizzes da Fé
        </h4>
        <p style="font-size: 0.98rem; color: #5A3825;">
            Monitore em tempo real o avanço dos catecúmenos na plataforma: encontros estudados em casa, acertos nos quizzes e anotações espirituais.
        </p>
        """, unsafe_allow_html=True)

        relatorio_online = database.get_relatorio_engajamento_turma()

        if relatorio_online:
            # Cards de resumo pastoral
            total_alunos = len(relatorio_online)
            total_encontros_concluidos_geral = sum(r["encontros_concluidos"] for r in relatorio_online)
            media_conclusao = round(sum(r["pct_conclusao"] for r in relatorio_online) / total_alunos, 1) if total_alunos > 0 else 0
            total_quizzes_geral = sum(r["quizzes_respondidos"] for r in relatorio_online)
            total_acertos_geral = sum(r["quizzes_acertos"] for r in relatorio_online)
            taxa_acerto_geral = round((total_acertos_geral / total_quizzes_geral) * 100.0, 1) if total_quizzes_geral > 0 else 0.0

            col_m1, col_m2, col_m3, col_m4 = st.columns(4)
            with col_m1:
                st.metric("Catecúmenos Ativos", total_alunos)
            with col_m2:
                st.metric("Média de Conclusão", f"{media_conclusao}%", delta="dos 40 encontros")
            with col_m3:
                st.metric("Exercícios Feitos", total_quizzes_geral)
            with col_m4:
                st.metric("Índice de Acertos", f"{taxa_acerto_geral}%", delta=f"{total_acertos_geral} acertos")

            st.markdown("---")

            # Tabela detalhada
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
            st.info("Nenhum catecúmeno ativo registrado para exibir relatório.")

    # 5. Cadastrar Novo Catecúmeno
    with tab_novo:
        st.markdown("""
        <h4 style="color: #781826; font-family: 'Cinzel', serif;">
            ➕ Ficha de Inscrição de Adulto no Catecumenato
        </h4>
        """, unsafe_allow_html=True)

        with st.form("form_novo_catecumeno", clear_on_submit=True):
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                nome_novo = st.text_input("Nome Completo do Catecúmeno *:")
                email_novo = st.text_input("E-mail para contato:")
                telefone_novo = st.text_input("Telefone / WhatsApp (com DDD):")
                data_nasc_novo = st.text_input("Data de Nascimento (AAAA-MM-DD):", placeholder="Ex: 1990-08-15")
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
                        obs=obs_novo.strip()
                    )
                    st.success(f"Catecúmeno(a) {nome_novo} cadastrado(a) com louvor no Catecumenato!")
                    st.rerun()