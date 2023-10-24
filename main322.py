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