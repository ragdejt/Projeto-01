import tkinter
from functions import *
from new_employee import new_employee
from new_appointment import new_appointment
from new_supplier import new_supplier
def menu():
    # App.
    app = create_app("MENU PRINCIPAL", "1080x960")
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

    frame1 = create_frame(app, 0, 0, "nsew")
    frame2 = create_frame(app, 1, 0, "nsew")

    app.mainloop()


