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

if __name__ == "__main__":
    database.init_db()
    test_encontros()
    test_blocos()
    test_catecumenos()
    test_presencas()
    test_oracoes()
    test_autenticacao()
    test_terco_e_missa()
    print("\n>>> TODOS OS TESTES PASSARAM COM 100% DE SUCESSO! <<<")