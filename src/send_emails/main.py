import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

from utils.csv_save import load_emails_from_csv


def send_email(subject, message, recipient_email):
    load_dotenv()
    SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
    SMTP_SERVER = os.environ.get('SMTP_SERVER')
    SMTP_PORT = os.environ.get("SMTP_PORT")

    FROM_EMAIL = os.environ.get('FROM_EMAIL')

    try:
        # Create message
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "html"))

        # Set sender and recipient
        msg["From"] = FROM_EMAIL
        msg["To"] = recipient_email

        # Send email
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {str(e)}")
        return False


def main():
    # MESSAGE
    subject = "Descubre cómo Novabits puede impulsar tu presencia en línea"
    message = '''
         <html lang="es">

      <head>

          <meta name="viewport" content="width=device-width" />

          <style type="text/css">
              a {
                  text-decoration: underline;
                  color: inherit;
                  font-weight: bold;
                  color: #253342;
              }

              h1 {
                  font-size: 56px;
              }

              h2 {
                  font-size: 28px;
                  font-weight: 900;
              }

              p {
                  font-weight: 100;
              }

              td {
                  vertical-align: top;
              }

              .subtle-link {
                  font-size: 9px;
                  text-transform: uppercase;
                  letter-spacing: 1px;
                  color: #CBD6E2;
              }
          </style>
      </head>

      <body bgcolor="#F5F8FA" style="width: 100%; margin: auto 0; padding:0; font-family:sans-serif; font-size:18px; color:#33475B;">
          <div id="email">
              <table role="presentation" width="100%">
                  <tr>
                      <td bgcolor="#000" align="center" style="color: white; padding: 20px 0">
                          <a href="http://novabitsve.com">
                              <img alt="Novabits logo" src="https://novabitsve.com/novabits.png" width="100px">
                          </a>
                      </td>
                  </tr>
              </table>

              <table role="presentation" bgcolor="#EAF0F6" width="100%">
                  <tr>
                      <td style="padding: 30px 30px;">
                          <h2>¡Hola!</h2>
                          <h4>Me alegra contactarte. Soy parte del equipo de Novabits, una agencia especializada en el desarrollo de páginas web y soluciones digitales.</h4>
                          <h4>Queremos ayudarte a llevar tu negocio al siguiente nivel en línea. Con nuestra experiencia en diseño y desarrollo web, podemos crear una página web personalizada y atractiva que refleje la identidad de tu negocio.</h4>
                          <h4>Ofrecemos una variedad de servicios, incluyendo el desarrollo de sitios web, tiendas en línea, mantenimiento y consultoría. Nos adaptamos a tus necesidades y te brindamos soluciones eficientes y efectivas.</h4>
                          <h4>Si estás buscando mejorar tu presencia en línea, estaremos encantados de discutir tus objetivos y ofrecerte una solución personalizada. No dudes en contactarnos para más información.</h4>
                          <h4>¡Esperamos trabajar contigo y ayudarte a alcanzar el éxito en línea!</h4>
                          <p>Saludos cordiales,</p>
                          <p>El equipo de <a href="http://novabitsve.com">Novabits</a></p>
                      </td>
                  </tr>
              </table>
          </div>
      </body>

      </html>
'''

    emails = load_emails_from_csv()

    # Stats
    total_emails = len(emails)
    sent_emails = 0
    error_emails = 0

    for email in emails:
        if send_email(subject, message, email):
            sent_emails += 1
        else:
            error_emails += 1

    print(f"Total emails: {total_emails}")
    print(f"Sent emails: {sent_emails}")
    print(f"Error emails: {error_emails}")
