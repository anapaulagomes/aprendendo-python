"""
Regras:

- Pedra ganha de Tesoura
- Tesoura ganha de Papel
- Papel ganha de Pedra
"""
import random


opcoes = ["pedra", "papel", "tesoura"]

pontos_do_computador = 0
pontos_do_humano = 0

print("Pedra, papel e tesoura\n\n")
jogada_do_humano = ""

while jogada_do_humano.lower() != "sair":
    jogada_do_humano = input("Qual a sua jogada?")
    if jogada_do_humano in opcoes:
        jogada_do_computador = random.choice(opcoes)
        print(f"Computador jogou: {jogada_do_computador}")

        # pedra ganha de tesoura
        if jogada_do_humano == "pedra" and jogada_do_computador == "tesoura":
            print("\o/ humano ganhou!")
            pontos_do_humano = pontos_do_humano + 1
        elif jogada_do_computador == "pedra" and jogada_do_humano == "tesoura":
            print(":/ computador ganhou!")
            pontos_do_computador = pontos_do_computador + 1
        
        # tesoura ganha de papel
        if jogada_do_humano == "tesoura" and jogada_do_computador == "papel":
            print("\o/ humano ganhou!")
            pontos_do_humano = pontos_do_humano + 1
        elif jogada_do_computador == "tesoura" and jogada_do_humano == "papel":
            print(":/ computador ganhou!")
            pontos_do_computador = pontos_do_computador + 1

        # papel ganha de pedra        
        if jogada_do_humano == "papel" and jogada_do_computador == "pedra":
            print("\o/ humano ganhou!")
            pontos_do_humano = pontos_do_humano + 1
        elif jogada_do_computador == "papel" and jogada_do_humano == "pedra":
            print(":/ computador ganhou!")
            pontos_do_computador = pontos_do_computador + 1

        print(f"\n\nHumano {pontos_do_humano} x {pontos_do_computador} Computador")
    elif jogada_do_humano.lower() != "sair":
        print(f"Escolha uma das opções: {opcoes}")
