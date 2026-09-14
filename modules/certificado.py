# -*- coding: utf-8 -*-
"""
Módulo de Emissão de Certificado Solene de Conclusão do Catecumenato
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import streamlit as st
from datetime import datetime

def render_certificado_html(nome_catecumeno, data_conclusao=None, nome_paroquia="Paróquia Bom Jesus dos Aflitos — Sorocaba / SP"):
    if not data_conclusao:
        data_conclusao = datetime.now().strftime("%d de %B de %Y")
        
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Certificado do Catecumenato — {nome_catecumeno}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
            
            @page {{
                size: A4 landscape;
                margin: 10mm;
            }}
            
            body {{
                margin: 0;
                padding: 0;
                background-color: #FAF5EB;
                font-family: 'Playfair Display', serif;
                color: #2B1810;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}
            
            .certificado-borda-externa {{
                border: 12px double #781826;
                padding: 24px;
                background: #FAF8F5;
                box-shadow: inset 0 0 40px rgba(120, 24, 38, 0.08);
                margin: 10px auto;
                max-width: 980px;
                box-sizing: border-box;
            }}
            
            .certificado-borda-interna {{
                border: 2px solid #C5A059;
                padding: 30px 40px;
                text-align: center;
                background: #FFFDF9;
                position: relative;
            }}
            
            .cruz {{
                font-size: 3rem;
                color: #781826;
                line-height: 1;
                margin-bottom: 8px;
            }}
            
            .diocese {{
                font-family: 'Cinzel', serif;
                font-size: 1rem;
                letter-spacing: 3px;
                color: #5A3825;
                text-transform: uppercase;
                margin-bottom: 4px;
            }}
            
            .paroquia {{
                font-family: 'Cinzel', serif;
                font-size: 1.4rem;
                font-weight: 700;
                color: #781826;
                letter-spacing: 2px;
                margin-bottom: 4px;
            }}
            
            .ordem {{
                font-size: 0.9rem;
                font-style: italic;
                color: #5A3825;
                margin-bottom: 20px;
            }}
            
            .titulo-cert {{
                font-family: 'Cinzel', serif;
                font-size: 2.3rem;
                font-weight: 900;
                color: #781826;
                letter-spacing: 4px;
                text-transform: uppercase;
                margin: 15px 0;
                border-top: 1px solid #C5A059;
                border-bottom: 1px solid #C5A059;
                padding: 8px 0;
            }}
            
            .texto-corpo {{
                font-size: 1.25rem;
                line-height: 1.8;
                color: #2E1B10;
                margin: 25px auto;
                max-width: 800px;
            }}
            
            .nome-aluno {{
                font-family: 'Cinzel', serif;
                font-size: 2rem;
                font-weight: 700;
                color: #781826;
                text-decoration: underline;
                text-underline-offset: 8px;
                display: block;
                margin: 15px 0;
            }}
            
            .assinaturas {{
                display: flex;
                justify-content: space-around;
                margin-top: 60px;
                padding-top: 10px;
            }}
            
            .linha-assinatura {{
                width: 280px;
                border-top: 1px solid #5A3825;
                font-size: 0.95rem;
                color: #4A2E1B;
                padding-top: 6px;
                text-align: center;
            }}
            
            .data-emissao {{
                font-style: italic;
                font-size: 1.05rem;
                color: #5A3825;
                margin-top: 25px;
            }}
            
            @media print {{
                .no-print {{
                    display: none !important;
                }}
                body {{
                    background: none;
                }}
                .certificado-borda-externa {{
                    box-shadow: none;
                    margin: 0;
                    max-width: 100%;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="no-print" style="text-align: center; padding: 15px; background: #EEDCCE; border-bottom: 2px solid #781826;">
            <button onclick="window.print()" style="background: #781826; color: white; border: none; padding: 10px 24px; font-size: 1.1rem; font-family: 'Cinzel', serif; font-weight: bold; border-radius: 4px; cursor: pointer;">
                🖨️ Imprimir / Salvar em PDF
            </button>
        </div>
        
        <div class="certificado-borda-externa">
            <div class="certificado-borda-interna">
                <div class="cruz">☩</div>
                <div class="diocese">Arquidiocese de Sorocaba / SP</div>
                <div class="paroquia">PARÓQUIA BOM JESUS DOS AFLITOS</div>
                <div class="ordem">Ordem dos Frades Menores — Província Franciscana da Imaculada Conceição</div>
                
                <div class="titulo-cert">CERTIFICADO DE FORMAÇÃO CATEQUÉTICA</div>
                
                <div class="texto-corpo">
                    Certificamos com júbilo pastoral que o(a) irmão(ã) em Cristo
                    <span class="nome-aluno">{nome_catecumeno}</span>
                    completou com zelo, assiduidade e aproveitamento doutrinal todo o itinerário formativo dos 
                    <strong>40 Encontros do Catecumenato de Adultos</strong>, tendo aprofundado as Sagradas Escrituras, 
                    o Magistério da Santa Igreja Católica e a piedade franciscana, estando habilitado(a) e preparado(a) 
                    para a solene recepção dos Sacramentos da Iniciação Cristã.
                </div>
                
                <div class="data-emissao">
                    Sorocaba / SP, {data_conclusao}.
                </div>
                
                <div class="assinaturas">
                    <div class="linha-assinatura">
                        <strong>Fr. Pároco / Guardião, OFM</strong><br>
                        Pároco da Paróquia Bom Jesus dos Aflitos
                    </div>
                    <div class="linha-assinatura">
                        <strong>Catequista Administrador</strong><br>
                        Coordenação do Catecumenato de Adultos
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html
