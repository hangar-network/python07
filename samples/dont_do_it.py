import random

# Pode não parecer, mas este programa é equivalente à versão alternativa do
# Pedra, Papel e Tesoura. Legibilidade é muito importante na hora de codificar!
def f(i):
    c = random.randrange(0,3)
    print("\First: {}    Second: {}".format(i, c))
    if c == (i + 1)%3:
        print(":D")
    elif c == i:
        print(":/")
    else:
        print(":( ")


a = input()
f(a)
