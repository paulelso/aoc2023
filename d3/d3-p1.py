def calculate_card_pts(winning_nums, my_nums):
    count = 0
    pts = 0
    for num in winning_nums:
        if num.isdigit() and num in my_nums:
            count += 1
            if count == 1:
                pts += 1
            if count > 1:
                pts = pts * 2
    return pts

def process_file(file_name):
    deck_pts = 0
    with open(file_name, "r") as file:
        for line in file:
            card_num, nums = line.strip().split(": ")
            winning_nums, my_nums = nums.split(" | ")
            winning_nums = winning_nums.split(" ")
            my_nums = my_nums.split(" ")
            deck_pts += calculate_card_pts(winning_nums, my_nums)
    return deck_pts

def main():
    file_name = "d3-input.txt"
    deck_pts = process_file(file_name)
    print(f"AOCOD2023 Day3 Part1 Solution: {deck_pts}")

if __name__ == "__main__":
    main()