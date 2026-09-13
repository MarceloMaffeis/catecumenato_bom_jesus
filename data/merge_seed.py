# -*- coding: utf-8 -*-
"""
Mescla os 40 encontros e define orações e dados iniciais
"""
import json
import os

base_dir = r"C:\Users\marce\.gemini\antigravity\scratch\catecumenato_bom_jesus\data"

all_encontros = []
for i in range(1, 6):
    part_path = os.path.join(base_dir, f"encontros_part{i}.json")
    with open(part_path, "r", encoding="utf-8") as f:
        part_data = json.load(f)
        all_encontros.extend(part_data)

print(f"Total encounters merged: {len(all_encontros)}")

ORACOES = [
    {
        "titulo": "Oração da Paz (Oração de São Francisco)",
        "categoria": "Franciscanas",
        "origem_autor": "Tradição Franciscana",
        "texto": """Senhor, fazei-me instrumento de vossa paz.
Onde houver ódio, que eu leve o amor;
Onde houver ofensa, que eu leve o perdão;
Onde houver discórdia, que eu leve a união;
Onde houver dúvida, que eu leve a fé;
Onde houver erro, que eu leve a verdade;
Onde houver desespero, que eu leve a esperança;
Onde houver tristeza, que eu leve a alegria;
Onde houver trevas, que eu leve a luz.

Ó Mestre, fazei que eu procure mais:
Consolar, que ser consolado;
Compreender, que ser compreendido;
Amar, que ser amado.
Pois é dando que se recebe,
É perdoando que se é perdoado,
E é morrendo que se vive para a vida eterna. Amém."""
    },
    {
        "titulo": "Oração diante do Crucifixo de São Damião",
        "categoria": "Franciscanas",
        "origem_autor": "São Francisco de Assis (1206)",
        "texto": """Altíssimo, glorioso Deus,
iluminai as trevas do meu coração.
Dai-me uma fé reta,
esperança certa
e caridade perfeita,
bom senso e discernimento, ó Senhor,
para que eu cumpra o vosso santo
e verídico mandamento. Amém."""
    },
    {
        "titulo": "Cântico das Criaturas (Cântico do Irmão Sol)",
        "categoria": "Franciscanas",
        "origem_autor": "São Francisco de Assis (1225)",
        "texto": """Altíssimo, onipotente, bom Senhor,
Teus são os louvores, a glória, a honra e toda a bênção.
A Ti somente, Altíssimo, eles convêm,
E homem algum é digno de Te nomear.

Louvado sejas, meu Senhor, com todas as Tuas criaturas,
Especialmente o senhor irmão Sol,
Que clareia o dia e por ele nos alumias.
E ele é belo e radiante com grande esplendor:
De Ti, Altíssimo, é a imagem.

Louvado sejas, meu Senhor, pela irmã Lua e as Estrelas:
No céu as formaste claras, preciosas e belas.
Louvado sejas, meu Senhor, pelo irmão Vento,
Pelo ar, nublado ou claro, e todo o tempo,
Pelo qual às Tuas criaturas dás sustento.

Louvado sejas, meu Senhor, pela irmã Água,
Que é muito útil e humilde e preciosa e casta.
Louvado sejas, meu Senhor, pelo irmão Fogo,
Pelo qual iluminas a noite:
E ele é belo e jucundo e vigoroso e forte.

Louvado sejas, meu Senhor, por nossa irmã a mãe Terra,
Que nos sustenta e governa,
E produz diversos frutos com flores coloridas e ervas.

Louvado sejas, meu Senhor, por aqueles que perdoam por Teu amor
E suportam enfermidades e tribulações.
Bem-aventurados aqueles que as suportarem em paz,
Pois por Ti, Altíssimo, serão coroados.

Louvado sejas, meu Senhor, por nossa irmã a Morte corporal,
Da qual homem algum vivente pode escapar.
Ai daqueles que morrerem em pecado mortal!
Bem-aventurados aqueles que ela encontrar na Tua santíssima vontade,
Pois a segunda morte não lhes fará mal.

Louvai e bendizei a meu Senhor,
E dai-Lhe graças e servi-O com grande humildade. Amém."""
    },
    {
        "titulo": "Bênção a Frei Leão",
        "categoria": "Franciscanas",
        "origem_autor": "São Francisco de Assis (Monte Alverne, 1224)",
        "texto": """O Senhor te abençoe e te guarde!
O Senhor te mostre a sua face e tenha compaixão de ti!
O Senhor volva para ti o seu olhar e te dê a paz!
O Senhor te abençoe, Frei Leão! (Sinal do Tau ☩)"""
    },
    {
        "titulo": "Saudação à Bem-Aventurada Virgem Maria",
        "categoria": "Franciscanas",
        "origem_autor": "São Francisco de Assis",
        "texto": """Salve, ó Senhora Santa, Rainha santíssima, Mãe de Deus, ó Maria,
que sois Virgem feita Igreja,
eleita pelo santíssimo Pai do Céu,
a quem consagrou com seu santíssimo e amado Filho
e o Espírito Santo Paráclito!
Em Vós residiu e reside toda a plenitude da graça e todo o bem!
Salve, ó palácio de Deus!
Salve, ó tabernáculo de Deus!
Salve, ó casa de Deus!
Salve, ó vestimenta de Deus!
Salve, ó serva de Deus!
Salve, ó Mãe de Deus!
E salve vós todas, santas virtudes,
que pela graça e iluminação do Espírito Santo
sois derramadas nos corações dos fiéis,
para que de infiéis os façais fiéis a Deus! Amém."""
    },
    {
        "titulo": "Oração do Catequista antes do Encontro",
        "categoria": "Litúrgicas",
        "origem_autor": "Pastoral Catequética",
        "texto": """Senhor Jesus Cristo, Divino Mestre,
Vós que chamastes os discípulos para estarem convosco e os enviastes a pregar,
olhai para mim, vosso servo humilde, chamado a ministrar a catequese aos adultos de nossa paróquia.
Despojai-me de toda vaidade e auto-suficiência;
colocai em meus lábios a Vossa divina Palavra e inflamai meu coração com a Vossa santa caridade.
Que através do meu testemunho e do meu amor respeitoso,
estes catecúmenos encontrem verdadeiramente a Vós, Caminho, Verdade e Vida.
Que a Vossa graça opere o que minhas pobres palavras não alcançam.
Santa Maria, Mãe e primeira catequista, rogai por nós.
São Francisco e Santa Clara de Assis, rogai por nós. Amém."""
    },
    {
        "titulo": "Oração a São Miguel Arcanjo",
        "categoria": "Tradicionais Católicas",
        "origem_autor": "Papa Leão XIII (1886)",
        "texto": """São Miguel Arcanjo, defendei-nos no combate;
sede o nosso refúgio contra as maldades e ciladas do demônio.
Ordene-lhe Deus, instantemente o pedimos,
e vós, príncipe da milícia celeste,
pelo divino poder, precipitai no inferno a Satanás
e a todos os espíritos malignos
que andam pelo mundo para perder as almas. Amém."""
    },
    {
        "titulo": "Ato de Contrição Perfeita",
        "categoria": "Tradicionais Católicas",
        "origem_autor": "Liturgia Romana",
        "texto": """Senhor meu Jesus Cristo, Deus e Homem verdadeiro,
Criador e Redentor meu,
por serdes Vós quem sois, sumamente bom e digno de ser amado sobre todas as coisas,
e porque Vos amo e estimo,
pesa-me, Senhor, de todo o meu coração de Vos ter ofendido;
pesa-me também de ter perdido o Céu e merecido o Inferno;
mas proponho firmemente, auxiliado com os auxílios da Vossa divina graça,
fazer penitência, confessar-me, nunca mais pecar
e fugir de todas as ocasiões próximas de Vos ofender. Amém."""
    },
    {
        "titulo": "Símbolo dos Apóstolos (Credo Breve)",
        "categoria": "Tradicionais Católicas",
        "origem_autor": "Tradição Apostólica Romana",
        "texto": """Creio em Deus Pai todo-poderoso,
Criador do céu e da terra.
E em Jesus Cristo, seu único Filho, nosso Senhor,
que foi concebido pelo poder do Espírito Santo,
nasceu da Virgem Maria,
padeceu sob Pôncio Pilatos,
foi crucificado, morto e sepultado;
desceu à mansão dos mortos;
ressuscitou ao terceiro dia;
subiu aos céus,
está sentado à direita de Deus Pai todo-poderoso,
donde há de vir a julgar os vivos e os mortos.
Creio no Espírito Santo,
na santa Igreja Católica,
na comunhão dos santos,
na remissão dos pecados,
na ressurreição da carne,
na vida eterna. Amém."""
    }
]

CATECUMENOS_INICIAIS = [
    {
        "nome": "Carlos Eduardo Ribeiro",
        "email": "carlos.ribeiro@email.com",
        "telefone": "(15) 99781-4421",
        "data_nascimento": "1988-05-14",
        "estado_civil": "Casado",
        "batizado": 1,
        "primeira_eucaristia": 0,
        "crismado": 0,
        "padrinho_madrinha": "Marcelo Henrique da Silva",
        "observacoes": "Casado na Igreja, busca completar os sacramentos da Eucaristia e Crisma. Muito participativo nas partilhas.",
        "ativo": 1
    },
    {
        "nome": "Mariana Souza Toledo",
        "email": "mariana.toledo@email.com",
        "telefone": "(15) 99124-8833",
        "data_nascimento": "1995-11-20",
        "estado_civil": "Solteira",
        "batizado": 0,
        "primeira_eucaristia": 0,
        "crismado": 0,
        "padrinho_madrinha": "Teresa Cristina Toledo",
        "observacoes": "Catecúmena não-batizada. Fará a iniciação cristã completa (Batismo, Crisma e Eucaristia) na Vigília Pascal.",
        "ativo": 1
    },
    {
        "nome": "Antonio Marcos Ferreira",
        "email": "antonio.ferreira@email.com",
        "telefone": "(15) 98112-3004",
        "data_nascimento": "1976-02-09",
        "estado_civil": "Casado",
        "batizado": 1,
        "primeira_eucaristia": 1,
        "crismado": 0,
        "padrinho_madrinha": "Francisco de Assis Lima",
        "observacoes": "Fez a 1ª comunhão na infância em Minas Gerais, agora busca a confirmação (Crisma). Tem grande interesse na espiritualidade franciscana.",
        "ativo": 1
    },
    {
        "nome": "Beatriz Alcantara Mendes",
        "email": "beatriz.mendes@email.com",
        "telefone": "(15) 99655-7090",
        "data_nascimento": "2001-08-30",
        "estado_civil": "Solteira",
        "batizado": 0,
        "primeira_eucaristia": 0,
        "crismado": 0,
        "padrinho_madrinha": "Helena Mendes Silva",
        "observacoes": "Jovem adulta (25 anos), estudante universitária. Busca o encontro pessoal com Cristo.",
        "ativo": 1
    },
    {
        "nome": "Roberto Camargo de Oliveira",
        "email": "roberto.camargo@email.com",
        "telefone": "(15) 98843-1982",
        "data_nascimento": "1969-07-12",
        "estado_civil": "Viúvo",
        "batizado": 1,
        "primeira_eucaristia": 0,
        "crismado": 0,
        "padrinho_madrinha": "Paulo Sérgio de Oliveira",
        "observacoes": "Retornando à prática da fé católica após muitos anos afastado. Deseja confessar e comungar.",
        "ativo": 1
    }
]

catalog = {
    "encontros": all_encontros,
    "oracoes": ORACOES,
    "catecumenos_iniciais": CATECUMENOS_INICIAIS
}

output_path = os.path.join(base_dir, "seed_completo.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Catalog successfully compiled into {output_path} with {len(all_encontros)} encounters and {len(ORACOES)} prayers!")