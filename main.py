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
    invoice_nr, invoice_date = filename.split("-")
    """ 
    invoice_nr = filename.split("-")[0]
    invoice_date = filename.split("-")[1] 
    a,b = ["a","b"]
    
    """

    pdf.set_font(family="Times", size=16, style= "B")
    pdf.cell(w=50, h=14, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style= "B")
    pdf.cell(w=50, h=10, txt=f"Date:{invoice_date}",ln=1)
    
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt= columns[0], border=1)
    pdf.cell(w=70, h=8, txt= columns[1], border=1)
    pdf.cell(w=30, h=8, txt= columns[2], border=1)
    pdf.cell(w=30, h=8, txt= columns[3], border=1)
    pdf.cell(w=30, h=8, txt= columns[4], border=1,ln=1)
    
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
    
    #add total sum
    total_sum = df["total_price"].sum()
    pdf.cell(w=30, h=8, border=1)
    pdf.cell(w=70, h=8, border=1)
    pdf.cell(w=30, h=8, border=1)
    pdf.cell(w=30, h=8, border=1)
    pdf.cell(w=30, h=8, txt= str(total_sum), border=1, ln=1)

    pdf.set_font(family="Times", size=20, style="B")
    pdf.cell(w=30, h=15, txt=f"Your total price is {total_sum} Dollars.", ln=1)

    #add company name and logo
    pdf.set_font(family="Times", size=14)
    pdf.cell(w=25, h=8, txt="PythonHow")
    pdf.image("pythonhow.png",w=10)
    
    pdf.output(f"PDFs/{filename}.pdf")