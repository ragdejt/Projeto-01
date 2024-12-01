import sqlite3
import shutil
import pandas
from tkinter import messagebox
from app_functions import *
from constants import *
from log_record import LOG_EMPLOYEE
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome:str
    nascimento:str
    sexo:str
    cargo:str
    admissao:str
    salario:float
    ctps:int
    rg:int
    cpf:int
    estado_civil:str
    contrato:str
    escolaridade:str
    endereço:str
    cidade:str
    estado:str
    telefone:str
    email:str

def add_employee(employee: Funcionario):
    conectar = sqlite3.connect(DB_FUNCIONARIOS)
    cursor = conectar.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS FUNCIONARIOS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        nascimento TEXT NOT NULL,
        sexo TEXT NOT NULL,
        cargo TEXT NOT NULL,
        admissao TEXT NOT NULL,
        salario TEXT NOT NULL,
        ctps TEXT NOT NULL,
        rg TEXT NOT NULL,
        cpf TEXT NOT NULL,
        estado_civil TEXT NOT NULL,
        contrato TEXT NOT NULL,
        escolaridade TEXT NOT NULL,
        endereço TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)
    conectar.commit()
    try:
        cursor.execute("""
        INSERT INTO FUNCIONARIOS (nome, nascimento, sexo, cargo, admissao, salario, ctps, rg, cpf, estado_civil, contrato, escolaridade, endereço, cidade, estado, telefone, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (employee.nome, employee.nascimento, employee.sexo, employee.cargo, employee.admissao, employee.salario, employee.ctps, employee.rg, employee.cpf, employee.estado_civil, employee.contrato, employee.escolaridade, employee.endereço, employee.cidade, employee.estado, employee.telefone, employee.email))
        conectar.commit()
    except sqlite3.IntegrityError:
        LOG_EMPLOYEE.debug(f"[FUNCIONARIO]: {employee.nome} - [ENCONTRADO] - [BANCO DE DADOS]: {DB_FUNCIONARIOS}")
        LOG_EMPLOYEE.info()
    else:
        conectar.close()


def new_employee():
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

        employee_path = FUNCIONARIOS / (new_data['NOME'][0])
        employee_path.mkdir(exist_ok=True)
        
        with pandas.ExcelWriter(path=f"{employee_path}.xlsx", engine="xlsxwriter") as writer:
            pandas.DataFrame(columns=COLUMN_LIST_EMPLOYEE, data=new_data).to_excel(writer, sheet_name=new_data["NOME"][0], index=False)


        shutil.copy(admission_path.get(), employee_path / ("Exame admissional.pdf"))
        shutil.copy(ctps_path.get(), employee_path / ("Carteira de trabalho profissional.pdf"))
        shutil.copy(rg_path.get(), employee_path / ("Registro Geral.pdf"))
        shutil.copy(cpf_path.get(), employee_path / ("Cadastro de pessoa fisica.pdf"))
        shutil.copy(contract_path.get(), employee_path / ("Contrato.pdf"))
        shutil.copy(education_path.get(), employee_path / ("Comprovante de escolaridade.pdf"))
        shutil.copy(address_path.get(), employee_path / ("Comprovante de endereço.pdf"))
        
        LOG_EMPLOYEE.debug(f"[FUNCIONARIO]: {new_data['NOME'][0]} - [CADASTRADO] - [✓]")
        LOG_EMPLOYEE.info(f"[ARQUIVO]: {admission_path.get()} - [COPIADO] - [✓]")
        LOG_EMPLOYEE.info(f"[ARQUIVO]: {ctps_path.get()} - [COPIADO] - [✓]")
        LOG_EMPLOYEE.info(f"[ARQUIVO]: {rg_path.get()} - [COPIADO] - [✓]")
        LOG_EMPLOYEE.info(f"[ARQUIVO]: {cpf_path.get()} - [COPIADO] - [✓]")
        LOG_EMPLOYEE.info(f"[ARQUIVO]: {contract_path.get()} - [COPIADO] - [✓]")
        LOG_EMPLOYEE.info(f"[ARQUIVO]: {education_path.get()} - [COPIADO] - [✓]")
        LOG_EMPLOYEE.info(f"[ARQUIVO]: {address_path.get()} - [COPIADO] - [✓]")

        messagebox.showinfo("Informação cadastrada", "Informação cadastrada")
        
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

        funcionario = Funcionario(
            nome=new_data["NOME"][0],
            nascimento=new_data["DATA/NASCIMENTO"][0],
            sexo=new_data["SEXO"][0],
            cargo=new_data["CARGO"][0],
            admissao=new_data["DATA DE ADMISSÃO"][0],
            salario=new_data["SALARIO"][0],
            ctps=new_data["CTPS"][0],
            rg=new_data["RG"][0],
            cpf=new_data["CPF"][0],
            estado_civil=new_data["ESTADO/CIVIL"][0],
            contrato=new_data["CONTRATO"][0],
            escolaridade=new_data["ESCOLARIDADE"][0],
            endereço=new_data["ENDEREÇO"][0],
            cidade=new_data["CIDADE"][0],
            estado=new_data["ESTADO"][0],
            telefone=new_data["TELEFONE/CELULAR"][0],
            email=new_data["EMAIL"][0]
        )

        add_employee(funcionario)

        LOG_EMPLOYEE.debug(f"[FUNCIONARIO]: {funcionario.nome} - [CADASTRADO] - [BANCO DE DADOS]: {DB_FUNCIONARIOS} - [✓]")

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