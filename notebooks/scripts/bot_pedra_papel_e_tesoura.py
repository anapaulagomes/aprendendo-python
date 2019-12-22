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
