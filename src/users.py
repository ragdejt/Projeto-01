import sqlite3
import customtkinter
from app_functions import *
from databases import *
from menu import menu

def login():
    def verify_login():

        entry_user = username.get()
        entry_pass = password.get()
        connect = sqlite3.connect(DB_USUARIOS)
        cursor = connect.cursor()
        
        query = "SELECT * FROM USUARIOS WHERE username = ? AND password = ?"
        cursor.execute(query, (entry_user, entry_pass))
        result = cursor.fetchone()
        if result:
            LOG_USUARIOS.info(f"[USUARIO]: {entry_user} - [✓] - [BANCO DE DADOS]: {DB_USUARIOS}")
            label1.configure(text="Usuário encontrado")
            app.destroy()
            menu(entry_user)
        else:
            LOG_USUARIOS.warning(f"[USUARIO]: {entry_user} - [✗] - [BANCO DE DADOS]: {DB_USUARIOS}")
            label1.configure(text="Usuário não encontrado")
        connect.close()
    try:
        connect = sqlite3.connect(DB_USUARIOS)
        cursor = connect.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL               
        )
        """)
        cursor.execute("INSERT INTO USUARIOS (username, password) VALUES (?, ?)", ("Admin", "Admin"))
    except sqlite3.IntegrityError:
        pass
    finally:
        connect.commit()
        connect.close()

    app = create_app("Login", "350x175")
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    frame0 = create_frame(app, 0, 0, "nsew")
    frame0.grid_columnconfigure(0, weight=1)
    label1 = create_label(frame0, "Login", 0, 0, "nsew")
    username = create_entry(frame0, "Usuario", 0, 1, "nsew")
    password = customtkinter.CTkEntry(master=frame0, placeholder_text="Senha", show="*", font=("Courier New", 15))
    password.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)
    create_button(frame0, "Entrar", 0, 3, "nsew", verify_login)
    app.mainloop()