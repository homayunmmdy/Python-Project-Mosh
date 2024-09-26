import random
from termcolor import cprint

quiz = [
    {
        'question': 'What is the capital of France ?',
        'options': ['A. Berlin', 'B. Madrid', 'C. Parice', 'D. Rome'],
        'answer': 'C'
    },
    {
        'question': 'Which planet is known as the red planet ?',
        'options': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        'answer': 'B'
    },
    {
        'question': 'What is the larget ocean on Earth ?',
        'options': ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
        'answer': 'D'
    }
]

random.shuffle(quiz)
score = 0

for index,item in enumerate(quiz, 1):
    print(f'Question {index}: {item["question"]}')
    for option in item['options']:
        print(option)
        
    answer = input('Your anser: ').upper().strip()
    
    if answer == item['answer']:
        cprint('Correct!', 'green')
        score += 1
    else:
        cprint(f'Wrong! The correct answer is {item["answer"]}', 'red')   
    print()    
    
print(f'Quiz over! Your final score is {score} out {len(quiz)}')