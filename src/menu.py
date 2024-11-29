import tkinter
from functions import *
from new_employee import new_employee
from new_appointment import new_appointment
from new_supplier import new_supplier
#def menu():
    # App.
app = create_app("MENU PRINCIPAL", "1080x860")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
# Menu principal.
menu_bar = tkinter.Menu(app)
menu_principal = tkinter.Menu(menu_bar, tearoff=0)
open_menu = tkinter.Menu(menu_principal, tearoff=0)
edit_menu = tkinter.Menu(menu_principal, tearoff=0)
add_menu = tkinter.Menu(menu_principal, tearoff=0)
rem_menu = tkinter.Menu(menu_principal, tearoff=0)
report_menu = tkinter.Menu(menu_principal, tearoff=0)
log_menu = tkinter.Menu(menu_principal, tearoff=0)
help_menu = tkinter.Menu(menu_principal, tearoff=0)
# Abrir.
menu_principal.add_cascade(label="Abrir", menu=open_menu)
open_menu.add_command(label="Funcionario", command=None)
open_menu.add_command(label="Fornecedor", command=None)
open_menu.add_command(label="Cliente", command=None)
open_menu.add_command(label="Estoque", command=None)
open_menu.add_command(label="Agendamento", command=None)
open_menu.add_command(label="Separação", command=None)
open_menu.add_command(label="Expedição", command=None)
open_menu.add_command(label="Compra", command=None)
open_menu.add_command(label="Venda", command=None)
open_menu.add_command(label="Financeiro", command=None)
# Editar.
menu_principal.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label="Funcionario", command=None)
edit_menu.add_command(label="Fornecedor", command=None)
edit_menu.add_command(label="Cliente", command=None)
edit_menu.add_command(label="Estoque", command=None)
edit_menu.add_command(label="Agendamento", command=None)
edit_menu.add_command(label="Separação", command=None)
edit_menu.add_command(label="Expedição", command=None)
edit_menu.add_command(label="Compra", command=None)
edit_menu.add_command(label="Venda", command=None)
edit_menu.add_command(label="Financeiro", command=None)
# Adicionar.
menu_principal.add_cascade(label="Adicionar", menu=add_menu)
add_menu.add_command(label="Funcionario", command=new_employee)
add_menu.add_command(label="Fornecedor", command=new_supplier)
add_menu.add_command(label="Cliente", command=None)
add_menu.add_command(label="Estoque", command=None)
add_menu.add_command(label="Agendamento", command=new_appointment)
add_menu.add_command(label="Separação", command=None)
add_menu.add_command(label="Expedição", command=None)
add_menu.add_command(label="Compra", command=None)
add_menu.add_command(label="Venda", command=None)
add_menu.add_command(label="Financeiro", command=None)
# Remover.
menu_principal.add_cascade(label="Remover", menu=rem_menu)
rem_menu.add_command(label="Funcionario", command=None)
rem_menu.add_command(label="Fornecedor", command=None)
rem_menu.add_command(label="Cliente", command=None)
rem_menu.add_command(label="Estoque", command=None)
rem_menu.add_command(label="Agendamento", command=None)
rem_menu.add_command(label="Separação", command=None)
rem_menu.add_command(label="Expedição", command=None)
rem_menu.add_command(label="Compra", command=None)
rem_menu.add_command(label="Venda", command=None)
rem_menu.add_command(label="Financeiro", command=None)
# Relatórios.
menu_principal.add_cascade(label="Relatório", menu=report_menu)
report_menu.add_command(label="Funcionario", command=None)
report_menu.add_command(label="Fornecedor", command=None)
report_menu.add_command(label="Cliente", command=None)
report_menu.add_command(label="Estoque", command=None)
report_menu.add_command(label="Agendamento", command=None)
report_menu.add_command(label="Separação", command=None)
report_menu.add_command(label="Expedição", command=None)
report_menu.add_command(label="Compra", command=None)
report_menu.add_command(label="Venda", command=None)
report_menu.add_command(label="Financeiro", command=None)
# Registros.
menu_principal.add_cascade(label="Registro", menu=log_menu)
log_menu.add_command(label="Funcionario", command=None)
log_menu.add_command(label="Fornecedor", command=None)
log_menu.add_command(label="Cliente", command=None)
log_menu.add_command(label="Estoque", command=None)
log_menu.add_command(label="Agendamento", command=None)
log_menu.add_command(label="Separação", command=None)
log_menu.add_command(label="Expedição", command=None)
log_menu.add_command(label="Compra", command=None)
log_menu.add_command(label="Venda", command=None)
log_menu.add_command(label="Financeiro", command=None)
# Ajuda.
menu_principal.add_cascade(label="Ajuda", menu=help_menu)
help_menu.add
app.config(menu=menu_principal)

#
frame1 = customtkinter.CTkFrame(app)
frame1.grid(sticky="nsew", padx=5, pady=5, column=0, row=0)
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_rowconfigure(1, weight=1)
frame1_1 = customtkinter.CTkFrame(frame1)
frame1_1.grid(sticky="ew", padx=5, pady=5, column=0, row=0)

frame1_2 = customtkinter.CTkFrame(frame1)
frame1_2.grid(sticky="nsew", padx=5, pady=5, column=0, row=1)

#
frame2 = customtkinter.CTkFrame(app)
frame2.grid(sticky="nsew", padx=5, pady=5, column=1, row=0)
frame2.grid_rowconfigure(1, weight=1)

frame2_1 = customtkinter.CTkFrame(frame2)
frame2_1.grid(sticky="", padx=5, pady=5, column=0, row=0)

frame2_2 = customtkinter.CTkFrame(frame2)
frame2_2.grid(sticky="nsew", padx=5, pady=5, column=0, row=1)
frame2_2.grid_columnconfigure(0, weight=1)

button0 = customtkinter.CTkButton(frame2_2, text="Agendamento",command=lambda: open_folder(SCRIPT_FOLDER_1))
button0.grid(sticky="nsew", padx=10, pady=10, column=0, row=0)

button1 = customtkinter.CTkButton(frame2_2, text="Compra", command=lambda: open_folder(SCRIPT_FOLDER_2))
button1.grid(sticky="nsew", padx=10, pady=10, column=0, row=1)

button2 = customtkinter.CTkButton(frame2_2, text="Cliente", command=lambda: open_folder(SCRIPT_FOLDER_3))
button2.grid(sticky="nsew", padx=10, pady=10, column=0, row=2)

button3 = customtkinter.CTkButton(frame2_2, text="Financeiro", command=lambda: open_folder(SCRIPT_FOLDER_4))
button3.grid(sticky="nsew", padx=10, pady=10, column=0, row=3)

button4 = customtkinter.CTkButton(frame2_2, text="Fornecedores", command=lambda: open_folder(SCRIPT_FOLDER_5))
button4.grid(sticky="nsew", padx=10, pady=10, column=0, row=4)

button5 = customtkinter.CTkButton(frame2_2, text="Funcionarios", command=lambda: open_folder(SCRIPT_FOLDER_6))
button5.grid(sticky="nsew", padx=10, pady=10, column=0, row=5)

button6 = customtkinter.CTkButton(frame2_2, text="Estoque", command=lambda: open_folder(SCRIPT_FOLDER_7))
button6.grid(sticky="nsew", padx=10, pady=10, column=0, row=6)

button7 = customtkinter.CTkButton(frame2_2, text="Registro", command=lambda: open_folder(SCRIPT_FOLDER_8))
button7.grid(sticky="nsew", padx=10, pady=10, column=0, row=7)

button8 = customtkinter.CTkButton(frame2_2, text="Recebimento", command=lambda: open_folder(SCRIPT_FOLDER_9))
button8.grid(sticky="nsew", padx=10, pady=10, column=0, row=8)

button9 = customtkinter.CTkButton(frame2_2, text="Relatorio", command=lambda: open_folder(SCRIPT_FOLDER_10))
button9.grid(sticky="nsew", padx=10, pady=10, column=0, row=9)

button10 = customtkinter.CTkButton(frame2_2, text="Separação", command=lambda: open_folder(SCRIPT_FOLDER_11))
button10.grid(sticky="nsew", padx=10, pady=10, column=0, row=10)

button11 = customtkinter.CTkButton(frame2_2, text="Expedição", command=lambda: open_folder(SCRIPT_FOLDER_12))
button11.grid(sticky="nsew", padx=10, pady=10, column=0, row=11)

button12 = customtkinter.CTkButton(frame2_2, text="Venda", command=lambda: open_folder(SCRIPT_FOLDER_13))
button12.grid(sticky="nsew", padx=10, pady=10, column=0, row=12)

app.mainloop()


