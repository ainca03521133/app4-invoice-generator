from fpdf import FPDF
import pandas as pd
from pathlib import Path
from glob import glob

#create filepath by glob to catch list of filename 
filepaths = glob("pratice/*.txt")

#set PDF standtard format 必須先設在外面才能跟add迭代產出各個title()
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename= Path(filepath).stem
    """ with open(filepath,'r') as f:
        text = f.read()
        print(text) """
    name = filename.title()
    
    pdf.add_page()
    #add page to the PDF document for each text file
       
    pdf.set_font(family="Times",size= 20, style="B")
    pdf.cell(w=50, h=10, txt=name, ln=1 )

pdf.output("pratice.pdf")
        