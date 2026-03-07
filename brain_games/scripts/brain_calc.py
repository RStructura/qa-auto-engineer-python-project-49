from brain_games.engine import run_game
from brain_games.games.calc import DESCRIPTION, get_round_data


def main():
    run_game(DESCRIPTION, get_round_data)
