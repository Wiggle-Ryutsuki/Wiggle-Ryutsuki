# Maimoona Aziz

from fpdf import FPDF


# Prompt for user's name
name = input("Name: ")
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Open pdf file | Portrait and A4 size (210m * 297 mm)
pdf.add_page()

# Top of PDF has “CS50 Shirtificate” as text, centered horizontally.
pdf.set_font("helvetica", "B", 40)
pdf.cell(0, 10, "CS50 Shirtificate", align="C")

# Paste image, centered horizontally
pdf.image("shirtificate.png", x="C", y=50, h=170)

# "(name) took CS50" should be on top of the shirt, in white text.
pdf.set_text_color(255, 255, 255)
pdf.set_font("helvetica", "B", 20)
pdf.set_xy(55, 100)
text = f"{name} took CS50"
width = 100

pdf.cell(width, 10, text, align="C")
# Output
pdf.output("shirtificate.pdf")

