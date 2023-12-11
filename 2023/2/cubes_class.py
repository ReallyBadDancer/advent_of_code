from math import prod
from pprint import pprint

test = False

if test:
    test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    games = test_input.split('\n')
else:
    with open("test_input") as ifile:
        games = ifile.read().splitlines()

# pprint(games)

split_games = []
for game in games:  # Split off the game sequence number from the game contents
    split_games.append(game.split(': '))

game_dict = {}
for game in split_games:  # Turn game sequence numbers into integer keys and game contents into values
    game[0] = game[0].removeprefix('Game ')  # Remove game prefix
    game[0] = int(game[0])  # Reference games by integer
    game[1] = game[1].split('; ')  # Split up game into individual rounds
    game_dict[game[0]] = game[1]  # Add game to game dictionary

# pprint(game_dict)
print("Splitting all games into individual rounds:")
for game, rounds in game_dict.items():
    game_dict[game] = [r.split(', ') for r in rounds]  # Split all the games in the game dictionary into individual rounds.

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

# pprint(game_dict)

class CubeGame:
    bag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    def __init__(self, seq_no: int, round_set: list):
        self.seq_no = seq_no
        self.round_set = round_set
        self.valid = True
        self.min_required_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        self.power_level = 0
        print(f"Game: {self.seq_no}, Rounds: {self.round_set}")

    def eval_self_validity(self):
        """
        Determine whether the game is actually valid (are there enough cubes in the bag to play all the games?)
        :return: None
        """
        for rnd in self.round_set:
            for colr, amt in rnd.items():
                if amt > self.bag[colr]:
                    self.valid = False
                    break
        # print(f"Game {self.seq_no} possibility is {self.valid}.")
    def eval_min_required_cubes(self):
        """
        Determine the minimum number of cubes in the bag to play all the games.
        :return:
        """
        for rnd in self.round_set:
            for key, value in rnd.items():
                if value > self.min_required_cubes[key]:
                    # print(f"Found new minimum for {key}. Updating to {value}")
                    self.min_required_cubes[key] = value

    def calculate_power_level(self):
        """
        Determine the total power level of the minimum cubes to play the game by multiplying the number of each color
        together.
        :return:
        """
        print("Power Levels: ", list(self.min_required_cubes.values()))
        self.power_level = prod(list(self.min_required_cubes.values()))
        print("Total Power Level: ", self.power_level)
        return self.power_level
        # for color_value in self.min_required_cubes.values()

print("Creating an object for each game... ")
game_list = []
for key, value in game_dict.items():
    game_list.append(CubeGame(key, value))

part_one = False
if part_one:
    answer1 = 0
    print("Check each game for validity and add game sequence no to total if it's valid.")
    for game in game_list:
        game.eval_self_validity()
        if game.valid:
            print(game.seq_no, "is valid, adding")
            answer1 += game.seq_no
        else:
            print(game.seq_no, "is invalid, not adding")

    print("Answer to part 1 is: ", answer1)

answer2 = 0
for game in game_list:
    game.eval_min_required_cubes()
    answer2 += game.calculate_power_level()

print(answer2)
