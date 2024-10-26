# Import necessary libraries.
from dataclasses import dataclass

@dataclass
class Fornecedor():
    name:str
    cnpj:int
    address:str
    city:str
    state:str
    phone:int
    email:str

ID_1000 = Fornecedor(
    name="Fornecedor-1",
    cnpj=13344677590,
    address="Rua Um, 123",
    city="São Paulo",
    state="SP",
    phone=28374687535,
    email="fornecedor1@empresa.com"
)

ID_1001 = Fornecedor(
    name="Fornecedor-2",
    cnpj=24893746522,
    address="Avenida Dois, 456",
    city="Rio de Janeiro",
    state="RJ",
    phone=21987654321,
    email="fornecedor2@empresa.com"
)

ID_1002 = Fornecedor(
    name="Fornecedor-3",
    cnpj=37659843219,
    address="Rua Três, 789",
    city="Belo Horizonte",
    state="MG",
    phone=3134876532,
    email="fornecedor3@empresa.com"
)

ID_1003 = Fornecedor(
    name="Fornecedor-4",
    cnpj=43876598124,
    address="Praça Quatro, 101",
    city="Porto Alegre",
    state="RS",
    phone=5187654321,
    email="fornecedor4@empresa.com"
)

ID_1004 = Fornecedor(
    name="Fornecedor-5",
    cnpj=56983472109,
    address="Rua Cinco, 202",
    city="Curitiba",
    state="PR",
    phone=41987654321,
    email="fornecedor5@empresa.com"
)

ID_1005 = Fornecedor(
    name="Fornecedor-6",
    cnpj=61029384756,
    address="Avenida Seis, 303",
    city="Salvador",
    state="BA",
    phone=7187654321,
    email="fornecedor6@empresa.com"
)

ID_1006 = Fornecedor(
    name="Fornecedor-7",
    cnpj=72384910567,
    address="Rua Sete, 404",
    city="Recife",
    state="PE",
    phone=8187654321,
    email="fornecedor7@empresa.com"
)

ID_1007 = Fornecedor(
    name="Fornecedor-8",
    cnpj=83471029348,
    address="Rua Oito, 505",
    city="Manaus",
    state="AM",
    phone=92987654321,
    email="fornecedor8@empresa.com"
)

ID_1008 = Fornecedor(
    name="Fornecedor-9",
    cnpj=94562038479,
    address="Avenida Nove, 606, Brasília, DF",
    city="",
    state="",
    phone=6187654321,
    email="fornecedor9@empresa.com"
)

ID_1009 = Fornecedor(
    name="Fornecedor-10",
    cnpj=10938475629,
    address="Rua Dez, 707",
    city="Fortaleza",
    state="CE",
    phone=8587654321,
    email="fornecedor10@empresa.com"
)
