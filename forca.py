import random


def imprimir_abertura():
    print("-=-" * 5)
    print("jogo da forca")
    print("-=-" * 5)


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    index_palavra_secreta = random.randint(0, len(palavras) - 1)

    palavra_secreta = palavras[index_palavra_secreta].upper()

    return palavra_secreta


def inicializar_espacos_letras(palavra_secreta):
    lista = ["_" for letra in palavra_secreta]
    return lista


def capturar_chute_jogador():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1
    print(letras_acertadas)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_vencedor(palavra_secreta):
    print("\n\n")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    acertou = True
    return acertou


def imprime_perdedor(erros, palavra_secreta):
    if erros == 7:
        enforcou = True
        print("\n\n")
        print("Puxa, você foi enforcado!")
        print(f"A palavra secreta era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        return enforcou


def jogar():
    enforcou = False
    acertou = False
    erros = 0

    imprimir_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializar_espacos_letras(palavra_secreta)
    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = capturar_chute_jogador()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)

            if "_" not in letras_acertadas:
                imprime_vencedor(palavra_secreta)
                break
            else:
                continue

        else:
            erros += 1
            desenha_forca(erros)
            enforcou = imprime_perdedor(erros, palavra_secreta)

    print("Fim de jogo")


# somente executa o codigo se for executado diretamente neste arquivo
if __name__ == "__main__":
    jogar()
