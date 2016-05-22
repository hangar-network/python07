import cripto
import tkinter as tk
from tkinter.filedialog import askopenfilename

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # Button for encrypt command
        self.encrypt_button = tk.Button(self)
        self.encrypt_button["text"] = "Criptografar Documento"
        self.encrypt_button["command"] = self.encrypt_file
        self.encrypt_button.pack(side="top")

        self.decrypt_button = tk.Button(self)
        self.decrypt_button["text"] = "Criptografar texto"
        self.decrypt_button["command"] = self.encrypt_text_box
        self.decrypt_button.pack(side="top")

        self.ask_label = tk.Label(self)
        self.ask_label["text"] = "Insira o seu texto na caixinha abaixo..."
        self.ask_label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.display_content = tk.Text(self, background = "green")
        self.display_content.pack()

        self.quit_button = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit_button.pack()

    def encrypt_file(self):
        filename = askopenfilename()
        encrypted_text = ""
        with open(filename, 'r') as secretfile:
            content = secretfile.read()
            encrypted_text, key = cripto.encrypt(content)
            self.display_content.delete("1.0", tk.END)
            self.display_content.insert(tk.END, encrypted_text)
            print("updated display")
            #print(encrypted_text)

    def encrypt_text_box(self):
        content = self.entry.get()
        encrypted_text, key = cripto.encrypt(content)
        self.display_content.delete("1.0", tk.END)
        self.display_content.insert(tk.END, encrypted_text)
        print("updated display")

    def decrypt_file(self):
        # precisa da chave!!!
        filename = askopenfilename()
        print(filename)

    #def update_display(self):


root = tk.Tk()
app = Application(master=root)
app.mainloop()
