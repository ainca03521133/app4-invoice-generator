import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoice/*.xlsx")
#print(filepaths)

for filepath in filepaths:
    # INTERATE TO FILEPATHS(LIST)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit ="mm", format="A4")
    pdf.add_page()
    filename= Path(filepath).stem 
    #Path().stem獲取該路徑下的檔案名稱不包含附檔名
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style= "B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")