# https://www.blog.pythonlibrary.org/2010/09/21/reportlab-tables-creating-tables-in-pdfs-with-python/

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import random
import numpy as np

def generate_random_a_b_c(min = 1, max = 10, increment = 1):
    a = random.randrange(min,max,increment)
    b = random.randrange(min,max,increment)
    c = random.randrange(min,max,increment)
    return a,b,c

def generate_addition_question(min = 1, max = 10, increment = 1):

    a,b,c = generate_random_a_b_c(min, max, increment)

    return f' {a} + {b} + {c} = ______ ' #{a + b}'


doc = SimpleDocTemplate(f"multi_stage_addition.pdf", pagesize=A4)
# container for the 'Flowable' objects
styles = getSampleStyleSheet()
print(styles)
elements = []

width, height = A4

# num_questions = 20
min = 1
max = 10
increment = 1

columns = 1
rows = 10

data = []
row = []

for r in range(rows):
    for c in range(columns):
        row.append((generate_addition_question(min, max, increment)))
    data.append(row)
    row=[]

for row in data:
    print(row)

title_text = f'Multi stage addition!'
title = Paragraph(title_text, style=styles['Title'])
elements.append(title)

t=Table(data,5 * inch, 0.9 * inch)
print(f'inch:{inch}')

t.setStyle(TableStyle([
('FONTSIZE',(0,0),(-1,-1),24),
('ALIGN',(0,0),(-1,-1),'CENTER'),
('VALIGN',(0,0),(-1,-1),'MIDDLE'),
('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
('BOX', (0,0), (-1,-1), 0.25, colors.black),
]))

elements.append(t)
# write the document to disk
doc.build(elements)

'''
# https://stackoverflow.com/questions/53529173/how-to-draw-a-table-on-a-canvas-in-python-using-report-lab
# looks simple

width = 400
height = 100
x = 100
y = 800
f = Table(data)
f.wrapOn(p, width, height)
f.drawOn(p, x, y)

'''