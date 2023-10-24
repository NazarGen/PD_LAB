import pandas as pd


def get_data_for_date(input_date, file_path):
    try:

        date_str = input_date

        data = pd.read_csv(file_path)

        row = data[data['Date'] == date_str]

        if not row.empty:
            return row['USD_Rate'].values[0]
        else:
           return None
    except Exception as e:
       print(f"Произошла ошибка: {e}")
       return None


file_path = 'dataset.csv'
input_date ="2023-10-21T11:30:00+03:00"

result = get_data_for_date(input_date, file_path)
if result is not None:
    print(f"Данные для {input_date}: {result}")
else:
    print(f"Данные для {input_date} не найдены.")