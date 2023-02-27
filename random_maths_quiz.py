import random
num_questions = 30
min = 1
max = 10

def generate_random_maths_question(min,max):
    operations = ['add', 'subtract', 'multiply'] #, 'divide']   
    a = random.randint(min,max)
    b = random.randint(min,max)
    operation = operations[random.randint(0, len(operations)-1)]

    if  (operation == 'add'):
        return f'{a} + {b} = ____' #{a + b}'
    elif (operation == 'subtract'):
        while True:
            a = random.randint(min,max)
            b = random.randint(min,max)
            answer = b-a
            if answer >= 0:
                return f'{b} - {a} = ____' #{answer}'
    elif (operation == 'multiply'):
        return f'{a} x {b} = ____' #{a * b}'
    elif (operation == 'divide'):
        while True:
            a = random.randint(min,max)
            b = random.randint(min,max)
            answer = b / a
            if answer % 1 == 0:
                return f'{b} ÷ {a} = ____' #{int(answer)}'

for i in range(num_questions):
    print(generate_random_maths_question(min, max))
