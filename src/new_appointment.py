import time
import pandas
from constants import SCRIPT_FOLDER_2_1, COLUMN_LIST_APPOINTMENT, SPREADSHEET_NAME
from functions import create_app, create_button, create_entry, create_frame, popup


def app_new_appointment():
    def button_new_appointment():
        new_data = {
            "CLIENTE":[cliente.get()],
            "PRODUTO":[produto.get()],
            "MATERIAL":[material.get()],
            "ALTURA":[altura.get()],
            "LARGURA":[largura.get()],
            "COMPRIMENTO":[comprimento.get()],
            "QUANTIDADE":[quantidade.get()],
            "RESPONSAVEL/AGENDAMENTO":[resp_agendamento.get()],
            "DATA/AGENDAMENTO":[data_agendamento.get()],
        }
        spreadsheet_name = time.strftime(SPREADSHEET_NAME)
        with pandas.ExcelWriter(path=SCRIPT_FOLDER_2_1 / (spreadsheet_name + ".xlsx"), engine="xlsxwriter") as writer:
            pandas.DataFrame(columns=COLUMN_LIST_APPOINTMENT, data=new_data).to_excel(writer, sheet_name=spreadsheet_name, index=False)
        
        cliente.delete(0, "end")
        produto.delete(0, "end")
        material.delete(0, "end")
        altura.delete(0, "end")
        largura.delete(0, "end")
        comprimento.delete(0, "end")
        quantidade.delete(0, "end")
        resp_agendamento.delete(0, "end")
        data_agendamento.delete(0, "end")

        popup()

    app = create_app("480x480")
    app.grid_columnconfigure(0, weight=1)
    
    frame0 = create_frame(app, 0, 0, "nsew")
    frame0.grid_columnconfigure(0, weight=1)
    frame0.grid_rowconfigure(0, weight=1)
 
    cliente = create_entry(frame0, "Cliente")
    produto = create_entry(frame0, "Produto")
    material = create_entry(frame0, "Material")
    altura = create_entry(frame0, "Altura")
    largura = create_entry(frame0, "Largura")
    comprimento = create_entry(frame0, "Comprimento")
    quantidade = create_entry(frame0, "Quantidade")
    resp_agendamento = create_entry(frame0, "Responsavel/Agendamento")
    data_agendamento = create_entry(frame0, "Data/Agendamento")

    frame1 = create_frame(app, 0, 8, "nsew")
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_rowconfigure(1, weight=1)
    create_button(frame1, "Cadastrar", button_new_appointment)

    app.mainloop()