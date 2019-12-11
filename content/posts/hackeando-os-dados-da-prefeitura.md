---
layout: post
title:  "Aula 3: dados abertos"
img: "dados-abertos.png"
date: "2019-11-11"
notebook: "Aula 3 - Lidando com arquivos.ipynb"
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

