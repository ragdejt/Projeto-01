import sqlite3
from pathlib import Path
def connect_db(db_path:Path, db_name:str):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {db_name} (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL UNIQUE,
        CPF_CNPJ INTEGER NOT NULL UNIQUE,
        ENDEREÇO TEXT NOT NULL,
        CIDADE TEXT NOT NULL,
        ESTADO TEXT NOT NULL,
        TELEFONE INTEGER NOT NULL,
        EMAIL TEXT NOT NULL
    )"""
    )
    connect.commit()
    connect.close()
