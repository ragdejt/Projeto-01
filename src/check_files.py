from constants import *
from log_record import LOG_CHECK

def checking_files():
    LOG_CHECK.debug("[ARQUIVOS/DIRETÓRIOS] - [VERIFICANDO]")
    for cam in FOLDER_LIST:
        cam.mkdir(exist_ok=True)
        LOG_CHECK.info(f"[DIRETÓRIO]:{cam}")
        if cam.exists():
            LOG_CHECK.info(f"[STATUS]: [OK] - [✓]")
        else:
            LOG_CHECK.error(f"[STATUS]: [NÃO ENCONTRADO] - [✗]")
    DB_USUARIOS.touch(exist_ok=True)
    LOG_CHECK.info(f"[ARQUIVO]:{DB_USUARIOS}")
    if DB_USUARIOS.exists():
        LOG_CHECK.info(f"[STATUS]: [OK] - [✓]")
    else:
        LOG_CHECK.error(f"[STATUS]:[NÃO ENCONTRADO] - [✗]")
    LOG_CHECK.debug("[ARQUIVOS/DIRETÓRIOS] - [VERIFICADOS]")