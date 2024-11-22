# Import necessary libraries.
from constants import *
from login import login


# Main.
def main():
    SCRIPT_PATH.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2.mkdir(exist_ok=True)
    SCRIPT_FOLDER_3.mkdir(exist_ok=True)
    SCRIPT_FOLDER_4.mkdir(exist_ok=True)
    SCRIPT_FOLDER_5.mkdir(exist_ok=True)
    SCRIPT_FOLDER_6.mkdir(exist_ok=True)
    SCRIPT_FOLDER_7.mkdir(exist_ok=True)
    SCRIPT_FOLDER_8.mkdir(exist_ok=True)
    SCRIPT_FOLDER_9.mkdir(exist_ok=True)
    SCRIPT_FOLDER_10.mkdir(exist_ok=True)
    SCRIPT_FOLDER_11.mkdir(exist_ok=True)
    SCRIPT_FOLDER_12.mkdir(exist_ok=True)
    DB_USUARIOS.touch(exist_ok=True)

    login()
if __name__ == "__main__":
    main()