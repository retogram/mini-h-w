import random

while True:

    def hangman():
        list_ = ["cracker", "hacker", "warez", "pirate", "pentest"]
        int_rand = random.randint(0, 4)
        word = list_[int_rand]

        wrong_guesses = 0
        stages = [
            "░█░█░█░█▀▀▀░█░░░░█▀▀▀░█▀▀█░█▀█▀█░█▀▀▀░ ",
            "░█░█░█░█▀▀▀░█░░░░█░░░░█░░█░█░█░█░█▀▀▀░ ",
            "░▀▀▀▀▀░▀▀▀▀░▀▀▀▀░▀▀▀▀░▀▀▀▀░▀░▀░▀░▀▀▀▀░"
        ]
        stages1 = [
            "", "------------------------", "___░██▓███░░░███▓██░",
            "__ ░██▓░░▓██░██▓░░▓██░", "_░██▓░░░░▓███▓░░░░▓██░",
            "_░██▓░░░░░▓█▓░░░░░▓██░", "__ ░██▓░░░░░░░░░░░░▓██░",
            "____░██▓░░░░░░░██░▓██░", "______ ░██▓░░░░██▓██░",
            "________██_██▓░███▌▐█", "______ ███ __██▓███▌██▌",
            "______███______████▐██▌", "_____████_____████▐███",
            "_____████___████▐████▐██", "____██████████▐████▐███",
            "___██████████▐████▐███▌", "__███████████████▐███▌",
            "█▐██████████████▐███......"
        ]
        stages2 = [
            "", "──────▐▀▄─────────▄▀▌", "──────▐▓░▀▄▀▀▀▀▀▄▀░▓▌",
            "──────▐░▓░▄▀░░░▀▄░▓░▌", "───────█░░▌█▐░▌█▐░░█",
            "────▄▄▄▐▀░░░▀█▀░░░▀▌▄▄▄", "───█▐▐▐▌▀▄░▀▄▀▄▀░▄▀▐▌▌▌█"
        ]
        stages3 = [
            "░░░░░░░░░░░░▄▐", "░░░░░░▄▄▄░░▄██▄", "░░░░░▐▀█▀▌░░░░▀█▄",
            "░░░░░▐█▄█▌░░░░░░▀█▄", "░░░░░░▀▄▀░░░▄▄▄▄▄▀▀", "░░░░▄▄▄██▀▀▀▀",
            "░░░█▀▄▄▄█░▀▀", "░░░▌░▄▄▄▐▌▀▀▀", "▄░▐░░░▄▄░█░▀▀", "▀█▌░░░▄░▀█▀░▀",
            "░░░░░░░▄▄▐▌▄▄", "░░░░░░░▀███▀█░▄", "░░░░░░▐▌▀▄▀▄▀▐▄",
            "░░░░░░▐▀░░░░░░▐▌", "░░░░░░█░░░░░░░░█", "░░░░░▐▌░░░░░░░░░█",
            "░░░░░█░░░░░░░░░░▐▌"
        ]
        remaining_letters = list(word)
        letter_board = ["__"] * len(word)
        win = False
        for welcome in stages:
            print(welcome)
        print('''the gallows game begins, if you win, you will receive a reward
There are only 5 words in this game so far, but I will ask 5 questions.Let's start
1.A person hacking protection systems (in particular software protection.)
2.An extremely qualified IT specialist, a person who understands the very depths of computer systems.
3.Products protected by copyright and distributed illegally.
4.A person who uses stolen computer products
5.A method of assessing the security of computer systems or networks by means of modeling an attacker's attack.'''
              )
        while wrong_guesses < len(stages2) - 1:
            print('\n')
            guess = input("Enter the letter: ")
            if guess in remaining_letters:
                character_index = remaining_letters.index(guess)
                letter_board[character_index] = guess
                remaining_letters[character_index] = '$'
            else:
                wrong_guesses += 1
            print((' '.join(letter_board)))
            print('\n'.join(stages2[0:wrong_guesses + 1]))
            if '__' not in letter_board:
                word_win = (' '.join(letter_board))
                print(
                    f"The word was made up: {word_win}. You've won! Get your ass"
                )
                for ass in stages1:
                    print(ass)
                win = True
                break

        if not win:
            print("You've lost! The word was made up: {}".format(word))
            for lose in stages3:
                print(lose)

    hangman()
    ready = input('''STOP the game, press:X
to continue, press any button ''')
    if ready == 'X':
        break