import requests

# http requests

import smtplib

# email body

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
from os.path import basename

# system data and time manuplation


class NotificationManager:
    def __init__(self) -> None:
        self.now = datetime.datetime.now()
        self.SERVER = "smtp.gmail.com"
        self.PORT = 587
        self.FROM = "yasuomonkey68@gmail.com"  # Your Email
        self.TO = "monkeydyasuo1@gmail.com"  # The Person you wanna send to
        self.PASS = "xihyssylrlwdmwpd"  # Password to your Email (password you generate through ur email)

    def send_deals(self, list_of_users):
        msg = MIMEMultipart()
        msg["Subject"] = (
            "Top New Deals [Automated Email]"
            + " "
            + str(self.now.day)
            + "-"
            + str(self.now.month)
            + "-"
            + str(self.now.year)
        )
        msg["From"] = self.FROM
        self.TO = ",".join(list_of_users)
        msg["TO"] = self.TO
        content = """\
                    <html>
                    <body>
                        <h1>טיסות הכי זולות השבוע</h1>
                        <a href="https://excelflights.com/remove_user">הסר אותי מהרשימה</a>
                    </body>
                    </html>
                    """
        msg.attach(MIMEText(content, "html"))

        file_name = "topDeals.xlsx"

        with open(file_name, "rb") as f:
            attachment = MIMEApplication(f.read(), name=basename(file_name))
            attachment["Content-Disposition"] = 'attachment;file_name="{}"'.format(
                basename(file_name)
            )
        msg.attach(attachment)
        self.send_the_message(msg)

    def notify_me(self, name, email, message):
        msg = MIMEMultipart()
        msg["Subject"] = f"request from: {name} , Email: {email}"
        msg["From"] = self.FROM
        msg["TO"] = self.TO
        content = message
        msg.attach(MIMEText(content, "html"))
        self.notify_the_user(email, name)
        self.send_the_message(msg)

    def notify_the_user(self, email, name):
        msg = MIMEMultipart()
        msg["Subject"] = f"hello, {name}! "
        msg["From"] = self.FROM
        msg["TO"] = email
        content = "we got your message we will contact you soon.\nstay tuned!"
        msg.attach(MIMEText(content, "html"))
        self.send_the_message(msg)

    def send_the_message(self, msg):

        # Authentiction through smtp
        print("Initiating Server ...")
        with smtplib.SMTP(self.SERVER, self.PORT) as server:
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.login(self.FROM, self.PASS)
            server.send_message(msg)

            print("Email Sent..")
            server.quit()

    def send_welcome_deals(self, email):
        msg = MIMEMultipart()
        msg["Subject"] = (
            "Top New Deals [Automated Email]"
            + " "
            + str(self.now.day)
            + "-"
            + str(self.now.month)
            + "-"
            + str(self.now.year)
        )
        msg["From"] = self.FROM
        self.TO = email
        msg["TO"] = self.TO
        content = """\
                    <html>
                    <body>
                        <h1>טיסות הכי זולות השבוע</h1>
                        <a href="https://excelflights.com/remove_user">הסר אותי מהרשימה</a>
                    </body>
                    </html>
                    """
        msg.attach(MIMEText(content, "html"))

        file_name = "topDeals.xlsx"

        with open(file_name, "rb") as f:
            attachment = MIMEApplication(f.read(), name=basename(file_name))
            attachment["Content-Disposition"] = 'attachment;file_name="{}"'.format(
                basename(file_name)
            )
        msg.attach(attachment)
        self.send_the_message(msg)
