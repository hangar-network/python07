import getpass
import json
from signup import dbfilename, applyhash

userdbfilename = "user_data.json"

def ask_data_and_login():
    email = input("Email: ")
    hashed_password = applyhash(getpass.getpass("Senha: "))
    return authenticate(email, password)


def authenticate(email, password):
    with open(dbfilename, "r") as dbfile:
        users = json.load(dbfile)
        if email in users:
            if password == users[email]:
                print("Usuário autenticado com sucesso")
                return True
            else:
                print("Email e senha não conferem")
        else:
            print("Usuário não cadastrado")
    return False

def ask_complimentary_data():
    nickname = input("Olá, por favor, digite um nick: ")
    presentation_msg = input("Mensagem de Apresentação (outras pessoas verão essa mensagem quando você entrar): ")
    save_userdata(nick, presentation_msg)

def save_userdata(nick, presentation):
    #put the code to save data in a json file here
    pass

if __name__ == '__main__':
    ask_data_and_login()
