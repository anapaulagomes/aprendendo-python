---
title:  "Aula 4: Enviando emails com Python!"
img: "bot.png"
date: "2019-12-12"
draft: false
notebook: "Aula 4 - Enviando emails.ipynb"
---

# Enviando emails

Com Python é possível fazer muitas coisas, desde conectar com outros
sites como Youtube, Vagalume e Twitter (via APIs) e também enviar emails.

O envio de emails pode ser útil em diversas circunstâncias. Algumas delas:

* Notificar alguém em caso de erro
* Criação de um curso online por email
* Lembretes

Nessa atividade vamos criar um programa que envia emails a partir
de um email do Gmail.

**Importante**

* Emails institucionais podem não ter permissões para esse tipo de envio
* Se você tem o 2FA (autenticação de dois fatores ou two factor authentication) talvez precise criar uma senha para esse tipo de envio [aqui](https://security.google.com/settings/security/apppasswords)



```python
import smtplib

server = smtplib.SMTP_SSL(
    'smtp.gmail.com', 465
)
server.login(
    "seu_email@gmail.com",
    "senha do seu email"
)

assunto = "Oi!"
texto = "Esse email foi enviado com Python!"
mensagem = f'Subject: {assunto}\n\n{texto}'
try:
    server.sendmail(
        "SEU_EMAIL@gmail.com", # remetente
        "EMAIL_QUE_VOCE_QUER_ENVIAR_UMA_MSG@gmail.com", # destinatario
        mensagem
    )
    server.quit()
except:
    print('Algo deu errado =/')
else:
    print('Email enviado.')

```

Veja esse notebook [aqui](https://github.com/anapaulagomes/aprendendo-python/tree/master/notebooks).
