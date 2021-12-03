import random

def jogar():
    print("*****************************************")
    print("*****BEM VINDO AO JOGO DE ADIVINHAÇÃO*****")
    print("*****************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativa = 0
    pontos = 500

    print("DEFINA O NÍVEL DE DIFICULDADE:")
    print("(1) EASY   (2) MEDIUM   (3) HARD")

    nivel = int(input("Nível: "))
    if(nivel == 1):
        total_de_tentativa = 15
    elif(nivel == 2):
        total_de_tentativa = 10
    else:
        total_de_tentativa = 7

    for rodada in range(1, total_de_tentativa + 1):
        print("Tentativa {}/{}".format(rodada, total_de_tentativa))

        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("!!!Você deve digitar um número entre 1 e 100!!!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("\nVocê acertou! Parabéns!")
            print("##### O número secreto é:", numero_secreto)
            print("PONTUAÇÃO:", pontos)
            break
        else:
            if(maior):
                print("\n-------Menos!!!-------")
            elif(menor):
                print("\n-------Mais!!!-------")
            ponto_perdidos = abs(chute)
            pontos = pontos - ponto_perdidos

    print("########FIM DE JOGO!########")


if(__name__ == "__main__"):
    jogar()