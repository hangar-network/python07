import random


valid_choices = ["pedra", "tesoura", "papel"]

def jokenpo(player1, player2):
    """This function evaluates the result of a Jo Ken Po game against the CPU"""

    player1 = player1.lower()
    player2 = player2.lower()

    print("\nJogador 1: {}    Jogador 2: {}".format(player1, player2))
    # como a expressão é muito grande, separei em 3 linhas. Repare nos parênteses
    if ((player1 == "pedra" and player2 == "tesoura")
        or (player1 == "tesoura" and player2 == "papel")
        or (player1 == "papel" and player2 == "pedra")):
        print("Você ganhou :D !")
    elif player2 == player1:
        print("Empatou :/ ...")
    else:
        print("Não foi dessa vez :( ")


# versão alternativa com uma conta mais elaborada (apenas 1 jogador)
def alternative_jokenpo(user_choice:str):
    """This function evaluates the result of a Jo Ken Po game against the CPU"""

    cpu_chosen_index = random.randrange(0,len(valid_choices))
    user_chosen_index = valid_choices.index(str.lower(user_choice))
    print("\nJogador: {}    CPU: {}".format(user_choice, valid_choices[cpu_chosen_index]))
    if cpu_chosen_index == (user_chosen_index + 1)%len(valid_choices):
        print("Você ganhou :D !")
    elif cpu_chosen_index == user_chosen_index:
        print("Empatou :/ ...")
    else:
        print("Não foi dessa vez :( ")


should_play_again = True
#Sempre passa ao menos 1 vez, pois iniciamos should_play_again com True
while(should_play_again):
    print("Pedra, Papel e Tesoura!")
    mode = input("Digite:\n 1 - para um jogador\n 2 - para dois jogadores\n")
    if mode == "1":
        jogador1 = input("Jogador 1, digite pedra, papel ou tesoura: ")
        cpu = random.choice(valid_choices)
        jokenpo(jogador1, cpu)
    elif mode == "2":
        jogador1 = input("Jogador 1, digite pedra, papel ou tesoura: ")
        jogador2 = input("Jogador 2, digite pedra, papel ou tesoura: ")
        jokenpo(jogador1, jogador2)
    else:
        print("Número de jogadores inválido")
    answer = input("Pressione a tecla 'S' para jogar novamente: ")
    if answer == "S" or answer == "s":
        should_play_again = True
    else:
        should_play_again = False
print("Encerrando jogo...")
