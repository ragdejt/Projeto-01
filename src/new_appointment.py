import time
import pandas
from tkinter import messagebox
from constants import *
from app_functions import *
from log_record import LOG_APPOINTMENT

def new_appointment():
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

        with pandas.ExcelWriter(path=AGENDAMENTOS / f"{spreadsheet_name}.xlsx", engine="xlsxwriter") as writer:
            pandas.DataFrame(columns=COLUMN_LIST_APPOINTMENT, data=new_data).to_excel(writer, sheet_name=new_data["CLIENTE"][0], index=False)

        LOG_APPOINTMENT.debug(f"[AGENDAMENTO]: {spreadsheet_name} - [RESPONSAVEL/AGENDAMENTO]: {resp_agendamento.get()} - [CADASTRADO] - [✓]")
        messagebox.showinfo("Informação cadastrada", "Informação cadastrada")

        cliente.delete(0, "end")
        produto.delete(0, "end")
        material.delete(0, "end")
        altura.delete(0, "end")
        largura.delete(0, "end")
        comprimento.delete(0, "end")
        quantidade.delete(0, "end")
        resp_agendamento.delete(0, "end")
        data_agendamento.delete(0, "end")


    app = create_app("Novo agendamento","480x400")
    app.grid_columnconfigure(0, weight=1)
    
    frame0 = create_frame(app, 0, 0, "nsew")
    frame0.grid_columnconfigure(0, weight=1)
    frame0.grid_rowconfigure(0, weight=1)
 
    cliente = create_entry(frame0, "Cliente", 0, 0, "nsew")
    produto = create_entry(frame0, "Produto", 0, 1, "nsew")
    material = create_entry(frame0, "Material", 0, 2, "nsew")
    altura = create_entry(frame0, "Altura", 0, 3, "nsew")
    largura = create_entry(frame0, "Largura", 0, 4, "nsew")
    comprimento = create_entry(frame0, "Comprimento", 0, 5, "nsew")
    quantidade = create_entry(frame0, "Quantidade", 0, 6, "nsew")
    resp_agendamento = create_entry(frame0, "Responsavel/Agendamento", 0, 7, "nsew")
    data_agendamento = create_entry(frame0, "Data/Agendamento", 0, 8, "nsew")

    frame1 = create_frame(app, 0, 1, "nsew")
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_rowconfigure(1, weight=1)
    create_button(frame1, "Cadastrar", 0, 0, "nsew", button_new_appointment)

    app.mainloop()