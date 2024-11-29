import logging
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

LOG_CHECK = create_log("checkingfiles.log", "[CHECKING]")
LOG_LOGIN = create_log("login.log", "[LOGIN]")
LOG_EMPLOYEE = create_log("employees.log", "[EMPLOYEE]")
LOG_CUSTOMER = create_log("customers.log", "[CUSTOMER]")
LOG_SUPPLIER = create_log("suppliers.log", "[SUPPLIER]")
LOG_ACQUISITION = create_log("procurement.log", "[PROCUREMENT]")
LOG_SALE = create_log("sales.log", "[SALE]")
LOG_REPORT = create_log("reports.log", "[REPORT]")
LOG_APPOINTMENT = create_log("appointments.log", "[APPOINTMENT]")


