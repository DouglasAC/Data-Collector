from dotenv import load_dotenv
load_dotenv() 
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_email(email, height, average_height, count):
    from_email = os.getenv('FROM_EMAIL')
    from_password = os.getenv('FROM_PASSWORD')
    to_email = email

    subject = "Datos de altura"
    message = "¡Hola! Tu altura es <strong>%s</strong>. ¡Mantente erguido! El promedio de todos es %s y eso se calcula entre %s personas." % (height, average_height, count)

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    msg.attach(MIMEText(message, 'html'))
    
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        gmail = smtplib.SMTP(smtp_server, smtp_port)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email, from_password)
        gmail.sendmail(from_email, to_email, msg.as_string())
    except Exception as e:
        print(f"Error al enviar correo: {e}")
    finally:
        gmail.quit()
    print("Correo enviado")
    
    