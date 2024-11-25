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
COLUMN_LIST_EMPLOYEE = [
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

COLUMN_LIST_SUPPLIER = [
    "NOME",
    "CNPJ",
    "EMAIL",
    "TELEFONE",
    "CATEGORIA",
    "ENDEREÇO",
    "ESTADO",
    "CIDADE",
    "BANCO",
    "AGENCIA",
    "CONTA",
    "PIX",
    "RESPONSAVEL/CADASTRO"
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

STATES = [
    "Acre (AC)",
    "Alagoas (AL)",
    "Amapá (AP)",
    "Amazonas (AM)",
    "Bahia (BA)",
    "Ceará (CE)",
    "Distrito Federal (DF)",
    "Espírito Santo (ES)",
    "Goiás (GO)",
    "Maranhão (MA)",
    "Mato Grosso (MT)",
    "Mato Grosso do Sul (MS)",
    "Minas Gerais (MG)",
    "Pará (PA)",
    "Paraíba (PB)",
    "Paraná (PR)",
    "Pernambuco (PE)",
    "Piauí (PI)",
    "Rio de Janeiro (RJ)",
    "Rio Grande do Norte (RN)",
    "Rio Grande do Sul (RS)",
    "Rondônia (RO)",
    "Roraima (RR)",
    "Santa Catarina (SC)",
    "São Paulo (SP)",
    "Sergipe (SE)",
    "Tocantins (TO)"
]

BANKS = [
    "Banco do Brasil (BB) - 001",
    "Caixa Econômica Federal (Caixa) - 104",
    "Itaú Unibanco - 341",
    "Bradesco - 237",
    "Santander Brasil - 033",
    "Nubank - 260",
    "Banco Inter - 077",
    "BTG Pactual - 208",
    "C6 Bank - 336",
    "Banco Safra - 422"
]

SUPPLIER_CATEGORY = [
    "Prestador de serviço",
    "Fornecedor de produto"
]
