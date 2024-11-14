# Import necessary libraries.
from constants import *
from app.new_employee import app_new_employee
from app.new_appointment import app_new_appointment
# Main.
def main():
    SCRIPT_PATH.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1_1.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1_2.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1_3.mkdir(exist_ok=True)
    SCRIPT_FOLDER_1_4.mkdir(exist_ok=True)

    SCRIPT_FOLDER_2.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2_1.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2_2.mkdir(exist_ok=True)
    SCRIPT_FOLDER_2_3.mkdir(exist_ok=True)

    app_new_employee()
if __name__ == "__main__":
    main()