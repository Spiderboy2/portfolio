import smtplib, ssl


def send_mail(message):

    host = "smtp.gmail.com"
    port = 465

    username = "csoni1243@gmail.com"
    password = "nuge aumx zczq fbgc"
    reciver = "csoni1243@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciver, message)
