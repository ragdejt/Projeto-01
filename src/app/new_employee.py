import pandas
import customtkinter
from app.popup import popup
from constants import SCRIPT_FOLDER_1_1, COLUMN_LIST0, EDUCATION, STATUS, MASC_FEM, CONTRACT, POSITION
from tkinter.filedialog import askopenfilename
# App novo funcionario.   
def app_new_employee():
    # Função selecionar arquivo.
    def select_arq(entry):
        arq = askopenfilename(title="Selecione um arquivo", filetypes=[("Todos os Arquivos", "*.*"), ("Arquivos PDF", "*.pdf")])
        if arq:
            entry.delete(0, "end")
            entry.insert(0, arq)
        
    # Função criar seleção.         
    def create_seletion(texto):
        entry = customtkinter.CTkEntry(master=frame02, placeholder_text=texto)
        entry.grid(sticky="ew", padx=5, pady=5)
        button_select = customtkinter.CTkButton(master=frame02, text="Selecionar arquivo", command=lambda: select_arq(entry))
        button_select.grid(sticky="ew", padx=5, pady=5)
    #
    def button_new_employee():
        new_data = {
            "NOME":[name.get()],
            "DATA/NASCIMENTO":[birth.get()],
            "SEXO":[sex.get()],
            "CARGO":[position.get()],
            "DATA DE ADMISSÃO":[admission_date.get()],
            "SALARIO":[salary.get()],
            "CTPS":[ctps.get()],
            "RG":[rg.get()],
            "CPF":[cpf.get()],
            "ESTADO/CIVIL":[status.get()],
            "CONTRATO":[contract.get()],
            "ESCOLARIDADE":[education.get()],
            "ENDEREÇO":[address.get()],
            "CIDADE":[city.get()],
            "ESTADO":[state.get()],
            "TELEFONE/CELULAR":[phone.get()],
            "EMAIL":[email.get()]
        }
        with pandas.ExcelWriter(path=SCRIPT_FOLDER_1_1 / (f"{new_data['NOME'][0]}.xlsx"), engine="xlsxwriter") as writer:
            pandas.DataFrame(columns=COLUMN_LIST0, data=new_data).to_excel(writer, sheet_name=new_data["NOME"][0], index=False)

        name.delete(0, "end")
        birth.delete(0, "end")
        admission_date.delete(0, "end")
        salary.delete(0, "end")
        ctps.delete(0, "end")
        rg.delete(0, "end")
        cpf.delete(0, "end")
        contract.delete(0, "end")
        address.delete(0, "end")
        city.delete(0, "end")
        state.delete(0, "end")
        phone.delete(0, "end")
        email.delete(0, "end")



        popup()

    # App.
    app = customtkinter.CTk()
    app.title("Adicionar funcionario")
    app.geometry("1000x800")
    app.resizable(False, False)
    app._set_appearance_mode("dark")
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=2)

    # Primeiro frame.
    frame01 = customtkinter.CTkFrame(master=app)
    frame01.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
    frame01.grid_columnconfigure(0, weight=1)
    # Nome completo
    name = customtkinter.CTkEntry(master=frame01, placeholder_text="Nome completo")
    name.grid(sticky="ew", padx=5, pady=5)
    # Data de nascimento.
    birth = customtkinter.CTkEntry(master=frame01, placeholder_text="Data de nascimento")
    birth.grid(column=0, row=1, sticky="ew", padx=5, pady=5)
    # Escolaridade.
    education = customtkinter.CTkOptionMenu(master=frame01, values=EDUCATION)
    education.grid(sticky="ew", padx=5, pady=5)
    # Estado civil.
    status = customtkinter.CTkOptionMenu(master=frame01, values=STATUS)
    status.grid(sticky="ew", padx=5, pady=5)
    # Sexo.
    sex = customtkinter.CTkOptionMenu(master=frame01, values=MASC_FEM)
    sex.grid(sticky="ew", padx=5, pady=5)
    # Tipo de contrato.
    contract0 = customtkinter.CTkOptionMenu(master=frame01, values=CONTRACT)
    contract0.grid(sticky="ew", padx=5, pady=5)
    # Cargo.
    position = customtkinter.CTkOptionMenu(master=frame01, values=POSITION)
    position.grid(sticky="ew", padx=5, pady=5)
    # Salario.
    salary = customtkinter.CTkEntry(master=frame01, placeholder_text="Salario")
    salary.grid(sticky="ew", padx=5, pady=5)
    # Admissão.
    admission_date = customtkinter.CTkEntry(master=frame01, placeholder_text="Data de admissão")
    admission_date.grid(sticky="ew", padx=5, pady=5)
    # Carteira de trabalho profissional.
    ctps = customtkinter.CTkEntry(master=frame01, placeholder_text="Numero CTPS")
    ctps.grid(sticky="ew", padx=5, pady=5)
    # Registro Geral.
    rg = customtkinter.CTkEntry(master=frame01, placeholder_text="Numero RG")
    rg.grid(sticky="ew", padx=5, pady=5)
    # Cadastro de pessoa fisica.
    cpf = customtkinter.CTkEntry(master=frame01, placeholder_text="Numero do CPF")
    cpf.grid(sticky="ew", padx=5, pady=5)
    # Contrato.
    contract = customtkinter.CTkEntry(master=frame01, placeholder_text="Numero do contrato")
    contract.grid(sticky="ew", padx=5, pady=5)
    # Endereço.
    address = customtkinter.CTkEntry(master=frame01, placeholder_text="Endereço")
    address.grid(sticky="ew", padx=5, pady=5)
    # Cidade.
    city = customtkinter.CTkEntry(master=frame01, placeholder_text="Cidade")
    city.grid(sticky="ew", padx=5, pady=5)
    # Estado.
    state = customtkinter.CTkEntry(master=frame01, placeholder_text="Estado")
    state.grid(sticky="ew", padx=5, pady=5)
    # Telefone.
    phone = customtkinter.CTkEntry(master=frame01, placeholder_text="Telefone/Celular")
    phone.grid(sticky="ew", padx=5, pady=5)
    # Email.
    email = customtkinter.CTkEntry(master=frame01, placeholder_text="Email")
    email.grid(sticky="ew", padx=5, pady=5)



    # Segundo frame.
    frame02 = customtkinter.CTkFrame(master=app)
    frame02.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)
    frame02.grid_columnconfigure(0, weight=1)
    # Admissão.
    create_seletion("Exame admissional")
    # Carteira de trabalho profissional.
    create_seletion("Carteira de trabalho profissional (CTPS)")
    # Registro Geral.
    create_seletion("Registro Geral (RG)")
    # Cadastro de pessoa fisica.
    create_seletion("Cadastro de pessoa fisica (CPF)")
    # Contrato.
    create_seletion("Contrato")
    # Escolaridade.
    create_seletion("Certificado de escolaridade")
    # Endereço
    create_seletion("Comprovante de endereço")

    # Terceiro frame.
    frame03 = customtkinter.CTkFrame(master=app)
    frame03.grid(column=0, row=1, sticky="ew", padx=5, pady=5, columnspan=2)
    frame03.grid_columnconfigure(0, weight=1)
    button_cad = customtkinter.CTkButton(master=frame03, text="Cadastrar", command=button_new_employee)
    button_cad.grid(sticky="ew", padx=5, pady=5)

    app.mainloop()