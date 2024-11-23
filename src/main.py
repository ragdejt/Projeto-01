# Import necessary libraries.
import logging
from login import login
from constants import *

log_file01 = logging.FileHandler(filename='checking_files.log', mode='a', encoding='utf-8')
log_file01.setLevel(logging.DEBUG)
log_file01.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))

log_check = logging.getLogger("[VERIFICANDO]")
log_check.addHandler(log_file01)
log_check.setLevel(logging.DEBUG)

def checking_files():
    log_check.debug("[VERIFICANDO ARQUIVOS/DIRETÓRIOS NECESSARIOS]")
    for cam in FOLDER_LIST:
        cam.mkdir(exist_ok=True)
        log_check.info(f"[DIRETÓRIO]:{cam}")
        if cam.exists():
            log_check.info(f"[STATUS]: [OK]")
        else:
            log_check.error(f"[STATUS]: [NÃO ENCONTRADO]")
    DB_USUARIOS.touch(exist_ok=True)
    log_check.info(f"[ARQUIVO]:{DB_USUARIOS}")
    if DB_USUARIOS.exists():
        log_check.info(f"[STATUS]:[OK]")
    else:
        log_check.error(f"[STATUS]:[NÃO ENCONTRADO]")

# Main.
def main():
    checking_files()
    login()
if __name__ == "__main__":
    main()