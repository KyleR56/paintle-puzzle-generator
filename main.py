import json
import itertools
import random

num_puzzles = 366
colors = ["red", "orange", "yellow", "green", "blue"]
size = len(colors)

def generate_pattern():
    pattern = [[None for _ in range(size)] for _ in range(size)]
    product = list(itertools.product([i for i in range(size)], ["row", "column"]))
    random.shuffle(product)
    for index, dir in product:
        if dir == "row":
            for column in range(size):
                pattern[index][column] = colors[index]
        else:
            for row in range(size):
                pattern[row][index] = colors[index]
    return pattern


def generate_puzzles():
    puzzles = []
    for day in range(1, num_puzzles + 1):
        puzzle = {
            "day": day,
            "pattern": generate_pattern()
        }
        puzzles.append(puzzle)
    return puzzles

puzzles = generate_puzzles()

with open("puzzles.json", "w") as file:
    json.dump(puzzles, file, indent=4)

print(str(num_puzzles) + " puzzles have been generated and saved to puzzles.json")
