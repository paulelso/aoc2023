import re

file_path = "/Users/psousa/Python/acod2023/d01_input.txt"
total = 0

with open(file_path, "r") as file:
    lines = file.readlines()

for line in lines:
    res = list(filter(lambda x: x.isdigit(), line))
    first_digit = res[0]
    last_digit = res[-1]
    line_total = int(str(first_digit) + str(last_digit))
    total += line_total

print(f"ACOD2023 Day1 Part1 Solution: {total}")