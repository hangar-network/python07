import random


def encrypt(text, key = None):
    """Essa funcao criptografa um texto com cifra de Cesar"""

    alphabet_size = ord('Z') - ord('A') + 1
    if key is None:
        print("Chave gerada automaticaente")
        key = random.randint(1, alphabet_size)

    cripto = ""
    for char in text:
        num = ord(char)
        if num in range(ord('A'), ord('Z') +1):
            num = ord('A') + ((num - ord('A')) + key)%alphabet_size
            cripto += chr(num)
        elif num in range(ord('a'), ord('z') +1):
            num = ord('a') + ((num - ord('a')) + key)%alphabet_size
            cripto += chr(num)
        else:
            cripto += char
    return cripto, key

def decrypt(text, key):
    return encrypt(text, -key)


def encrypt_file(filename = None, key = None):
    if filename is None:
        filename = input("Digite o nome do arquivo criptografado: ")
    text = ""
    with open(filename, 'r') as textfile:
        text = textfile.read()

    with open("encrypted_" + filename, 'w') as encryptedfile:
        encrypted, k = cripto.encrypt(text, key)
        encryptedfile.write(encrypted)
    print("Arquivo '{}' criptografado com sucesso".format(filename))
    return key

def encrypt_all_files(foldername = None, key = None):
    if foldername is None:
        foldername = input("Digite o nome da pasta com os arquivos a serem criptografados")
    names = [n for n in os.listdir(foldername) if n.endswith(".txt")]
    for name in names:
        encrypt_file(name, key)
    return key

if __name__ == '__main__':
    print("Nothing here")
