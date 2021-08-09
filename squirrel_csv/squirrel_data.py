import pandas as pd

data = pd.read_csv('Squirrel_Data.csv')

print(data)

red_fur_data = data[data.Fur_Color == "Cinnamon"]
print(red_fur_data)
gray_fur_data = data[data.Fur_Color == "Gray"]
black_fur_data = data[data.Fur_Color == "Black"]

print("hello")

squirrel_info = {
    'Fur Color': ['grey', 'red', 'black'],
    'count': [len(gray_fur_data), len(red_fur_data), len(black_fur_data)]
}

squirrel_data = pd.DataFrame(squirrel_info)
squirrel_data.to_csv('Squirrel_data.csv')