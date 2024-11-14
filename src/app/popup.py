import customtkinter

def popup():
    def close_app():
        app.destroy()

    app = customtkinter.CTk()
    app.title("Informação cadastrada!")
    app.geometry("360x100")
    app.resizable(False, False)
    app._set_appearance_mode("dark")
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)

    frame0 = customtkinter.CTkFrame(master=app)
    frame0.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
    frame0.grid_columnconfigure(0, weight=1)

    frame1 = customtkinter.CTkFrame(master=frame0)
    frame1.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
    frame1.grid_columnconfigure(0, weight=1)

    text0 = customtkinter.CTkLabel(master=frame1, text="Informação cadastrada!")
    text0.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

    frame2 = customtkinter.CTkFrame(master=frame0)
    frame2.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)
    frame2.grid_columnconfigure(0, weight=1)

    button0 = customtkinter.CTkButton(master=frame2, text="Fechar", command=close_app)
    button0.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)

    app.mainloop()
