# Import necessary libraries.
import sqlite3
from util.Paths import SCRIPT_PATH, SCRIPT_FOLDER_1, SCRIPT_FOLDER_2, MONTHS, DB__EMPLOYEES, DB_SUPPLIERS


# Main.
def main():
    SCRIPT_PATH.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2.mkdir(exist_ok=True)
    for month in MONTHS:
        cam = SCRIPT_FOLDER_2 / month
        cam.mkdir(exist_ok=True)

if __name__ == "__main__":
    main()