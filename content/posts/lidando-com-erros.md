---
layout: post
title: Lidando com erros
img: image-5.png
date: "2019-11-08"
---

# Como lidar com os erros que aparecem na tela?

Vamos ver essa listinha de coisas para fazer que possam ajudar:

1. Ler a mensagem de erro na tela
2. Caso não entenda, pode copiar e colar no [Google Tradutor](translate.google.com)

Um exemplo:

Eu escrevi esse código e está dando erro:

*Código*
```python
bebidas = 5  # 5 garrafas de refrigerante
comidas = 100  # 100 pasteis
convidados = None  # vou decidir depois

print('Bebidas por convidados:')
print(bebidas/convidados)
print('Comidas por convidados:')
print(comidas/convidados)
```

*Erro*
```bash
Bebidas por convidados:
Traceback (most recent call last):
  File "festa.py", line 6, in <module>
    print(bebidas/convidados)
TypeError: unsupported operand type(s) for /: 'int' and 'NoneType'
```
O erro mostra onde aconteceu o erro (o arquivo, a linha e o local):
`File "festa.py", line 6, in <module>`. Então você já pode ir lá
no arquivo `festa.py` dar uma olhada na linha 6.

Caso não consiga identificar o erro apenas olhando a linha,
confira de onde vem as variáveis, métodos ou outras estruturas
que você está usando. Nesse caso as variáveis `bebidas` e
`convidados`.

A mensagem de erro também te dá uma dica do que pode estar
errado: `TypeError: unsupported operand type(s) for /: 'int' and 'NoneType'`.
Vamos por partes:

- `TypeError`: é uma exceção (um tipo de erro). Nesse caso, traduzindo
ficaria `Erro de Tipo`. Então já sabemos que tem a ver com o tipo dos
dados envolvidos.
- `unsupported operand type(s) for /: 'int' and 'NoneType'`: aqui temos
uma mensagem mais clara do que está acontecendo. A mensagem diz:
`tipo(s) de operando não suportado para /: 'int' e 'NoneType'`. O que isso
quer dizer? Quer dizer dizer que estamos usando tipos que não são
suportados em uma divisão. Nesse caso a variável `bebidas` tem um
dado do tipo inteiro (5) e `convidados` tem um tipo `None`. Não dá pra
dividir `5/None`. Para corrigir esse erro, basta dar um valor válido para
`convidados`.

Se ainda não conseguir, abra o Google e copie a mensagem de erro. Vão
aparecer muitas páginas com muitas pessoas relatando o mesmo problema e
pedindo ajuda. Você também pode pedir ajuda nesses sites. Um site muito
famoso entre a comunidade desenvolvedora é o [StackOverflow](https://pt.stackoverflow.com/)
(versão em português).

Caso você tenha ficado preocupada(o) em ter que fazer isso toda vez,
não se preocupe. Os erros se repetem e depois de um tempo você já
estará fazendo tudo no automático.
