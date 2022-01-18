# Exercício 2: Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras e escolherá uma aleatoriamente. O jogador terá três tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se a pessoa ganhou ou perdeu o jogo.
# 🦜 Para embaralhar uma palavra faça: scrambled_word = "".join(random.sample(word, len(word)))
# 🦜 O sorteio de uma palavra aleatória pode ser feito utilizando o método choice: random.choice(["word1", "word2", "word3"]) -> "word2" .

import random

wordsList = [
    "bola",
    "piano",
    "pepino",
    "paralelepipedo",
    "trybe",
    "sinuca",
]

randomWord = random.choice(wordsList)


def generateScrambledWord():

    scrambledWord = "".join(random.sample(randomWord, len(randomWord)))

    print(scrambledWord)


generateScrambledWord()


def gameWords():
    inputedWord = input("Guess the word: ")
    counter = 3
    acertos = 0
    result = "Não foi dessa vez, tente novamente"
    while counter > 1:
        if inputedWord == randomWord:
            inputedWord = input("Guess the word: ")
            acertos += 1
            counter -= 1
        elif inputedWord != randomWord:
            inputedWord = input("Guess the word: ")
            counter -= 1

    if acertos > 0:
        print("Parabéns você acertou")
    else:
        print(result)


gameWords()
