# -*- coding: utf-8 -*-
"""
Gerador dos 40 Encontros do Catecumenato
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import json

ENCONTROS = [
    # 1. Sagrada Escritura (2 Encontros)
    {
        "numero": 1,
        "bloco": "Sagrada Escritura",
        "titulo": "A Sagrada Escritura",
        "subtemas": "a) A Bíblia é inspirada por Deus (2Pd 1,20-21 e 2Tm 3,14-17).\nb) Deus é o autor da Sagrada Escritura (1Tm 6,14; Tt 2,13).\nc) O Antigo Testamento e o Novo Testamento (1Cor 10,11; 1Pd 1,10; Hb 1,2).\nd) Em que língua foi escrita a Bíblia (Antigo Testamento em hebraico e, em grego, no Novo Testamento).\ne) O Papa e os bispos são os intérpretes da Sagrada Escritura (2Pd 1,20).",
        "resumo": "Introdução ao mistério da Sagrada Escritura como Palavra de Deus inspirada aos hagiógrafos e confiada à Igreja para a salvação de todos os homens.",
        "referencias_biblicas": "2Pd 1,20-21; 2Tm 3,14-17; 1Tm 6,14; Tt 2,13; 1Cor 10,11; 1Pd 1,10; Hb 1,1-2",
        "referencias_magisterio": "CIC 101-141 (A Sagrada Escritura; Inspiração e Verdade; O Cânon das Escrituras; A Escritura na vida da Igreja); Concílio Vaticano II, Constituição Dogmática Dei Verbum 9-13; CDC Cân. 747.",
        "fontes_complementares": "Didaqué cap. 4; São Jerônimo ('Desconhecer as Escrituras é desconhecer a Cristo'); Suma Teológica I, q. 1, a. 8-10.",
        "reflexao_franciscana": "São Francisco venerava toda palavra escrita do Senhor: 'Onde quer que os nomes do Senhor e suas sagradas palavras forem encontrados em lugares indecorosos, devem ser recolhidos e guardados em lugar digno' (Carta a todos os Clérigos). Francisco fez do Santo Evangelho a regra e a vida de seus irmãos.",
        "roteiro_encontro": "1. Acolhida com a saudação de São Francisco: 'Paz e Bem!'.\n2. Canto e Oração inicial ao Espírito Santo (Veni Creator).\n3. Rito de Entronização da Bíblia na sala de catequese.\n4. Exposição: Quem escreveu a Bíblia? Inspiração Divina, autores humanos e gêneros literários.\n5. Prática: Como manusear a Bíblia católica (73 livros: 46 no AT e 27 no NT).\n6. Partilha em grupos: Como a Palavra de Deus tem guiado minhas decisões?\n7. Compromisso da semana: Leitura diária do Evangelho de São Lucas.\n8. Oração final e bênção.",
        "oracao_final": "Senhor Deus, Pai misericordioso, que por amor inspirastes os autores sagrados e nos destes a Sagrada Escritura como luz para os nossos passos, abri nossos corações e inteligências para que, guiados pela Igreja, conheçamos a Verdade que nos liberta. Por Cristo, nosso Senhor. Amém."
    },
    {
        "numero": 2,
        "bloco": "Sagrada Escritura",
        "titulo": "Sagrada Escritura, Sagrada Tradição e o Sagrado Magistério",
        "subtemas": "O tripé da fé católica: a transmissão da Revelação divina através da Sagrada Escritura, da Tradição Apostólica viva e do Magistério autêntico da Igreja (CIC 54 a 73; CIC 80 a 95).",
        "resumo": "A revelação de Deus não se encerra na letra escrita isolada, mas floresce na Tradição viva da Igreja e é interpretada com assistência infalível do Espírito Santo pelo Magistério dos sucessores dos Apóstolos.",
        "referencias_biblicas": "2Ts 2,15 ('Permanecei firmes e guardai as tradições'); 1Tm 3,15 ('A Igreja é coluna e fundamento da verdade'); Mt 28,19-20; Jo 20,30; Jo 21,25.",
        "referencias_magisterio": "CIC 54-73; CIC 80-95; Dei Verbum 7-10; Catecismo Maior de São Pio X; CDC Cân. 750.",
        "fontes_complementares": "Santo Irineu de Lyon (Adversus Haereses III, 3, 1: A sucessão apostólica como garantia da verdade); Didaqué cap. 11; Suma Teológica II-II, q. 1, a. 1.",
        "reflexao_franciscana": "Em sua Segunda Carta aos Fiéis, São Francisco exorta: 'Devemos também visitar com frequência as igrejas e venerar e ter em reverência os sacerdotes, não tanto por eles mesmos, mas pelo ofício deles e pela administração do santíssimo corpo e sangue de nosso Senhor Jesus Cristo'. Para Francisco, a fidelidade à Sé Apostólica era inegociável.",
        "roteiro_encontro": "1. Acolhida e oração inicial.\n2. Ilustração pedagógica: O banco de três pernas (Escritura, Tradição e Magistério). Se tirar uma perna, a fé cai no relativismo.\n3. Diferença entre Tradição Apostólica (imutável, transmitida pelos Apóstolos) e tradições culturais/humanas.\n4. O papel do Papa (sucessor de Pedro) e dos Bispos em comunhão com ele.\n5. Diálogo: Por que a Igreja Católica tem 2000 anos de unidade doutrinal?\n6. Compromisso: Rezar um Pai Nosso e uma Ave Maria pelas intenções do Papa e do Bispo diocesano.\n7. Oração conclusiva.",
        "oracao_final": "Deus eterno e todo-poderoso, que edificastes a Vossa Igreja sobre a rocha dos Apóstolos e prometestes que as portas do inferno jamais prevaleceriam contra ela, dai-nos a graça do amor filial à Santa Igreja e a fidelidade inabalável à sã doutrina. Por Jesus Cristo, Nosso Senhor. Amém."
    },
    # 2. Deus é amor (2 Encontros)
    {
        "numero": 3,
        "bloco": "Deus é amor",
        "titulo": "Quem é Deus? (CIC 200-274)",
        "subtemas": "a) Deus é a verdade (Jo 18,37).\nb) Ele é o único Deus (Is 45,5).\nc) Deus é ternura e compaixão (Ex 34,5-6).\nd) Deus é eterno (Sl 101,26-28).\ne) Deus é onipotente (Is 45,5).\nf) Deus é onipresente (Hb 4,13).\ng) Deus é onisciente (Sl 139,7-10).",
        "resumo": "A revelação do Ser de Deus a Moisés no Sinai e pelos profetas: Deus é o Vivente, Puro Amor, Verdade Absoluta, Criador Onipotente, Eterno e Providente.",
        "referencias_biblicas": "Jo 18,37; Is 45,5; Ex 3,14 ('Eu Sou Aquele que Sou'); Ex 34,5-6; Sl 101(102),26-28; Hb 4,13; Sl 139(138),1-10; 1Jo 4,8.16.",
        "referencias_magisterio": "CIC 200-274 (Eu creio em Deus Pai; Os atributos de Deus; Deus é a Verdade e o Amor; Consequências da fé no Deus Único).",
        "fontes_complementares": "Santo Agostinho (De Trinitate; Confissões I, 1); São Tomás de Aquino (Suma Teológica I, q. 2: As Cinco Vias da Existência de Deus; q. 3-14: Atributos).",
        "reflexao_franciscana": "Nos 'Louvores a Deus', escritos de próprio punho por São Francisco no Monte Alverne: 'Vós sois Santo, Senhor Deus Único, o que faz maravilhas. Vós sois o Forte, Vós sois o Grande, Vós sois o Altíssimo, Vós sois o Rei onipotente... Vós sois o Amor, a Caridade! Vós sois a Sabedoria, a Humildade, a Paciência! Vós sois a Segurança, o Descanso, o Gozo, a nossa Esperança e a nossa Justiça!'.",
        "roteiro_encontro": "1. Acolhida e oração dos Louvores ao Deus Altíssimo.\n2. Exposição: A revelação da sarça ardente (Ex 3) e os 7 atributos de Deus descritos no currículo.\n3. Esclarecimento: Deus não é um conceito filosófico frio, mas uma Pessoa que quer se relacionar conosco.\n4. Leitura meditada do Salmo 139: 'Senhor, tu me perscrutas e me conheces...'.\n5. Partilha: Como você imaginava Deus na infância e como o descobre hoje?\n6. Compromisso: Fazer 15 minutos diários de recolhimento e oração pessoal.\n7. Oração final e bênção.",
        "oracao_final": "Altíssimo, Glorioso Deus, iluminai as trevas do meu coração. Dai-me uma fé reta, esperança certa e caridade perfeita, bom senso e discernimento, para que eu cumpra o Vosso santo e verídico mandamento. Amém. (Oração diante do Crucifixo de São Damião)."
    },
    {
        "numero": 4,
        "bloco": "Deus é amor",
        "titulo": "O amor de Deus por nós",
        "subtemas": "O amor de Deus por nós é:\na) Pessoal: Ele conhece-nos pelo nome (Is 43,1-4).\nb) Eterno: Ele nunca nos deixará de amar (Jr 31,3).\nc) Incondicional: Ele não coloca condições para amar-nos (1Jo 4,19).",
        "resumo": "A descoberta transformadora de que Deus nos ama de forma individual, indelével e incondicional. Não somos fruto do acaso, mas do afeto eterno do Criador.",
        "referencias_biblicas": "Is 43,1-4 ('És precioso aos meus olhos... e eu te amo'); Jr 31,3 ('Com amor eterno eu te amei'); 1Jo 4,19 ('Ele nos amou primeiro'); Lc 15,11-32 (O Pai Misericordioso); Rm 8,38-39.",
        "referencias_magisterio": "CIC 218-221 (O amor apaixonado de Deus por seu povo); CIC 604-605 (Deus toma a iniciativa do amor redentor); Carta Encíclica Deus Caritas Est de Bento XVI.",
        "fontes_complementares": "Santa Teresinha do Menino Jesus (O caminho da infância espiritual e da confiança total); Santa Clara de Assis (Cartas a Santa Inês de Praga).",
        "reflexao_franciscana": "São Francisco chorava pelos caminhos exclamando: 'O Amor não é amado! O Amor não é amado!'. Sua vida inteira foi uma resposta apaixonada à gratuidade do amor divino manifestado na manjedoura de Belém e na Cruz do Calvário.",
        "roteiro_encontro": "1. Acolhida e abraço da paz franciscana.\n2. Oração inicial.\n3. Dinâmica do espelho: 'Deus te conhece pelo teu nome e te gravou na palma de Suas mãos'.\n4. Análise dos três traços: Amor Pessoal, Amor Eterno, Amor Incondicional.\n5. O amor de Deus versus o amor interesseiro do mundo.\n6. Partilha: Já houve algum momento em que você sentiu fortemente que Deus cuidava de você?\n7. Compromisso: Reconciliar-se com alguém ou expressar amor incondicional a um familiar.\n8. Oração final.",
        "oracao_final": "Senhor Jesus Cristo, que por nosso amor vos entregastes até o fim na Cruz, imprimi em nossa alma a certeza consoladora de que nada nos poderá separar do Vosso Santo Amor. Ensinai-nos a amar como Vós nos amastes. Vós que viveis e reinais para sempre. Amém."
    },
    # 3. O mundo invisível (1 Encontro)
    {
        "numero": 5,
        "bloco": "O mundo invisível",
        "titulo": "Os Santos Anjos e sua função",
        "subtemas": "A existência dos anjos na Revelação divina (Cl 1,16), suas ordens celestes e a missão do Santo Anjo da Guarda na vida de cada cristão (CIC 336).",
        "resumo": "Doutrina católica sobre o mundo invisível: seres espirituais criados por Deus que adoram incessantemente a Trindade e servem aos desígnios da salvação humana.",
        "referencias_biblicas": "Cl 1,16 ('Nele foram criadas todas as coisas celestes e terrestres, visíveis e invisíveis'); Sl 90(91),11-12; Mt 18,10; Ex 23,20-21; Lc 1,26-38; Ap 12,7-9; Tb 12,12-15.",
        "referencias_magisterio": "CIC 328-336 (Quem são os anjos; Cristo com todos os seus anjos; Os anjos na liturgia e na oração; O Anjo da Guarda pessoal).",
        "fontes_complementares": "São Tomás de Aquino (O Doutor Angélico, Suma Teológica I, qq. 50-64); São Bernardo de Claraval (Sermões sobre o Salmo 90: 'Eles estão sempre conosco para nos guardar').",
        "reflexao_franciscana": "São Francisco tinha imensa devoção aos Santos Anjos e em particular a São Miguel Arcanjo. Jejuava quarenta dias na festa de São Miguel no Monte Alverne. Foi durante esse retiro quaresmal que um Serafim de seis asas apareceu e imprimiu em seu corpo as chagas de Cristo.",
        "roteiro_encontro": "1. Acolhida e oração do Santo Anjo do Senhor.\n2. Desmistificação: O que a Igreja ensina versus o esoterismo/superstição da 'New Age'.\n3. Os Três Santos Arcanjos na Bíblia: Miguel ('Quem como Deus?'), Gabriel ('Fortaleza de Deus') e Rafael ('Medicina de Deus').\n4. O Anjo Custódio: companheiro espiritual invisível desde a concepção até a passagem para a eternidade.\n5. Partilha: Você costuma pedir auxílio ao seu Anjo da Guarda na vida diária e nas tentações?\n6. Oração a São Miguel Arcanjo composta pelo Papa Leão XIII.\n7. Bênção final.",
        "oracao_final": "Santo Anjo do Senhor, meu zeloso guardador, já que a ti me confiou a piedade divina, sempre me rege, me guarde, me governe, me ilumine. São Miguel Arcanjo, defendei-nos no combate contra as ciladas do demônio. Amém."
    },
    # 4. O mundo visível (2 Encontros)
    {
        "numero": 6,
        "bloco": "O mundo visível",
        "titulo": "O mistério da criação (CIC 279-301)",
        "subtemas": "a) A criação pode ser entendida pela razão (Rm 1,20).\nb) A criação é obra da Santíssima Trindade (Gn 1,1; Jo 1,1-3; Sl 103,30).",
        "resumo": "Deus criou o universo do nada (ex nihilo) livremente, por pura bondade e amor. A Criação é o primeiro passo da Aliança e manifesta a glória da Santíssima Trindade.",
        "referencias_biblicas": "Gn 1,1-31; Rm 1,20 ('Pois desde a criação do mundo as perfeições invisíveis de Deus são contempladas nas criaturas'); Sl 18(19),2; Jo 1,1-3; Sb 13,1-9.",
        "referencias_magisterio": "CIC 279-301 (A criação é obra da Trindade; Criado do nada; Deus sustenta e governa a criação; A Providência Divina).",
        "fontes_complementares": "Suma Teológica I, qq. 44-46; São Boaventura (A criação como espelho e vestígio da Trindade); Encíclica Laudato Si' do Papa Francisco.",
        "reflexao_franciscana": "O Cântico das Criaturas (ou Cântico do Irmão Sol) de São Francisco de Assis: 'Louvado sejas, meu Senhor, com todas as tuas criaturas, especialmente o meu senhor irmão Sol... Louvado sejas pela irmã Lua, pelo irmão Vento, pela irmã Água, preciosa e casta, pelo irmão Fogo e pela nossa irmã mãe Terra!'.",
        "roteiro_encontro": "1. Acolhida e oração do Cântico das Criaturas.\n2. Exposição: Fé e Razão na Criação (A Igreja Católica nunca foi contra a ciência autêntica; Gênesis não é um tratado de biologia, mas a revelação do sentido teológico).\n3. O papel de cada Pessoa da Trindade: O Pai planeja, o Filho gera pelo Verbo, o Espírito Santo vivifica sobre as águas.\n4. A ecologia integral católica: o cuidado da Criação como dádiva divina.\n5. Partilha: Como contemplo a presença de Deus nas belezas da natureza?\n6. Compromisso: Praticar um ato concreto de respeito e cuidado com a criação durante a semana.\n7. Oração de louvor e bênção.",
        "oracao_final": "Onipotente, Altíssimo, Bom Senhor Deus, que no início fizestes todas as coisas com sabedoria infinita e as conservais com amorosa Providência, ensinai-nos a ver Vossas pegadas em toda a criação e a viver como fiéis administradores dos Vossos dons. Por Cristo, Nosso Senhor. Amém."
    },
    {
        "numero": 7,
        "bloco": "O mundo visível",
        "titulo": "Criação do homem e da mulher",
        "subtemas": "Criação do homem e da mulher à imagem e semelhança de Deus (Gn 1,26-27) e sua santidade original (Gn 2,8-15):\na) Imortalidade: o homem jamais morreria.\nb) Impassibilidade: ausência de dor e sofrimento.\nc) Integridade: harmonia interior, livre da concupiscência.\nd) Ciência moral infusa: conheciam a vontade de Deus e eram aptos para assumir suas responsabilidades perante o Senhor.",
        "resumo": "A vocação altíssima do ser humano como ápice da criação visível, dotado de alma espiritual e imortal, e os dons preternaturais no estado de inocência original.",
        "referencias_biblicas": "Gn 1,26-28; Gn 2,7-25; Sl 8,4-7 ('Fizeste-o pouco menor que os anjos, de glória e honra o coroaste'); Mt 19,4-6; 1Ts 5,23.",
        "referencias_magisterio": "CIC 355-384 (O homem à imagem de Deus; Corpo e alma um só ser; 'Homem e mulher os criou'; O estado de justiça original).",
        "fontes_complementares": "Suma Teológica I, qq. 93-102 (Da justiça original e dos dons preternaturais de Adão e Eva); São João Paulo II (Teologia do Corpo).",
        "reflexao_franciscana": "São Francisco exorta na Quinta Admoestação: 'Considera, ó homem, a que alta dignidade te elevou o Senhor Deus, pois te criou e formou à imagem do seu amado Filho segundo o corpo, e à sua semelhança segundo o espírito!'.",
        "roteiro_encontro": "1. Acolhida e oração inicial.\n2. Exposição: A singularidade do ser humano (corpo material e alma imortal criada imediatamente por Deus).\n3. Homem e Mulher: Igual dignidade e rica complementaridade querida por Deus desde o princípio.\n4. Estudo dos 4 Dons Preternaturais do Paraíso: Imortalidade, Impassibilidade, Integridade e Ciência Infusa.\n5. Partilha: Como a sociedade atual degrada a imagem humana e como o Evangelho resgata nossa dignidade?\n6. Compromisso: Reconhecer a imagem de Cristo nos irmãos que sofrem ou são desprezados.\n7. Oração conclusiva.",
        "oracao_final": "Senhor Deus, Pai de bondade, que criastes a criatura humana de modo admirável e de modo mais admirável ainda a resgatastes pelo Sangue do Vosso Filho, concedei-nos viver segundo a sublime vocação de filhos adotivos de Deus. Por Jesus Cristo, Nosso Senhor. Amém."
    }
]

with open(r"C:\Users\marce\.gemini\antigravity\scratch\catecumenato_bom_jesus\data\encontros_part1.json", "w", encoding="utf-8") as f:
    json.dump(ENCONTROS, f, ensure_ascii=False, indent=2)

print(f"Part 1 written with {len(ENCONTROS)} encounters")