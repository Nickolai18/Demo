import customtkinter as ctk

appTest = ctk.CTk()
appTest.geometry("400x400")
appTest.title("First Example")

labelUsername = ctk.CTkLabel(appTest, text="Username")
labelUsername.grid(row=0, column=0)

labelPassword = ctk.CTkLabel(appTest, text="Password")
labelPassword.grid(row=1, column=0)

# button = ctk.CTkButton(appTest, text="firstButton", width="50", height="39", fg_color="black")
# button = ctk.CTkButton(appTest, text="firstButton")
# button.grid(row=3, column=0, padx=20, pady=10)

appTest.mainloop()
# ctk.set_default_color_theme("white")
# ctk.deactivate_automatic_dpi_awareness()
