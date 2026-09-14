# -*- coding: utf-8 -*-
"""
Atualização do Banco de Dados SQLite com Imagens Sacras, Novas Orações e Autenticação
Paróquia Bom Jesus dos Aflitos - Sorocaba / Franciscanos
"""

import sqlite3
import os
import json
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "catequese.db")
SEED_PATH = os.path.join(os.path.dirname(__file__), "data", "seed_completo.json")

SENHA_CATEQUISTA_PADRAO = "pazebem"

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS configuracoes (
        chave TEXT PRIMARY KEY,
        valor TEXT NOT NULL
    )
    """)

    # Senha padrão do catequista se não existir
    cur.execute("INSERT OR IGNORE INTO configuracoes (chave, valor) VALUES ('senha_catequista', ?)", (SENHA_CATEQUISTA_PADRAO,))

    cur.execute("""
    CREATE TABLE IF NOT EXISTS encontros (
        numero INTEGER PRIMARY KEY,
        bloco TEXT NOT NULL,
        titulo TEXT NOT NULL,
        subtemas TEXT,
        resumo TEXT,
        referencias_biblicas TEXT,
        referencias_magisterio TEXT,
        fontes_complementares TEXT,
        reflexao_franciscana TEXT,
        roteiro_encontro TEXT,
        oracao_final TEXT,
        imagem_url TEXT,
        imagem_legenda TEXT
    )
    """)

    # Verificar se colunas imagem_url e imagem_legenda existem
    cur.execute("PRAGMA table_info(encontros)")
    colunas = [r[1] for r in cur.fetchall()]
    if "imagem_url" not in colunas:
        cur.execute("ALTER TABLE encontros ADD COLUMN imagem_url TEXT")
    if "imagem_legenda" not in colunas:
        cur.execute("ALTER TABLE encontros ADD COLUMN imagem_legenda TEXT")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS catecumenos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT,
        telefone TEXT,
        data_nascimento TEXT,
        estado_civil TEXT,
        batizado INTEGER DEFAULT 0,
        primeira_eucaristia INTEGER DEFAULT 0,
        crismado INTEGER DEFAULT 0,
        padrinho_madrinha TEXT,
        observacoes TEXT,
        ativo INTEGER DEFAULT 1,
        data_cadastro TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS presencas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        catecumeno_id INTEGER NOT NULL,
        encontro_numero INTEGER NOT NULL,
        data TEXT NOT NULL,
        presente INTEGER DEFAULT 1,
        justificativa TEXT,
        UNIQUE(catecumeno_id, encontro_numero),
        FOREIGN KEY(catecumeno_id) REFERENCES catecumenos(id),
        FOREIGN KEY(encontro_numero) REFERENCES encontros(numero)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS anotacoes_diario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        catecumeno_id INTEGER DEFAULT 0,
        encontro_numero INTEGER NOT NULL,
        autor TEXT,
        texto TEXT NOT NULL,
        data_registro TEXT NOT NULL,
        FOREIGN KEY(encontro_numero) REFERENCES encontros(numero)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS progresso_encontros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        catecumeno_id INTEGER NOT NULL,
        encontro_numero INTEGER NOT NULL,
        concluido INTEGER DEFAULT 1,
        data_conclusao TEXT NOT NULL,
        UNIQUE(catecumeno_id, encontro_numero),
        FOREIGN KEY(catecumeno_id) REFERENCES catecumenos(id),
        FOREIGN KEY(encontro_numero) REFERENCES encontros(numero)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS respostas_quiz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        catecumeno_id INTEGER NOT NULL,
        encontro_numero INTEGER NOT NULL,
        questao_idx INTEGER NOT NULL,
        opcao_escolhida INTEGER NOT NULL,
        acertou INTEGER NOT NULL,
        data_resposta TEXT NOT NULL,
        UNIQUE(catecumeno_id, encontro_numero, questao_idx),
        FOREIGN KEY(catecumeno_id) REFERENCES catecumenos(id),
        FOREIGN KEY(encontro_numero) REFERENCES encontros(numero)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS oracoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        categoria TEXT NOT NULL,
        origem_autor TEXT,
        texto TEXT NOT NULL
    )
    """)

    conn.commit()

    # Atualizar imagens sacras dos 40 encontros
    atualizar_imagens_sacras(conn)

    # Inserir novas orações dos Santos se ainda não inseridas
    inserir_novas_oracoes_santos(conn)

    conn.close()

def atualizar_imagens_sacras(conn):
    cur = conn.cursor()
    
    LEGENDAS_ENCONTROS = {
        1: "São Jerônimo no Estudo da Palavra Sagrada — Caravaggio (1605)",
        2: "Cristo entrega as Chaves do Reino a São Pedro — Pietro Perugino (Capela Sistina)",
        3: "A Criação de Adão — Michelangelo Buonarroti (Capela Sistina, Vaticano)",
        4: "O Retorno do Filho Pródigo ao Pai Misericordioso — Rembrandt van Rijn (1669)",
        5: "São Miguel Arcanjo derrota o Maligno — Guido Reni (Igreja Santa Maria della Concezione, Roma)",
        6: "A Separação da Luz e das Trevas no Gênesis — Michelangelo (Capela Sistina)",
        7: "A Criação da Mulher a partir do Homem — Michelangelo (Capela Sistina)",
        8: "A Queda Original e a Expulsão do Paraíso — Michelangelo Buonarroti",
        9: "A Fé Inabalável de Abraão e o Sacrifício de Isaac — Caravaggio (Galleria degli Uffizi)",
        10: "Moisés com as Tábuas da Aliança no Monte Sinai — Rembrandt (1659)",
        11: "Josué Conduz o Povo de Deus na Terra Prometida — John Martin",
        12: "O Santo Rei Davi Entoando os Salmos ao Senhor — Gerard van Honthorst (1622)",
        13: "O Profeta Isaías Anuncia o Servo de Deus — Michelangelo (Capela Sistina)",
        14: "A Encarnação do Verbo: A Anunciação do Arcanjo Gabriel — Fra Angelico (Museo del Prado)",
        15: "O Santo Crucifixo de São Damião: Cristo Vencedor da Morte na Cruz — Ícone Franciscano",
        16: "A Efusão do Espírito Santo no Cenáculo em Pentecostes — El Greco (Museo del Prado)",
        17: "Os Dons Celestiais do Espírito Santo sobre os Apóstolos — Giotto di Bondone (Capela Scrovegni)",
        18: "Cristo Glorioso Edifica e Sustenta a Santa Igreja Católica — Fra Angelico",
        19: "A Comunhão e Fraternidade na Igreja Primitiva dos Apóstolos — Masaccio (Florença)",
        20: "São Pedro e São Paulo: Colunas da Igreja Una, Santa e Apostólica — El Greco",
        21: "O Retábulo dos Sete Sacramentos da Igreja — Rogier van der Weyden (1445)",
        22: "O Batismo de Nosso Senhor Jesus Cristo no Rio Jordão — Piero della Francesca",
        23: "O Santo Batismo e o Nascimento para a Vida da Graça — Fra Angelico",
        24: "A Unção do Santo Crisma e a Confirmação — Rogier van der Weyden (Detalhe)",
        25: "O Sagrado Rito da Crisma e o Selo do Espírito Santo — Nicolas Poussin (1645)",
        26: "Os Frutos da Confirmação: O Testemunho Corajoso da Fé no Mundo — Masolino da Panicale",
        27: "A Instituição da Santíssima Eucaristia na Última Ceia — Philippe de Champaigne (Museu do Louvre)",
        28: "A Disputa e Adoração do Santíssimo Sacramento — Rafael Sanzio (Palácio Apostólico, Vaticano)",
        29: "A Santa Comunhão dos Apóstolos — Luca Signorelli (1512)",
        30: "O Sacramento da Sagrada Ordem e a Sucessão Apostólica — Nicolas Poussin",
        31: "O Casamento da Bem-Aventurada Virgem Maria e São José — Rafael Sanzio (1504)",
        32: "A Infinita Misericórdia e o Perdão dos Pecados na Reconciliação — Guercino",
        33: "O Bom Samaritano: Cristo Cuida e Cura as Nossas Chagas — Eugène Delacroix",
        34: "A Celebração do Santo Sacrifício da Missa (A Missa de Bolsena) — Rafael Sanzio (Palácio Apostólico, Vaticano)",
        35: "A Adoração do Cordeiro Místico de Deus no Ano Litúrgico — Jan van Eyck",
        36: "O Sagrado Ícone da Santíssima Trindade — Santo Andrei Rublev (1411)",
        37: "O Juízo Particular e a Esperança da Visão Beatífica — Fra Angelico",
        38: "O Juízo Universal e a Gloriosa Ressurreição da Carne — Michelangelo (Capela Sistina)",
        39: "Santa Maria, Mãe de Deus e Virgem Perpétua — Rafael Sanzio (Madonna Sistina)",
        40: "A Imaculada Conceição e a Assunção de Nossa Senhora — Bartolomé Esteban Murillo"
    }

    for num, leg in LEGENDAS_ENCONTROS.items():
        caminho = f"assets/images/encontro_{num:02d}.jpg"
        cur.execute("UPDATE encontros SET imagem_url = ?, imagem_legenda = ? WHERE numero = ?", (caminho, leg, num))
    
    conn.commit()

def inserir_novas_oracoes_santos(conn):
    cur = conn.cursor()
    
    NOVAS_ORACOES = [
        {
            "titulo": "Oração da Santa Cruz de São Bento (Crux Sacra)",
            "categoria": "São Bento",
            "origem_autor": "São Bento de Núrsia (Tradição Beneditina)",
            "texto": """A Cruz Sagrada seja a minha luz,
Não seja o dragão meu guia.
Retira-te, satanás!
Nunca me aconselhes coisas vãs.
É mau o que tu me ofereces,
Bebe tu mesmo o teu veneno!

(Em latim:
Crux Sacra Sit Mihi Lux / Non Draco Sit Mihi Dux / Vade Retro Satana / Numquam Suade Mihi Vana / Sunt Mala Quae Libas / Ipse Venena Bibas).

O Senhor me abençoe e me defenda de todo o mal, e me conduza à vida eterna. Amém."""
        },
        {
            "titulo": "Oração de Proteção e Libertação de São Bento",
            "categoria": "São Bento",
            "origem_autor": "Ordem de São Bento",
            "texto": """Glorioso São Bento, que dedicastes toda a vossa vida a Cristo e aos irmãos,
afastai de nós, de nossa família e de nossa comunidade toda cilada do demônio,
todo ódio, inveja, discórdia e enfermidade espiritual.
Pelo poder da Santa Cruz de Nosso Senhor Jesus Cristo,
abençoai o nosso lar, guardai os nossos passos e dai-nos a graça de perseverar
fielmente nos mandamentos divinos até a glória eterna. Por Cristo, Nosso Senhor. Amém."""
        },
        {
            "titulo": "Bênção Solene de Santa Clara de Assis",
            "categoria": "Santa Clara",
            "origem_autor": "Santa Clara de Assis (Escritos)",
            "texto": """Em nome do Pai e do Filho e do Espírito Santo. Amém.
O Senhor vos abençoe e vos guarde!
Mostre-vos a sua face e tenha misericórdia de vós!
Volte para vós o seu olhar e vos dê a sua paz!
O Senhor esteja sempre convosco e faça que estejais sempre com Ele.
Eu vos abençoo em minha vida e depois de minha morte,
com todas as bênçãos com que o Pai das misericórdias abençoou
e abençoará seus filhos e filhas no Céu e na terra.
Abençoo-vos em nome do Pai e do Filho e do Espírito Santo. Amém."""
        },
        {
            "titulo": "Oração do Espelho de Cristo",
            "categoria": "Santa Clara",
            "origem_autor": "Santa Clara de Assis (4ª Carta a Santa Inês de Praga)",
            "texto": """Olha diariamente para este Espelho, ó alma consagrada,
e nele contempla continuamente a tua face,
para que possas ornar-te toda inteira, interior e exteriormente,
vestida com a variedade de todas as virtudes.
Neste Espelho resplandece a bem-aventurada pobreza,
a santa humildade e a inefável caridade de Cristo Jesus.
Olha para o princípio deste Espelho: a pobreza Daquele que foi colocado no presépio e envolvido em panos!
Olha para o meio: a santa humildade com que suportou fadigas e afrontas por nosso amor!
Olha para o fim: a inefável caridade com que escolheu morrer na Cruz,
entregando o seu Espírito nas mãos do Pai.
Permanece em oração diante deste Espelho de amor! Amém."""
        },
        {
            "titulo": "Oração de Santa Clara perante o Santíssimo Sacramento",
            "categoria": "Santa Clara",
            "origem_autor": "Tradição Franciscana-Clarissa (São Damião, 1240)",
            "texto": """Ó meu Senhor Jesus Cristo,
guardai vós mesmo estas vossas servas que eu agora não posso guardar!
Senhor, olhai para a vossa humilde grei que tanto Vos ama.
(E da Custódia com a Hóstia Consagrada ouviu-se a voz de Cristo: 'Eu vos guardarei sempre!').
Ó Jesus Eucarístico, nosso escudo e nossa fortaleza invencível,
protegei a Santa Igreja contra todos os perigos espirituais e temporais. Amém."""
        },
        {
            "titulo": "Tarde Te Amei, ó Beleza tão antiga e tão nova",
            "categoria": "Santo Agostinho",
            "origem_autor": "Santo Agostinho de Hipona (Confissões, Livro X)",
            "texto": """Tarde Te amei, ó Beleza tão antiga e tão nova, tarde Te amei!
Eis que habitavas dentro de mim e eu Te procurava fora!
Eu, disforme, me lançava sobre as belas formas de Tuas criaturas.
Estavas comigo, mas eu não estava Contigo.
Retinham-me longe de Ti aquelas coisas que não existiriam se não existissem em Ti.
Chamaste-me, clamaste, e rompeste a minha surdez!
Brilhaste, resplandeceste, e dissipaste a minha cegueira!
Exalaste o Teu perfume, respirei-o, e agora suspiro por Ti!
Provei-Te, e agora tenho fome e sede de Ti!
Tocaste-me, e abraso-me na Tua paz! Amém."""
        },
        {
            "titulo": "Oração ao Espírito Santo (Respira em mim)",
            "categoria": "Santo Agostinho",
            "origem_autor": "Santo Agostinho de Hipona",
            "texto": """Respira em mim, ó Espírito Santo, para que todos os meus pensamentos sejam santos.
Age em mim, ó Espírito Santo, para que meu trabalho também seja santo.
Atrai o meu coração, ó Espírito Santo, para que eu ame somente o que é santo.
Fortalece-me, ó Espírito Santo, para que eu defenda tudo o que é santo.
Guarda-me, ó Espírito Santo, para que eu nunca perca o que é santo. Amém."""
        },
        {
            "titulo": "Nada te turbe (Só Deus Basta)",
            "categoria": "Santa Teresa d'Ávila",
            "origem_autor": "Santa Teresa de Jesus / d'Ávila (Doutora da Igreja)",
            "texto": """Nada te turbe,
Nada te espante,
Tudo passa,
Deus não muda.
A paciência tudo alcança;
Quem a Deus tem,
Nada lhe falta:
Só Deus basta! Amém."""
        },
        {
            "titulo": "Oração antes dos Estudos",
            "categoria": "São Tomás de Aquino",
            "origem_autor": "São Tomás de Aquino (O Doutor Angélico)",
            "texto": """Criador inefável, que das vossas infinitas riquezas elegestes as três hierarquias dos anjos
e as colocastes com ordem admirável sobre o céu empíreo,
e distribuístes o universo com perfeita harmonia;
Vós, que sois a verdadeira fonte da luz e o princípio supremo da sabedoria,
dignai-vos derramar sobre as trevas da minha inteligência um raio da vossa claridade,
afastando de mim a dupla escuridão na qual nasci: o pecado e a ignorância.
Vós, que tornais eloquente a língua das crianças, purificai os meus lábios
e derramai neles a bênção da vossa graça.
Dai-me penetração para compreender, capacidade para reter,
método e facilidade para aprender, subtileza para interpretar e graça abundante para falar.
Orientai o meu início, dirigi o meu progresso e coroai o meu fim.
Vós, que sois verdadeiro Deus e verdadeiro Homem, e viveis e reinais pelos séculos dos séculos. Amém."""
        },
        {
            "titulo": "Hino Eucarístico: Adoro Te Devote",
            "categoria": "São Tomás de Aquino",
            "origem_autor": "São Tomás de Aquino (1264)",
            "texto": """Adoro-Te com amor, Divindade escondida,
Que sob estas figuras verdadeiramente Te ocultas:
A Ti meu coração se submete inteiramente,
Pois, contemplando-Te, todo ele desfalece.

A vista, o tato e o gosto em Ti se enganam,
Mas só com o ouvir se crê com firmeza:
Creio em tudo o que disse o Filho de Deus,
Nada há de mais verdadeiro que esta Palavra de Verdade.

Na Cruz estava oculta só a Divindade,
Mas aqui também a humanidade se esconde:
Eu, porém, crendo e professando uma e outra,
Peço aquilo que pediu o bom ladrão arrependido.

Ó memorial da morte do Senhor!
Pão vivo que dás a vida ao homem!
Faze que minha alma viva de Ti
E que para ela sejas sempre doce!

Jesus, a quem agora vejo sob véus,
Rogo que se cumpra o que tanto desejo:
Que, contemplando-Te com a face revelada,
Eu seja bem-aventurado na visão da Tua glória! Amém."""
        },
        {
            "titulo": "Oração de Entrega Total (Suscipe, Domine)",
            "categoria": "Santo Inácio de Loyola",
            "origem_autor": "Santo Inácio de Loyola (Exercícios Espirituais)",
            "texto": """Tomai, Senhor, e recebei toda a minha liberdade,
a minha memória, a minha inteligência e toda a minha vontade,
tudo o que tenho e possuo;
Vós me destes, a Vós, Senhor, o restituo.
Tudo é vosso, disponde de tudo inteiramente segundo a vossa vontade.
Dai-me somente o vosso amor e a vossa graça,
pois esta me basta. Amém."""
        },
        {
            "titulo": "Fica Comigo, Senhor (Oração Pós-Comunhão)",
            "categoria": "São Padre Pio",
            "origem_autor": "São Pio de Pietrelcina",
            "texto": """Fica comigo, Senhor, porque é necessária a Vossa presença para não Vos esquecer.
Sabeis com que facilidade Vos abandono.
Fica comigo, Senhor, porque sou fraco e preciso da Vossa força para não cair tantas vezes.
Fica comigo, Senhor, porque Vós sois a minha vida e, sem Vós, desfaleço no fervor.
Fica comigo, Senhor, porque Vós sois a minha luz e, sem Vós, estou nas trevas.
Fica comigo, Senhor, para me mostrar a Vossa vontade.
Fica comigo, Senhor, para que eu ouça a Vossa voz e a siga.
Fica comigo, Jesus, porque, por mais pobre que seja minha alma,
deseja ser para Vós um lugar de consolo e um ninho de amor. Amém."""
        }
    ]

    for o in NOVAS_ORACOES:
        cur.execute("SELECT id FROM oracoes WHERE titulo = ?", (o["titulo"],))
        if not cur.fetchone():
            cur.execute("""
            INSERT INTO oracoes (titulo, categoria, origem_autor, texto)
            VALUES (?, ?, ?, ?)
            """, (o["titulo"], o["categoria"], o["origem_autor"], o["texto"]))

    conn.commit()

# Autenticação e Configurações
def verificar_senha_catequista(senha_digitada):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT valor FROM configuracoes WHERE chave = 'senha_catequista'")
    row = cur.fetchone()
    conn.close()
    senha_correta = row[0] if row else SENHA_CATEQUISTA_PADRAO
    return senha_digitada == senha_correta

def alterar_senha_catequista(nova_senha):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO configuracoes (chave, valor) VALUES ('senha_catequista', ?)", (nova_senha,))
    conn.commit()
    conn.close()

# Consultas de Encontros
def get_encontros(bloco=None, termo_busca=None):
    conn = get_connection()
    cur = conn.cursor()
    query = "SELECT * FROM encontros WHERE 1=1"
    params = []

    if bloco and bloco != "Todos os Blocos":
        query += " AND bloco = ?"
        params.append(bloco)

    if termo_busca:
        query += " AND (titulo LIKE ? OR subtemas LIKE ? OR resumo LIKE ? OR referencias_biblicas LIKE ?)"
        like_term = f"%{termo_busca}%"
        params.extend([like_term, like_term, like_term, like_term])

    query += " ORDER BY numero ASC"
    cur.execute(query, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def get_encontro_by_numero(numero):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM encontros WHERE numero = ?", (numero,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def get_blocos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT bloco FROM encontros GROUP BY bloco ORDER BY MIN(numero)")
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return rows

# Consultas e Operações de Catecúmenos
def get_catecumenos(filtro_ativo=True):
    conn = get_connection()
    cur = conn.cursor()
    if filtro_ativo:
        cur.execute("SELECT * FROM catecumenos WHERE ativo = 1 ORDER BY nome ASC")
    else:
        cur.execute("SELECT * FROM catecumenos ORDER BY nome ASC")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def get_catecumeno(cid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM catecumenos WHERE id = ?", (cid,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def add_catecumeno(nome, email, telefone, data_nasc, estado_civil, batizado, eucaristia, crismado, padrinhos, obs):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO catecumenos (nome, email, telefone, data_nascimento, estado_civil,
                             batizado, primeira_eucaristia, crismado, padrinho_madrinha,
                             observacoes, ativo, data_cadastro)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
    """, (nome, email, telefone, data_nasc, estado_civil, batizado, eucaristia, crismado, padrinhos, obs, datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id

def update_catecumeno(cid, nome, email, telefone, data_nasc, estado_civil, batizado, eucaristia, crismado, padrinhos, obs, ativo):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    UPDATE catecumenos
    SET nome=?, email=?, telefone=?, data_nascimento=?, estado_civil=?,
        batizado=?, primeira_eucaristia=?, crismado=?, padrinho_madrinha=?,
        observacoes=?, ativo=?
    WHERE id=?
    """, (nome, email, telefone, data_nasc, estado_civil, batizado, eucaristia, crismado, padrinhos, obs, ativo, cid))
    conn.commit()
    conn.close()

def delete_catecumeno(cid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM presencas WHERE catecumeno_id=?", (cid,))
    cur.execute("DELETE FROM anotacoes_diario WHERE catecumeno_id=?", (cid,))
    cur.execute("DELETE FROM progresso_encontros WHERE catecumeno_id=?", (cid,))
    cur.execute("DELETE FROM respostas_quiz WHERE catecumeno_id=?", (cid,))
    cur.execute("DELETE FROM catecumenos WHERE id=?", (cid,))
    conn.commit()
    conn.close()

# Presenças e Frequência
def salvar_presencas_encontro(encontro_numero, data_encontro, registros_presenca):
    conn = get_connection()
    cur = conn.cursor()
    for cid, pres in registros_presenca.items():
        cur.execute("""
        INSERT INTO presencas (catecumeno_id, encontro_numero, data, presente, justificativa)
        VALUES (?, ?, ?, ?, '')
        ON CONFLICT(catecumeno_id, encontro_numero) DO UPDATE SET
            presente=excluded.presente,
            data=excluded.data
        """, (cid, encontro_numero, data_encontro, 1 if pres else 0))
    conn.commit()
    conn.close()

def get_presencas_encontro(encontro_numero):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT catecumeno_id, presente, data FROM presencas WHERE encontro_numero = ?", (encontro_numero,))
    rows = {r["catecumeno_id"]: bool(r["presente"]) for r in cur.fetchall()}
    conn.close()
    return rows

def get_estatisticas_frequencia():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT c.id, c.nome, c.batizado, c.primeira_eucaristia, c.crismado,
           COUNT(CASE WHEN p.presente = 1 THEN 1 END) as total_presencas,
           COUNT(p.id) as total_aulas_registradas
    FROM catecumenos c
    LEFT JOIN presencas p ON c.id = p.catecumeno_id
    WHERE c.ativo = 1
    GROUP BY c.id
    ORDER BY c.nome ASC
    """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

# Anotações do Diário Espiritual
def add_anotacao(catecumeno_id, encontro_numero, autor, texto):
    conn = get_connection()
    cur = conn.cursor()
    data_reg = datetime.now().strftime("%d/%m/%Y %H:%M")
    cur.execute("""
    INSERT INTO anotacoes_diario (catecumeno_id, encontro_numero, autor, texto, data_registro)
    VALUES (?, ?, ?, ?, ?)
    """, (catecumeno_id, encontro_numero, autor, texto, data_reg))
    conn.commit()
    conn.close()

def get_anotacoes(encontro_numero, catecumeno_id=None):
    conn = get_connection()
    cur = conn.cursor()
    if catecumeno_id:
        cur.execute("""
        SELECT a.*, c.nome as nome_catecumeno
        FROM anotacoes_diario a
        LEFT JOIN catecumenos c ON a.catecumeno_id = c.id
        WHERE a.encontro_numero = ? AND (a.catecumeno_id = ? OR a.catecumeno_id = 0)
        ORDER BY a.id DESC
        """, (encontro_numero, catecumeno_id))
    else:
        cur.execute("""
        SELECT a.*, c.nome as nome_catecumeno
        FROM anotacoes_diario a
        LEFT JOIN catecumenos c ON a.catecumeno_id = c.id
        WHERE a.encontro_numero = ?
        ORDER BY a.id DESC
        """, (encontro_numero,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

# Orações
def get_oracoes(categoria=None):
    conn = get_connection()
    cur = conn.cursor()
    if categoria and categoria != "Todas as Orações":
        cur.execute("SELECT * FROM oracoes WHERE categoria = ? ORDER BY titulo ASC", (categoria,))
    else:
        cur.execute("SELECT * FROM oracoes ORDER BY categoria, titulo ASC")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def get_categorias_oracoes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT categoria FROM oracoes ORDER BY categoria ASC")
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return rows

# ==============================================================================
# Acompanhamento de Progresso e Quizzes dos Catecúmenos
# ==============================================================================

def marcar_encontro_concluido(catecumeno_id, encontro_numero):
    """Registra a conclusão de estudo de um encontro para o catecúmeno."""
    if not catecumeno_id:
        return
    conn = get_connection()
    cur = conn.cursor()
    data_concl = datetime.now().strftime("%d/%m/%Y %H:%M")
    cur.execute("""
    INSERT INTO progresso_encontros (catecumeno_id, encontro_numero, concluido, data_conclusao)
    VALUES (?, ?, 1, ?)
    ON CONFLICT(catecumeno_id, encontro_numero) DO UPDATE SET
        concluido = 1,
        data_conclusao = excluded.data_conclusao
    """, (catecumeno_id, encontro_numero, data_concl))
    conn.commit()
    conn.close()

def desmarcar_encontro_concluido(catecumeno_id, encontro_numero):
    """Desmarca a conclusão de estudo de um encontro."""
    if not catecumeno_id:
        return
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM progresso_encontros WHERE catecumeno_id = ? AND encontro_numero = ?", (catecumeno_id, encontro_numero))
    conn.commit()
    conn.close()

def is_encontro_concluido(catecumeno_id, encontro_numero):
    """Verifica se o encontro específico já foi concluído pelo catecúmeno."""
    if not catecumeno_id:
        return False
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT concluido, data_conclusao FROM progresso_encontros WHERE catecumeno_id = ? AND encontro_numero = ? AND concluido = 1", (catecumeno_id, encontro_numero))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def get_progresso_catecumeno(catecumeno_id):
    """Retorna métricas consolidadas de progresso nos 40 encontros."""
    if not catecumeno_id:
        return {"total_concluidos": 0, "total_encontros": 40, "percentual": 0.0, "lista_concluidos": set()}
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT encontro_numero FROM progresso_encontros WHERE catecumeno_id = ? AND concluido = 1", (catecumeno_id,))
    concluidos = {r[0] for r in cur.fetchall()}
    conn.close()
    total_c = len(concluidos)
    pct = round((total_c / 40.0) * 100.0, 1)
    return {
        "total_concluidos": total_c,
        "total_encontros": 40,
        "percentual": pct,
        "lista_concluidos": concluidos
    }

def salvar_resposta_quiz(catecumeno_id, encontro_numero, questao_idx, opcao_escolhida, acertou):
    """Salva a resposta do catecúmeno para uma questão de quiz."""
    if not catecumeno_id:
        return
    conn = get_connection()
    cur = conn.cursor()
    data_resp = datetime.now().strftime("%d/%m/%Y %H:%M")
    cur.execute("""
    INSERT INTO respostas_quiz (catecumeno_id, encontro_numero, questao_idx, opcao_escolhida, acertou, data_resposta)
    VALUES (?, ?, ?, ?, ?, ?)
    ON CONFLICT(catecumeno_id, encontro_numero, questao_idx) DO UPDATE SET
        opcao_escolhida = excluded.opcao_escolhida,
        acertou = excluded.acertou,
        data_resposta = excluded.data_resposta
    """, (catecumeno_id, encontro_numero, questao_idx, opcao_escolhida, 1 if acertou else 0, data_resp))
    conn.commit()
    conn.close()

def get_respostas_quiz(catecumeno_id, encontro_numero):
    """Recupera todas as respostas salvas do quiz para um encontro específico."""
    if not catecumeno_id:
        return {}
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT questao_idx, opcao_escolhida, acertou, data_resposta
    FROM respostas_quiz
    WHERE catecumeno_id = ? AND encontro_numero = ?
    """, (catecumeno_id, encontro_numero))
    res = {}
    for r in cur.fetchall():
        res[r["questao_idx"]] = {
            "opcao_escolhida": r["opcao_escolhida"],
            "acertou": bool(r["acertou"]),
            "data_resposta": r["data_resposta"]
        }
    conn.close()
    return res

def get_estatisticas_quiz_catecumeno(catecumeno_id):
    """Retorna estatísticas gerais de acertos em quizzes para o catecúmeno."""
    if not catecumeno_id:
        return {"total_respondidas": 0, "total_acertos": 0, "taxa_acerto": 0.0}
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT COUNT(*) as total, SUM(acertou) as acertos
    FROM respostas_quiz
    WHERE catecumeno_id = ?
    """, (catecumeno_id,))
    row = cur.fetchone()
    conn.close()
    total = row["total"] if row and row["total"] else 0
    acertos = row["acertos"] if row and row["acertos"] else 0
    taxa = round((acertos / total) * 100.0, 1) if total > 0 else 0.0
    return {
        "total_respondidas": total,
        "total_acertos": acertos,
        "taxa_acerto": taxa
    }

def get_relatorio_engajamento_turma():
    """Retorna relatório pastoral consolidado de engajamento de todos os catecúmenos ativos."""
    conn = get_connection()
    cur = conn.cursor()
    
    # Busca catecúmenos ativos
    cur.execute("SELECT id, nome FROM catecumenos WHERE ativo = 1 ORDER BY nome ASC")
    catecumenos = [dict(r) for r in cur.fetchall()]
    
    relatorio = []
    for c in catecumenos:
        cid = c["id"]
        
        # Encontros concluídos
        cur.execute("SELECT COUNT(*) as total FROM progresso_encontros WHERE catecumeno_id = ? AND concluido = 1", (cid,))
        total_concluidos = cur.fetchone()["total"]
        pct_concluido = round((total_concluidos / 40.0) * 100.0, 1)
        
        # Quizzes
        cur.execute("SELECT COUNT(*) as total, SUM(acertou) as acertos FROM respostas_quiz WHERE catecumeno_id = ?", (cid,))
        q_row = cur.fetchone()
        q_total = q_row["total"] if q_row and q_row["total"] else 0
        q_acertos = q_row["acertos"] if q_row and q_row["acertos"] else 0
        q_taxa = round((q_acertos / q_total) * 100.0, 1) if q_total > 0 else 0.0
        
        # Anotações no Diário
        cur.execute("SELECT COUNT(*) as total FROM anotacoes_diario WHERE catecumeno_id = ?", (cid,))
        total_anotacoes = cur.fetchone()["total"]
        
        # Última atividade
        cur.execute("""
        SELECT MAX(data) as ultima FROM (
            SELECT data_conclusao as data FROM progresso_encontros WHERE catecumeno_id = ?
            UNION
            SELECT data_resposta as data FROM respostas_quiz WHERE catecumeno_id = ?
            UNION
            SELECT data_registro as data FROM anotacoes_diario WHERE catecumeno_id = ?
        )
        """, (cid, cid, cid))
        row_ult = cur.fetchone()
        ultima_ativ = row_ult["ultima"] if row_ult and row_ult["ultima"] else "Sem registro"
        
        relatorio.append({
            "id": cid,
            "nome": c["nome"],
            "encontros_concluidos": total_concluidos,
            "pct_conclusao": pct_concluido,
            "quizzes_respondidos": q_total,
            "quizzes_acertos": q_acertos,
            "taxa_acerto_quiz": q_taxa,
            "total_reflexoes": total_anotacoes,
            "ultima_atividade": ultima_ativ
        })
        
    conn.close()
    return relatorio