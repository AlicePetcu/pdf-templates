from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    x1 = 10
    x2 = 200
    y1 = 21
    y2 = 21
    pdf.add_page()
    #Set header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(x1, 21, x2, 21)

    for i in range(21, 298, 10):
        pdf.line(x1, i, x2, i)

    # Set footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1, border=0)

    #Add more pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for j in range(21, 298, 10):
            pdf.line(x1, j, x2, j)

        # Set foter
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1, border=0)

pdf.output("output.pdf")
