
def get_random_word():
    import random
    def load_words():
        with open('words.txt', 'r') as f:
            line = f.readline()
        wordlist = line.split()
        print(" --- ", len(wordlist), "words loaded. --- ")
        print("")
        return wordlist

    wordlist = load_words()
    return random.choice(wordlist)

def generate_state(word, letters_guessed):
    output = ''
    for letter in word:
        if letter in letters_guessed:
            output += letter
        else:
            output += '_'
    return output

def num_guesses(nguess, letter, word):
    if letter in word:
        return nguess
    else:
        return nguess + 1

def play(word = get_random_word()):
    letters_guessed = ''
    guessing = True
    nguess = 0
    max_guess = 10

    while guessing and nguess < max_guess:
        print('-'*30)
        print('Guessed letters:', letters_guessed)
        print('Incorrect guesses left:', max_guess - nguess)
        print('Status:', generate_state(word, letters_guessed))
        guess = input('Please guess a letter: ')
        letters_guessed += guess
        nguess = num_guesses(nguess, guess, word)
        if not '_' in generate_state(word, letters_guessed):
            guessing = False

    print('-'*30)
    if not guessing:
        print('The word was:', word)
        print('You guessed it!')
        print('It took you', nguess, 'incorrect guesses!')
    else:
        print('You lost!')
        print('The word was:', word)
        print('Better luck next time.')

if __name__ == '__main__':
    play('fish')

    


    
