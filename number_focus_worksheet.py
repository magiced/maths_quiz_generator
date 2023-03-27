# https://www.blog.pythonlibrary.org/2010/09/21/reportlab-tables-creating-tables-in-pdfs-with-python/

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import random
import numpy as np

def generate_random_a_b(number, min = 1, max = 10, increment = 1):
    rand_bool = random.randint(0,1)
    print(f'rand bool: {rand_bool}')
    if rand_bool:  
        a = number
        b = random.randrange(min,max,increment)
    else: 
        a = random.randrange(min,max,increment)
        b = number
    return a,b

def generate_random_maths_question_for_a_number(number, min = 1, max = 10, increment = 1):
    operations = ['add', 'subtract', 'multiply', 'divide']   
    # operations = ['subtract'] #, 'divide']

    a,b = generate_random_a_b(number, min, max, increment)

    operation = operations[random.randint(0, len(operations)-1)]

    if  (operation == 'add'):
        return f'{a} + {b} = ____' #{a + b}'

    elif (operation == 'subtract'):
        while True:
            a,b = generate_random_a_b(number, min, max, increment)
            
            if (a >= b):
                answer = a-b
                if answer >= 0:
                    return f'{a} - {b} = ____'# {answer}'
                else:
                    continue
            else:
                answer = b-a
                if answer >= 0:
                    return f'{b} - {a} = ____'# {answer}'
                else:
                    continue

    elif (operation == 'multiply'):
        return f'{a} x {b} = ____' #{a * b}'

    elif (operation == 'divide'):
        while True:
            a,b = generate_random_a_b(number, min, max, increment)
            answer = a * number
            if answer % 1 == 0:
                return f'{answer} ÷ {number} = ____' #{int(answer)}'
            # answer = b / number
            # if answer % 1 == 0:
            #     return f'{b} ÷ {number} = ____' #{int(answer)}'

number = 5

print()

doc = SimpleDocTemplate(f"number_focus_worksheet_{number}.pdf", pagesize=A4, )
# container for the 'Flowable' objects
styles = getSampleStyleSheet()
print(styles)
elements = []

width, height = A4

num_questions = 10
min = 1
max = 10
increment = 1

columns = 3
rows = 10

data = []
row = []

for r in range(rows):
    for c in range(columns):
        row.append((generate_random_maths_question_for_a_number(number, min, max, increment)))
    data.append(row)
    row=[]

for row in data:
    print(row)

title_text = f'Focusing on {number}!'
title = Paragraph(title_text, style=styles['Title'])
elements.append(title)

t=Table(data,2*inch, 0.8*inch)
print(f'inch:{inch}')

t.setStyle(TableStyle([
('FONTSIZE',(0,0),(-1,-1),18),
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