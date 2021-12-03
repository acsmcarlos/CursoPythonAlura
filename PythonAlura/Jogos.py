import Adivinhacao
import Forca

print("****************************************")
print("-----===== ESCOLHA O SEU JOGO =====-----")
print("****************************************")

print("      (1) FORCA    (2) ADIVINHAÇÃO")
print("========================================")
jogo = int(input("Qual jogo você quer escolher? "))

if(jogo == 1):
    print("Você escolheu o jogo da Forca")
    Forca.jogar()

elif(jogo == 2):
    print("Você escolheu o jogo da Adivinhação")
    Adivinhacao.jogar()
