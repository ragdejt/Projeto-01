from pathlib import Path

# Paths.
USER_PATH = Path.home()
SCRIPT_PATH = USER_PATH / ("Projeto-01")
# Folder 1.
SCRIPT_FOLDER_1 = SCRIPT_PATH / ("01-ADMINISTRAÇÃO")
SCRIPT_FOLDER_1_1 = SCRIPT_FOLDER_1 / ("01-FUNCIONARIOS")
SCRIPT_FOLDER_1_2 = SCRIPT_FOLDER_1 / ("02-FORNECEDORES")
SCRIPT_FOLDER_1_3 = SCRIPT_FOLDER_1 / ("03-CLIENTES")
SCRIPT_FOLDER_1_4 = SCRIPT_FOLDER_1 / ("04-ESTOQUE")
# Folder 2.
SCRIPT_FOLDER_2 = SCRIPT_PATH / ("02-LOGISTICA")
SCRIPT_FOLDER_2_1 = SCRIPT_FOLDER_2 / ("01-AGENDAMENTO")
SCRIPT_FOLDER_2_2 = SCRIPT_FOLDER_2 / ("02-SEPARAÇÃO")
SCRIPT_FOLDER_2_3 = SCRIPT_FOLDER_2 / ("03-EXPEDIÇÃO")
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


