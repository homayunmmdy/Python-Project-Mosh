- Read the list of the words from the file(words.txt)
- Choose a random word
- Attemps = 6
- Loop attempts > 0
  - Display word
    - For each letter in scret word
      - If user guessed that letter
        Print it
        Else
        print _
  - Ask the user to enter a letter
  - Validate input
    - Single character
    - Only a - z
    - Not duplicate
  - If letter is in the scret word
    - Print good guess
    - Check if word is guessed
      - For each letter in secret word
        - If letter is not in the list of guessed letter
          - The word is not guessed
      - Print congratulations 
      - Break
  - Else 
    Print wrong attempts
    decress attemps 
    