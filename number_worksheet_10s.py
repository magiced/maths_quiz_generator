# https://www.blog.pythonlibrary.org/2010/09/21/reportlab-tables-creating-tables-in-pdfs-with-python/

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import random
import numpy as np

def generate_random_maths_question(min = 1, max = 10, increment = 1):
    operations = ['add', 'subtract', 'multiply'] #, 'divide']   
    # operations = ['subtract'] #, 'divide']  
    a = random.randrange(min,max,increment)
    b = random.randrange(min,max,increment)
    operation = operations[random.randint(0, len(operations)-1)]

    if  (operation == 'add'):
        return f'{a} + {b} = ____' #{a + b}'

    elif (operation == 'subtract'):
        while True:
            a = random.randrange(min,max,increment)
            b = random.randrange(min,max,increment)
            
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
        return f'{int(a/10)} x {b} = ____' #{a * b}'

    elif (operation == 'divide'):
        while True:
            a = random.randrange(min,max,increment)
            b = random.randrange(min,max,increment)
            answer = b / a
            if answer % 1 == 0:
                return f'{b} ÷ {a} = ____' #{int(answer)}'

number = 10

doc = SimpleDocTemplate(f"number_worksheet_{number}.pdf", pagesize=A4)
# container for the 'Flowable' objects
elements = []

width, height = A4

num_questions = 10
min = 0
max = 101
increment = 10

columns = 3
rows = 10

data = []
row = []

for r in range(rows):
    for c in range(columns):
        row.append((generate_random_maths_question(min, max, increment)))
    data.append(row)
    row=[]

for row in data:
    print(row)

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