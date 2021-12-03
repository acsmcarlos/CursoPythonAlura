
def jogar():
    print("****************************************")
    print("---=== BEM VINDO AO JOGO DA FORCA ===---")
    print("****************************************")

    palavra_secreta = "macarronada"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta.upper():
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                # print("Letra [{}][{}]".format(letra, index))
            index += 1

        print(letras_acertadas)
        print("\nContinue jogando...")





    print("############# FIM DE JOGO! #############")

if(__name__ == "__main__"):
    jogar()