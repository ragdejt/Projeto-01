import tkinter
from app_functions import *
from new_employee import new_employee
from new_appointment import new_appointment
from new_supplier import new_supplier
from graph import create_graph

def menu(entry_user):
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
    # Ajuda.
    menu_principal.add_cascade(label="Ajuda", menu=help_menu)
    help_menu.add
    app.config(menu=menu_principal)

    #
    frame1 = customtkinter.CTkFrame(app)
    frame1.grid(sticky="nsew", padx=5, pady=5, column=0, row=0)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_rowconfigure(1, weight=1)

    frame11 = customtkinter.CTkFrame(frame1)
    frame11.grid(sticky="ew", padx=5, pady=5, column=0, row=0)
    frame11.grid_columnconfigure(0, weight=4)
    frame11.grid_columnconfigure(1, weight=1)
    
    entry111 = customtkinter.CTkEntry(frame11, placeholder_text="Selecionar o arquivo/diretorio")
    entry111.grid(sticky="sew", padx=10, pady=10, column=0, row=0)

    button111 = customtkinter.CTkButton(frame11, text="Procurar", command=lambda: select_file(entry111))
    button111.grid(sticky="sew", padx=10, pady=10, column=1, row=0)

    button_report = customtkinter.CTkButton(
        frame11,
        text="Gerar relatorio",
        command=lambda: create_graph(
            x=[1, 4 ,7 ,8 ,9, 12],
            y=[2, 4, 6, 8, 9, 13],
            axXname="Eixo X",
            axYname="Eixo Y",
            title="Grafico 1",
            texto="Demonstração",
            grade=True
    ))
    button_report.grid(sticky="nsew", padx=10, pady=10, column=2, row=0)


    frame12 = customtkinter.CTkFrame(frame1)
    frame12.grid(sticky="nsew", padx=5, pady=5, column=0, row=1)

    #
    frame2 = customtkinter.CTkFrame(app)
    frame2.grid(sticky="nsew", padx=5, pady=5, column=1, row=0)
    frame2.grid_rowconfigure(1, weight=1)

    frame21 = customtkinter.CTkFrame(frame2)
    frame21.grid(sticky="nsew", padx=5, pady=5, column=0, row=0)
    frame21.grid_columnconfigure(0, weight=1)
    label211 = customtkinter.CTkLabel(frame21, text=f"USUARIO: {entry_user}")
    label211.grid(sticky="nsew", padx=5, pady=5, column=0, row=0)

    frame2_2 = customtkinter.CTkFrame(frame2)
    frame2_2.grid(sticky="nsew", padx=5, pady=5, column=0, row=1)
    frame2_2.grid_columnconfigure(0, weight=1)

    button0 = customtkinter.CTkButton(frame2_2, text="Agendamentos",command=lambda: open_folder(AGENDAMENTOS))
    button0.grid(sticky="nsew", padx=10, pady=10, column=0, row=0)

    button1 = customtkinter.CTkButton(frame2_2, text="Compras", command=lambda: open_folder(COMPRAS))
    button1.grid(sticky="nsew", padx=10, pady=10, column=0, row=1)

    button2 = customtkinter.CTkButton(frame2_2, text="Clientes", command=lambda: open_folder(CLIENTES))
    button2.grid(sticky="nsew", padx=10, pady=10, column=0, row=2)

    button3 = customtkinter.CTkButton(frame2_2, text="Financeiro", command=lambda: open_folder(FINANCEIRO))
    button3.grid(sticky="nsew", padx=10, pady=10, column=0, row=3)

    button4 = customtkinter.CTkButton(frame2_2, text="Fornecedores", command=lambda: open_folder(FORNECEDORES))
    button4.grid(sticky="nsew", padx=10, pady=10, column=0, row=4)

    button5 = customtkinter.CTkButton(frame2_2, text="Funcionarios", command=lambda: open_folder(FUNCIONARIOS))
    button5.grid(sticky="nsew", padx=10, pady=10, column=0, row=5)

    button6 = customtkinter.CTkButton(frame2_2, text="Estoque", command=lambda: open_folder(ESTOQUE))
    button6.grid(sticky="nsew", padx=10, pady=10, column=0, row=6)

    button7 = customtkinter.CTkButton(frame2_2, text="Registros", command=lambda: open_folder(REGISTROS))
    button7.grid(sticky="nsew", padx=10, pady=10, column=0, row=7)

    button8 = customtkinter.CTkButton(frame2_2, text="Recebimentos", command=lambda: open_folder(RECEBIMENTOS))
    button8.grid(sticky="nsew", padx=10, pady=10, column=0, row=8)

    button9 = customtkinter.CTkButton(frame2_2, text="Relatorios", command=lambda: open_folder(RELATORIOS))
    button9.grid(sticky="nsew", padx=10, pady=10, column=0, row=9)

    button10 = customtkinter.CTkButton(frame2_2, text="Separação", command=lambda: open_folder(SEPARACAO))
    button10.grid(sticky="nsew", padx=10, pady=10, column=0, row=10)

    button11 = customtkinter.CTkButton(frame2_2, text="Expedição", command=lambda: open_folder(EXPEDICAO))
    button11.grid(sticky="nsew", padx=10, pady=10, column=0, row=11)

    button12 = customtkinter.CTkButton(frame2_2, text="Vendas", command=lambda: open_folder(VENDAS))
    button12.grid(sticky="nsew", padx=10, pady=10, column=0, row=12)



    app.mainloop()


