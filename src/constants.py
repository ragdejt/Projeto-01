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
# Lista de pastas.
FOLDER_LIST = [
    SCRIPT_PATH,
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
# Banco de dados - [AGENDAMENTOS]
DB_AGENDAMENTOS = REGISTROS / ("AGENDAMENTOS.db")
COLUMN_LIST_AGENDAMENTOS = [
    "CLIENTE",
    "PRODUTO",
    "MOLDE",
    "ALTURA",
    "LARGURA",
    "COMPRIMENTO",
    "QUANTIDADE",
    "RESPONSAVEL_AGENDAMENTOS",
    "DATA_AGENDAMENTOS"
]
# Banco de dados - [COMPRAS]
DB_COMPRAS = REGISTROS / ("COMPRAS.db")
COLUMN_LIST_COMPRAS = [""]
# Banco de dados - [CLIENTES]
DB_CLIENTES = REGISTROS / ("CLIENTES.db")
COLUMN_LIST_CLIENTES = [""]
# Banco de dados - [FINANCEIRO]
DB_FINANCEIRO = REGISTROS / ("FINANCEIRO.db")
COLUMN_LIST_FINANCEIRO = [""]
# Banco de dados - [FORNECEDORES]
DB_FORNECEDORES = REGISTROS / ("FORNECEDORES.DB")
COLUMN_LIST_FORNECEDORES = [
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
    "RESPONSAVEL_CADASTRO"
]
# Banco de dados - [FUNCIONARIOS]
DB_FUNCIONARIOS = REGISTROS / ("FUNCIONARIOS.db")
COLUMN_LIST_FUNCIONARIOS = [
    "NOME",
    "NASCIMENTO",
    "SEXO",
    "CARGO",
    "ADMISSÃO",
    "SALARIO",
    "CTPS",
    "RG",
    "CPF",
    "ESTADO_CIVIL",
    "CONTRATO",
    "ESCOLARIDADE",
    "ENDEREÇO",
    "CIDADE",
    "ESTADO",
    "TELEFONE",
    "EMAIL"
]
# Banco de dados - [ESTOQUE]
DB_ESTOQUE = REGISTROS / ("ESTOQUE.db")
COLUMN_LIST_ESTOQUE = [""]
# Banco de dados - [RECEBIMENTOS]
DB_RECEBIMENTOS = REGISTROS / ("RECEBIMENTOS.db")
COLUMN_LIST_RECEBIMENTOS = [""]
# Banco de dados - [RELATORIOS]
DB_RELATORIOS = REGISTROS / ("RELATORIOS.db")
COLUMN_LIST_RELATORIOS = [""]
# Banco de dados - [SEPARAÇÃO]
DB_SEPARACAO = REGISTROS / ("SEPARACAO.db")
COLUMN_LIST_SEPARACAO = [""]
# Banco de dados - [EXPEDIÇÃO]
DB_EXPEDICAO = REGISTROS / ("EXPEDICAO.db")
COLUMN_LIST_EXPEDICAO = [""]
# Banco de dados - [VENDAS]
DB_VENDAS = REGISTROS / ("VENDAS.db")
COLUMN_LIST_VENDAS = [""]
# Banco de dados - [USUARIOS]
DB_USUARIOS = REGISTROS / ("USUARIOS.db")
COLUMN_LIST_USUARIOS = [
    "USERNAME",
    "PASSWORD"
]
#
SPREADSHEET_NAME = "%Y%m%d%H%M%S"
#
MASC_FEM = ["Masculino", "Feminino"]
#
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

