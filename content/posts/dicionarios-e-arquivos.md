---
layout: post
title:  "Aula 3: Dicionários e Arquivos"
img: "python.png"
date: "2019-12-11"
notebook: "Aula 3 - Dicionários e arquivos.ipynb"
---

## Dicionários

Agora que já sabemos o que são listas podemos criar uma agenda telefônica, com o número dos nossos
melhores amigos. Como podemos fazer isso? Com listas?

```
amigos = ['Mateus', 'Ana', 'Lari']
telefone_dos_amigos = [123456, 998765, 56742534]
```

Até poderíamos fazer mas teríamos que mudar as duas listas juntas todas as vezes.
E se errarmos a posição dos números? Essa agenda telefônica não seria muito confiável.

Para resolver esse problema onde precisamos de um identificador único para armazenar dados,
podemos utilizar uma estrutura de dados chamada Dicionários.


```python
agenda = {
    'Mateus': 123456,
    'Ana': 998765,
    'Lari': 5674253,
}

print(f"O telefone de Lari é: {agenda.get('Lari')}")

# podemos mostrar também dessa forma
print(f"O telefone de Lari é: {agenda['Lari']}")
```

    O telefone de Lari é: 5674253
    O telefone de Lari é: 5674253



```python
print(f"O telefone de Mari é: {agenda['Mari']}")  # gera um erro porque Mari não está na agenda ainda :)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-2-aff0053c66a1> in <module>
    ----> 1 print(f"O telefone de Mari é: {agenda['Mari']}")  # gera um erro porque Mari não está na agenda ainda :)
    

    KeyError: 'Mari'



```python
agenda['Mari'] = 6769798  # adicionamos o número de Mari

print(agenda)
```

Os dicionários utilizam uma estrutura de **chave** e **valor**, onde a chave é o identificador único
e o valor pode ser qualquer coisa: inclusive outro dicionário.

O que acontece se você utilizar a mesma chave com valores diferentes?
Consegue adivinha qual número será impresso na tela?


```python
agenda = {
    'Mateus': 123456,
    'Ana': 998765,
    'Lari': 5674253,
    'Mateus': 99900009999,  # mudou de número
}

# print(f"O telefone de Mateus é: {agenda.get('Mateus')}")
```

Nenhum erro será apontado pelo Python porque a linguagem entende que você pode atualizar os valores
mais tarde. Tem que tomar cuidado para não fazer isso por acidente.

Falando em atualizar, como podemos atualizar um número de alguém que você já tem na agenda?

### Exercício

Você já sabe como receber dados de um usuário com `input`. Que tal
combinar seu conhecimento sobre listas e dicionários e criar uma agenda que adiciona
nomes e telefones de alguém?


## Lidando com Arquivos

Escrever e ler arquivos é uma das coisas mais legais que podemos fazer com programação.
Com eles você pode salvar dados e adicionar informações ao seu programa.


```python
# criando um novo arquivo

meu_arquivo = open('novo-arquivo.txt', 'w')  # esse w indica que o arquivo é "writable" (pode ter algo escrito, em português)
meu_arquivo.write('olha aqui o que eu criei')
meu_arquivo.close()
```


```python
# atualizando um arquivo que já existe

meu_arquivo = open('novo-arquivo.txt', 'a')  # esse a indica que o arquivo é "appendable" (pode ser adicionado, em português)
meu_arquivo.write('\nessa deve ser a segunda linha')
meu_arquivo.close()
```


```python
# abrindo um arquivo somente para leitura

meu_arquivo = open('novo-arquivo.txt', 'r')  # esse r significa "readable" (de legível)
# ou
meu_arquivo = open('novo-arquivo.txt')  # o r fica implícito
meu_arquivo.write('\nessa deve ser a segunda linha')  # dá erro
meu_arquivo.close()

```


    ---------------------------------------------------------------------------

    UnsupportedOperation                      Traceback (most recent call last)

    <ipython-input-5-c77ce516307f> in <module>
          4 # ou
          5 meu_arquivo = open('novo-arquivo.txt')  # o r fica implícito
    ----> 6 meu_arquivo.write('\nessa deve ser a segunda linha')
          7 meu_arquivo.close()


    UnsupportedOperation: not writable



```python
meu_arquivo = open('novo-arquivo.txt')
meu_arquivo.read()  # mostra o conteúdo
```




    'olha aqui o que eu criei\nessa deve ser a segunda linha'




```python
meu_arquivo = open('novo-arquivo.txt')
meu_arquivo.readlines()  # te devolve uma lista de linhas
```




    ['olha aqui o que eu criei\n', 'essa deve ser a segunda linha']



## Projeto: Salvando a agenda em nosso arquivo

Em sala nós criamos um programa para nos ajudar a memorizar qualquer coisa.
Mas sempre que saímos do programa ele perde toda a memória e nós temos que adicionar
novos itens sempre.

Com arquivos, nós podemos salvar os itens e recuperá-los quando abrimos o programa.


```python
import json
import os
import random

try:
    para_memorizar = json.load(open("minha_memoria.txt", "r"))
except:
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
        os.system("clear")  # cls
        adivinhar = input(
            f"\nQual seu palpite? A palavra é: {item_para_testar}\n")
        if adivinhar == para_memorizar[item_para_testar]:
            print("Acertou!\n")
        else:
            print("Precisa estudar mais!")
    elif opcao == "3":
        print(para_memorizar)
    elif opcao == "sair":
        minha_memoria = open("minha_memoria.txt", "w")
        minha_memoria.write(json.dumps(para_memorizar))

```

    1) Adicionar
    2) Testar
    3) Ver tudo
    
    Opção: 3
    {}
    1) Adicionar
    2) Testar
    3) Ver tudo
    
    Opção: 1
    Item: green
    Resposta certa: verde
    1) Adicionar
    2) Testar
    3) Ver tudo
    
    Opção: 3
    {'green': 'verde'}
    1) Adicionar
    2) Testar
    3) Ver tudo
    
    Opção: sair

Veja os códigos dessa lição [aqui](https://github.com/anapaulagomes/aprendendo-python/tree/master/notebooks).
