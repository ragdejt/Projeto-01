import pandas
from functions import *
from constants import EDUCATION, STATUS, MASC_FEM, CONTRACT, POSITION, SCRIPT_FOLDER_1, COLUMN_LIST0

def app_new_employee():
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
            "CONTRATO":[contract0.get()],
            "NUMERO/CONTRATO":[contract.get()],
            "ESCOLARIDADE":[education.get()],
            "ENDEREÇO":[address.get()],
            "CIDADE":[city.get()],
            "ESTADO":[state.get()],
            "TELEFONE/CELULAR":[phone.get()],
            "EMAIL":[email.get()]
        }

        employee_path = SCRIPT_FOLDER_1 / (new_data['NOME'][0])
        employee_path.mkdir(exist_ok=True)


        with pandas.ExcelWriter(path=employee_path / (f"{new_data['NOME'][0]}.xlsx"), engine="xlsxwriter") as writer:
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

    # App.
    app = create_app("Adicionar funcionario", "1000x750")
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=2)

    # Primeiro frame.
    frame01 = create_frame(app, 0, 0, "ew")
    frame01.grid_columnconfigure(0, weight=1)
    # Nome completo
    name = create_entry(frame01, "Nome completo", 0, 0, "nsew")
    # Data de nascimento.
    birth = create_entry(frame01, "Data de nascimento", 0, 1, "nsew")
    # Escolaridade.
    education = create_menu_opt(frame01, EDUCATION, 0, 2,"nsew")
    # Estado civil.
    status = create_menu_opt(frame01, STATUS, 0, 3,"nsew")
    # Sexo.
    sex = create_menu_opt(frame01, MASC_FEM, 0, 4,"nsew")
    # Tipo de contrato.
    contract0 = create_menu_opt(frame01, CONTRACT, 0, 5,"nsew")
    # Cargo.
    position = create_menu_opt(frame01, POSITION, 0, 6,"nsew")
    # Salario.
    salary = create_entry(frame01, "Salario", 0, 7,"nsew")
    # Admissão.
    admission_date = create_entry(frame01, "Data de admissão", 0, 8, "nsew")
    # Carteira de trabalho profissional.
    ctps = create_entry(frame01, "Numero CTPS", 0, 9, "nsew")
    # Registro Geral.
    rg =create_entry(frame01, "Numero RG", 0, 10, "nsew")
    # Cadastro de pessoa fisica.
    cpf = create_entry(frame01, "CPF", 0, 11, "nsew")
    # Contrato.
    contract = create_entry(frame01, "Numero do contrato", 0, 12, "nsew")
    # Endereço.
    address = create_entry(frame01, "Endereço", 0, 13, "nsew")
    # Cidade.
    city = create_entry(frame01, "Cidade", 0, 14, "nsew")
    # Estado.
    state = create_entry(frame01, "Estado", 0, 15, "nsew")
    # Telefone.
    phone = create_entry(frame01, "Telefone/Celular", 0, 16, "nsew")
    # Email.
    email = create_entry(frame01, "Email", 0, 17, "nsew")

    # Segundo frame.
    frame02 = create_frame(app, 1, 0, "nsew")
    frame02.grid_columnconfigure(0, weight=1)
    # Admissão.
    admission_path = create_entry(frame02, "Arquivo: Exame admissional", 0, 0, "nsew")
    create_button(frame02, "Selecionar arquivo", 0, 1, "nsew", lambda: select_file(admission_path))
    # Carteira de trabalho profissional.
    ctps_path = create_entry(frame02, "Arquivo: Carteira de trabalho(CTPS)", 0, 2, "nsew")
    create_button(frame02, "Selecionar arquivo", 0, 3, "nsew", lambda: select_file(ctps_path))
    # Registro Geral.
    rg_path = create_entry(frame02, "Arquivo: Registro Geral(RG)", 0, 4, "nsew")
    create_button(frame02, "Selecionar arquivo", 0, 5, "nsew", lambda: select_file(rg_path))
    # Cadastro de pessoa fisica.
    cpf_path = create_entry(frame02, "Arquivo: Cadastro de pessoa fisica(CPF)", 0, 6, "nsew")
    create_button(frame02, "Selecionar arquivo", 0, 7, "nsew", lambda: select_file(cpf_path))
    # Contrato.
    contract_path = create_entry(frame02, "Arquivo: Contrato de trabalho", 0, 8, "nsew")
    create_button(frame02, "Selecionar arquivo", 0, 9, "nsew", lambda: select_file(contract_path))
    # Escolaridade.
    education_path = create_entry(frame02, "Arquivo: Comprovante de escolaridade", 0, 10, "nsew")
    create_button(frame02, "Selecionar arquivo", 0, 11, "nsew", lambda: select_file(education_path))
    # Endereço
    address_path = create_entry(frame02, "Arquivo: Comprovante de endereço", 0, 12, "nsew")
    create_button(frame02, "Selecionar arquivo", 0, 13, "nsew", lambda: select_file(address_path))
    # Terceiro frame.
    

    create_button(app, "Cadastrar", 0, 1, "nsew", button_new_employee)
    app.mainloop()