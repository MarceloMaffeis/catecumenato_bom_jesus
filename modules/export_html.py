# -*- coding: utf-8 -*-
"""
Gerador de Documentos HTML Elegantes para o Diretório de Sorocaba
Catequese da Igreja Católica Apostólica Romana
Permite download de Anotações Pessoais e Testes da Fé em formato HTML independente
"""

from datetime import datetime

HTML_STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600&display=swap');

:root {
    --bordo: #781826;
    --bordo-escuro: #4E0D16;
    --ouro: #C5A059;
    --ouro-suave: #F4EAD4;
    --fundo: #FAF8F5;
    --pergaminho: #F5EFEB;
    --texto: #242120;
    --texto-suave: #5A3825;
    --borda: #D8C8B4;
    --verde-acerto: #2E7D32;
    --vermelho-erro: #C62828;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background-color: var(--fundo);
    color: var(--texto);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 18px;
    line-height: 1.6;
    padding: 2.5rem 1.5rem;
}

.documento-container {
    max-width: 860px;
    margin: 0 auto;
    background: #FFFFFF;
    border: 2px solid var(--ouro);
    border-radius: 12px;
    padding: 2.5rem;
    box-shadow: 0 8px 30px rgba(78, 13, 22, 0.08);
    position: relative;
}

.cabecalho-sacro {
    text-align: center;
    border-bottom: 2px solid var(--ouro);
    padding-bottom: 1.8rem;
    margin-bottom: 2rem;
    background: linear-gradient(135deg, #4E0D16 0%, #781826 70%, #5A3825 100%);
    color: #FAF8F5;
    padding: 2rem 1.5rem;
    border-radius: 8px;
}

.cabecalho-sacro .cruz {
    font-size: 2.2rem;
    color: #F8E7BE;
    line-height: 1;
    margin-bottom: 0.4rem;
}

.cabecalho-sacro h1 {
    font-family: 'Cinzel', serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: #F8E7BE;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.cabecalho-sacro .subtitulo {
    font-size: 1.15rem;
    color: var(--ouro-suave);
    font-style: italic;
    letter-spacing: 0.5px;
}

.cabecalho-sacro .meta-badge {
    display: inline-block;
    margin-top: 0.8rem;
    background: rgba(197, 160, 89, 0.25);
    border: 1px solid var(--ouro);
    padding: 4px 14px;
    border-radius: 20px;
    font-family: 'Cinzel', serif;
    font-size: 0.85rem;
    color: #F8E7BE;
    letter-spacing: 1px;
}

.card-info {
    background: var(--pergaminho);
    border-left: 5px solid var(--bordo);
    padding: 1.2rem 1.5rem;
    border-radius: 6px;
    margin-bottom: 1.8rem;
    border: 1px solid var(--borda);
    border-left: 5px solid var(--bordo);
}

.card-info h2 {
    font-family: 'Cinzel', serif;
    color: var(--bordo);
    font-size: 1.45rem;
    margin-bottom: 0.4rem;
}

.card-info .dados-meta {
    font-size: 1rem;
    color: var(--texto-suave);
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    margin-top: 0.5rem;
}

.bloco-conteudo {
    margin-bottom: 2rem;
}

.secao-titulo {
    font-family: 'Cinzel', serif;
    color: var(--bordo);
    font-size: 1.25rem;
    border-bottom: 1px solid var(--borda);
    padding-bottom: 0.4rem;
    margin: 1.5rem 0 1rem 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.texto-anotacao {
    background: #FFFDF9;
    border: 1px solid var(--borda);
    border-left: 4px solid var(--ouro);
    padding: 1.5rem;
    border-radius: 6px;
    font-size: 1.15rem;
    line-height: 1.8;
    color: #2D1B13;
    white-space: pre-wrap;
    text-align: justify;
}

/* Estilos de Quiz */
.placar-box {
    text-align: center;
    background: linear-gradient(135deg, #FAF5EB 0%, #F5ECE0 100%);
    border: 2px solid var(--ouro);
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1.5rem 0 2rem 0;
}

.placar-numero {
    font-family: 'Cinzel', serif;
    font-size: 2.8rem;
    font-weight: 900;
    color: var(--bordo);
    line-height: 1.1;
}

.placar-aproveitamento {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--texto-suave);
    margin-top: 0.3rem;
}

.questao-card {
    background: #FFFFFF;
    border: 1px solid var(--borda);
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
}

.questao-card.acerto {
    border-left: 6px solid var(--verde-acerto);
}

.questao-card.erro {
    border-left: 6px solid var(--vermelho-erro);
}

.questao-enunciado {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--texto);
    margin-bottom: 0.8rem;
}

.opcao-linha {
    padding: 0.4rem 0.6rem;
    margin: 0.25rem 0;
    border-radius: 4px;
    font-size: 1rem;
}

.opcao-marcada-acerto {
    background: #E8F5E9;
    color: var(--verde-acerto);
    font-weight: bold;
    border: 1px solid #C8E6C9;
}

.opcao-marcada-erro {
    background: #FFEBEE;
    color: var(--vermelho-erro);
    font-weight: bold;
    border: 1px solid #FFCDD2;
}

.opcao-gabarito {
    background: #F1F8E9;
    color: #33691E;
    font-style: italic;
    border-left: 3px solid var(--verde-acerto);
}

.explicacao-box {
    margin-top: 0.8rem;
    background: #FAF8F5;
    border: 1px dashed var(--borda);
    padding: 0.8rem 1rem;
    border-radius: 6px;
    font-size: 0.98rem;
    color: var(--texto-suave);
    line-height: 1.5;
}

.rodape-sacro {
    text-align: center;
    border-top: 1px solid var(--borda);
    padding-top: 1.5rem;
    margin-top: 2.5rem;
    font-size: 0.95rem;
    color: var(--texto-suave);
}

.btn-print {
    background: var(--bordo);
    color: #FFFFFF;
    border: 1px solid var(--ouro);
    font-family: 'Cinzel', serif;
    font-size: 0.95rem;
    font-weight: bold;
    padding: 0.6rem 1.4rem;
    border-radius: 6px;
    cursor: pointer;
    margin-bottom: 1.5rem;
    display: inline-block;
}

.btn-print:hover {
    background: var(--bordo-escuro);
}

@media print {
    body {
        background: #FFFFFF;
        padding: 0;
    }
    .documento-container {
        border: none;
        box-shadow: none;
        padding: 0;
        max-width: 100%;
    }
    .btn-print {
        display: none;
    }
    .questao-card {
        page-break-inside: avoid;
    }
}
</style>
"""

def gerar_html_anotacoes(encontro, texto_anotacao, nome_autor=""):
    """
    Gera um documento HTML completo e autônomo com as anotações do encontro.
    """
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")
    autor_str = f"<strong>Catequisando / Estudante:</strong> {nome_autor}<br>" if nome_autor.strip() else ""
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anotações — Encontro {encontro['numero']:02d}: {encontro['titulo']}</title>
    {HTML_STYLE}
</head>
<body>
    <div class="documento-container">
        <button class="btn-print" onclick="window.print()">🖨️ Imprimir / Salvar em PDF</button>

        <header class="cabecalho-sacro">
            <div class="cruz">☩</div>
            <h1>CATEQUESE DA IGREJA CATÓLICA APOSTÓLICA ROMANA</h1>
            <div class="subtitulo">Diretório de Sorocaba • Hub de Consulta & Formação</div>
            <div class="meta-badge">DIÁRIO ESPIRITUAL & ANOTAÇÕES PESSOAIS</div>
        </header>

        <section class="card-info">
            <h2>Encontro {encontro['numero']:02d}: {encontro['titulo']}</h2>
            <div class="dados-meta">
                <span><strong>Módulo:</strong> {encontro['bloco']}</span>
                <span><strong>Data:</strong> {agora}</span>
            </div>
            {f'<div style="margin-top: 0.4rem; font-size: 1rem; color: #5A3825;">{autor_str}</div>' if autor_str else ''}
        </section>

        <section class="bloco-conteudo">
            <h3 class="secao-titulo">📖 Fundamentação & Leituras Sagradas</h3>
            <p style="font-size: 1.05rem; margin-bottom: 0.5rem;">
                <strong>Passagens Bíblicas:</strong> {encontro.get('referencias_biblicas', '')}
            </p>
            <p style="font-size: 1.05rem; color: var(--texto-suave);">
                <strong>Catecismo da Igreja Católica (CIC):</strong> {encontro.get('referencias_magisterio', '')}
            </p>
        </section>

        <section class="bloco-conteudo">
            <h3 class="secao-titulo">✍️ Apontamentos & Reflexão Pessoal</h3>
            <div class="texto-anotacao">{texto_anotacao}</div>
        </section>

        <section class="bloco-conteudo">
            <h3 class="secao-titulo">🙏 Oração Conclusiva do Encontro</h3>
            <blockquote style="font-style: italic; background: #FAF5EB; border-left: 4px solid var(--ouro); padding: 1rem 1.2rem; border-radius: 4px; color: #4A2E1B;">
                "{encontro.get('oracao_final', '')}"
            </blockquote>
        </section>

        <footer class="rodape-sacro">
            <p><strong>Catequese da Igreja Católica Apostólica Romana — Diretório de Sorocaba</strong></p>
            <p style="font-style: italic; font-size: 0.88rem; margin-top: 0.3rem;">
                "A fé vem pelo ouvir, e o ouvir pela Palavra de Cristo." (Rm 10,17) &bull; Documento gerado para estudo pessoal.
            </p>
        </footer>
    </div>
</body>
</html>
"""
    return html


def gerar_html_quiz(encontro, perguntas, respostas_usuario, nota, total, percentual, reflexao_texto="", nome_autor=""):
    """
    Gera um documento HTML completo e autônomo com o resultado do Teste da Fé.
    """
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")
    autor_str = f"<strong>Estudante / Catequisando:</strong> {nome_autor}<br>" if nome_autor.strip() else ""

    # Avaliação e Conceito
    if percentual == 100:
        conceito = "Excelente aproveitamento! Sã doutrina plenamente assimilada."
        cor_conceito = "#2E7D32"
    elif percentual >= 70:
        conceito = "Bom aproveitamento! Continue meditando as passagens bíblicas e o Catecismo."
        cor_conceito = "#8C6A1D"
    else:
        conceito = "Recomenda-se reler com atenção o roteiro do encontro e o Magistério."
        cor_conceito = "#C62828"

    questoes_html = ""
    for idx, p in enumerate(perguntas):
        resp_dada = respostas_usuario.get(idx)
        acertou = (resp_dada == p['correta']) if resp_dada is not None else False
        classe_status = "acerto" if acertou else "erro"
        simbolo = "✅ Correta" if acertou else "❌ Incorreta"

        opcoes_html = ""
        for i_op, op in enumerate(p['opcoes']):
            if i_op == resp_dada and acertou:
                opcoes_html += f'<div class="opcao-linha opcao-marcada-acerto">✓ {op} (Sua resposta — Correta)</div>'
            elif i_op == resp_dada and not acertou:
                opcoes_html += f'<div class="opcao-linha opcao-marcada-erro">✗ {op} (Sua resposta — Incorreta)</div>'
            elif i_op == p['correta'] and not acertou:
                opcoes_html += f'<div class="opcao-linha opcao-gabarito">★ Resposta correta: {op}</div>'
            else:
                opcoes_html += f'<div class="opcao-linha" style="color: #666;">• {op}</div>'

        explicacao = p['explicacao_acerto'] if acertou else p['explicacao_erro']

        questoes_html += f"""
        <div class="questao-card {classe_status}">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-family: 'Cinzel', serif; font-weight: bold; color: var(--bordo);">Questão {idx + 1} de {len(perguntas)}</span>
                <span style="font-weight: bold; color: {'var(--verde-acerto)' if acertou else 'var(--vermelho-erro)'};">{simbolo}</span>
            </div>
            <div class="questao-enunciado">{p['enunciado']}</div>
            <div class="opcoes-container">
                {opcoes_html}
            </div>
            <div class="explicacao-box">
                <strong>Fundamentação Teológica:</strong> {explicacao}
            </div>
        </div>
        """

    reflexao_html = ""
    if reflexao_texto and reflexao_texto.strip():
        reflexao_html = f"""
        <section class="bloco-conteudo">
            <h3 class="secao-titulo">🕊️ Meditação & Oração do Estudante</h3>
            <div class="texto-anotacao">{reflexao_texto}</div>
        </section>
        """

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste de Fé — Encontro {encontro['numero']:02d}: {encontro['titulo']}</title>
    {HTML_STYLE}
</head>
<body>
    <div class="documento-container">
        <button class="btn-print" onclick="window.print()">🖨️ Imprimir / Salvar em PDF</button>

        <header class="cabecalho-sacro">
            <div class="cruz">☩</div>
            <h1>CATEQUESE DA IGREJA CATÓLICA APOSTÓLICA ROMANA</h1>
            <div class="subtitulo">Diretório de Sorocaba • Hub de Consulta & Formação</div>
            <div class="meta-badge">RELATÓRIO DO TESTE DE FIXAÇÃO DA FÉ</div>
        </header>

        <section class="card-info">
            <h2>Encontro {encontro['numero']:02d}: {encontro['titulo']}</h2>
            <div class="dados-meta">
                <span><strong>Módulo:</strong> {encontro['bloco']}</span>
                <span><strong>Data da Avaliação:</strong> {agora}</span>
            </div>
            {f'<div style="margin-top: 0.4rem; font-size: 1rem; color: #5A3825;">{autor_str}</div>' if autor_str else ''}
        </section>

        <div class="placar-box">
            <div style="font-family: 'Cinzel', serif; font-size: 1rem; color: var(--texto-suave); text-transform: uppercase; letter-spacing: 1px;">
                Resultado do Teste
            </div>
            <div class="placar-numero">Nota: {nota} / {total}</div>
            <div class="placar-aproveitamento">{percentual}% de Aproveitamento</div>
            <div style="font-size: 1.05rem; color: {cor_conceito}; font-weight: 600; margin-top: 0.4rem; font-style: italic;">
                {conceito}
            </div>
        </div>

        <section class="bloco-conteudo">
            <h3 class="secao-titulo">📝 Detalhamento das Questões & Gabarito</h3>
            {questoes_html}
        </section>

        {reflexao_html}

        <footer class="rodape-sacro">
            <p><strong>Catequese da Igreja Católica Apostólica Romana — Diretório de Sorocaba</strong></p>
            <p style="font-style: italic; font-size: 0.88rem; margin-top: 0.3rem;">
                "Guardai o depósito sagrado da fé." (1Tm 6,20) &bull; Documento gerado pelo Hub de Consulta Catequética.
            </p>
        </footer>
    </div>
</body>
</html>
"""
    return html
