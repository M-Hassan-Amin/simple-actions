from base_action import BaseAction
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class WriteEmailAction(BaseAction):
    def __init__(self, smtp_server, smtp_port, smtp_username, smtp_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def run(self, recipient, subject, body):
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.smtp_username
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Secure the connection
            server.login(self.smtp_username, self.smtp_password)
            text = msg.as_string()
            server.sendmail(self.smtp_username, recipient, text)
            server.quit()
            return f"Email successfully sent to {recipient}"
        except Exception as e:
            return f"Failed to send email: {e}"
