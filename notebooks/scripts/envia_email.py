import smtplib

server = smtplib.SMTP_SSL(
    'smtp.gmail.com', 465
)
server.login(
    "apgomes88@gmail.com",
    "<senha do email>"
)

assunto = "Oi!"
texto = "Esse email foi enviado com Python!"
mensagem = f'Subject: {assunto}\n\n{texto}'
try:
    server.sendmail(
        "SEU_EMAIL@gmail.com", # remetente
        "apgomes88@gmail.com", # destinatario
        mensagem
    )
    server.quit()
except:
    print('Algo deu errado =/')
else:
    print('Email enviado.')
