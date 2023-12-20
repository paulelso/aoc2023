import re

def get_digit(s):
    digit_mapping = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return int(digit_mapping.get(s, s))

def main():
    patterns = 'one|1|two|2|three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9'
    total = 0

    input_file_path = "/Users/psousa/Python/acod2023/d01_input.txt"
    output_file_path = "/Users/psousa/Python/acod2023/d01_output.txt"  # Specify the output file path

    try:
        with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
            lines = input_file.readlines()

            for line in lines:
                digits = re.findall(patterns, line)
                first_digit = get_digit(digits[0])
                last_digit = get_digit(digits[-1])
                line_total = (10 * first_digit + last_digit)
                total += line_total
                output_file.write(f"Line: {line}, Line_total: {line_total}, Total: {total}\n")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    print(total)

if __name__ == "__main__":
    main()
