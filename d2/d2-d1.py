import pandas as pd
import re

file_path = 'd2-input.txt'

data = pd.DataFrame()

results_list = []
with open(file_path, 'r') as file:
    for line in file:
        game, results = line.strip().split(':')
        game_number = int(game.split(' ')[-1])
        results = results.split(';')
        for r in results:
            green_match = re.search(r'(\d+)\s+green', r)
            red_match = re.search(r'(\d+)\s+red', r)
            blue_match = re.search(r'(\d+)\s+blue', r)
            res = {'game_number': game_number, 'green': 0, 'red': 0, 'blue': 0}
            if blue_match:
                res['blue'] = int(blue_match.group(1))
            if green_match:
                res['green'] = int(green_match.group(1))
            if red_match:
                res['red'] = int(red_match.group(1))

            
            results_list.append(res)
# Create a tabular data structure with labeled columns from the results_list
df = pd.DataFrame(results_list)
# Assign the DataFrame to the variable df where a new column 'passed_test' is added. 
# This column is created using a logical expression that checks the counts of the cubes
# i.e. extracts counts of blue, green, and red cubes from a string, stores them in a DataFrame, 
# and adds a new column indicating whether the counts pass a certain test.
df['passed_test'] = (df['blue'] <= 14) & (df['green'] <= 13) & (df['red'] <= 12)
df_pct = df.groupby('game_number')['passed_test'].mean().reset_index()

solution = df_pct.query('passed_test == 1')['game_number'].sum()
print(f"AOC2023 Day2 Part1 Solution: {solution}")