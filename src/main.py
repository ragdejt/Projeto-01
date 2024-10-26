# Import necessary libraries.
from util.Paths import *
from app.Database import connect_db
from app.Constants import DB__EMPLOYEES, DB_SUPPLIERS
# Main.
def main():
    SCRIPT_PATH.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1_1.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1_2.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2_1.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2_2.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2_3.mkdir(exist_ok=True)
    
    for month in MONTHS:
        cam = SCRIPT_FOLDER_2_1 / month
        cam.mkdir(exist_ok=True)
    for month in MONTHS:
        cam1 = SCRIPT_FOLDER_2_2 / month
        cam1.mkdir(exist_ok=True)

    connect_db(db_path=DB__EMPLOYEES, db_name="Funcionarios")
    connect_db(db_path=DB_SUPPLIERS, db_name="Fornecedores")
if __name__ == "__main__":
    main()