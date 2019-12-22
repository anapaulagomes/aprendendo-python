"""
Exercício de revisão:

Você deve escolher o tema do seu programa.
Ele deve:

1. Mostrar uma mensagem na tela (usando print)
2. Ter uma variável com algum valor
3. Mostrar a variável que você criou na tela 
(usando print)
4. Receber um valor do usuário (usando input)
5. Se o que a pessoa digitou for vazio, 
mostrar uma mensagem "Digite alguma coisa!" 
(usando if e print)

Acabou?

Que tal criar uma calculadora? :)
"""

print("--- CALCULADORA ---")
print("1) SOMA")
print("2) SUBTRAI")
print("3) MULTIPLICA")
print("4) DIVIDE")

numero1 = input("\n\nDigite o número 1:")
numero2 = input("\n\nDigite o número 2:")
operacao = input("\n\nDigite a operação:")

numero1 = int(numero1)
numero2 = int(numero2)
operacao = int(operacao)

if operacao == 1:  # aqui soma!
    soma = numero1 + numero2
    print(f"A soma de {numero1} + {numero2} = {soma}")
elif operacao == 2:
    subtracao = numero1 - numero2
    print(f"A subtracao de {numero1} - {numero2} = {subtracao}")
elif operacao == 3:
    multiplicacao = numero1 * numero2
    print(f"A multiplicacao de {numero1} * {numero2} = {multiplicacao}")
elif operacao == 4:
    divisao = numero1 / numero2
    print(f"A divisao de {numero1} / {numero2} = {divisao}")
