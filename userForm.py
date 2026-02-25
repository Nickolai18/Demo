import customtkinter as ctk

appTest = ctk.CTk()
appTest.geometry("400x400")
appTest.title("First Example")
for i in range(3):
    appTest.grid_columnconfigure(i, weight=1)
    appTest.grid_rowconfigure(i, weight=1)
# labelUsername = ctk.CTkLabel(appTest, text="Username")
# labelUsername.grid(row=0, column=0)
#
# labelPassword = ctk.CTkLabel(appTest, text="Password")
# labelPassword.grid(row=1, column=0)

entryName = ctk.CTkEntry(appTest, width=120, height=20, placeholder_text="Name")
entryName.pack(padx=5, pady=75)

entryPassword = ctk.CTkEntry(appTest, width=120, height=20, placeholder_text="Password")
entryPassword.pack(padx=10, pady=10)

# button = ctk.CTkButton(appTest, text="firstButton", width="50", height="39", fg_color="black")
button = ctk.CTkButton(appTest, text="firstButton")
button.pack(padx=10, pady=10)

appTest.mainloop()
# ctk.set_default_color_theme("white")
# ctk.deactivate_automatic_dpi_awareness()
