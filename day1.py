import re

# Regular expression pattern to match spelled-out numbers and digits at the start and end of the line
pattern = re.compile(r'(?i)(one|two|three|four|five|six|seven|eight|nine|zero|\d)(?:[^\d]*)?(\d|zero|one|two|three|four|five|six|seven|eight|nine)(?![a-zA-Z])')

# Dictionary to map spelled-out numbers to digits
number_map = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

# Function to convert spelled-out numbers or digits to a single digit
def convert_to_digit(word):
    return number_map.get(word.lower(), word)

# Function to extract and sum calibration values
def sum_calibration_values(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Find matches for spelled-out numbers and digits
            matches = pattern.search(line)
            if matches:
                # Convert the first and last match to their digit form
                first_digit = convert_to_digit(matches.group(1))
                last_digit = convert_to_digit(matches.group(2))
                # Form the calibration value
                calibration_value = int(first_digit + last_digit)
                # Add the calibration value to the total sum
                total_sum += calibration_value
    return total_sum

# Path to the input file
file_path = 'input.txt'

# Calculate and print the sum of calibration values
calibration_sum = sum_calibration_values(file_path)
print(f"The sum of all calibration values is: {calibration_sum}")
