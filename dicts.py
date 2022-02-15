gorod = {
    "city": "Москва", 
    "temperature": "20"
}
print(gorod['city']) # Выведите на экран значение ключа city
gorod["temperature"] = int(gorod["temperature"]) - 5 # Уменьшите значение "temperature" на 5
print(gorod) # Выведите на экран весь словарь

print(gorod.get('country', 'Россия')) # Выведите значение по-умолчанию "Россия" для ключа country

gorod['date'] = '27.05.2019' # Добавьте в словарь элемент date со значением "27.05.2019"
print(len(gorod)) # Выведите на экран длину словаря