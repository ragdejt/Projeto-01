import customtkinter
def create_app(geometry:str):
    app = customtkinter.CTk()
    app.title("PROJETO-01")
    app.geometry(geometry)
    app.resizable(False, False)
    app._set_appearance_mode("dark")
    return app

def create_frame(frame, coluna:int, linha:int, expand:str):
    frame = customtkinter.CTkFrame(master=frame)
    frame.grid(column=coluna, row=linha, sticky=expand, padx=5, pady=5)
    return frame

def create_button(frame, texto:str, comando):
    button = customtkinter.CTkButton(master=frame, text=texto, command=comando)
    button.grid(sticky="nsew", padx=5, pady=5)
    return button

def create_entry(frame, texto:str):
    entry = customtkinter.CTkEntry(master=frame, placeholder_text=texto)
    entry.grid(sticky="nsew", padx=5, pady=5)
    return entry

def create_label(frame, texto:str):
    label = customtkinter.CTkLabel(master=frame, text=texto)
    label.grid(sticky="nsew", padx=5, pady=5)
    return label

def create_menu_opt(frame, valores):
    menu = customtkinter.CTkOptionMenu(master=frame, values=valores)
    menu.grid(sticky="nsew", padx=5, pady=5)
    return menu

    

def popup():
    def destroy_app():
        info_cadastrada.destroy()
    info_cadastrada = create_app("360x100")
    frame0 = create_frame(info_cadastrada, 0, 0, "nsew")
    frame0.grid_columnconfigure(0, weight=1)
    create_label(frame0, "Informação cadastrada")
    create_button(frame0, "Fechar", destroy_app)
    info_cadastrada.mainloop()