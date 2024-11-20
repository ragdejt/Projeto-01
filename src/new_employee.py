import pandas
from functions import create_app, create_button, create_entry, create_frame, create_menu_opt, popup
from constants import EDUCATION, STATUS, MASC_FEM, CONTRACT, POSITION, SCRIPT_FOLDER_1_1, COLUMN_LIST0


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

        employee_path = SCRIPT_FOLDER_1_1 / (new_data['NOME'][0])
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

        popup()

    app = create_app("1000x750")
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=2)
    # Primeiro frame.
    frame01 = create_frame(app, 0, 0, "ew")
    frame01.grid_columnconfigure(0, weight=1)
    # Nome completo
    name = create_entry(frame01, "Nome completo")
    # Data de nascimento.
    birth = create_entry(frame01, "Data de nascimento")
    # Escolaridade.
    education = create_menu_opt(frame01, EDUCATION)
    # Estado civil.
    status = create_menu_opt(frame01, STATUS)
    # Sexo.
    sex = create_menu_opt(frame01, MASC_FEM)
    # Tipo de contrato.
    contract0 = create_menu_opt(frame01, CONTRACT)
    # Cargo.
    position = create_menu_opt(frame01, POSITION)
    # Salario.
    salary = create_entry(frame01, "Salario")
    # Admissão.
    admission_date = create_entry(frame01, "Data de admissão")
    # Carteira de trabalho profissional.
    ctps = create_entry(frame01, "Numero CTPS")
    # Registro Geral.
    rg =create_entry(frame01, "Numero RG")
    # Cadastro de pessoa fisica.
    cpf = create_entry(frame01, "CPF")
    # Contrato.
    contract = create_entry(frame01, "Numero do contrato")
    # Endereço.
    address = create_entry(frame01, "Endereço")
    # Cidade.
    city = create_entry(frame01, "Cidade")
    # Estado.
    state = create_entry(frame01, "Estado")
    # Telefone.
    phone = create_entry(frame01, "Telefone/Celular")
    # Email.
    email = create_entry(frame01, "Email")

    # Segundo frame.
    frame02 = create_frame(app, 1, 0, "nsew")
    frame02.grid_columnconfigure(0, weight=1)
    # Admissão.
    # Carteira de trabalho profissional.
    # Registro Geral.
    # Cadastro de pessoa fisica.
    # Contrato.
    # Escolaridade.
    # Endereço
    # Terceiro frame.
    frame03 = create_frame(app, 0, 2, "ew")
    frame03.grid_columnconfigure(0, weight=1)
    create_button(frame03, "Cadastrar", button_new_employee)
    app.mainloop()