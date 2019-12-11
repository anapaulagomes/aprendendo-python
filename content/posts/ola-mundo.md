---
title:  "Aula 1: Olá, mundo!"
date:   2019-11-09 10:51:47 +0530
img: "python.png"
notebook: "Aula 1 - Olá, mundo.ipynb"
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

## Comentários

PS.: a essa altura do campeonato você já deve ter notado umas **hashtags** rolando por aí.
Elas são chamadas de **comentários**.
O conteúdo delas será ignorado pelo Python e você pode escrever o que você quiser.
É importante para documentar o que você está fazendo ou pontos que queira explicar
para o seu eu do futuro ou para o seu time.

`# eu sou um comentário`

Comentários podem ter também múltiplas linhas:

```
"""
Esse programa é um jogo de salada de frutas.
Ele escolhe a letra automaticamente e conta os pontos no final
"""
```


## Input

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


## Estruturas de controle

Existem algumas ações que gostaríamos de controlar e tomamos decisões baseadas nos dados
ou informações que temos. Já fazemos isso bastante no nosso dia a dia. Um exemplo disso
é atravessar a rua. Você só atravessa uma rua quando sabe que é seguro o suficiente, sendo
porquê o sinal está fechado ou quando não tem carros vindo. Seu cérebro organiza tudo para
você:

- para no passeio
- vê se o sinal está fechado
- o sinal está fechado?
- SIM! Posso atravessar a rua
- o sinal está fechado?
- NÃO! Não posso atravessar a rua

Na programação não é diferente. Temos estruturas chamadas **estruturas de controle**. Utilizamos as
palavras-chave `if` (que significa "se") e `else` (que significa "senão") para controlar o que vamos fazer.

Aproveitando o exemplo da idade, vamos verificar se uma pessoa pode votar ou não:


```python
if idade >= 16:
    print("Já pode votar! :)")
else:
    print("Não pode votar! :(")

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-24-83d40b5203e4> in <module>
    ----> 1 if idade >= 16:
          2     print("Já pode votar! :)")
          3 else:
          4     print("Não pode votar! :(")


    TypeError: '>=' not supported between instances of 'str' and 'int'


Ops, encontramos um erro. A mensagem diz que não podemos dizer se uma _string_ (um texto)
é menor que um número (16, nesse caso). Porquê? Porque `idade` foi digitada pelo usuário.
Por padrão, o que vem do `input` é um texto. Temos que **converter** do tipo _string_ para
um número inteiro.

Em Python é bem fácil. Basta utilizar o nome do tipo para converter o dado.


```python
idade = int(idade)  # convertemos o tipo e já substituímos!

if idade >= 16:
    print("Já pode votar! :)")
else:
    print("Não pode votar! :(")

```

# Projeto da Aula: Salada de Frutas

Nessa aula criamos um jogo chamado Salada de Frutas com Python.
Esse jogo também é conhecido como STOP ou adedanha.

Lembrando como o jogo funciona:

* Sorteamos uma letra automaticamente
* Recebemos do jogador as colunas (nome, fruta, etc)
* Verificamos se a pessoa preencheu tudo e se o valor preenchido começa com a letra sorteada
* Somamos 1 ponto para cada coluna preenchida corretamente
* Mostramos o total no final

**Atenção**: Nós deixamos a letra escolhida minúscula porque o Python
diferencia minúsculas e maiúsculas. Caso ele sorteasse T e você digitasse
o nome "thiago", o programa iria entender como coisas diferentes.



```python
import string
import random


print("Vamos jogar salada de frutas?")

letra = random.choice(string.ascii_letters)
letra = letra.lower()  # a função lower() deixa o texto em letras minúsculas

print(f"A letra é... {letra}

")

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

```

    Vamos jogar salada de frutas?
    A letra é... l
    
    
    Nome: Livia
    Fruta: Limão
    Cidade, Estado ou País: Liverpool
    Animal: Leão
    Minha sogra é...Legal
    Objeto: Livro
    Cantor(a): Leonardo
    Ator(a): Leandra Leal
    Novela: 
    Música: Leãozinho
    TOTAL: 9


