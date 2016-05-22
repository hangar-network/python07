import cripto as cp
import os


while(True):
    print("Este programa criptografa textos\n")
    print("Digite 1 para criptografar textos digitados no terminal")
    print("Digite 2 para criptografar um arquivo")
    print("Digite 3 para criptografar todos os arquivos de uma pasta")
    print("Digite qualquer outra coisa para encerrar o programa")
    choice = input("Sua escolha: ")

    # Neste modelo, essa escolha não deveria estar aqui, pois o usuário pode ter
    # optado por encerrar o programa (não faz sentido pedir a chave nesse caso)
    # mas manterei aqui para pensarmos em como resolver
    key = input("Digite a chave a ser usada (aperte 'Enter' sem digitá-la se quiser gerar uma automaticamente) : ")
    try:
        key = int(key)
    except ValueError as e:
        print("Chave não reconhecida, será gerada uma chave automática")
        key = None

    if choice == "1":
        text = input("Digite o texto a ser criptografado: ")
        encrypted, _ = cripto.encrypt(text, key)
        print("Texto criptografado: ", encrypted)
    elif choice == "2":
        cripto.encrypt_file(key = key)
    elif choice == "3":
        cripto.encrypt_all_files(key = key)
    else:
        break
    print("\n\n\n")
