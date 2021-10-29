import string
import random

"""WELCOME TO THE PYTHON MYSTERY WORD GAME: DEMON MODE! A mysterious arrangement of blanks
is presented to the user, and they are asked to submit letters they believe would complete a word
which corresponds, in length, to the amount of blanks shown. The computer is trying to 'dodge'
their guesses by drawing from the largest pool of words that follows the pattern of the user's
input. A spooky twist on the traditional mystery word game! The user gets 8 guesses."""

def demon_word_game(file):

    """This function first calls generate_random_blanks_list which generates a random list of blanks that
    represents a word-length this user must try to pin the computer down on."""

    # The user is welcomed to the game.
    print('*************************************************************************')
    print('*      .-._                                                   _,-,      *')
    print('*       `._`-._                                           _,-\'_,\'       *')
    print('*          `._ `-._                                   _,-\' _,\'          *')
    print('*             `._  `-._        __.-----.__        _,-\'  _,\'             *')
    print('*                `._   `#==="""           """===#\'   _,\'                *')
    print('*                   `._/)  ._               _.  (\_,\'                   *')
    print('*                    )*\'     **.__     __.**     \'*(                    *')
    print('*                    #  .==..__  ""   ""  __..==,  #                    *')
    print('*                    #   `"._(_).       .(_)_."\'   #                    *')
    print('*************************************************************************')



    print(
        "WELCOME TO THE MYSTERY WORD GAME: DEMON EDITION! In this game, you will try to pin down the demon by guessing letters with the goal of completing a word!"
    )
    print("Correctly complete the word, and you will win!")
    print("Your letter submissions will need to be in lowercase.")
    print("At any time, type QUIT to exit.")

    with open(file) as text:
        content = text.read()
        formatted_content = content.replace(string.punctuation, "")
        word_list = (
            formatted_content.replace("-", " ")
            .replace("—", " ")
            .replace(".", "")
            .replace(",", "")
            .replace(":", "")
            .replace("'", "")
            .replace('"', "")
            .replace("-\n", "")
            .lower()
            .split()
        )

    user_quit = False

    difficulty = difficulty_selection()
    blanks_list = list(generate_word_length(difficulty))
    length_list = [word for word in word_list if len(word) == len(blanks_list)]

    guessed_letter_list = []
    incorrect_correct_guess_counter = 0

    print(blanks_list)

    # The user is prompted to make a guess. The prompts will continue to come so long as the incorrect_correct_guess_counter
    # is less than 8 or there are still "_" characters in the blanks_list.

    while (
        incorrect_correct_guess_counter < 8
        and "_" in blanks_list
        and user_quit is False
    ):
        guess = input("Please make a guess: ")
        if guess == "QUIT":
            user_quit = True
        # This checks to see if the user input was a letter.
        elif (
            len(guess) != 1
            or guess in string.punctuation
            or guess in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        ):
            print("Ooooooh... I'm so sorry that was not a letter.")
        else:
            # If the user guessed a letter correctly, the blanks list is updated with that letter at corresponding
            # indices.
            if guess.isupper() == True:
                print("Please submit a letter in lower-case.")

# --------------------------------------------------------------------------------------------------------------------------------

            else:
                length_list = guess_received_reference_segmented(guess, length_list, len(blanks_list))
                sample = random.choice(length_list)

                ##Need to remove words in the length list that don't match the pattern of the randomly selected sample.
                
                print(length_list)
                print(sample)
                if guess in sample:
                    for i in range(len(blanks_list)):
                        if sample[i] == guess:
                            blanks_list[i] = guess
                    guessed_letter_list.append(guess)
                    print(
                        f"Nice Work! You guessed correctly! Here's what you know about the word so far: {blanks_list}"
                        )
                    print(f"Here are the letters you've so far: {guessed_letter_list}")
                else:
                    guessed_letter_list.append(guess)
                    incorrect_correct_guess_counter += 1
                    print(
                        f"Shucks! Not in the word! Here's what you know about the word so far: {blanks_list}"
                    )
                    print(f"Here are the letters you've so far: {guessed_letter_list}")
                    print(
                        f"You have {8 - incorrect_correct_guess_counter} guesses left."
                    )

#--------------------------------------------------------------------------------------------------------------------------


def difficulty_selection():

    """This function returns the difficulty the user has selected, or quits them out of the game
    or prompts them to provide input again."""

    selector_flag = True
    while selector_flag == True:
        difficulty_selector = input(
            "Please select either HARD, NORMAL, or EASY difficulty: "
        )

        if difficulty_selector in ["QUIT", "HARD", "NORMAL", "EASY"]:
            selector_flag = False
            return difficulty_selector
        else:
            print("I'm sorry, I didn't recognize that input.")


def generate_word_length(difficulty):

    """This function opens the text file, removes all punctuation, converts it
    to lowercase, creates a list where each word is an index, and selects a random
    word from the list."""



    if difficulty == "QUIT":
        print("Thanks for playing!")
        quit()
    elif difficulty == "EASY":
        easy_list = []
        for idx in range(random.randint(4, 6)):
            easy_list.append("_")    
        return easy_list
    elif difficulty == "NORMAL":
        normal_list = []
        for idx in range(random.randint(6, 8)):
            normal_list.append("_")    
        return normal_list
    elif difficulty == "HARD":
        hard_list = []
        for idx in range(random.randint(8, 10)):
            hard_list.append("_")    
        return hard_list

def guess_received_reference_segmented(letter, reference, length):

    """This function takes in the user's guess, breaks the reference into groups based
    on the index position of the user's guess, and selects the largest of those groups as the
    next point of reference."""

    index_at_dictionary = {}

    for i in range(length + 1):
        index_at_dictionary[i] = []

    for word in reference:
        if letter not in word:
            index_at_dictionary[length].append(word)
        else:
            for i in range(length):
                if word[i] == letter:
                    index_at_dictionary[i].append(word)
    
    return index_at_dictionary[max(index_at_dictionary, key = index_at_dictionary.get)]


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Get the word frequency in a text file."
    )
    parser.add_argument("file", help="file to read")
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        demon_word_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

"""print(
                        f"Nice Work! You guessed correctly! Here's what you know about the word so far: {blanks_list}"
                    )
print(f"Here are the letters you've so far: {guessed_letter_list}")
print(
                        f"You have {8 - incorrect_correct_guess_counter} guesses left."
                    )
print(
                        f"Shucks! Not in the word! Here's what you know about the word so far: {blanks_list}"
                    )
print("Thanks for playing!")
print("Congratulations! You've guessed the mystery word!")
print("Bummer!! You ran out of guesses!")"""