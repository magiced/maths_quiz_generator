# https://www.blog.pythonlibrary.org/2010/09/21/reportlab-tables-creating-tables-in-pdfs-with-python/

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import random
import numpy as np

number = 10

doc = SimpleDocTemplate(f"Ready_Steady_Go_{number}.pdf", pagesize=A4)
# container for the 'Flowable' objects
elements = []

width, height = A4

# data=   [['00', '01', '02', '03', '04'],
#          ['10', '11', '12', '13', '14'],
#          ['20', '21', '22', '23', '24'],
#          ['30', '31', '32', '33', '34']]

line = [i for i in range(4)]
data = [line for i in range(10)]

num_list = [i for i in range(1,13)]

tt_list = []
tt_list.append('Ready')
for i in range(1,13):
    answer = i * number
    string = f"{i} x {number} =_____"
    tt_list.append(string)
    # print(string)

steady_list = []
steady_list.append('Steady')
random.shuffle(num_list)
for i in num_list:
    answer = i * number
    string = f"{i} x {number} =_____"
    steady_list.append(string)
    # print(string)

go_list = []
go_list.append('Go')
random.shuffle(num_list)
for i in num_list:
    answer = i * number
    string = f"{answer} ÷ {number} =_____"
    go_list.append(string)
    # print(string)

data = [tt_list, steady_list, go_list]
# print(data)

data = np.array(data)
transposed_data = data.T
transposed_data = transposed_data.tolist()
print(transposed_data)

t=Table(transposed_data,2*inch, 0.65*inch)
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