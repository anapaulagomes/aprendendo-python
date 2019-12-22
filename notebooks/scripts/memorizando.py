import json
import os
import random


try:  # tente
    para_memorizar = json.load(open("minha_memoria.txt", "r"))
except:  # caso dê erro, execute:
    para_memorizar = {}

opcao = ""
while opcao != "sair":
    print("1) Adicionar")
    print("2) Testar")
    print("3) Ver tudo")
    opcao = input("\nOpção: ")

    if opcao == "1":
        item = input("Item: ")
        resposta_certa = input("Resposta certa: ")
        para_memorizar[item] = resposta_certa
    elif opcao == "2":
        item_para_testar = random.choice(list(para_memorizar.keys()))
        os.system("clear")  # cls para windows
        adivinhar = input(
            f"\nQual seu palpite? A palavra é: {item_para_testar}\n")
        if adivinhar == para_memorizar[item_para_testar]:
            print("Acertou!\n")
        else:
            print("Precisa estudar mais!")
    elif opcao == "3":
        print(para_memorizar)
    elif opcao == "sair":
        minha_memoria = open(
            "minha_memoria.txt", "w")
        minha_memoria.write(
            json.dumps(para_memorizar))
