import random

def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join([str(digit) for digit in digits[:4]])
    
def calculate_cows_and_bulls(secret , guess):
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret[i]]) - bulls

    return cows, bulls

def main():
    secret = generate_secret()
    while True:
        guess = input('Guess: ')
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            cows , bulls = calculate_cows_and_bulls(secret, guess)
            print(f"{cows} cows, {bulls} bulls")
            
            if bulls == 4:
                print('Congratulation! You guessed the correct number')
                break
        else:
            print('Invalid guess Please enter a 4-digiet number with unique digit')   
    
if __name__ == '__main__':
    main()