import re

# Define the word to digit mapping
word_to_digit_map = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

# Define the regular expression pattern for finding spelled-out numbers or digits
pattern = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|zero|\d)')

# Function to convert spelled-out numbers to digits
def word_to_digit(word):
    return word_to_digit_map.get(word, '')

# Function for "first function" logic
def find_first_digit(line):
    matches = pattern.findall(line)
    if matches:
        first_match = matches[0]
        return word_to_digit(first_match) if first_match.isalpha() else first_match
    return None

# Function for "second function" logic
def find_last_digit(line):
    matches = pattern.findall(line)
    if matches:
        last_match = matches[-1]
        return word_to_digit(last_match) if last_match.isalpha() else last_match
    return None

# Function for "third function" logic
def find_single_number(line):
    matches = pattern.findall(line)
    if len(matches) == 1:
        number = word_to_digit(matches[0]) if matches[0].isalpha() else matches[0]
        return number
    return None

# Initialize cumulative total
cumulative_total = 0

# Debugging output
debug_output = []

# Process the file
with open('day1.txt', 'r') as file:
    for line in file:
        line = line.strip()
        single_number = find_single_number(line)

        if single_number is not None:
            cumulative_total += int(single_number)*11
            debug_output.append(f"Single number found: {single_number}, cumulative total: {cumulative_total}\n")
        else:
            first_digit = find_first_digit(line)
            last_digit = find_last_digit(line)
            if first_digit is not None and last_digit is not None:
                cumulative_total += int(first_digit) * 10
                cumulative_total += int(last_digit)
                debug_output.append(f"First digit: {first_digit}, last digit: {last_digit}, cumulative total: {cumulative_total}\n")

# Print the final value of cumulative total
print(f"Final cumulative total: {cumulative_total}")

# Write debug output to file
with open('debug.txt', 'w') as debug_file:
    debug_file.writelines(debug_output)
