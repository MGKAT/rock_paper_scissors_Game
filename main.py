"""
This is a simple rock-paper-scissors game where you can play against the computer or
 with other player.
"""
import random
import time
import os
try:
    from easygui import passwordbox
    from easygui import msgbox
except ImportError:
    pass

our_choices = ["rock", "paper", "scissors"]
GREEN = "\033[0;32m"


def valid_answer(answer):
    """
    Check if the provided answer is a valid choice.

    :param answer: string -- The player choice.
    :return: string -- The player choice.
    """
    return answer in our_choices


def winner_answers(answer1, answer2):
    """
    Determine the winner between two choices.

    :param answer1: string -- The first player's choice
    :param answer2: string -- The second player's choice.
    :return: bool -- True if the answer1 win, False if is not.
    """
    if answer1 == "rock" and answer2 == "scissors":
        return True
    if answer1 == "paper" and answer2 == "rock":
        return True
    if answer1 == "scissors" and answer2 == "paper":
        return True
    return False


def equal_answers(answer1, answer2):
    """
    Check if choice result in a tie.

    :param answer1: string -- The first player's choice
    :param answer2: string -- The second player's choice.
    :return: bool -- True if the answer1 win, None if is not.
    """
    if answer1 == answer2:
        return True
    return None


def clear_console():
    """
    Clear the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def player_choice():
    """
    Get the player choice from user input.

    :return: string -- The player choice.
    """
    choice_player = input("Type your choice: ")
    return choice_player


def display_result(player_choice1, computer_choice):
    """
    Display the result

    :param player_choice1: string -- The player choice.
    :param computer_choice: string -- The computer choice.
    :return: string -- message indicating the result of the party.
    """
    if equal_answers(player_choice1, computer_choice):
        return "IT'S A TIE!!!"
    if winner_answers(player_choice1, computer_choice):
        return f"{player_choice1} beats {computer_choice}\nYou WIN!!!"
    return f"{computer_choice} beats {player_choice1}\nYOU LOOSE"


def get_choice():
    """
    Get the player choice from user input.

    :return: string -- The player choice.
    """
    choice = player_choice()
    while not valid_answer(choice):
        print(f"Not a valid option, expecting: {our_choices}")
        choice = player_choice()
    return choice


def get_choice_getpass():
    """
    Get the player choice anad hidden in
    :return:
    """
    choice = passwordbox("Enter your choice: ", title="Player 1")
    while not valid_answer(choice):
        msgbox(f"Not a valid option, expecting: {our_choices}", title="Invalid choice")
        choice = passwordbox("Enter your choice: ", title="Player 1")
    return choice


def play_round():
    """
    Play a round game

    :return: None
    """
    choice_player1 = get_choice()

    print("you choose: ", choice_player1)
    time.sleep(0.5)
    print("computer is thinking...")
    time.sleep(1)
    pc_answer = random.choice(our_choices)
    print("computer choose: ", pc_answer)
    print('\n')

    result_message = display_result(choice_player1, pc_answer)
    print(result_message)


def play_round_another_player():
    """
    Play a round between two players.

    :return: None
    """
    print("Player 1 turn: ")
    choice_player1 = get_choice_getpass()

    print("Player 2 turn: ")
    choice_player2 = get_choice()

    print("Player 1 choose:", choice_player1)
    print("Player 2 choose:", choice_player2)

    result_message = display_result(choice_player1, choice_player2)
    print(result_message)


def menu():
    """
    Display the menu
    """
    print("""
    1. You Vs the AI
    2. You Vs another player
    3. Rules
    4. End
    """)


def rules():
    """
    Display the rules of the rock_paper_scissors game.
    :return: None
    """
    print("Rock crushes scissors.")
    print("Scissors cut paper.")
    print("Paper covers rock.")
    print("If both players choose the same option, it's a tie.")
    print("\nTo play:")
    print("1. Choose to play against the computer (option 1) or against another player (option2).")
    print("2. Enter your choice when prompted.")
    print("3. See the result of the round based on the rules.")
    print("\nEnjoy the game!")


def main():
    """
    Main function to run the rock-paper-scissors game.

    This function clears the console, displays the game title, and enters a loop for the game menu.
    The user can choose different options, including playing with AI or another player and checking
    the rules or ending the game.

    :return: str -- Message to display after.
    """
    clear_console()
    print(GREEN)
    print("### rock paper scissors game ###")
    running = True

    while running:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("\n### rock paper scissors game ###")
            play_round()
        elif choice == "2":
            play_round_another_player()
        elif choice == "3":
            rules()
        elif choice == "4":
            running = False
        else:
            print("Invalid choice. Please choose a correct number between 1 and 4.")

    # Message
    return "have a good day"


if __name__ == '__main__':
    main()
