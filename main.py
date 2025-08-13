import random

def atividade():
    numeros = [random.randint(1, 100) for _ in range(7)]
    return sum(numeros)/len(numeros)

print(atividade())


def cumprimento(texto):
    return f"Olá, {texto}"

nomealuno = input("Digite seu nome completo: ")
print(cumprimento(nomealuno))