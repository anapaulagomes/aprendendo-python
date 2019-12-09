---
title:  "Aula 1: Olá, mundo!"
date:   2019-11-09 10:51:47 +0530
img: "python.png"
---

Introdução aos computadores, a linha de comando e conceitos
básicos da linguagem de programação Python.

---

Veja uma Introdução a Linha de Comando [aqui](https://tutorial.djangogirls.org/pt/intro_to_command_line/).

# Olá, mundo

Mostrando um "Olá, mundo" na tela foi como boa parte das pessoas programadoras começou.
Chegou a sua vez!


```python
print("Olá, mundo!")
```

    Olá, mundo!


Repare que você teve que colocar a sua mensagem dentro de parênteses antecedidos por `print`. O `print` é um método (ou uma função) responśavel por mostrar alguma informação na tela.

Você pode mostrar outras coisas também:


```python
print("Meu nome é Ana")
print(f"Eu tenho {2019 - 1988} anos")
print("
C
J
C
C
")
```

    Meu nome é Ana
    Eu tenho 31 anos
    
    C
    J
    C
    C
    


# Variáveis e tipos de dados

Mas não só de imprimir seu nome na tela viverá a pessoa programadora.:)
Seria muito legal se a gente conseguisse salvar informações. Isso é
possível graças ás **variáveis**!


```python
nome = 'Ana Paula Gomes'
ano_de_nascimento = 1988
dinheiro_na_carteira = 4.89
eh_programadora = True  # True significa verdadeiro / False significa falso

print('---------- Ficha ----------')
print(f'Nome: {nome}')
print(f'Idade: {2019 - ano_de_nascimento}')
print(f'Saldo: {dinheiro_na_carteira}')
print(f'É programadora? {eh_programadora}')

```

    ---------- Ficha ----------
    Nome: Ana Paula Gomes
    Idade: 31
    Saldo: 4.89
    É programadora? True


Cada tipo de informação está guardada dentro das suas caixinhas (variáveis) e você pode reutilizá-las ou modificá-las quantas vezes quiser. Em Python, os nomes de variáveis podem:

* incluir letras e números (e _underscores_ `_` também)
* embora possa incluir números, não pode iniciar com eles (você pode criar um `carro1` mas não um `1carro`)
* são _case sensitive_ ; ou seja, ele vai diferenciar letras maiúsculas e minúsculas

Python infere qual o tipo de dado você está utilizando a partir do dado que você atribui as suas variáveis.
Se você quiser saber qual tipo de variável está utilizando, basta chamar o método `type`:


```python
eh_estudante = True
print(type(eh_estudante))
```

    <class 'bool'>


| Tipo de dado     | Exemplo | Descrição        |
| :---: | :---: | :--- |
| string (`str`) | `"CJCC"`, `"Estou vendo um filme na Netflix"` | Utilizado para representar números inteiros. Exemplo: número de telefone, idade, ano de nascimento, número da casa |
| inteiro (`int`) | `2020` | Utilizado para representar números inteiros. Exemplo: número de telefone, idade, ano de nascimento, número da casa |
| float (`float`) | `9.99` | Utilizado para representar números decimais. Exemplo: dinheiro, quantidade de um líquido |
| boleano (`bool`) | `True` / `False` | Utilizado para representar informações que podem ser classificadas em verdadeiro ou falso. Exemplo: tem mais de 18 anos? Gosta de coentro? |

O que acha de tentar o método `type` com as outras variáveis?

### Exercício

Agora é a sua vez. Crie uma ficha sobre você com as seguintes informações:

* Seu nome completo
* Apelido
* Idade
* É a primeira vez que você programa?
* O que você gosta de fazer no seu tempo livre?

Você deve utilizar variáveis e imprimir todas as informações na tela.

# Listas

E se você quiser guardar uma lista das mesmas coisas, como os seus seriados preferidos?
Você poderia criar uma variável pra cada um.


```
seriado1 = "The Crown"
seriado2 = "Bojack Horseman"
seriado3 = "Explicando"

```

Conforme a lista for crescendo, vai ser difícil gerenciar todas as variáveis, já que elas
estão separadas. Com o Python você pode criar suas próprias **listas**:


```python
seriados = ["The Crown", "Bojack Horseman", "Explicando"]
print(seriados)
```

    ['The Crown', 'Bojack Horseman', 'Explicando']


Você pode também criar listas combinando tipos diferentes:

```
notas = [10, 8.9, 7.5, 9.2]  # inteiros e decimais
```

### Exercício

Crie listas com:

* Coisas que você adora fazer em Feira de Santana
* Coisas que você não gosta em Feira de Santana
* O que você mais curte fazer na internet

PS.: a essa altura do campeonato você já deve ter notado umas **hashtags** rolando por aí.
Elas são chamadas de **comentários**. O conteúdo delas será ignorado pelo Python e você
pode escrever o que você quiser. É importante para documentar o que você está fazendo ou
pontos que queira explicar para o seu eu do futuro ou para o seu time.

`# eu sou um comentário`

Comentários podem ter também múltiplas linhas:

```
"""
Muitas
Linhas
Aqui
"""
```

## Mais ação com listas

Dá pra fazer bastante coisas com listas. Elas são uma estrutura de dados poderosa!

Vamos ver como:

* adicionar
* remover
* buscar
* ordenar

Elementos em uma lista!


```python
# primeiro, vamos ver o que tem nessa lista:

print('--- O que tem na lista:')
print(seriados)

# adicionando itens a uma lista que já existe

print('--- Novo item:')
seriados.append('Irmandade')
print(seriados)

# acessando itens em uma lista

print('--- Primeiro item da lista:')
print(seriados[0])  # o primeiro item da lista - isso mesmo, Python começa a contar do zero!

### Encontrando um item em uma lista

print('--- Onde está The Crown?')
onde_esta_esse_seriado = seriados.index('The Crown')  # O Python vai te dizer em que posição o que você busca está
print(onde_esta_esse_seriado)
print(seriados[onde_esta_esse_seriado])

### Ordenando uma lista

print('--- Seriados ordenados:')
seriados = sorted(seriados)  # substituímos a lista desordenada pela ordenada
print(seriados)

### Deletando um item de uma lista

print('--- Deletamos o primeiro e o último da lista')
seriados.pop(0)  # deleta o primeiro da lista
seriados.pop(0)  # deleta o útil da lista
print(seriados)
```

    --- O que tem na lista:
    ['The Crown', 'Bojack Horseman', 'Explicando']
    --- Novo item:
    ['The Crown', 'Bojack Horseman', 'Explicando', 'Irmandade']
    --- Primeiro item da lista:
    The Crown
    --- Onde está The Crown?
    0
    The Crown
    --- Seriados ordenados:
    ['Bojack Horseman', 'Explicando', 'Irmandade', 'The Crown']
    --- Deletamos o primeiro e o último da lista
    ['Irmandade', 'The Crown']


# Dicionários

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

    <ipython-input-26-048e1b6587a7> in <module>
    ----> 1 print(f"O telefone de Mari é: {agenda['Mari']}")
    

    KeyError: 'Mari'



```python
agenda['Mari'] = 6769798  # adicionamos o número de Mari

print(agenda)
```

    {'Mateus': 123456, 'Ana': 998765, 'Lari': 5674253, 'Mari': 6769798}


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


```python
agenda['Ana'] = 112233
agenda['Camila'] = 445566  # novo amigo na agenda

agenda['ana'] = 89898989  # novo ou não?
agenda
```




    {'Mateus': 99900009999,
     'Ana': 112233,
     'Lari': 5674253,
     'Camila': 445566,
     'ana': 89898989}



O potencial de programação vai muito além do que já vimos aqui.
Uma das coisas mais legais é poder interagir com o mundo fora do código: com pessoas!

Podemos receber dados das pessoas através do `input`. O programa vai esperar a entrada de dados
de um usuário e salvá-la em uma variável:


```python
idade = input('Quantos anos você tem?')
"""
Vai mostrar essa mensagem na tela, esperar o usuário digitar algo e dar enter,
e salvar o que ele digitou em `idade`
"""
print(f'Você tem {idade} anos')
```

    Quantos anos você tem?31
    Você tem 31 anos



```python

```

