def debug(message):
    with open('debug.txt', 'a') as file:
        file.write(message + '\n')

def read_mappings(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    debug(f"Total lines read: {len(lines)}")

    # Check if the file has enough lines
    if len(lines) < 2:
        debug("Error: Input file does not contain enough lines.")
        raise ValueError("Input file does not contain enough lines.")

    # Attempt to read the seeds line
    try:
        seeds_line = next((line for line in lines if 'seeds:' in line), None)
        if seeds_line is None:
            debug("Error: Seeds line not found.")
            raise ValueError("Seeds line not found.")
        # Process the seed ranges
        seed_ranges = list(map(int, seeds_line.split(': ')[1].split()))
        seeds = []
        for i in range(0, len(seed_ranges), 2):
            start, length = seed_ranges[i], seed_ranges[i+1]
            seeds.extend(range(start, start + length))
        debug(f"Seeds: {seeds}")
    except IndexError as e:
        debug(f"Error reading seeds: {e}")
        raise

    mappings = {}
    current_map = None

    # Start reading from the line after the seeds line
    start_index = lines.index(seeds_line) + 2
    for line in lines[start_index:]:
        if line.strip() == '':
            continue
        if 'map:' in line:
            current_map = line.split(':')[0]
            mappings[current_map] = {}
            debug(f"Current map: {current_map}")
        else:
            destination_start, source_start, length = map(int, line.split())
            for i in range(length):
                mappings[current_map][source_start + i] = destination_start + i
            debug(f"Mapping line: {line.strip()}")

    return seeds, mappings

def map_value(value, mapping, memo):
    if value in memo:
        return memo[value]
    if value in mapping:
        memo[value] = mapping[value]
    else:
        memo[value] = value
    return memo[value]

def find_lowest_location(seeds, mappings):
    lowest_location = float('inf')
    memo = {}
    for category in mappings.keys():
        memo[category] = {}

    for seed in seeds:
        debug(f"Processing seed: {seed}")
        value = seed
        for category, mapping in mappings.items():
            value = map_value(value, mapping, memo[category])
            debug(f"{category[:-4].capitalize()} {seed} maps to {category[:-4].capitalize()} {value}")
        lowest_location = min(lowest_location, value)

    return lowest_location

# Clear the debug file before starting
open('debug.txt', 'w').close()

# Read the mappings from the input file
seeds, mappings = read_mappings('day5.txt')

# Find the lowest location number
lowest_location = find_lowest_location(seeds, mappings)

# Output the result
print(f"The lowest location number is: {lowest_location}")
