import os 

def main():
    filename = input('Enter the file name to open or create: ').strip()
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        else:
            with open(filename, 'w') as file:
                pass
    except OSError:
        print(f"{filename} could not be opened")
        return
    
    print('\n Enter your text (type SAVE on a new line to save and exit)')
    content = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        content.append(line)
    try:    
        with open(filename, 'w') as file:
            file.write('\n'.join(content))
            print(f"{filename} saved.")
    except OSError:
        print(f"{filename} could not be saved")
    
if __name__ == '__main__':
    main()