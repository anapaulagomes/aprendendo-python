---
layout: post
title:  "Aula 5: Criando um bot"
img: "bot.png"
date: "2019-12-13"
draft: false
notebook: "Aula 5 - Criando um bot.ipynb"
---

# Criando um bot

Nessa aula vamos criar um bot para o Telegram. Para isso você
precisa ter o Telegram instalado e configurado no seu celular.


### Configurando seu ambiente (computador)

* Você precisa ter o PIP instalado (gerenciador de pacotes Python)

Salve o arquivo [get-pip.py](https://bootstrap.pypa.io/get-pip.py) e,
na mesma pasta que você salvou ele, execute:

```
python get-pip.py
```

Em seguida instale o seguinte pacote:

```
pip install python-telegram-bot

```

Acabamos de instalar o `python-telegram-bot` com a ajuda do PIP
para criar um bot para o Telegram com Python.

### Criando o bot no Telegram

Agora vamos criar o bot no Telegram. Abra seu aplicativo e busque
por **BotFather**, um bot do próprio Telegram para criar outros bots. 🤖

Para criar seu bot, envie para o BotFather: `/newbot`

Ele irá te fazer algumas perguntas (em inglês) nessa sequência:

* Nome do bot
* Username (usuário)

Lembre-se de pôr um nome de usuário mais original. Nomes fáceis já foram,
provavelmente, cadastrados por outras pessoas.

Dando tudo certo você deve ver uma mensagem como a do final dessa tela:

![](/images/ppt_bot.jpg)

Copie todo o código depois de _Use this token to access the HTTP API:_.
Ele é o seu token - um código único (tipo uma senha) para você
gerenciar o seu bot. Guarde esse código bem guardado pois apenas com ele
você poderá manter seu bot funcionando.

## Bot Pedra, papel e tesoura

Algumas aulas atrás nós aprendemos como criar o jogo Pedra, Papel e Tesoura
com Python. Agora, usando a mesma lógica que havíamos desenvolvido, vamos
criar o nosso bot.

A ideia é que o jogador inicie um jogo e ele jogue contra o computador. Basicamente,
precisamos que o jogador:

* inicie uma nova jogada
* diga qual a sua opção: pedra, papel ou tesoura

Ao iniciar uma jogada, vamos saudar o jogador pelo seu nome e perguntar qual a opção.

## Métodos

Durante as aulas utilizamos alguns métodos, como o `print()` mas não
criamos os nossos próprios.
Os métodos (ou funções) são trechos de código
que podem isolar certa lógica e ter seu próprio contexto.

Para criar um método (ou _declarar_) utilizamos a palavra reservada **def**.

```
def mostrar_nome_na_tela(nome):
    print(nome)
```

O método `mostrar_nome_na_tela` recebe um argumento (ou parâmetro) chamado `nome`.
Isso significa que sempre que usarmos (ou chamarmos) esse método precisamos
passar um nome para ele:

```
mostrar_nome_na_tela("Ana Paula")
```

Esse método irá apenas mostrar o nome "Ana Paula" na tela mas se quisessemos
mostrar apenas o primeiro nome, por exemplo, poderíamos.

```
def mostrar_nome_na_tela(nome):
    primeiro_nome = nome.split(' ')[0]  # pega o primeiro nome antes do espaço
    print(primeiro_nome)
```

O ponto aqui é: podemos fazer modificações nos argumentos e outras coisas que
ficarão isoladas dentro do método.
Isso permite deixar o nosso código mais organizado e mais fácil de ler.

## Voltando ao bot

Aqui vamos precisar criar alguns métodos para amarrar um comportamento a certos comandos
do bot.
Antes de ver o código inteiro, vamos a uma explicação passo a passo:

```
bot = Updater('seu-token-aqui', use_context=True)
```

Nessa linha vamos conectar o seu código Python com o bot que já
existe no Telegram. Pra isso o Telegram precisa saber que você
é você e por isso passamos o token para o `Updater`.

Logo depois precisamos dizer quem é que vai lidar com certos eventos.

Acima nós estabelecemos que faríamos duas coisas: iniciar uma jogada nova
e jogar (escolher pedra, papel ou tesoura).

Para iniciar uma nova jogada, o usuário terá que enviar um `/jogar`.
Uma palavra com a barra na frente no Telegram significa um comando.
Para gerenciar um comando precisamos do `CommandHandler`. Nele
vamos dizer qual o nome do comando ("jogar") e qual o método que vai
executar alguma ação quando o usuário enviar esse comando.

```
comando_jogar = CommandHandler('jogar', jogar)
```

Depois de criar o comando, associamos esse comando ao nosso
recém-nascido bot. :)


```
bot.dispatcher.add_handler(comando_jogar)
```

Para entender o que o usuário está jogando, fazemos um
esquema bem parecido: criamos algo para lidar com essa mensagem.
A diferença é que vamos receber um texto e passar para
o método `jogada`. Lá vamos verificar qual foi a jogada
realizada pelo jogador.

_Trecho completo:_

```
bot = Updater('seu-token-aqui', use_context=True)
comando_jogar = CommandHandler('jogar', jogar)
bot.dispatcher.add_handler(comando_jogar)

mensagem = MessageHandler(Filters.text, jogada)
bot.dispatcher.add_handler(mensagem)
```

Nos nossos métodos recebemos dois argumentos: `update` e `context`.
Vamos nos concentrar no `update`, único usado até aqui.

Com ele podemos:

* Pegar informações do usuário que enviou a mensagem:

```python
# seu primeiro nome:
update.message.from_user.first_name
```

* Pegar o texto digitado pelo usuário:

```python
update.message.text
```

Note que colocamos o texto em minúsculo utilizando o método
`lower()` para facilitar a comparação com as opções disponíveis.

* Responder uma mensagem:

```
update.message.reply_text(f"{jogada_do_humano} x {jogada_do_computador}")
```

Você pode ver o código completo a seguir:



```python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random


def jogar(update, context):
    nome = update.message.from_user.first_name
    update.message.reply_text(f'Qual a sua jogada, {nome}?\n Pedra, papel ou tesoura?')


def jogada(update, context):
    digitado_pelo_usuario = update.message.text.lower()
    opcoes = ['pedra', 'papel', 'tesoura']
    jogada_do_computador = random.choice(opcoes)

    jogada_do_humano = None
    for opcao in opcoes:
        if opcao in digitado_pelo_usuario:
            jogada_do_humano = opcao

    update.message.reply_text(f"{jogada_do_humano} x {jogada_do_computador}")
    if jogada_do_humano:
        if jogada_do_humano == jogada_do_computador:
            update.message.reply_text("EMPATE!")
        # pedra ganha de tesoura
        if jogada_do_humano == "pedra" and jogada_do_computador == "tesoura":
            update.message.reply_text("Vitória do humano!")
        elif jogada_do_computador == "pedra" and jogada_do_humano == "tesoura":
            update.message.reply_text("Vitória do computador!")
        
        # tesoura ganha de papel
        if jogada_do_humano == "tesoura" and jogada_do_computador == "papel":
            update.message.reply_text("Vitória do humano!")
        elif jogada_do_computador == "tesoura" and jogada_do_humano == "papel":
            update.message.reply_text("Vitória do computador!")
        # papel ganha de pedra        
        if jogada_do_humano == "papel" and jogada_do_computador == "pedra":
            update.message.reply_text("Vitória do humano!")
        elif jogada_do_computador == "papel" and jogada_do_humano == "pedra":
            update.message.reply_text("Vitória do computador!")        
    else:
        update.message.reply_text('Opção inválida!')



bot = Updater('seu-token-aqui', use_context=True)
comando_jogar = CommandHandler('jogar', jogar)
bot.dispatcher.add_handler(comando_jogar)

mensagem = MessageHandler(Filters.text, jogada)
bot.dispatcher.add_handler(mensagem)

bot.start_polling()
bot.idle()

```

Veja os códigos dessa lição [aqui](https://github.com/anapaulagomes/aprendendo-python/tree/master/notebooks).
