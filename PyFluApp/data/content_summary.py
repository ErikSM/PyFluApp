import io


book_one = (
    ("1", "O modelo de dados do Python"),
    ("1.2", "Um baralho pythônico"),
    ("1.3", "Como os métodos especiais são utilizados"),
    ("1.4", "Visão geral dos métodos especiais"),
    ("1.5", "Por que len não é um método?"),

    ("2", "Uma coleção de sequências"),
    ("2.2", "Uma visão geral das sequências embutidas"),
    ("2.3", "Compreensões de listas e expressões geradoras"),
    ('2.4', "Tuplas não são apenas listas imutáveis"),
    ("2.5", "Desempacotando sequências e iteráveis"),
    ("2.6", "Pattern matching com sequências"),
    ("2.7", "Fatiamento"),
    ("2.8", "Usando + e * com sequências"),
    ("2.9", "list.sort versus a função embutida sorted"),
    ("2.10", "Quando uma lista não é a resposta"),

    ("3", "Dicionários e conjuntos"),
    ("3.2", "A sintaxe moderna dos dicts"),
    ("3.3", "Pattern matching com mapeamentos"),
    ("3.4", "A API padrão dos tipos de mapeamentos"),
    ("3.5", "Tratamento automático de chaves ausentes"),
    ("3.6", "Variações de dict"),
    ("3.7", "Mapeamentos imutáveis"),
    ("3.8", "Views de dicionários"),
    ("3.9", "Consequências práticas da forma como dict funciona"),
    ("3.10", "Teoria dos conjuntos"),
    ("3.11", "Consequências práticas da forma de funcionamento dos conjuntos"),
    ("3.12", "Operações de conjuntos em views de dict"),

    ("4", "Texto em Unicode versus Bytes"),
    ("4.2", "Questões de caracteres"),
    ("4.3", "Os fundamentos do byte"),
    ("4.4", "Codificadores/Decodificadores básicos"),
    ("4.5", "Entendendo os problemas de codificação/decodificação"),
    ("4.6", "Processando arquivos de texto"),
    ("4.7", "Normalizando o Unicode para comparações confiáveis"),
    ("4.8", "Ordenando texto Unicode"),
    ("4.9", "O banco de dados do Unicode"),
    ("4.10", "APIs de modo dual para str e bytes"),

    ("5", "Fábricas de classes de dados"),
    ("5.2", "Visão geral das fábricas de classes de dados"),
    ("5.3", "Tuplas nomeadas clássicas"),
    ("5.4", "Tuplas nomeadas com tipo"),
    ("5.5", "Introdução às dicas de tipo"),
    ("5.6", "Mais detalhes sobre @dataclass"),
    ("5.7", "A classe de dados como cheiro no código"),
    ("5.8", "Pattern Matching com instâncias de classes"),

    ("6", "Referências, mutabilidade, e memória"),
    ("6.2", "Variáveis não são caixas"),
    ("6.3", "Identidade, igualdade e apelidos"),
    ("6.4", "A princípio, cópias são rasas"),
    ("6.5", "Parâmetros de função como referências"),
    ("6.6", "del e coleta de lixo"),
    ("6.7", "Peças que Python prega com imutáveis")
)

chapters_of_book_one = {
    book_one[0][1]: book_one[0:5], book_one[5][1]: book_one[5:15], book_one[15][1]: book_one[15:27],
    book_one[27][1]: book_one[27:36], book_one[36][1]: book_one[36:43], book_one[43][1]: book_one[43:50]
}

python_books = {
    'I- Estruturas de dados': chapters_of_book_one,
    'II- Funções como objetos': None,
    'III- Classes e protocolos': None,
    'IV- Controle de fluxo': None,
    'V- Metaprogramação': None
}

def open_file(file_name, directory='data/chapters_texts'):
    file = io.open(f'{directory}/{file_name}.txt', 'r', encoding='utf8')
    text = file.read()
    file.close()

    return text
