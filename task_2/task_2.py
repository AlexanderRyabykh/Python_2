import json
import datetime


def write_order_to_json(item, quantity,  price, buyer, date):
    with open('orders.json', 'w') as f:
        dict_to_json = {'item': item, 'quantity': quantity,
                        'price': price, 'buyer': buyer, 'date': date}
        json.dump(dict_to_json, f, indent=4)


today_date = str(datetime.datetime.now().date().isoformat())
write_order_to_json('Ножницы', 5, 50, 'Саша', today_date)

with open('orders.json') as f:
    print(f.read())