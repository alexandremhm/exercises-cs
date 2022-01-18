# Exercício 3: Modifique o exercício anterior para que as palavras sejam lidas de um arquivo. Considere que o arquivo terá cada palavra em uma linha.

import random

file = open("data.txt")

words = file.read()

wordsList = words.split('\n')

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

file.close()
