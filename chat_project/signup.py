import getpass
import json

dbfilename = "registered_users.json"

def applyhash(password):
    return password

# View
def ask_data():
    print("Preencha todos os dados para cadastro, por favor\n")

    email = input("Email: ")
    name = input("Nome: ")

    password = getpass.getpass("Senha: ")
    password_confirmation = getpass.getpass("Confirme a senha: ")

    if dataisvalid(email, password, password_confirmation):
        password = applyhash(password)
        register_user(email, password)

def dataisvalid(email, password, password_confirmation):

    with open(dbfilename, "r") as dbfile:
        registered_users = json.load(dbfile)
        # email is already taken
        if email in registered_users:
            print("Este email já se encontra em uso\n")
            return False

    if password != password_confirmation:
        print("Senhas não conferem, por favor digite novamente\n")
        return False

    return True


def register_user(email, hashed_password):
    registered_users = {}
    with open(dbfilename, "r") as dbfile:
        # loads json to dictionary
        registered_users = json.load(dbfile)
    # creates new pair (key, value) in dictionary
    registered_users[email] = hashed_password
    with open(dbfilename, "w") as dbfile:
        # serializes and writes
        dbfile.write(json.dumps(registered_users))
    print("Usuário cadastrado com sucesso\n\n")


if __name__ == '__main__':
    ask_data()

# View
# def ask_data():
#     print("Preencha todos os dados para cadastro, por favor\n")
#
#     dbfile = open(dbfilename, "r")
#     register_users = json.load(dbfile)
#     email = ""
#     while(email == ""):
#         email = input("Email: ")
#         # email already taken
#         if email in register_users:
#             email = ""
#             print("Este email já se encontra em uso, por favor, tente outro\n")
#
#     name = input("Nome: ")
#
#     hashed_password = ""
#     while(hashed_password == ""):
#         password = getpass.getpass("Senha: ")
#         password_confirmation = getpass.getpass("Confirme a senha: ")
#
#         if password != password_confirmation:
#             print("Senhas não conferem, por favor digite novamente\n")
#         else:
#             hashed_password = applyhash(password)
