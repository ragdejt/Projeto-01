import os
import subprocess
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
    entry = customtkinter.CTkEntry(master=master, placeholder_text=texto, font=("Courier New", 15))
    entry.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return entry

def create_button(master, texto, coluna, linha, expand, comando):
    button = customtkinter.CTkButton(master=master, text=texto, font=("Calibri", 15), command=comando)
    button.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return button

def button_folder(frame, texto, coluna, linha, comando):
    button = customtkinter.CTkButton(master=frame, text=texto, font=("Courier New", 15), command=comando)
    button.grid(sticky="nsew", padx=10, pady=10, column=coluna, row=linha)
    return button


def create_label(master, texto, coluna, linha, expand):
    label = customtkinter.CTkLabel(master=master, text=texto, font=("Courier New", 15))
    label.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return label

def create_menu_opt(frame, valores, coluna, linha, expand):
    menu = customtkinter.CTkOptionMenu(master=frame, values=valores, font=("Courier New", 15))
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

def open_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        subprocess.Popen(f'explorer "{folder_path}"', shell=True)