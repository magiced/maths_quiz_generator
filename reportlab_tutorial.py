# https://docs.reportlab.com/reportlab/userguide/ch1_intro/
# https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
width, height = A4
c = canvas.Canvas("test.pdf")

c.setTitle()
c.drawString(width/2, height/2, 'MIDDLE')

c.save()

