from pathlib import Path

# Paths.
USER_PATH = Path.home()
SCRIPT_PATH = USER_PATH / ("Projeto-01")
# Folder 1.
SCRIPT_FOLDER_1 = SCRIPT_PATH / ("01-FUNCIONARIOS")
SCRIPT_FOLDER_2 = SCRIPT_PATH / ("02-FORNECEDORES")
SCRIPT_FOLDER_3 = SCRIPT_PATH / ("03-CLIENTES")
SCRIPT_FOLDER_4 = SCRIPT_PATH / ("04-ESTOQUE")
SCRIPT_FOLDER_5 = SCRIPT_PATH / ("05-AGENDAMENTO")
SCRIPT_FOLDER_6 = SCRIPT_PATH / ("06-SEPARAÇÃO")
SCRIPT_FOLDER_7 = SCRIPT_PATH / ("07-EXPEDIÇÃO")
SCRIPT_FOLDER_8 = SCRIPT_PATH / ("08-COMPRAS")
SCRIPT_FOLDER_9 = SCRIPT_PATH / ("09-VENDAS")
SCRIPT_FOLDER_10 = SCRIPT_PATH / ("10-FINANCEIRO")
SCRIPT_FOLDER_11 = SCRIPT_PATH / ("11-RELATORIOS")
SCRIPT_FOLDER_12 = SCRIPT_PATH / ("12-REGISTROS")

FOLDER_LIST = [
    SCRIPT_FOLDER_1,
    SCRIPT_FOLDER_2,
    SCRIPT_FOLDER_3,
    SCRIPT_FOLDER_4,
    SCRIPT_FOLDER_5,
    SCRIPT_FOLDER_6,
    SCRIPT_FOLDER_7,
    SCRIPT_FOLDER_8,
    SCRIPT_FOLDER_9,
    SCRIPT_FOLDER_10,
    SCRIPT_FOLDER_11,
    SCRIPT_FOLDER_12
]

# Data bases.
DB_USUARIOS = SCRIPT_PATH / ("USUARIOS.db")
#
SPREADSHEET_NAME = "%Y%m%d%H%M%S"
#
COLUMN_LIST0 = [
    "NOME",
    "DATA/NASCIMENTO",
    "SEXO",
    "CARGO",
    "DATA DE ADMISSÃO",
    "SALARIO",
    "CTPS",
    "RG",
    "CPF",
    "ESTADO/CIVIL",
    "CONTRATO",
    "ESCOLARIDADE",
    "ENDEREÇO",
    "CIDADE",
    "ESTADO",
    "TELEFONE/CELULAR",
    "EMAIL"
]

COLUMN_LIST_APPOINTMENT = [
    "CLIENTE",
    "PRODUTO",
    "MATERIAL",
    "ALTURA",
    "LARGURA",
    "COMPRIMENTO",
    "QUANTIDADE",
    "RESPONSAVEL/AGENDAMENTO",
    "DATA/AGENDAMENTO"
]

MASC_FEM = ["Masculino", "Feminino"]

POSITION = [
    "Auxiliar Administrativo",
    "Gerente Administrativo",
    "Vendedor Jr",
    "Vendedor Senior",
    "Vendedor Pleno",
    "Gerente Comercial",
    "Auxiliar logistico",
    "Conferente",
    "Gerente Logistico"
]
STATUS = ["Solteiro", "Casado"]

CONTRACT = ["CLT", "PJ"]

EDUCATION = [
    "Ensino Fundamental Completo",
    "Ensino Fundamental Incompleto",
    "Ensino Médio Completo",
    "Ensino Médio Incompleto",
    "Ensino Superior Completo",
    "Ensino Superior Incompleto"
]


