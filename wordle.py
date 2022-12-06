import random
import sys
from colorama import Fore, Style


def read_file(file_name):
    with open(file_name) as file: 
        words = file.readlines()
        return words

def ask_file_name():
    file_name = input("[leave empty to use words.txt for now] : ")
    if not file_name:
        return 'words.txt'
    return file_name

def select_random_word(words):
    random_index = random.randint(0, len(words)-1) #This line of code, makes the program choose a random word to use for the game
    word = words[random_index].strip()
    return word


def user_input():
    return input("Guess the 5 letter word: ")
    

def show_results(correct_digits_and_position, correct_digits_only, coloured_guess):
    """Show the results from one turn"""

    print(f'Number of correct letters in correct place:     ' 
                + str(correct_digits_and_position))
    print('Number of correct letters not in correct place: ' 
                + str(correct_digits_only))
    print(''.join(coloured_guess))


def show_word(word):
    """Show Code that was created to user"""

    print('The word was: '+str(word))

def check_correctness(correct_digits_and_position):
    """Checks correctness of answer and show output to user"""
    if correct_digits_and_position == 5:
        return True
    else:
        return False
        

def run_game(word):
    """Main function for running the game"""
    global guess
    global coloured_guess

    correct = False

    print(word)
    print("guess a 5 letter word, you have 12 tries! ")
    turns = 12
    while turns > 0:
        guess = user_input()
        #if len(guess) == 5:
        if guess == "quit" or guess == "exit":        #if the player enters quit or exit
            print("Bye!")
            break 
        else:
            if len(guess) == 5:
                correct_digits_and_position = 0
                correct_digits_only = 0
                coloured_guess = []
                for i in range(len(guess)):
                    if word[i] == guess[i]:
                        correct_digits_and_position += 1
                        coloured_guess.append(f'{Fore.GREEN}{guess[i]}{Style.RESET_ALL}')

                    elif word[i] in guess:
                        correct_digits_only += 1
                        coloured_guess.append(f'{Fore.YELLOW}{guess[i]}{Style.RESET_ALL}')

                    else:
                        coloured_guess.append(guess[i])


                correct = check_correctness(correct_digits_and_position)
                show_results(correct_digits_and_position, correct_digits_only, coloured_guess)
                turns -= 1
                if correct == True:
                    print('Congratulations! You win!')
                    break
                else:
                    print('Turns left: ' + str(turns))
            else:
                continue
        

    show_word(word)


if __name__ == "__main__":
    if len(sys.argv)>1:
        words_file = sys.argv[1]
    else:
        words_file = "words.txt"
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)

    run_game(selected_word)