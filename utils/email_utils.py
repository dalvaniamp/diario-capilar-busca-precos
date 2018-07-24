import smtplib

class EmailUtils():
    @staticmethod
    def enviaEmail(mensagem):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, senha) 
        server.sendmail(email, email, mensagem)
        server.quit()
