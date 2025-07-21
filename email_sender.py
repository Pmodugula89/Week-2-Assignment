import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()
def send_email(report_path):
    msg = EmailMessage()
    msg['Subject'] = 'Daily Gaming Analytics Report'
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = os.getenv("EMAIL_RECEIVER")
    msg.set_content("Attached is the daily gaming analytics report.")
    with open(report_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename='daily_report.pdf')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)	
  .env
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_password
EMAIL_RECEIVER=receiver@example.com
