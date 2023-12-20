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
df_max = df.groupby(['game_number'])[['blue', 'green', 'red']].max()
df['power'] = df_max['blue'] * df_max['green'] * df_max['red']
pt2_solution = int(df['power'].sum())
print(f"ACOD2023 Day2 Part2 Solution: {pt2_solution}")
