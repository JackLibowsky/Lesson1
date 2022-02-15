def format_price(price):
    price = int(price)
    formated_price = f'Цена: {price} руб.'
    return formated_price
print(format_price(56.24))