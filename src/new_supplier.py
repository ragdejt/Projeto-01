import shutil
from log_record import LOG_SUPPLIER
from functions import *
from constants import *
from tkinter import messagebox

def new_supplier():
    def button_new_supplier():
        new_data = {
            "NOME":[razao_social.get()],
            "CNPJ":[cnpj.get()],
            "EMAIL":[email.get()],
            "TELEFONE":[phone.get()],
            "CATEGORIA":[supplier_category.get()],
            "ENDEREÇO":[address.get()],
            "ESTADO":[state.get()],
            "CIDADE":[city.get()],
            "BANCO":[bank.get()],
            "AGENCIA":[agency.get()],
            "CONTA":[account.get()],
            "PIX":[pix.get()],
            "RESPONSAVEL/CADASTRO":[user.get()]
        }

        supplier_path = SCRIPT_FOLDER_2 / (razao_social.get())
        supplier_path.mkdir(exist_ok=True)

        with pandas.ExcelWriter(path=f"{supplier_path}.xlsx" , engine="xlsxwriter") as writer:
            pandas.DataFrame(columns=COLUMN_LIST_SUPPLIER, data=new_data).to_excel(writer, sheet_name=razao_social.get(), index=False)

        shutil.copy(alvara_path.get(), supplier_path / ("Alvara.pdf"))
        shutil.copy(mei_path.get(), supplier_path / ("Certificado MEI.pdf"))
        shutil.copy(contract_path.get(), supplier_path / ("Contrato Social.pdf"))
        shutil.copy(license_path.get(), supplier_path / ("Certificado_Licença.pdf"))

        LOG_SUPPLIER.debug(f"[FORNECEDOR]: {razao_social.get()} - [CADASTRADO] - [✓]")
        LOG_SUPPLIER.info(f"[ARQUIVO]: {alvara_path.get()} - [COPIADO] - [✓]")
        LOG_SUPPLIER.info(f"[ARQUIVO]: {mei_path.get()} - [COPIADO] - [✓]")
        LOG_SUPPLIER.info(f"[ARQUIVO]: {contract_path.get()} - [COPIADO] - [✓]")
        LOG_SUPPLIER.info(f"[ARQUIVO]: {license_path.get()} - [COPIADO] - [✓]")

        razao_social.delete(0, "end")
        cnpj.delete(0, "end")
        phone.delete(0, "end")
        email.delete(0, "end")
        address.delete(0, "end")
        city.delete(0, "end")
        agency.delete(0, "end")
        account.delete(0, "end")
        pix.delete(0, "end")
        user.delete(0, "end")

        messagebox.showinfo("Informação cadastrada", "Informação cadastrada")


    app = create_app("Novo fornecedor", "1080x750")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=2)

    frame1 = create_frame(app, 0, 0, "nsew")
    frame1.grid_columnconfigure(0, weight=1)
    frame2 = create_frame(app, 1, 0, "nsew")
    frame2.grid_columnconfigure(1, weight=1)

    # Razão social
    razao_social = create_entry(frame1, "Razão social", 0, 2, "nsew")
    # CNPJ
    cnpj = create_entry(frame1, "Cadastro Nacional de Pessoa Juridica", 0, 3, "nsew")
    # Telefone.
    phone = create_entry(frame1, "Telefone/Contato", 0, 4, "nsew")
    # Email.
    email = create_entry(frame1, "E-mail", 0, 5, "nsew")
    # Categoria de fornecedor
    supplier_category = create_menu_opt(frame1, SUPPLIER_CATEGORY, 0, 13, "nsew")
    # Endereço
    address = create_entry(frame1, "Endereço", 0, 6, "nsew")
    # Estado.
    state = create_menu_opt(frame1, STATES, 0, 7, "nsew")
    # Cidade.
    city = create_entry(frame1, "Cidade", 0, 8, "nsew")
    # Banco.
    bank = create_menu_opt(frame1, BANKS, 0, 9, "nsew")
    # Agencia.
    agency = create_entry(frame1, "Agencia", 0, 10, "nsew")
    # Conta corrente
    account = create_entry(frame1, "Conta corrente", 0, 11, "nsew")
    # Chave PIX.
    pix = create_entry(frame1, "Chave PIX", 0, 12, "nsew")
    # Responsavel pelo cadastro.
    user = create_entry(frame1, "Responsavel pelo cadastro", 0, 14, "nsew")


    # Alvará de funcionamento.
    alvara_path = create_entry(frame2, "Alvara de funcionamento", 1, 0, "nsew")
    create_button(frame2, "Selecionar arquivo", 1, 1, "nsew", lambda: select_file(alvara_path))
    # Certificado MEI.
    mei_path = create_entry(frame2, "Certificado MEI", 1, 2, "nsew")
    create_button(frame2, "Selecionar arquivo", 1, 3, "nsew", lambda: select_file(mei_path))
    # Contrato social.
    contract_path = create_entry(frame2, "Contrato social", 1, 4, "nsew")
    create_button(frame2, "Selecionar arquivo", 1, 5, "nsew", lambda: select_file(contract_path))
    # Certificado/Lincenças
    license_path = create_entry(frame2, "Certificado/Licença", 1, 6, "nsew")
    create_button(frame2, "Selecionar arquivo", 1, 7, "nsew", lambda: select_file(license_path))

    frame3 = create_frame(app, 0, 1, "nsew")
    frame3.grid_columnconfigure(0, weight=1)
    create_button(frame3, "Cadastrar", 0, 0, "nsew", button_new_supplier)
    app.mainloop()
