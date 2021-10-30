import string
import random

"""WELCOME TO THE PYTHON MYSTERY WORD GAME: DEMON MODE! A mysterious arrangement of blanks
is presented to the user, and they are asked to submit letters they believe would complete a word
which corresponds, in length, to the amount of blanks shown. The computer is trying to 'dodge'
their guesses by drawing from the largest pool of words that follows the pattern of the user's
input. A spooky twist on the traditional mystery word game! The user gets 8 guesses."""


def demon_word_game(file):

    """This, for all intents and purposes, is the main() function of the program. The function first calls generate_random_blanks_list
    which generates a random list of blanks that represents a word-length this user must try to pin the computer down on based on difficulty.
    EASY is 4-5 letters long, NORMAL is 6-7 letters long, and HARD is 8 plus letters. It then instantiates a number of variables including
    the blanks_list itself, the difficulty the user selected, and the reference for all words in the words.txt file which match the length
    generated by the game. The program proceeds to function in an input loop, which will be discussed in greater detail later."""

    # The user is welcomed to the game.
    print("*************************************************************************")
    print("*      .-._                                                   _,-,      *")
    print("*       `._`-._                                           _,-'_,'       *")
    print("*          `._ `-._                                   _,-' _,'          *")
    print("*             `._  `-._        __.-----.__        _,-'  _,'             *")
    print('*                `._   `#==="""           """===#\'   _,\'                *')
    print("*                   `._/)  ._               _.  (\_,'                   *")
    print("*                    )*'     **.__     __.**     '*(                    *")
    print('*                    #  .==..__  ""   ""  __..==,  #                    *')
    print('*                    #   `"._(_).       .(_)_."\'   #                    *')
    print("*************************************************************************")

    print(
        "WELCOME TO THE MYSTERY WORD GAME: DEMON EDITION! In this game, you will try to pin down the demon by guessing letters with the goal of completing a word!"
    )
    print("Correctly complete the word, and you will win!")
    print(
        "Your letter submissions will need to be in lowercase. YOU MAY NEED TO GUESS THE SAME LETTER TWICE!"
    )
    print("At any time, type QUIT to exit.")
    print(("*******************************************************"))
    print(("*******************************************************"))

    # The words.txt file is read in as a list of words.
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

    # This is the list of words filtered for the length selected by the generate_word_length() function.
    length_list = [word for word in word_list if len(word) == len(blanks_list)]

    # This is a list that stores and tracks all guessed letters.
    guessed_letter_list = []

    # Incorrect guesses start at 0. The game ends when this counter hits 8.
    incorrect_correct_guess_counter = 0

    # This print is to let the user know how many letters they need to fill.
    print(blanks_list)

    # The user is prompted to make a guess. The prompts will continue to come so long as the incorrect_correct_guess_counter
    # is less than 8 or there are still "_" characters in the blanks_list.

    # This while loop sets the conditions for user input. It will end when either: 8 incorrect guesses have been submitted, the
    # blanks are all solved for, or the user types 'QUIT' when prompted.

    while (
        incorrect_correct_guess_counter < 8
        and "_" in blanks_list
        and user_quit is False
    ):

        # The first set of conditions are set up to filter for input that is not a letter.
        guess = input("Please make a guess: ")
        if guess == "QUIT":
            user_quit = True
        # This checks to see if the user input was a letter.
        elif (
            len(guess) != 1
            or guess in string.punctuation
            or guess in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        ):
            print("**********************************************")
            print("Ooooooh... I'm so sorry that was not a letter.")
            print("**********************************************")
        else:
            if guess.isupper() == True:
                print("*************************************")
                print("Please submit a letter in lower-case.")
                print("*************************************")
            else:
                # If the user submits a lower-case letter, the guess_received_reference_segmented function runs.
                # Length_list is updated with each new submission.
                length_list = guess_received_reference_segmented(
                    guess, length_list, len(blanks_list)
                )
                # This checks to see if the list holding words not containing the letter was the longest, and
                # therefor, an incorect guess.
                print(length_list)
                if length_list[-1] == len(blanks_list):
                    guessed_letter_list.append(guess)
                    incorrect_correct_guess_counter += 1
                    print(
                        "************************************************************************************************"
                    )
                    print(
                        f"Shucks! Not in the word! Here's what you know about the word so far: {blanks_list}"
                    )
                    print(f"Here are the letters you've so far: {guessed_letter_list}")
                    print(
                        f"If you make {8 - incorrect_correct_guess_counter} more incorrect guesses, the word demon wins."
                    )
                    print(
                        "************************************************************************************************"
                    )
                    length_list.pop()
                    length_list.pop()
                else:

                    # The following two conditions check to see if the letter guess has been guessed already and if it reveals
                    # a new letter in the blanks_list.
                    if guess in guessed_letter_list:
                        if blanks_list[length_list[-1]] == "_":
                            blanks_list[length_list[-1]] = guess
                            guessed_letter_list.append(guess)
                            print(
                                "************************************************************************************************"
                            )
                            print(
                                f"Nice Work! You guessed correctly! Here's what you know about the word so far: {blanks_list}"
                            )
                            print(
                                f"Here are the letters you've so far: {guessed_letter_list}"
                            )
                            print(
                                "************************************************************************************************"
                            )
                            length_list.pop()
                            length_list.pop()
                        else:
                            incorrect_correct_guess_counter += 1
                            print(
                                "************************************************************************************************"
                            )
                            print(
                                f"Shucks! That didn't narrow down the field! Here's what you know about the word so far: {blanks_list}"
                            )
                            print(
                                f"Here are the letters you've so far: {guessed_letter_list}"
                            )
                            print(
                                f"If you make {8 - incorrect_correct_guess_counter} more incorrect guesses, the word demon wins."
                            )
                            print(
                                "************************************************************************************************"
                            )
                            length_list.pop()
                            length_list.pop()
                    else:
                        blanks_list[length_list[-1]] = guess
                        guessed_letter_list.append(guess)
                        print(
                            "************************************************************************************************"
                        )
                        print(
                            f"Nice Work! You guessed correctly! Here's what you know about the word so far: {blanks_list}"
                        )
                        print(
                            f"Here are the letters you've so far: {guessed_letter_list}"
                        )
                        print(
                            "************************************************************************************************"
                        )
                        length_list.pop()
                        length_list.pop()

    # The following are the game-end conditions.
    if user_quit == True:
        print("Thanks for playing!")
        print("**********************************************************")
        print("Credits: ASCII Demon Art by Deelkar via ASCII Art Archive.")
        print("**********************************************************")
    elif "_" not in blanks_list:
        print("**********************************************************")
        print("Congratulations! You've trapped the word demon!")
        print("**********************************************************")
        print("Credits: ASCII Demon Art by Deelkar via ASCII Art Archive.")
        print("**********************************************************")
    else:
        print("**********************************************************")
        print("Bummer!! You ran out of guesses!")
        print("**********************************************************")
        print("Credits: ASCII Demon Art by Deelkar via ASCII Art Archive.")
        print("**********************************************************")


def difficulty_selection():

    """This function returns the difficulty the user has selected, or quits them out of the game
    or prompts them to provide input again."""

    selector_flag = True
    while selector_flag == True:
        difficulty_selector = input(
            "Please select either HARD, NORMAL, or EASY difficulty: "
        )

        if difficulty_selector in ["QUIT", "HARD", "NORMAL", "EASY"]:

            # The while-loop will only break if the user selects a valid dificulty or quits.
            selector_flag = False
            return difficulty_selector
        else:
            print("I'm sorry, I didn't recognize that input.")


def generate_word_length(difficulty):

    """This function generates a list of blanks with a length based on the difficulty the user selected."""

    if difficulty == "QUIT":
        print("Thanks for playing!")
        print("**********************************************************")
        print("Credits: ASCII Demon Art by Deelkar via ASCII Art Archive.")
        print("**********************************************************")
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
    next point of reference (including the group that represents words that do not have that letter)."""

    # I decided to use a dictionary to store groups of words based on index points of where the guessed guessed
    # letter was or if it did not exist in the word.
    index_at_dictionary = {}

    # This generates an amount of keys equal to the word length +1 (for words without the letter), all with values
    # equal to blank lists.
    for i in range(length + 1):
        index_at_dictionary[i] = []

    # For each word in the list of words given to the function, this loop looks at where the letter is or isn't, and
    # appends the keys in the created dictionary based on that positioning.
    for word in reference:
        if letter not in word:
            index_at_dictionary[length].append(word)
        else:
            for i in range(length):
                if word[i] == letter:
                    index_at_dictionary[i].append(word)

    #'word_families' is a list that contains each word family list, 'family_count' is a list that counts the length of each family.
    # The word family with the longest length is then sorted for and returned as a list with where the guess appears, by index, in
    # the word family's position (or the length of the word family if the largest family does not contain the letter).

    word_families = []

    for key in index_at_dictionary:
        word_families.append(index_at_dictionary[key])

    family_count = [len(i) for i in word_families]
    max_count = max(family_count)
    index_max = family_count.index(max_count)

    if index_max == length:
        word_families[length].append(max_count)
        word_families[length].append(length)
        result = word_families[length]
    else:
        word_families[index_max].append(max_count)
        word_families[index_max].append(index_max)
        result = word_families[index_max]

    # The key with the largest list, by length, is selected and its reference is appended to the end of the list for use later.
    return result


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
