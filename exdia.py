# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.


def biggestNumber(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return num1
    else:
        return num2


num1 = 5
num2 = 5

print(biggestNumber(num1, num2))

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.


def averageCalculator(list):
    sum = 0
    for number in list:
        sum += number
    average = sum / len(list)
    return average


list = [1, 2, 3]

print(averageCalculator(list))


# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n . Por exemplo:


def printSquare(size):
    shouldStop = size
    while shouldStop > 0:
        print(size * "*")
        shouldStop -= 1


printSquare(4)


# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" .


def biggestCharSequence(list):
    isTheBiggestChar = ""
    for char in list:
        if len(char) > len(isTheBiggestChar):
            isTheBiggestChar = char
        elif len(isTheBiggestChar) == 0:
            isTheBiggestChar = char
    return isTheBiggestChar


print(biggestCharSequence(["ol", "aleluia", "ola", "batata", "paralelepipedo"]))


# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede(em m²).


def colorPriceCalculator(size):
    liters = size / 3
    bottle = liters / 18
    cost = bottle * 80.00
    return (float("{:.2f}".format(bottle)), float("{:.2f}".format(cost)))


print(colorPriceCalculator(200))

# Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo" , caso não seja possível formar um triângulo.


def whichTriangleIsIt(a, b, c):
    if a == b == c:
        print("Equilátero")
    elif a == b and b != c or a == c and a != c:
        print("Isóceles")
    elif a != b and a != c and b != c:
        print("Escaleno")
    else:
        print("Não é um triângulo")
