import re
from pprint import pprint

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

test = True

games = test_input.split('\n')
# print(games)

split_games = []
for game in games:
    split_games.append(game.split(': '))

game_dict = {}
for game in split_games:
    game[0] = game[0].removeprefix('Game ')  # Remove game prefix
    game[0] = int(game[0])  # Reference games by integer
    game[1] = game[1].split('; ')  # Split up game into individual rounds
    game_dict[game[0]] = game[1]  # Add game to game dictionary

# pprint(game_dict)
print("Splitting all games into individual rounds:")
for game, rounds in game_dict.items():
    game_dict[game] = [r.split(', ') for r in rounds] # Split all the games in the game dictionary into individual rounds.

# pprint(game_dict)
print("Creating Dictionary Version of Games:")
for key, game in game_dict.items():
    # print(f"Game: {key}:", key, rnd)
    tmp_game = []  # This will contain a list of dictionaries of game rounds
    for rnd in game:  # A "rnd" is list of numbers and colors, like ['3 red', '4 blue']
        # print("String Games:", rnd)
        split_string = [c.split(' ') for c in rnd]  # Split each color and number within the round.
        # print("List Games:", split_string)
        rnd_dict = {s[1]: int(s[0]) for s in split_string}  # Create a dictionary version of the round
        # print("Dictionary Round:", rnd_dict)
        tmp_game.append(rnd_dict)  # Add the dictionary version of the round to temporary game list.
    # print(f"Dictionary version of game {key}: ", tmp_game)
    game_dict[key] = tmp_game  # Replace the list of rounds with dictionaries of rounds.
pprint(game_dict)

print("Evaluation each game for whether it is possible based on number of cubes in the bag: ")
for game_no, game in game_dict.items():
    print(f"Processing game {game_no} with contents {game}")
    for rnd in game:
        for colr, amt in rnd.items():
            if amt > bag[colr]:
                print(f"Game {game_no} not possible.")
                break




