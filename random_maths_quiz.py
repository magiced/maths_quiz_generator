import random


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
        return f'{a} x {b} = ____' #{a * b}'

    elif (operation == 'divide'):
        while True:
            a = random.randrange(min,max,increment)
            b = random.randrange(min,max,increment)
            answer = b / a
            if answer % 1 == 0:
                return f'{b} ÷ {a} = ____' #{int(answer)}'

num_questions = 10
min = 10
max = 100
increment = 10

for i in range(num_questions):
    print(generate_random_maths_question(min, max, increment))
