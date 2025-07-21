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
