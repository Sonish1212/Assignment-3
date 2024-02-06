from logging import root
import tkinter as tk
from tkinter import PhotoImage, ttk, END, Scrollbar
import googletrans
from googletrans import Translator

# LanguageMixin class for language-related functionality
class LanguageMixin:
    def __init__(self):
        self.language = googletrans.LANGUAGES 
        self.languageV = list(self.language.values())

# Main application class with multiple inheritance
class TranslatorApp(tk.Tk, LanguageMixin):
    def __init__(self):
        super().__init__()
        LanguageMixin.__init__(self)  # Initialize LanguageMixin
        self.title("Google Translator")
        self.geometry("1080x400")
        self.create_widgets()
        self.label_change()

    # Encapsulation: Widget creation and initialization
    def create_widgets(self):
        # Combobox for selecting source language
        self.combo1 = ttk.Combobox(self, values=self.languageV, font="Roboto 14", state='readonly')
        self.combo1.place(x=10, y=10, width=200, height=30)
        self.combo1.set("ENGLISH")

        # Label for displaying selected source language
        self.label1 = tk.Label(self, text="ENGLISH", font="segoe 20 bold", bg="white", width=12, bd=5, relief=tk.GROOVE)
        self.label1.place(x=10, y=50, width=200, height=30)

        # Textbox for entering text to translate
        self.text1 = tk.Text(self, font="Roboto 14", bg="white", relief=tk.GROOVE, wrap=tk.WORD)
        self.text1.place(x=10, y=90, width=420, height=200)

        # Scrollbar for text1
        self.scrollbar1 = Scrollbar(self)
        self.scrollbar1.place(x=430, y=90, height=200)
        self.scrollbar1.configure(command=self.text1.yview)
        self.text1.configure(yscrollcommand=self.scrollbar1.set)

        # Combobox for selecting destination language
        self.combo2 = ttk.Combobox(self, values=self.languageV, font="Roboto 14", state='readonly')
        self.combo2.place(x=600, y=10, width=200, height=30)
        self.combo2.set("SELECT LANGUAGE")

        # Label for displaying selected destination language
        self.label2 = tk.Label(self, text="ENGLISH", font="segoe 20 bold", bg="white", width=12, bd=5, relief=tk.GROOVE)
        self.label2.place(x=600, y=50, width=200, height=30)

        # Textbox for displaying translated text
        self.text2 = tk.Text(self, font="Roboto 14", bg="white", relief=tk.GROOVE, wrap=tk.WORD)
        self.text2.place(x=600, y=90, width=420, height=200)

        # Scrollbar for text2
        self.scrollbar2 = Scrollbar(self)
        self.scrollbar2.place(x=1020, y=90, height=200)
        self.scrollbar2.configure(command=self.text2.yview)
        self.text2.configure(yscrollcommand=self.scrollbar2.set)

        # Translate button
        self.translate_button = tk.Button(self, text="Translate", font=("Roboto", 15), activebackground="white", 
                                           cursor="hand2", bd=1, width=10, height=2, bg="black", fg="white", command=self.translate_now)
        self.translate_button.place(x=460, y=300, width=120, height=50)

        self.arrow_image = PhotoImage(file="arrow.png")
        self.image_label = tk.Label(self, image=self.arrow_image, width=120)
        self.image_label.place(x=460, y=130)

    # Method to periodically update labels
    def label_change(self):
        c = self.combo1.get()
        c1 = self.combo2.get()
        self.label1.configure(text=c)
        self.label2.configure(text=c1)
        self.after(1000, self.label_change)

    # Polymorphism: Method to translate text
    def translate_now(self):
        text_ = self.text1.get(1.0, END)
        t1 = Translator()
        trans_text = t1.translate(text_, src=self.combo1.get(), dest=self.combo2.get())
        trans_text = trans_text.text

        self.text2.delete(1.0, END)
        self.text2.insert(END, trans_text)

# Entry point of the application
if __name__ == "__main__":
    app = TranslatorApp()
    app.configure(bg="white")
    app.mainloop()
