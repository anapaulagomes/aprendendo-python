---
title:  "Aula 2: Listas e Loops"
img: "python.png"
date: "2019-12-10"
notebook: "Aula 2 - Listas e Loops.ipynb"
---

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

## Projeto: Pedra, papel eeee tesoooura!

Quem nunca brincou de pedra, papel e tesoura, não é mesmo? :) Mas e se você
jogasse contra o computador. Como seria? Nesse projeto criamos um joguinho para
jogar esse jogo contra o computador e no final mostrar quantos pontos ele ou
você acumularam.


```python
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
        print(f"Computador jogou: {jogada_do_computador}\n")

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

```

    Pedra, papel e tesoura
    
    
    Qual a sua jogada?pedra
    Computador jogou: pedra
    
    
    
    Humano 0 x 0 Computador
    Qual a sua jogada?papel
    Computador jogou: pedra
    
    \o/ humano ganhou!
    
    
    Humano 1 x 0 Computador
    Qual a sua jogada?tesoura
    Computador jogou: tesoura
    
    
    
    Humano 1 x 0 Computador
    Qual a sua jogada?tesoura
    Computador jogou: papel
    
    \o/ humano ganhou!
    
    
    Humano 2 x 0 Computador
    Qual a sua jogada?pedra
    Computador jogou: tesoura
    
    \o/ humano ganhou!
    
    
    Humano 3 x 0 Computador
    Qual a sua jogada?pedra
    Computador jogou: papel
    
    :/ computador ganhou!
    
    
    Humano 3 x 1 Computador
    Qual a sua jogada?sair


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


# Estruturas de repetição (ou laços/loops)

Nós podemos mostrar os itens da lista um por um sem precisar acessar
os índices (a posição) de cada um utilizando **laços**.

O primeiro laço que vamos ver é o **for**.


```python
canais_do_youtube = ['Meteoro Brasil', 'Nerdologia', 'Se liga nessa história', 'Porta dos Fundos']

# significa para UM canal NA lista de canais do youtube que eu gosto
for canal in canais_do_youtube:
    print(canal)

```

    Meteoro Brasil
    Nerdologia
    Se liga nessa história
    Porta dos Fundos


O **for** itera sob uma sequência. O que significa isso?
Significa que ele vai passar item por item de uma sequência. A sequência que estamos
utilizando agora é uma lista.

Uma outra estrutura de laço é o **while**, que continuará executando até
que uma condição seja falsa.


```python
numero_desejado = 10
contador = 0

while contador != numero_desejado:
    contador = contador + 1
    print(contador)

```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10


**ATENÇÃO:** cuidado com o `while`. Sem querer você pode acabar criando um **loop infinito**,
que nada mais é que um loop que não acaba mais.

```python
while True:
    print('Eu vou executar pra sempre')
```

<!-- Imagem: https://clipground.com/ -->
