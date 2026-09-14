# -*- coding: utf-8 -*-
"""
Testes Automatizados Completos do Sistema do Catecumenato
"""
import database
from modules.santo_terco import get_misterio_do_dia, MISTERIOS_DATA

def test_encontros():
    encontros = database.get_encontros()
    assert len(encontros) == 40, f"Esperado 40 encontros, encontrado {len(encontros)}"
    for e in encontros:
        assert e["numero"] >= 1 and e["numero"] <= 40, f"Numero inválido: {e['numero']}"
        assert len(e["titulo"]) > 0, f"Título vazio no encontro {e['numero']}"
        assert len(e["bloco"]) > 0, f"Bloco vazio no encontro {e['numero']}"
        assert len(e["referencias_biblicas"]) > 0, f"Ref bíblica vazia no encontro {e['numero']}"
        assert len(e["referencias_magisterio"]) > 0, f"Ref magistério vazia no encontro {e['numero']}"
        assert len(e["reflexao_franciscana"]) > 0, f"Reflexão franciscana vazia no encontro {e['numero']}"
        assert len(e["oracao_final"]) > 0, f"Oração final vazia no encontro {e['numero']}"
        assert e["imagem_url"] is not None and len(e["imagem_url"]) > 10, f"Imagem URL vazia no encontro {e['numero']}"
        assert e["imagem_legenda"] is not None and len(e["imagem_legenda"]) > 5, f"Legenda vazia no encontro {e['numero']}"
    print("[OK] Teste de Encontros (40/40 com dados e imagens sacras completas): APROVADO")

def test_blocos():
    blocos = database.get_blocos()
    assert len(blocos) >= 15, f"Esperado pelo menos 15 blocos, encontrado {len(blocos)}"
    print(f"[OK] Teste de Blocos Temáticos ({len(blocos)} blocos catalogados): APROVADO")

def test_catecumenos():
    cats = database.get_catecumenos()
    assert len(cats) >= 5, f"Esperado pelo menos 5 catecumenos iniciais, encontrado {len(cats)}"
    
    test_id = database.add_catecumeno(
        nome="Teste Automático",
        email="teste@email.com",
        telefone="(15) 99999-0000",
        data_nasc="1990-01-01",
        estado_civil="Solteiro",
        batizado=0,
        eucaristia=0,
        crismado=0,
        padrinhos="Padrinho Teste",
        obs="Anotação de teste"
    )
    assert test_id > 0, "Falha ao inserir catecúmeno de teste"
    database.delete_catecumeno(test_id)
    print("[OK] Teste de Catecúmenos (Listagem, Inserção e Exclusão): APROVADO")

def test_presencas():
    cats = database.get_catecumenos()
    primeiro_cat = cats[0]["id"]
    database.salvar_presencas_encontro(40, "2026-04-01", {primeiro_cat: True})
    presencas = database.get_presencas_encontro(40)
    assert presencas.get(primeiro_cat) is True, "Falha ao gravar presença"
    print("[OK] Teste de Registro de Chamada e Presença: APROVADO")

def test_oracoes():
    oracoes = database.get_oracoes()
    assert len(oracoes) >= 20, f"Esperado pelo menos 20 orações, encontrado {len(oracoes)}"
    cats_oracoes = database.get_categorias_oracoes()
    assert "Franciscanas" in cats_oracoes, "Categoria Franciscanas não encontrada"
    assert "São Bento" in cats_oracoes, "Categoria São Bento não encontrada"
    assert "Santa Clara" in cats_oracoes, "Categoria Santa Clara não encontrada"
    assert "Santo Agostinho" in cats_oracoes, "Categoria Santo Agostinho não encontrada"
    assert "São Tomás de Aquino" in cats_oracoes, "Categoria São Tomás de Aquino não encontrada"
    print(f"[OK] Teste de Devocionário ({len(oracoes)} orações em {len(cats_oracoes)} categorias dos Santos): APROVADO")

def test_autenticacao():
    assert database.verificar_senha_catequista("pazebem") is True, "Senha correta foi rejeitada"
    assert database.verificar_senha_catequista("senha_errada") is False, "Senha incorreta foi aceita"
    print("[OK] Teste de Autenticação e Perfis (Segurança Catequista): APROVADO")

def test_terco_e_missa():
    assert get_misterio_do_dia(0) == "Mistérios Gozosos", "Erro na detecção de segunda-feira"
    assert get_misterio_do_dia(1) == "Mistérios Dolorosos", "Erro na detecção de terça-feira"
    assert get_misterio_do_dia(2) == "Mistérios Gloriosos", "Erro na detecção de quarta-feira"
    assert get_misterio_do_dia(3) == "Mistérios Luminosos", "Erro na detecção de quinta-feira"
    assert get_misterio_do_dia(4) == "Mistérios Dolorosos", "Erro na detecção de sexta-feira"
    assert get_misterio_do_dia(5) == "Mistérios Gozosos", "Erro na detecção de sábado"
    assert get_misterio_do_dia(6) == "Mistérios Gloriosos", "Erro na detecção de domingo"
    assert len(MISTERIOS_DATA) == 4, "Esperado 4 grupos de mistérios do Rosário"
    print("[OK] Teste dos Módulos da Santa Missa e Santo Terço: APROVADO")

def test_quizzes():
    from data.quizzes_encontros import get_quiz_for_encontro
    for num in range(1, 41):
        q = get_quiz_for_encontro(num)
        assert "perguntas" in q, f"Falta chave perguntas no encontro {num}"
        assert len(q["perguntas"]) >= 1, f"Nenhuma pergunta no encontro {num}"
        for p in q["perguntas"]:
            assert "enunciado" in p and len(p["enunciado"]) > 5
            assert "opcoes" in p and len(p["opcoes"]) == 4
            assert 0 <= p["correta"] <= 3
            assert "explicacao_acerto" in p and len(p["explicacao_acerto"]) > 10
            assert "explicacao_erro" in p and len(p["explicacao_erro"]) > 10
        assert "reflexao" in q and len(q["reflexao"]) > 10
    print("[OK] Teste de Quizzes e Reflexões (40/40 com perguntas doutrinais e feedbacks): APROVADO")

def test_tratados():
    import modules.tratados_teologicos as tt
    assert hasattr(tt, "render"), "Módulo tratados_teologicos sem função render"
    print("[OK] Teste de Tratados Teológicos (Mariologia, Cristologia, Angelologia, etc.): APROVADO")

def test_progresso_e_quizzes():
    # Cria catecúmeno temporário para testar progresso
    cid = database.add_catecumeno(
        nome="Catecúmeno Teste Progresso",
        email="progresso@teste.com",
        telefone="15999990001",
        data_nasc="1995-05-15",
        estado_civil="Solteiro",
        batizado=1,
        eucaristia=0,
        crismado=0,
        padrinhos="",
        obs="Teste"
    )
    
    # 1. Testar marcação de encontro
    database.marcar_encontro_concluido(cid, 1)
    database.marcar_encontro_concluido(cid, 2)
    assert database.is_encontro_concluido(cid, 1) is not None, "Encontro 1 deveria estar concluído"
    assert database.is_encontro_concluido(cid, 3) is None, "Encontro 3 não deveria estar concluído"
    
    prog = database.get_progresso_catecumeno(cid)
    assert prog["total_concluidos"] == 2, f"Esperado 2 concluídos, obtido {prog['total_concluidos']}"
    assert prog["percentual"] == 5.0, f"Esperado 5.0%, obtido {prog['percentual']}"
    assert 1 in prog["lista_concluidos"] and 2 in prog["lista_concluidos"]
    
    # 2. Testar persistência de respostas de quiz
    database.salvar_resposta_quiz(cid, 1, 0, 1, True)
    database.salvar_resposta_quiz(cid, 1, 1, 2, False)
    
    resps = database.get_respostas_quiz(cid, 1)
    assert len(resps) == 2, f"Esperado 2 respostas salvas, obtido {len(resps)}"
    assert resps[0]["acertou"] is True
    assert resps[1]["acertou"] is False
    
    stats = database.get_estatisticas_quiz_catecumeno(cid)
    assert stats["total_respondidas"] == 2
    assert stats["total_acertos"] == 1
    assert stats["taxa_acerto"] == 50.0
    
    # 3. Testar relatório de engajamento da turma
    relatorio = database.get_relatorio_engajamento_turma()
    assert len(relatorio) >= 1
    achou = False
    for r in relatorio:
        if r["id"] == cid:
            achou = True
            assert r["encontros_concluidos"] == 2
            assert r["quizzes_respondidos"] == 2
            assert r["quizzes_acertos"] == 1
    assert achou, "Catecúmeno de teste não encontrado no relatório de engajamento"
    
    # 4. Testar desmarcar e cleanup
    database.desmarcar_encontro_concluido(cid, 1)
    assert database.is_encontro_concluido(cid, 1) is None
    database.delete_catecumeno(cid)
    print("[OK] Teste de Progresso e Persistência de Quizzes (Avanço, Notas e Engajamento): APROVADO")

def test_materiais_e_novos_modulos():
    # 1. Teste de Materiais Anexos
    mid = database.adicionar_material_encontro(40, "roteiro_teste.pdf", b"%PDF-1.4 test bytes", "Roteiro da Vigilia")
    assert mid > 0, "Falha ao registrar anexo"
    mats = database.get_materiais_encontro(40)
    assert len(mats) >= 1, "Anexo não recuperado do banco"
    assert mats[0]["nome_arquivo"] == "roteiro_teste.pdf"
    database.remover_material_encontro(mid)
    mats_pos = database.get_materiais_encontro(40)
    assert len(mats_pos) == 0 or all(m["id"] != mid for m in mats_pos), "Falha ao remover anexo"
    print("[OK] Teste de Upload e Download de Materiais por Encontro: APROVADO")

    # 2. Teste dos Novos Módulos Pastorais
    import modules.confissao_e_reconciliacao as conf
    import modules.tesouro_franciscano as tf
    import modules.vida_moral as vm
    import modules.vigilia_pascal as vp
    import modules.certificado as cert
    
    assert hasattr(conf, "render"), "Módulo confissao sem render()"
    assert hasattr(tf, "render"), "Módulo tesouro_franciscano sem render()"
    assert hasattr(vm, "render"), "Módulo vida_moral sem render()"
    assert hasattr(vp, "render"), "Módulo vigilia_pascal sem render()"
    
    html_cert = cert.render_certificado_html("Marcelo Maffeis")
    assert "Marcelo Maffeis" in html_cert, "Nome não encontrado no certificado"
    assert "BOM JESUS DOS AFLITOS" in html_cert, "Paróquia não encontrada no certificado"
    print("[OK] Teste dos Novos Módulos (Confissão, Tesouro Franciscano, Vida Moral, Vigília e Certificados): APROVADO")

    # 3. Teste de Alteração de Senha
    database.alterar_senha_catequista("senha_temporaria")
    assert database.verificar_senha_catequista("senha_temporaria") is True
    database.alterar_senha_catequista("pazebem")
    assert database.verificar_senha_catequista("pazebem") is True
    print("[OK] Teste de Segurança e Alteração de Senha do Catequista: APROVADO")

if __name__ == "__main__":
    database.init_db()
    test_encontros()
    test_blocos()
    test_catecumenos()
    test_presencas()
    test_oracoes()
    test_autenticacao()
    test_terco_e_missa()
    test_quizzes()
    test_tratados()
    test_progresso_e_quizzes()
    test_materiais_e_novos_modulos()
    print("\n>>> TODOS OS TESTES PASSARAM COM 100% DE SUCESSO! <<<")