with open("d01_input.txt", "r") as file:
    data = []
    for line in file.readlines():
        item = []
        for char in line:
            if char >= '0' and char <= '9':
                item.append(int(char))
        data.append(item)

    total = 0
    for item in data:
        total += (10 * item[0])
        total += item[-1]

print(f"ACOD2023 Day1 Part1 Solution: {total}")