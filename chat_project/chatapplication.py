import tkinter as tk
import tkinter.scrolledtext as tkst
from firebase import firebase
from sseclient import SSEClient
from multiprocessing import Process
import pychat
import json
import queue

MESSAGE_PATTERN = "{} disse: {}\n"

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        print("showing: ", self)
        self.lift()

class LoginScreen(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        fieldsframe = tk.Frame(self)
        emailFrame = tk.Frame(fieldsframe)
        emaillabel = tk.Label(emailFrame, text="Email")
        emaillabel.pack(side="left")
        self.emailField = tk.Entry(emailFrame)
        self.emailField.pack(side="left", fill="x", expand=True)
        emailFrame.pack(side="top", fill="both")

        passWordFrame = tk.Frame(fieldsframe)
        passwordLabel = tk.Label(passWordFrame, text="Senha")
        passwordLabel.pack(side="left")

        self.passwordField = tk.Entry(passWordFrame)
        self.passwordField.pack(side="left", fill="x")
        passWordFrame.pack(side="top", fill="both")

        fieldsframe.pack(side="top", fill="both", expand=True)

        sendbutton = tk.Button(self, text="Cadastrar")
        sendbutton.pack(side="top", fill="both", expand=True)
        sendbutton["command"] = self.signup_user

    def signup_user(self):
        print("cadastrando")


class SignUpScreen(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        emailFrame = tk.Frame(self)
        emaillabel = tk.Label(emailFrame, text="Email")
        emaillabel.pack(side="left")
        self.emailField = tk.Entry(emailFrame)
        self.emailField.pack(side="left", fill="x", expand=True, padx=10)
        emailFrame.pack(side="top", fill="both")

        passWordFrame = tk.Frame(self)
        passwordLabel = tk.Label(passWordFrame, text="Senha")
        passwordLabel.pack(side="left")

        self.passwordField = tk.Entry(passWordFrame)
        self.passwordField.pack(side="left", fill="x", padx=10)
        passWordFrame.pack(side="top", fill="both")

        confirmationFrame = tk.Frame(self)
        confirmationLabel = tk.Label(confirmationFrame, text="Repita Senha")
        confirmationLabel.pack(side="left")

        self.confirmationField = tk.Entry(confirmationFrame)
        self.confirmationField.pack(side="left", fill="x", padx=10)
        confirmationFrame.pack(side="top", fill="both")

        sendbutton = tk.Button(self, text="Cadastrar")
        sendbutton.pack(side="top", fill="both", expand=True, padx=50, pady=50)
        sendbutton["command"] = self.signup_user
        # self.buttons_frame = tk.Frame(self)
        # self.login_button = tk.Button(self.buttons_frame, text="Entrar")
        # self.login_button.pack(side="top", expand=True)
        # self.login_button["command"] = self.gotToLogin
        #
        # self.signup_button = tk.Button(self.buttons_frame, text="Cadastrar")
        # self.signup_button.pack(side="top", expand = True)
        #
        # self.buttons_frame.pack(side="top", fill="x", expand=True)
    def signup_user(self):
        print("cadastrando")


class WelcomeScreen(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.signup_screen = SignUpScreen(self.master)

        label = tk.Label(self, text="Bem vindo ao nosso Chat!\nFaça Login ou Cadastre-se, é gratuito!")
        label.pack(side="top", fill="x", expand=True)

        self.buttons_frame = tk.Frame(self)
        self.login_button = tk.Button(self.buttons_frame, text="Entrar")
        self.login_button.pack(side="top", expand=True)
        self.login_button["command"] = self.goToLogin

        self.signup_button = tk.Button(self.buttons_frame, text="Cadastrar")
        self.signup_button.pack(side="top", expand = True)
        self.signup_button["command"] = self.signup_screen.show

        self.buttons_frame.pack(side="top", fill="x", expand=True)

    def goToLogin(self):
        print("indo pro login")


class ChatScreen(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.msgqueue = queue.Queue()
        self.textarea = tkst.ScrolledText(self)
        self.textarea.grid(row=0, column=0, rowspan=6, columnspan=6)

        #typingframe = tk.Frame(self).grid(row=1, column=0)
        self.typingarea = tk.Text(self, bg="gray", height=2)
        self.typingarea.grid(row=6, column=0, columnspan=3, ipadx=10)
        sendbutton = tk.Button(self, text="enviar")
        sendbutton.grid(row=6, column=4)
        sendbutton['command'] = self.sendmessage

        self.fb = firebase.FirebaseApplication(pychat.FIREBASE_URL, None)
        # self.process = Process(target=pychat.retrieve_and_print_messages)
        self.process = Process(target=self.enqueuemessages)
        self.process.start()
        self.master.after(500, self.dequeuemessages)

    def dequeuemessages(self):
        try:
            msg = self.msgqueue.get_nowait()
            print(msg)
            # self.textarea.insert(tk.END, msg)
        except queue.Empty:
            # print("tentei")
            pass
        self.master.after(100, self.dequeuemessages)


    def enqueuemessages(self):
        # Server Side Event.
        print("sse")
        sse = SSEClient(pychat.FIREBASE_URL + "Messages.json")
        for new_message in sse:
            # message_data is a dictionary (returned by json.loads). The content of this
            # dictionary is the same content of new_message.data (a string that respects
            # the JSON standard)
            message_data = json.loads(new_message.data)
            # If data field is empty (equal to None in the dictionary), we had no message, so let's skip
            if message_data is None or message_data["data"] is None:
                continue
            # Old messages and New messages are retrieved with a difference.
            # The old ones have this "appeareance":
            # { "data": { "UNIQUE_ID": {"name": "username", "message": "message sent by the user"}, "path": "/" }}
            # While the new ones are like:
            # { "data": {"name": "username", "message": "message sent by the user"}, "path": "/UNIQUE_ID" }
            # We need only the innermost data (name and message), so, we must split into 2 cases:
            if message_data["path"] == "/": #the old ones
                # print("Mensagens Antigas: ")
                # self.textarea.insert(tk.END, "Mensagens Antigas: \n")
                self.msgqueue.put_nowait("Mensagens Antigas: \n")
                # a way to iterate over a dictionary reading keys and values
                for (key, message) in message_data["data"].items():
                    # print(MESSAGE_PATTERN.format(message["name"], message["message"]))
                    #self.textarea.insert(tk.END, MESSAGE_PATTERN.format(message["name"], message["message"]))
                    self.msgqueue.put_nowait(MESSAGE_PATTERN.format(message["name"], message["message"]))
                # print("______________________________") # I want to separate old and new messages
                # self.textarea.insert(tk.END, "______________________________\n")
                self.msgqueue.put_nowait("______________________________\n")
            else: # the new ones
                # print(MESSAGE_PATTERN.format(message_data["data"]["name"], message_data["data"]["message"]))
                # self.textarea.insert(tk.END, MESSAGE_PATTERN.format(message_data["data"]["name"], message_data["data"]["message"]))
                self.msgqueue.put_nowait( MESSAGE_PATTERN.format(message_data["data"]["name"], message_data["data"]["message"]))
        # self.master.after(500, self.getmessages)
        print(self.msgqueue.qsize())

    def sendmessage(self):
        msg = self.typingarea.get("1.0", tk.END)
        print(msg)
        self.typingarea.delete("1.0", tk.END)
        self.fb.post('/Messages', {
            "name": "Hallison",
            "message": msg
        })

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = WelcomeScreen(self)
        p2 = LoginScreen(self)
        p3 = SignUpScreen(self)
        p4 = ChatScreen(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Boas Vindas", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Login", command=p2.show)
        b3 = tk.Button(buttonframe, text="Cadastro", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Chat Area", command=p4.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
