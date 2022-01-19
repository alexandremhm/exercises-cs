# Exercício 1: Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida. Exemplo:

name = input("Digite um nome: ")


def printName(name):
    size = len(name)
    stop = size
    separator = ""
    wordList = list(name)
    while stop > 0:
        print(separator.join(wordList))
        wordList.pop()
        stop -= 1


printName(name)
