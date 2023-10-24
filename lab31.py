
import pandas as pd


input_csv = 'dataset.csv'
data = pd.read_csv(input_csv)
dates = data['Date']
python_data = data['USD_Rate']


x_df = pd.DataFrame({'Date': dates})
y_df = pd.DataFrame({'USD_Rate': python_data})


x_df.to_csv('X.csv', index=False)
y_df.to_csv('Y.csv', index=False)

print("Файлы X.csv и Y.csv успешно созданы.")