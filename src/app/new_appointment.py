import time
import pandas
import customtkinter
from constants import SCRIPT_FOLDER_2_1
from app.popup import popup
SPREADSHEET_NAME = "%Y%m%d%H%M%S"

COLUMN_LIST0 = [
    "CLIENTE",
    "PRODUTO",
    "MATERIAL",
    "ALTURA",
    "LARGURA",
    "COMPRIMENTO",
    "QUANTIDADE",
    "RESPONSAVEL/AGENDAMENTO",
    "DATA/AGENDAMENTO"
]

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
            pandas.DataFrame(columns=COLUMN_LIST0, data=new_data).to_excel(writer, sheet_name=spreadsheet_name, index=False)
        
        

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

    app = customtkinter.CTk()
    app.title("Novo agendamento")
    app.geometry("480x480")
    app.resizable(False, False)
    app._set_appearance_mode("dark")
    app.grid_columnconfigure(0, weight=1)
    frame0 = customtkinter.CTkFrame(master=app)
    frame0.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
    frame0.grid_columnconfigure(0, weight=1)
    frame0.grid_rowconfigure(0, weight=1)
 
    cliente = customtkinter.CTkEntry(master=frame0, placeholder_text="Cliente")
    cliente.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

    produto = customtkinter.CTkEntry(master=frame0, placeholder_text="Produto")
    produto.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)

    material = customtkinter.CTkEntry(master=frame0, placeholder_text="Material")
    material.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)

    altura = customtkinter.CTkEntry(master=frame0, placeholder_text="Altura")
    altura.grid(column=0, row=3, sticky="nsew", padx=5, pady=5)

    largura = customtkinter.CTkEntry(master=frame0, placeholder_text="Largura")
    largura.grid(column=0, row=4, sticky="nsew", padx=5, pady=5)

    comprimento = customtkinter.CTkEntry(master=frame0, placeholder_text="Comprimento")
    comprimento.grid(column=0, row=5, sticky="nsew", padx=5, pady=5)

    quantidade = customtkinter.CTkEntry(master=frame0, placeholder_text="Quantidade")
    quantidade.grid(column=0, row=6, sticky="nsew", padx=5, pady=5)

    resp_agendamento = customtkinter.CTkEntry(master=frame0, placeholder_text="Responsavel/Agendamento")
    resp_agendamento.grid(column=0, row=7, sticky="nsew", padx=5, pady=5)

    data_agendamento = customtkinter.CTkEntry(master=frame0, placeholder_text="Data/Agendamento")
    data_agendamento.grid(column=0, row=8, sticky="nsew", padx=5, pady=5)

    frame1 = customtkinter.CTkFrame(master=app)
    frame1.grid(column=0, row=8, sticky="nsew", padx=5, pady=5)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_rowconfigure(1, weight=1)

    botao = customtkinter.CTkButton(master=frame1, text="Cadastrar", command=button_new_appointment)
    botao.grid(column=0, row=9, sticky="nsew", padx=5, pady=5)

    app.mainloop()