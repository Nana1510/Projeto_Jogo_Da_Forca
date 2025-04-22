import random

def carregar_palavras(arquivo='temas.txt'):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            palavras = f.read().splitlines()
        return palavras
    except FileNotFoundError:
        print("Arquivo de palavras não encontrado.")
        return []

def escolher_palavra(palavras):
    return random.choice(palavras).lower()

def exibir_forca(erros):
    estagios = [
        """
        ------
        |    |
        |
        |
        |
        ---------
        """,
        """
        ------
        |    |
        |    O
        |
        |
        ---------
        """,
        """
        ------
        |    |
        |    O
        |    |
        |
        ---------
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |
        ---------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        ---------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        ---------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        ---------
        """
    ]
    print(estagios[erros])

def jogar():
    palavras = carregar_palavras()
    if not palavras:
        return
    palavra = escolher_palavra(palavras)
    letras_descobertas = ['_' for _ in palavra]
    letras_erradas = []
    tentativas = 6
    print(" Olá!! Seja muio Bem-Vindo ao jogo da Forca 🎮")

    while True:
        print("\nPalavra: ", ' '.join(letras_descobertas))
        print("Letras erradas:", ', '.join(letras_erradas))
        letra = input("Faça seu palpite.Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Digite apenas uma letra válida.")
            continue
        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra!!")
            continue

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1

        exibir_forca(6 - tentativas)

        if '_' not in letras_descobertas:
            print("\n🎉 Parabéns! Você acertou a palavra:", palavra)
            break
        if tentativas == 0:
            print("\n💀 Você perdeu! A palavra era:", palavra , "Vamos jogar novamente??")
            break