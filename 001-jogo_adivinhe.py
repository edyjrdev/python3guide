# Jogo de Adivinhação de número sorteado
import random

# inicialização
numero_sorteado = random.randint(1, 10) # sorteia numero entre 1 e 10
cont_tentativas = 0
user_tentativa = -1 # -1 como número inválido de usuário

# enquanto tenativa do usuario diferente do numero sorteado
while user_tentativa != numero_sorteado:
    user_tentativa = int (input("Digite um número entre 1 e 10: "))
    cont_tentativas += 1

    if user_tentativa < numero_sorteado:
        print("O número sorteado é maior que ", user_tentativa)
        
    elif user_tentativa > numero_sorteado:
        print("O número sorteado é menor que ", user_tentativa)
    else:
        print("---------------")

else: # while else
    print("Parabéns! Você acertou o número sorteado ", numero_sorteado, " em ", cont_tentativas, " tentativas.")

print("Fim do jogo.")

