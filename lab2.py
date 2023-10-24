import requests
import json
import pandas as pd

# URL для получения данных с курсом доллара
url = "https://www.cbr-xml-daily.ru/daily_jsonp.js"

# Выполняем GET-запрос к URL
response = requests.get(url)

if response.status_code == 200:
    # Извлекаем JSON из JSONP-ответа
    jsonp_data = response.text
    json_data = json.loads(jsonp_data[jsonp_data.index("{"):jsonp_data.rindex("}") + 1])

    # Извлекаем информацию о курсе доллара
    usd_rates = json_data["Valute"]["USD"]["Value"]

    # Извлекаем дату
    date = json_data["Date"]

    # Создаем DataFrame с данными
    df = pd.DataFrame({"Date": [date], "USD_Rate": [usd_rates]})

    # Сохраняем DataFrame в CSV-файл
    df.to_csv("dataset.csv", index=False)

    print("Данные успешно сохранены в dataset.csv")
else:
    print("Ошибка при выполнении запроса")