def is_adjacent_to_symbol(x, y, schematic):
    # Define the adjacent positions (including diagonals)
    adjacent_positions = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1),               (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]
    
    # Check if any adjacent position has a symbol
    for ax, ay in adjacent_positions:
        if 0 <= ax < len(schematic) and 0 <= ay < len(schematic[0]) and schematic[ax][ay] in '*#+$':
            return True
    return False

def sum_part_numbers(filename):
    with open(filename, 'r') as file:
        # Read the file and store it as a list of strings, removing newline characters
        schematic = [line.strip() for line in file.readlines()]
    
    total_sum = 0
    # Iterate over each line
    for i, line in enumerate(schematic):
        # Iterate over each character in the line
        j = 0
        while j < len(line):
            char = line[j]
            # If the character is a digit, we check if it's part of a longer number
            if char.isdigit():
                # Check the entire number which might span multiple characters
                number_str = char
                k = j + 1
                while k < len(line) and line[k].isdigit():
                    number_str += line[k]
                    k += 1
                
                # Now we check if this number is adjacent to a symbol
                number_adjacent = is_adjacent_to_symbol(i, j, schematic)
                
                if number_adjacent:
                    # If the number is adjacent to a symbol, add it to the total sum
                    total_sum += int(number_str)
                    
                # Move the index j to the end of the current number to avoid re-checking the same digits
                j = k
            else:
                j += 1
    
    return total_sum

# Call the function and print the result
print(sum_part_numbers('day3.txt'))
