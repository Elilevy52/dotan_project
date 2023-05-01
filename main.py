NAME = input("Choose your nickname: ")

MAX_TRIES = 6

HANGMAN_ASCII_ART = ("Welcome to hangman, {}".format(NAME) + "\033[36m" + r"""
__/\\\________/\\\______/\\\\\\\\\______/\\\\\_____/\\\______/\\\\\\\\\\\\___/\\\\____________/\\\\______/\\\\\\\\\______/\\\\\_____/\\\_
 _\/\\\_______\/\\\____/\\\\\\\\\\\\\___\/\\\\\\___\/\\\____/\\\//////////___\/\\\\\\________/\\\\\\____/\\\\\\\\\\\\\___\/\\\\\\___\/\\\_
  _\/\\\_______\/\\\___/\\\/////////\\\__\/\\\/\\\__\/\\\___/\\\______________\/\\\//\\\____/\\\//\\\___/\\\/////////\\\__\/\\\/\\\__\/\\\_
   _\/\\\\\\\\\\\\\\\__\/\\\_______\/\\\__\/\\\//\\\_\/\\\__\/\\\____/\\\\\\\__\/\\\\///\\\/\\\/_\/\\\__\/\\\_______\/\\\__\/\\\//\\\_\/\\\_
    _\/\\\/////////\\\__\/\\\\\\\\\\\\\\\__\/\\\\//\\\\/\\\__\/\\\___\/////\\\__\/\\\__\///\\\/___\/\\\__\/\\\\\\\\\\\\\\\__\/\\\\//\\\\/\\\_
     _\/\\\_______\/\\\__\/\\\/////////\\\__\/\\\_\//\\\/\\\__\/\\\_______\/\\\__\/\\\____\///_____\/\\\__\/\\\/////////\\\__\/\\\_\//\\\/\\\_
      _\/\\\_______\/\\\__\/\\\_______\/\\\__\/\\\__\//\\\\\\__\/\\\_______\/\\\__\/\\\_____________\/\\\__\/\\\_______\/\\\__\/\\\__\//\\\\\\_
       _\/\\\_______\/\\\__\/\\\_______\/\\\__\/\\\___\//\\\\\__\//\\\\\\\\\\\\/___\/\\\_____________\/\\\__\/\\\_______\/\\\__\/\\\___\//\\\\\_
        _\///________\///___\///________\///___\///_____\/////____\////////////_____\///______________\///___\///________\///___\///_____\/////__
        """ + "\033[0m")

HANGMAN_PHOTOS = {
    0: "x-------x",

    1: """x-------x
|
|
|
|
|""",

    2: """x-------x
|       |
|       0
|
|
|""",

    3: """x-------x
|       |
|       0
|       |
|
|""",

    4: "\033[32m" + """x-------x
|       |
|       0
|      /|\\
|
|""" + "\033[0m",

    5: "\033[33m" + """x-------x
|       |
|       0
|      /|\\
|      /
|""" + "\033[0m",

    6: "\033[31m" + """x-------x
|       |
|       0
|      /|\\
|      / \\
|""" + "\033[0m"}

WIN_SCENARIO = "\033[32m" + """
         ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
        ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
        ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌
        ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌
        ▐░▌   ▄   ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌
        ▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌
        ▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌
        ▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌
        ▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌
        ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌
         ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀ """ + "\033[0m"

LOSE_SCENARIO = "\033[31m" + """

         ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
        ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
        ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
        ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          
        ▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
        ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
        ▐░▌          ▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
        ▐░▌          ▐░▌       ▐░▌          ▐░▌▐░▌          
        ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
         ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """ + "\033[0m"

WINNING = """\nCongratulations {}, you won! What's your next move, oh great champion?
1. Restart to main manu
2. Pick a new file to upload and play with.
3. Restart the game with the same file and enter a new index 
4. exit """.format(NAME)

LOSING = """\nListen up champ, I need to know -
are you gonna keep playing this game like a pro 
or wave the white flag and admit defeat like a soggy burrito?
1. Restart to main manu
2. Pick a new file to upload and play with.
3. Restart the game with the same file (you can pick the same index again for the same word, 
or you can be random and try your luck) 
4. exit """


def welcome_to():
    """Displays the ASCII art for the Hangman game and the maximum number of tries allowed.
    Creates a welcome screen
    :return: None
    """
    print("\n\n {} \n {} \n\n".format(HANGMAN_ASCII_ART, MAX_TRIES))


def print_hangman(num):
    """Prints the ASCII art for the Hangman game based on the number of incorrect guesses.
      :param num: the number of incorrect guesses
      :type num: int
      :return: None
      """
    print(HANGMAN_PHOTOS[num])


def choose_word(file_path, index):
    """Returns a word from a specified index in a file.
        Reads a file and splits the contents into a list of words.
        If the given index is greater than the length of the word list, it calculates the remainder of the
        index divided by the length of the word list and returns the word at the resulting index.
        :param file_path: the path to the file containing the words
        :param index: the index of the word to be returned
        :type file_path: str
        :type index: int
        :return: the word at the specified index in the file
        :rtype: str
        """

    with open(file_path, 'r') as data_base:
        fid = data_base.read()
        word_list = fid.split()

    if index <= len(word_list):
        secret_word = word_list[index - 1]
        return secret_word

    if index > len(word_list):
        x = index % len(word_list)
        secret_word = word_list[x - 1]
        return secret_word


def show_hidden_word(secret_word, old_letters_guessed):
    """Returns the unrevealed word with letters that has been guessed and underscores
    :param secret_word: the secret word
    :param old_letters_guessed: a list of letters that have been guessed
    :type secret_word: string
    :type old_letters_guessed: list
    :return: a string with underscores, and letters in the word that have already been guessed.
    :rtype: string
    """

    fixed_list = []

    for letter in secret_word:
        if letter in old_letters_guessed:
            fixed_list.append(letter)

        else:
            fixed_list.append("_")

    return " ".join(fixed_list)


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the input letter is valid for the game.
    If the letter is only 1 char in English and not have already been guessed.
    :param letter_guessed: the letter to be checked
    :param old_letters_guessed: a list of letters that were already guessed in previous turns
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the letter is a valid input, False otherwise
    :rtype: bool
    """
    if letter_guessed.lower() in old_letters_guessed:
        return False

    if letter_guessed.encode().isalpha() and len(letter_guessed) == 1:
        return True

    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Getting the result if the letter guessed is valid input or not
    and accordingly Appending valid letter to old_letters_guessed list or printing "X"
    and the letters that have been guessed sorted with arrows between.
    :param letter_guessed: the letter guessed by the user
    :param old_letters_guessed: the list of previous letters guessed by the user
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the letter is valid and was added to the old letter list, False otherwise
    :rtype: bool
    """
    result = check_valid_input(letter_guessed, old_letters_guessed)

    if result:
        old_letters_guessed.append(letter_guessed)
        return True

    else:
        print("\033[31m" + "X" + "\033[0m"), print(" -> ".join(sorted(old_letters_guessed)))
        return False


def check_win(secret_word, old_letters_guessed):
    """Check if all the letters in the secret word have been guessed by the player.
    :param secret_word: The secret word that the player is trying to guess
    :type secret_word: str
    :param old_letters_guessed: A list containing all the letters that the player has guessed so far
    :type old_letters_guessed: list
    :return: True if all the letters in the secret word have been guessed, False otherwise
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def upload_file():
    """Asks for player's chosen file path and index.
    and activates the game with the chosen secret word
    Also keeping the current path for future option for the player to stay with the same file
    :return: None"""
    path = input("Enter a file path: ")
    current_path = path
    ind = int(input("Enter index: "))
    secret_word = choose_word(path, ind).lower()
    game(secret_word, current_path)


def system_word_list():
    """Using the word_list.txt file inside this folder as the file to pick word from.
    And activates the game with the chosen secret word.
    :return: None"""
    with open("word_list.txt", "r") as data_base:
        fid = data_base.read()
        word_list = fid.split()
        index = int(input("Fun! \nNow enter an index: "))

    if index <= len(word_list):
        secret_word = word_list[index - 1]
        game(secret_word, "")

    if index > len(word_list):
        x = index % len(word_list)
        secret_word = word_list[x - 1]
        game(secret_word, "")


def main_manu():
    """Asking the player to choose between the system word list or file of his own to play with
    and activates accordingly
    :return: None
    """
    player_pick = input("Hi, {}.\nyour'e options are:\n1.play with your file.\n"
                        "2.play with a list of words from the system that contains:\n"
                        "foods, companies, brands, and animals, sounds easy? try!\nPlease, choose 1\\2: ".format(NAME))

    if player_pick == '1':
        upload_file()

    if player_pick == '2':
        system_word_list()


def game(secret_word, current_path):
    """Starts the game with the secret word.
      printing word length , and the hangman ascii art on current status
      Based on number of wrong tries.
      Use show_hidden_word function to reveal the letters one by one when guessed.
      And starts the game by asking the player for a letter guess, checks validation
      and accordingly revealing the advanced hidden word
      or printing how much lives left and an ":(" with advanced hangman.
      If the player guessed the whole word correctly prints 'win' in ascii art,
      and if he runs out of life prints 'lose' in ascii art.
      Afterward printing the proceeding options for the player to choose
      and use end_game_manu function with current_path param to get player request and run accordingly.
      :param secret_word: contains the current secret word
      :param current_path: contains the path to the chosen by player file
      :type secret_word: str
      :type current_path: str
      :return:None
      """

    num_of_tries = 0
    old_letters_guessed = []

    print_hangman(num_of_tries)

    print("\n{}, The length of your word is {} letters.\nEnjoy ☺.".format(NAME, len(secret_word)))

    print("\n {} \n".format(show_hidden_word(secret_word, old_letters_guessed)))

    while num_of_tries < MAX_TRIES:
        letter_guessed = input("\nGuess a letter: ").lower()
        letter_check = try_update_letter_guessed(letter_guessed, old_letters_guessed)

        if letter_check and letter_guessed not in secret_word:
            num_of_tries += 1
            print("{:d} ♥".format(MAX_TRIES - num_of_tries))
            print("):")
            print_hangman(num_of_tries)

        elif letter_check and letter_guessed in secret_word:
            print("\n {} \n ".format(show_hidden_word(secret_word, old_letters_guessed)))

        if check_win(secret_word, old_letters_guessed):
            print(WIN_SCENARIO, WINNING)
            end_game_manu(current_path)

        if num_of_tries == MAX_TRIES:
            print(LOSE_SCENARIO, LOSING)
            end_game_manu(current_path)


def end_game_manu(current_path):
    """This is additional function to the game.
    Gets input from the player and runs accordingly.
    If '1' pressed, restarting the game from beginning,
    if '2' pressed, letting the player upload a new file
    If '3' pressed, restarting with existing file using current_path param,
    and gets an input of a new(or same) index.
    If '4' pressed, exits
    else, shortly reminds the player his options
    :param current_path: contains the path to the chosen by player file
    :type current_path:str
    :return:None or exit code"""

    next_step = input("""So...what is it, boss ? """)

    if next_step == "1":
        main_manu()

    elif next_step == "2":
        upload_file()

    elif next_step == "3":
        if current_path == "":
            system_word_list()
        else:
            ind = int(input("Ok {},enter index and let's start over: ".format(NAME)))
            secret_word = choose_word(current_path, ind).lower()
            game(secret_word, current_path)

    elif next_step == "4":
        print("Goodbye, {}".format(NAME))
        return exit(0)

    else:
        print("{}, Please type in '1' if you want to go to main manu,"
              "'2' if you want to upload a new file to play with,"
              "'3' if you want to restart with the last file, "
              "and '4' if you want to exit the game".format(NAME))
        end_game_manu(current_path)


def main():
    welcome_to()
    main_manu()


if __name__ == "__main__":
    main()
