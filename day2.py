# Function to parse the game data from a line
def parse_game_data(line):
    subsets = line.strip().split('; ')
    game_subsets = []
    for subset in subsets:
        cube_counts = {'red': 0, 'green': 0, 'blue': 0}
        cubes = subset.split(', ')
        for cube in cubes:
            count, color = cube.split()
            count = int(count)
            cube_counts[color] = max(cube_counts[color], count)
        game_subsets.append(cube_counts)
    return game_subsets

# Function to calculate the power of a set of cubes
def calculate_power(cube_set):
    return cube_set['red'] * cube_set['green'] * cube_set['blue']

# Read the games from the file and calculate the minimum set of cubes for each game
total_power = 0
with open('day2.txt', 'r') as file:
    for line in file:
        game_id_str, game_data = line.split(': ')
        game_subsets = parse_game_data(game_data)

        # Find the minimum number of cubes for each color
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for subset in game_subsets:
            for color in min_cubes:
                min_cubes[color] = max(min_cubes[color], subset[color])

        # Calculate the power of the minimum set of cubes and add it to the total
        power = calculate_power(min_cubes)
        total_power += power

print(f"The sum of the power of the minimum sets of cubes is: {total_power}")
