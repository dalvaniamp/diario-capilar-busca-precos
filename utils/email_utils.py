import smtplib

class EmailUtils():
    @staticmethod
    def envia_email(mensagem):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, senha) 
        server.sendmail(email, email, mensagem)
        server.quit()
