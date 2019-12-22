agenda = {
    "Mateus": 123456789,
    "Tiago": 9876543,
    "Evelyn": 38172389
}

opcao = ""
while opcao != "5":
    print("1) Visualizar")
    print("2) Adicionar")
    print("3) Deletar")
    print("4) Atualizar")
    print("5) Sair")
    opcao = input("\n")

    if opcao == "1":
        print(agenda)
    if opcao == "2":
        nome = input("\nNome:")
        telefone = input("\nTelefone:")
        agenda[nome] = telefone
    if opcao == "3":
        nome = input("\nNome que você quer deletar:")
        del agenda[nome]
    if opcao == "4":
        nome = input("\nNome que você quer atualizar:")
        telefone = input("\nTelefone:")
        agenda[nome] = telefone
