"""
Test for the rock_paper_scissors game.

This module contains a series of unit tests for the functions of the rock_paper_scissors game.

Tests:
-`test_valid_answer`: Checks the validity of player choices.
-`test_winner_answers`: Verifies the logic for determining the winner between two choices.
-`test_equal_answers`: Tests the function for detecting a tie between two choices.
-`test_player_choice`: Ensures correct player input retrieval.
-`test_display_result`: Verifies the correct display of game results based on choice.
-`test_get_choice`: Tests the function for retrieving player choices.
-`test_get_choice_getpass`: Ensures the correct retrieval of a hidden player choice.
-`test_play_round`: Tests the main game round, verifying the player's victory based on
mocked computer choices.
-`test_play_round_another_player`: Verifies the interaction between two players in a game round.
-`test_clear_console`: Ensures the console is cleared appropriately.
-`test_menu`: Skipped test due to Tkinter issues in testing.
-`test_main`: Tests the main function of the game, simulating user input to exit the game.
"""
import os
from unittest.mock import patch
import pytest
from .main import (
    valid_answer,
    winner_answers,
    equal_answers,
    player_choice,
    display_result,
    get_choice,
    get_choice_getpass,
    play_round,
    play_round_another_player,
    menu,
    main,
    clear_console,
)


def test_valid_answer():
    """
    Checks whether the `valid_answer` function  correctly identifies choices.
    :return: None
    """
    assert valid_answer("rock")
    assert valid_answer("paper")
    assert valid_answer("scissors")
    assert not valid_answer("invalid_choice")


def test_winner_answers():
    """
    Verifies the correctness of the `winner_answers` function in determining the winner
     in different scenarios.
    :return: None
    """
    assert winner_answers("rock", "scissors")
    assert winner_answers("paper", "rock")
    assert winner_answers("scissors", "paper")
    assert not winner_answers("rock", "paper")


def test_equal_answers():
    """
    Checks if the `equal_answers` function correctly identifies when two choices result in a tie.
    :return: None
    """
    assert equal_answers("rock", "rock")
    assert equal_answers("paper", "paper")
    assert equal_answers("scissors", "scissors")
    assert equal_answers("rock", "paper") is None


def test_player_choice(monkeypatch):
    """
    Tests whether the `player_choice` function correctly retrieves player input.
    :param monkeypatch:
    :return: None
    """
    monkeypatch.setattr('builtins.input', lambda _: 'rock')
    assert player_choice() == 'rock'


def test_display_result():
    """
    Tests if the `display_result` function correctly displays the result of a game
     round based on player choices
    :return: None
    """
    assert display_result("rock", "scissors").lower() == "rock beats scissors\nyou win!!!"
    assert display_result("paper", "rock").lower() == "paper beats rock\nyou win!!!"
    assert display_result("scissors", "paper").lower() == "scissors beats paper\nyou win!!!"
    assert display_result("rock", "paper").lower() == "paper beats rock\nyou loose"
    assert display_result("rock", "rock").lower() == "it's a tie!!!"


def test_get_choice(monkeypatch):
    """
    Checks whether the `get_choice` function correctly retrieves and validates player choices.
    :param monkeypatch:
    :return: None
    """
    monkeypatch.setattr('builtins.input', lambda _: 'rock')
    assert get_choice() == 'rock'


def test_get_choice_getpass():
    """
    Tests if the `get_choice_getpass` function correctly retrieves a hidden
    player choice using `passwordbox`.
    :return: None
    """
    with patch('easygui.passwordbox', return_value='rock'):
        assert get_choice_getpass() == 'rock'


def test_play_round(capsys, monkeypatch):
    """
    Checks if the `play_round` function correctly simulates a game round
    and displays the expected results.
    :param capsys:
    :param monkeypatch:
    :return: None
    """
    monkeypatch.setattr('builtins.input', lambda _: 'rock')

    with patch('random.choice', return_value='scissors'):
        play_round()

    captured = capsys.readouterr()

    assert "you choose: " in captured.out.lower().strip()
    assert "computer is thinking..." in captured.out.lower()
    assert "computer choose:" in captured.out.lower()
    assert "you win" in captured.out.lower()


def test_play_round_another_player(capsys, monkeypatch):
    """
    Tests if the `play_round_another_player` function correctly simulates
    a game round between two players.
    :param capsys:
    :param monkeypatch:
    :return: None
    """
    monkeypatch.setattr('builtins.input', lambda *_: 'rock')

    with patch('easygui.passwordbox', return_value='scissors'):
        with patch('builtins.input', side_effect=['scissors']):
            play_round_another_player()

        captured = capsys.readouterr()
        assert "Player 1 turn:" in captured.out
        assert "Player 2 turn:" in captured.out
        assert "Player 1 choose: rock" in captured.out
        assert "Player 2 choose: scissors" in captured.out


def test_clear_console():
    """
    Tests if the `clear_console` function correctly clears the console based
     on the operating system.
    :return: None
    """
    with patch('os.system') as mock_os_sytem:
        clear_console()
        mock_os_sytem.assert_called_with("cls" if os.name == "nt" else "clear")


@pytest.mark.skip(reason="Tkinter issue in testing")
def test_menu(capsys):
    """
    This test is skipped due to know issues with Tkinter in the testing environment.
    :param capsys:
    :return: None
    """
    menu()
    captured = capsys.readouterr()
    assert "1. You Vs the AI" in captured.out
    assert "2. You Vs another player" in captured.out
    assert "3. Rules" in captured.out
    assert "4. End" in captured.out


def test_main(monkeypatch):
    """
    Checks if the `main` function correctly exists the game loop when the user chooses to end game.
    :param monkeypatch:
    :return: None
    """
    monkeypatch.setattr('builtins.input', lambda _: '4')

    result = main()

    assert "have a good day" in result.lower()
