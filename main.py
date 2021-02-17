from tinydb import TinyDB

def insert_db(data_csv):

    products_db = []
    for row in data_csv.split('\n')[1:]:
        cat,company,price = row.split(',')[1:]
        products_db.append({'model':cat,'company':company, 'price': int(price)})
        print(row)

    return products_db

db = TinyDB('db.json')
data = open('specifications.csv').read()

db.truncate()
products_db = insert_db(data)

db.insert_multiple(products_db)