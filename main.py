import os

from dotenv import load_dotenv
from fpdf import FPDF


def txt2pdf(file_in, file_out, logo):
    pdf = FPDF()
    pdf.set_left_margin(25)
    pdf.add_page()
    pdf.add_font('DejaVu', '', './fonts/DejaVuSansMono.ttf', uni=True)
    pdf.set_font('DejaVu', '', 8)
    pdf.set_fill_color(179, 184, 189)
    pdf.image(logo, w=40, h=15)
    records = open(file_in, 'r', encoding='cp1251').read().splitlines()
    while records[-1] == '':
        records.pop()
    for record in records:
        if 'К ВЫДАЧЕ РАБОТНИКУ' in record:
            pdf.cell(w=7, h=4, txt=' ', ln=0, align='L')
            pdf.cell(w=118, h=4, txt=' ' * 22 + record.lstrip(), ln=1,
                     align='L', fill=True)
        else:
            pdf.cell(w=125, h=4, txt=record, ln=1, align='L')
    pdf.output(file_out)


if __name__ == '__main__':

    load_dotenv()
    txt2pdf(os.getenv('FILE_IN'), os.getenv('FILE_OUT'), os.getenv('LOGO'))
