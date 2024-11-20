import customtkinter
from functions import create_app, create_button, create_entry, create_frame, create_label, create_menu_opt

app = create_app("1080x720")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
frame0 = create_frame(app, 0, 0, "nsew")
frame0.grid_rowconfigure(0, weight=1)
frame0.grid_columnconfigure(1, weight=1)
frame1 = create_frame(frame0, 0, 0, "ns")
button1 = create_button(frame1, "", None)

frame2 = create_frame(frame0, 1, 0, "nsew")

app.mainloop()