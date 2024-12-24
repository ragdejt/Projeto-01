import sqlite3
import logging
from pathlib import Path
def create_db(db:Path, table_name:str, log:logging, coluna:list[str]):
    def add_columns():
        connect = sqlite3.connect(db)
        cursor = connect.cursor()
        for i in coluna:
            try:
                cursor.execute(f"ALTER TABLE ? ADD COLUMN ? TEXT;", (table_name, i))
            except sqlite3.OperationalError:
                pass
            else:
                log.debug(f"[ADICIONAR] - [COLUNA]: {i} - [✓] - [BANCO DE DADOS]: {db}")
        connect.commit()
        connect.close()
    try:
        connect = sqlite3.connect(db)
        cursor = connect.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS ? (ID INTEGER PRIMARY KEY AUTOINCREMENT);", (table_name))
        connect.commit()
    except sqlite3.OperationalError:
        pass
    else:
        log.debug(f"[CRIAR] - [TABELA]: {table_name} - [✓] - [BANCO DE DADOS]: {db}")
    finally:
        connect.close()
        add_columns()

def create_log(file_name, log_name):
    log_file = logging.FileHandler(
        filename=file_name,
        mode="a",
        encoding="utf-8"
        
    )
    log_file.setLevel(logging.DEBUG)
    log_file.setFormatter(logging.Formatter('%(asctime)s - %(message)s - %(levelname)s', datefmt="[%d/%m/%Y] - [%H:%M:%S]"))
    log = logging.getLogger(log_name)
    log.addHandler(log_file)
    log.setLevel(logging.DEBUG)
    return log

LOG_CHECK = create_log("CHECKFILES.log", "CHECK")
LOG_CLIENTES = create_log("CLIENTES.log", "CLIENTE")
LOG_FORNECEDORES = create_log("FORNECEDORES.log", "FORNECEDOR")
LOG_FINANCEIRO = create_log("FINANCEIRO.log", "FINANCEIRO")
LOG_COMPRAS = create_log("COMPRAS.log", "COMPRA")
LOG_VENDAS = create_log("VENDAS.log", "VENDA")
LOG_RELATORIOS = create_log("RELATORIOS.log", "RELATORIO")
LOG_AGENDAMENTO = create_log("AGENDAMENTOS.log", "AGENDAMENTO")
LOG_USUARIOS = create_log("USUARIOS.log", "USUARIO")
LOG_FUNCIONARIOS = create_log("FUNCIONARIOS.log", "FUNCIONARIO")
LOG_ESTOQUE = create_log("ESTOQUE.log", "ESTOQUE")
LOG_RECEBIMENTOS = create_log("RECEBIMENTOS.log", "RECEBIMENTO")
LOG_SEPARACAO = create_log("SEPARACAO.log", "SEPARACAO")
LOG_EXPEDICAO = create_log("EXPEDICAO.log", "EXPEDICAO")