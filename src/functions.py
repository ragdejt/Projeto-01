import customtkinter
from tkinter import filedialog
from constants import *
def create_app(titulo, geometria):
    app = customtkinter.CTk()
    app.title(titulo)
    app.geometry(geometria)
    app.resizable(False, False)
    app._set_appearance_mode("dark")
    return app

def create_frame(master, coluna, linha, expand):
    frame = customtkinter.CTkFrame(master=master)
    frame.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return frame

def create_entry(master, texto, coluna, linha, expand):
    entry = customtkinter.CTkEntry(master=master, placeholder_text=texto)
    entry.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return entry

def create_button(master, texto, coluna, linha, expand, comando):
    button = customtkinter.CTkButton(master=master, text=texto, command=comando)
    button.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return button

def create_label(master, texto, coluna, linha, expand):
    label = customtkinter.CTkLabel(master=master, text=texto)
    label.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return label

def create_menu_opt(frame, valores, coluna, linha, expand):
    menu = customtkinter.CTkOptionMenu(master=frame, values=valores)
    menu.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return menu

def select_file(entry_file):
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo",
        filetypes=(("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*"))
    )
    if file_path:
        entry_file.delete(0, "end")
        entry_file.insert(0, file_path)

