from pathlib import Path

# Paths.
USER_PATH = Path.home()
SCRIPT_PATH = USER_PATH / ("Projeto-01")
# Folder 1.
AGENDAMENTOS = SCRIPT_PATH / ("01-AGENDAMENTOS")
COMPRAS = SCRIPT_PATH / ("02-COMPRAS")
CLIENTES = SCRIPT_PATH / ("03-CLIENTES")
FINANCEIRO = SCRIPT_PATH / ("04-FINANCEIRO")
FORNECEDORES = SCRIPT_PATH / ("05-FORNECEDORES")
FUNCIONARIOS = SCRIPT_PATH / ("06-FUNCIONARIOS")
ESTOQUE = SCRIPT_PATH / ("07-ESTOQUE")
REGISTROS = SCRIPT_PATH / ("08-REGISTROS")
RECEBIMENTOS = SCRIPT_PATH / ("09-RECEBIMENTO")
RELATORIOS = SCRIPT_PATH / ("10-RELATORIOS")
SEPARACAO = SCRIPT_PATH / ("11-SEPARAÇÃO")
EXPEDICAO = SCRIPT_PATH / ("12-EXPEDIÇÃO")
VENDAS = SCRIPT_PATH / ("13-VENDAS")

FOLDER_LIST = [
    AGENDAMENTOS,
    COMPRAS,
    CLIENTES,
    FINANCEIRO,
    FORNECEDORES,
    FUNCIONARIOS,
    ESTOQUE,
    REGISTROS,
    RECEBIMENTOS,
    RELATORIOS,
    SEPARACAO,
    EXPEDICAO,
    VENDAS    
]

# Data bases.
DB_USUARIOS = SCRIPT_PATH / ("USUARIOS.db")
DB_FUNCIONARIOS = SCRIPT_PATH / ("FUNCIONARIOS.db")
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
    "RESPONSAVEL/AGENDAMENTOS",
    "DATA/AGENDAMENTOS"
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

