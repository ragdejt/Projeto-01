import logging
from constants import *
# Registro de checagem de arquivos.
def create_log(file_name, log_name):
    log_file = logging.FileHandler(
        filename=file_name,
        mode="a",
        encoding="utf-8"
        
    )
    log_file.setLevel(logging.DEBUG)
    log_file.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s - %(levelname)s', datefmt="[%d/%m/%Y] - [%H:%M:%S]"))
    log = logging.getLogger(log_name)
    log.addHandler(log_file)
    log.setLevel(logging.DEBUG)
    return log

LOG_CHECK = create_log(REGISTROS / "checkingfiles.log", "[CHECKING]")
LOG_LOGIN = create_log(REGISTROS / "login.log", "[LOGIN]")
LOG_EMPLOYEE = create_log(REGISTROS / "employees.log", "[EMPLOYEE]")
LOG_CUSTOMER = create_log(REGISTROS / "customers.log", "[CUSTOMER]")
LOG_SUPPLIER = create_log(REGISTROS / "suppliers.log", "[SUPPLIER]")
LOG_ACQUISITION = create_log(REGISTROS / "procurement.log", "[PROCUREMENT]")
LOG_SALE = create_log(REGISTROS / "sales.log", "[SALE]")
LOG_REPORT = create_log(REGISTROS / "reports.log", "[REPORT]")
LOG_APPOINTMENT = create_log(REGISTROS / "appointments.log", "[APPOINTMENT]")



