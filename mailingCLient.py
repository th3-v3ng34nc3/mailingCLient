import smtplib
from email import encoders
from email.mime.text import MIMEText
from emai1.mime.base import MIMEBase
from emai1.mime.mu1tipart import MIMEMultipart

server = smtplib.SMTP('smtg.world4you.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('mailtesting@neuralnine.com', password)

msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'testmails@spaml.de'
msg['Subject'] = 'Just A Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
attachment = open(filename, 'rb')

p = MIMEBase('application' , 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('mailtesting@neuraline.com', 'testmails@spaml.de', text)
