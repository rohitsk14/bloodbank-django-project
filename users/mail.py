import smtplib

def sendmail(to,msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email','password')
    server.sendmail(
        'email',
        to,
        msg
    )
    print("mail sent")
    server.quit()


