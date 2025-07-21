# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programfrom data_fetch import fetch_data
from report_generator import generate_pdf_report
from email_sende
import pandas as pd

def fetch_data():
    # Simulate pulling data from gaming platform
    data = pd.DataFrame({
        'Game': ['Poker', 'Blackjack', 'Roulette'],
        'Players': [1200, 950, 670],
        'Revenue': [15000, 12000, 8000]
    })
    return data
r import send_email
import logging

logging.basicConfig(level=logging.INFO)

def main():
    try:
        data = fetch_data()
        report_path = generate_pdf_report(data)
        send_email(report_path)
        logging.info("Automation completed successfully.")
    except Exception as e:
        logging.error(f"Automation failed: {e}")

if __name__ == "__main__":
    main()
iz.pro")
from fpdf import FPDF
import os

def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Daily Gaming Analytics Report", ln=True, align='C')

    for index, row in data.iterrows():
        pdf.cell(200, 10, txt=f"{row['Game']}: {row['Players']} players, ${row['Revenue']} revenue", ln=True)

    output_path = os.path.join("sample_output", "daily_report.pdf")
    pdf.output(output_path)
    return output_path
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
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_password
EMAIL_RECEIVER=receiver@example.com
pandas
fpdf
python-dotenv

