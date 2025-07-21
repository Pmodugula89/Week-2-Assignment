from data_fetch import fetch_data
from report_generator import generate_pdf_report
from email_sender import send_email
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
