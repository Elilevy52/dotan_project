def welcome_to():
    """Displays the ASCII art for the Hangman game and the maximum number of tries allowed.
    Creates a welcome screen
    :return: The Hangman ASCII art and the maximum number of tries allowed.
    :rtype: str
    """
    MAX_TRIES = 6

    HANGMAN_ASCII_ART = ("Welcome to hangman" + "\033[36m" + r"""



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
    return HANGMAN_ASCII_ART + "\n" + str(MAX_TRIES)


def print_hangman(num):
    """Prints the ASCII art for the Hangman game based on the number of incorrect guesses.
      :param num: the number of incorrect guesses
      :type num: int
      :return: None
      """
    HANGMAN_PHOTOS = {
        1: "x-------x",
        2: """x-------x
|
|
|
|
|""",
        3: """x-------x
|       |
|       0
|
|
|""",
        4: """x-------x
|       |
|       0
|       |
|
|""",
        5: "\033[32m" + """x-------x
|       |
|       0
|      /|\\
|
|""" + "\033[0m",
        6: "\033[33m" + """x-------x
|       |
|       0
|      /|\\
|      /
|""" + "\033[0m",
        7: "\033[31m" + """x-------x
|       |
|       0
|      /|\\
|      / \\
|""" + "\033[0m"
    }
    print(HANGMAN_PHOTOS[num])


def choose_word(file_path, index):
    """Returns a word from a specified index in a file.
        Reads a file and splits the contents into a list of words. Returns the word at the given index
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
    """Checks if guessed letter is a valid input and adds it to the list of old letters guessed if valid.
        :param letter_guessed: the letter guessed by the user
        :param old_letters_guessed: the list of previous letters guessed by the user
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: True if the letter is valid and was added to the old letter list, False otherwise
        :rtype: bool
        """
    result = check_valid_input(letter_guessed, old_letters_guessed)
    if result:
        old_letters_guessed.append(letter_guessed.lower())
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


def start():
    """Starts the game by asking the player for a file path and index
    and using the choose_word function as the secret_word parameter for the
    game function witch run the hangman game
    Also keeping the current path for future option for the player to keep playing with same words file
    :return: None"""

    path = input("Enter a file path: ")
    current_path = path
    ind = int(input("Enter index: "))
    game(choose_word(path, ind).lower(), current_path)


def end_game_manu(current_path):
    """Gets input from the player and runs accordingly.
    If '1' pressed, restarting the game from beginning.
    If '2' pressed, restarting with existing file using current_path param,
    and gets an input of a new(or same) index.
    If '3' pressed, exits
    else, shortly reminds the player his options
    :param current_path: contains the path to the chosen by player file
    :type current_path:str
    :return:None or exit code"""

    next_step = input("""So...what is it, boss ? """)
    if next_step == "1":
        start()
    elif next_step == "2":
        ind = int(input("Ok,enter index and let's start over: "))
        game(choose_word(current_path, ind).lower(), current_path)
    elif next_step == "3":
        return exit(0)
    else:
        print("Type in '1' if you want to restart,"
              "'2' if you want to restart with the last file "
              "and '3' if you want to exit")
        end_game_manu(current_path)


def game(secret_word, current_path):
    r"""Starts the game with the secret word.
    Based on number of wrong tries by the player
    printing word length , and the hangman ascii art on current status
    Use show_hidden_word function to reveal the letters one by one
    and start the game by ask the player for a letter guess, checks validation
    and accordingly revealing the advanced hidden word
    or increasing num_of_tries by one
    and printing how much lives left and an advanced hangman.
    If the player guessed the word correctly prints 'win' in ascii art,
    and if he runs out of life prints 'lose' in ascii art.
    Afterward printing the player the proceeding options
    and use end_game_manu function with current_path param to run accordingly.
    :param secret_word: contains the current secret word
    :param current_path: contains the path to the chosen by player file
    :type secret_word: str
    :type current_path: str
    :return:None \ exit code(0)
    """

    print("\n the length of your word is {} letters\n".format(str(len(secret_word))))
    print_hangman(1)
    old_letters_guessed = []
    num_of_tries = 1
    MAX_TRIES = 6
    print("\n", show_hidden_word(secret_word, old_letters_guessed), "\n")
    while num_of_tries < 7:
        letter_guessed = input("\nGuess a letter: ").lower()
        letter_check = try_update_letter_guessed(letter_guessed, old_letters_guessed)

        if letter_check and letter_guessed not in secret_word:
            print("{} ♥".format(str(MAX_TRIES - num_of_tries)))
            num_of_tries += 1
            print("):")
            print_hangman(num_of_tries)
        elif letter_check and letter_guessed in secret_word:
            print("\n", show_hidden_word(secret_word, old_letters_guessed))

        if check_win(secret_word, old_letters_guessed):
            print("""
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
         ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀ 
         
Congratulations, you won! What's your next move, oh great champion?
1. Restart the game
2. Restart the game with your last picked file and enter a new index 
3. exit""")
            end_game_manu(current_path)

        if num_of_tries == 7:
            print("""

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
         ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
        
Listen up champ, I need to know -
are you gonna keep playing this game like a pro 
or wave the white flag and admit defeat like a soggy burrito?
1. Restart the game
2. Restart the game with your last picked file (you can pick the same index again for the same word, 
or you can be random and try your luck) 
3. exit""")
            end_game_manu(current_path)


def main():
    print('\n\n', welcome_to(), '\n\n')
    start()


if __name__ == "__main__":
    main()

# 99 foods and companies C:\Users\zolta\OneDrive\שולחן העבודה\תיכנות\hangman\random words\99 foods and companies.txt
