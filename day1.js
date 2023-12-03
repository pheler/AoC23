const fs = require('fs');

// Mapping of spelled-out numbers to their numerical equivalents
const numberWords = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
};

// Regular expression pattern to match all possible digits, including spelled-out numbers
const pattern = new RegExp(`\\b(${Object.keys(numberWords).join('|')})\\b|\\d`, 'g');

function convertToDigit(match) {
    return match in numberWords ? numberWords[match] : match;
}

function processLine(line) {
    // Find all matches in the line
    const matches = line.match(pattern);
    if (!matches) {
        return 0;
    }

    // Convert spelled-out numbers to digits
    const digits = matches.map(match => convertToDigit(match));

    // Combine the first and last digit to form a two-digit number
    return parseInt(digits[0] + digits[digits.length - 1], 10);
}

function calculateCalibrationValue(document) {
    let totalSum = 0;
    document.forEach(line => {
        totalSum += processLine(line);
    });
    return totalSum;
}

// Read the input file
fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }
    const calibrationDocument = data.split('\n').map(line => line.trim());
    // Calculate the sum of all calibration values
    const sumOfCalibrationValues = calculateCalibrationValue(calibrationDocument);
    console.log(`The sum of all calibration values is: ${sumOfCalibrationValues}`);
});
