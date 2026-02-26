import customtkinter as ctk

appTest = ctk.CTk()
appTest.geometry("400x400")
appTest.title("First Example")
widthEntry = 250
heightEntry = 25
# labelUsername = ctk.CTkLabel(appTest, text="Username")
# labelUsername.grid(row=0, column=0)
#
# labelPassword = ctk.CTkLabel(appTest, text="Password")
# labelPassword.grid(row=1, column=0)

frameForm = ctk.CTkFrame(appTest, width=300)
frameForm.pack(anchor="center", expand=1, padx=5, pady=5)

formLabel = ctk.CTkLabel(frameForm, text="Введите имя и пароль", font=('Arial', 25))
formLabel.pack(anchor="n")

entryName = ctk.CTkEntry(frameForm, width=widthEntry, height=heightEntry, placeholder_text="Name")
entryName.pack(padx=10, pady=10)

entryPassword = ctk.CTkEntry(frameForm, width=widthEntry, height=heightEntry, placeholder_text="Password")
entryPassword.pack()

# button = ctk.CTkButton(appTest, text="firstButton", width="50", height="39", fg_color="black")
button = ctk.CTkButton(frameForm, text="firstButton")
button.pack(padx=10, pady=10)

appTest.mainloop()
# ctk.set_default_color_theme("white")
# ctk.deactivate_automatic_dpi_awareness()
