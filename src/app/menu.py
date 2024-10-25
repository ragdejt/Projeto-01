import customtkinter

app = customtkinter.CTk()
app.title("Menu principal")
app.geometry("1080x720")
app.resizable(False, False)
app._set_appearance_mode("dark")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(1, weight=1)

frame_0 = customtkinter.CTkFrame(master=app)
frame_0.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

f0_b0 = customtkinter.CTkButton(master=frame_0, text="Abrir", command=None).grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
f0_b1 = customtkinter.CTkButton(master=frame_0, text="Editar", command=None).grid(column=1, row=0, sticky="nsew", padx=5, pady=5)
f0_b2 = customtkinter.CTkButton(master=frame_0, text="Ferramentas", command=None).grid(column=2, row=0, sticky="nsew", padx=5, pady=5)
f0_b3 = customtkinter.CTkButton(master=frame_0, text="", command=None).grid(column=3, row=0, sticky="nsew", padx=5, pady=5)
f0_b4 = customtkinter.CTkButton(master=frame_0, text="", command=None).grid(column=4, row=0, sticky="nsew", padx=5, pady=5)
f0_b5 = customtkinter.CTkButton(master=frame_0, text="", command=None).grid(column=5, row=0, sticky="nsew", padx=5, pady=5)
f0_b6 = customtkinter.CTkButton(master=frame_0, text="", command=None).grid(column=6, row=0, sticky="nsew", padx=5, pady=5)

frame_01 = customtkinter.CTkFrame(master=app)
frame_01.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)


frame_01_00 = customtkinter.CTkFrame(master=frame_01)
frame_01_00.grid_rowconfigure(0, weight=1)

frame_01_00.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
app.mainloop()