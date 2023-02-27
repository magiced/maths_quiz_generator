import random
num_questions = 10
min = 1
max = 5

def generate_random_maths_question(min,max):
    operations = ['add', 'subtract', 'multiply', 'divide']   
    a = random.randint(min,max)
    b = random.randint(min,max)
    operation = operations[random.randint(0, len(operations)-1)]

    if  (operation == 'add'):
        return f'{a} + {b} = {a + b}'
    elif (operation == 'subtract'):
        return f'{a} - {b} = {a - b}'
    elif (operation == 'multiply'):
        return f'{a} x {b} = {a * b}'
    elif (operation == 'divide'):
        return f'{a} ÷ {b} = {a / b:.2f}'

for i in range(num_questions):
    print(generate_random_maths_question(min, max))
