import string
import random


print("Vamos jogar salada de frutas?")

letra = random.choice(string.ascii_letters)
letra = letra.lower()  # deixa minúscula

print(f"A letra é... {letra}\n\n")

nome = input("Nome: ")
fruta = input("Fruta: ")
cep = input("Cidade, Estado ou País: ")
animal = input("Animal: ")
minha_sogra_eh = input("Minha sogra é...")
objeto = input("Objeto: ")
cantor_ou_cantora = input("Cantor(a): ")
ator_ou_atriz = input("Ator(a): ")
novela = input("Novela: ")
musica = input("Música: ")

total = 0
if nome != "" and nome.lower().startswith(letra):
    total = total + 1
if fruta != "" and fruta.lower().startswith(letra):
    total = total + 1
if cep != "" and cep.lower().startswith(letra):
    total = total + 1
if animal != "" and animal.lower().startswith(letra):
    total = total + 1
if minha_sogra_eh != "" and minha_sogra_eh.lower().startswith(letra):
    total = total + 1
if objeto != "" and objeto.lower().startswith(letra):
    total = total + 1
if cantor_ou_cantora != "" and cantor_ou_cantora.lower().startswith(letra):
    total = total + 1
if ator_ou_atriz != "" and ator_ou_atriz.lower().startswith(letra):
    total = total + 1
if novela != "" and novela.lower().startswith(letra):
    total = total + 1
if musica != "" and musica.lower().startswith(letra):
    total = total + 1

print(f'TOTAL: {total}')
