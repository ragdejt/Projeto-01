# Import necessary libraries.
import logging
from login import login
from constants import *


def checking_files():
    logging.debug("[VERIFICANDO ARQUIVOS/DIRETÓRIOS NECESSARIOS]")
    for cam in FOLDER_LIST:
        cam.mkdir(exist_ok=True)
        logging.info(f"[DIRETÓRIO]:{cam}")
        if cam.exists():
            logging.info(f"[STATUS]: [OK]")
        else:
            logging.error(f"[STATUS]: [NÃO ENCONTRADO]")
    DB_USUARIOS.touch(exist_ok=True)
    logging.debug(f"[ARQUIVO]:{DB_USUARIOS}")
    if DB_USUARIOS.exists():
        logging.info(f"[STATUS]:[OK]")
    else:
        logging.error(f"[STATUS]:[NÃO ENCONTRADO]")

# Main.
def main():
    checking_files()
    login()
if __name__ == "__main__":
    main()