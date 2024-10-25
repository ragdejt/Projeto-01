import sqlite3
from ..util.Paths import DB__EMPLOYEES, DB_SUPPLIERS
def connect_db_suppliers():
    connect = sqlite3.connect(DB_SUPPLIERS)
    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS FORNECEDORES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL UNIQUE,
        CNPJ INTEGER NOT NULL UNIQUE,
        ENDEREÇO TEXT NOT NULL,
        CIDADE TEXT NOT NULL,
        ESTADO TEXT NOT NULL,
        TELEFONE INTEGER NOT NULL,
        EMAIL TEXT NOT NULL
    )"""
    )
    connect.commit()
    connect.close()

def connect_db_employees():
    connect = sqlite3.connect(DB__EMPLOYEES)
    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS FUNCIONARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL UNIQUE,
        CPF INTEGER NOT NULL UNIQUE,
        ENDEREÇO TEXT NOT NULL,
        CIDADE TEXT NOT NULL,
        ESTADO TEXT NOT NULL,
        TELEFONE INTEGER NOT NULL,
        EMAIL TEXT NOT NULL
    )"""
    )
    connect.commit()
    connect.close()

connect_db_suppliers()
connect_db_employees()
