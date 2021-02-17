from tinydb import TinyDB, Query
from pprint import pprint

def document(dt_txt):
    doc_list = dt_txt.split('\n')
    doc_keys = doc_list[0].split(',')[1:]
    collection = list()
    for row in doc_list[1:]:
        doc_full = dict()
        for i, x in enumerate(row.split(',')[1:]):
            doc_full[doc_keys[i]] = x
        collection.append(doc_full)
    
    return collection
        


data1 = open('products.csv')
data2 = open('specifications.csv')

data1_text = data1.read()
data2_text = data2.read()

d1 = document(data1_text)
d2 = document(data2_text)

db = TinyDB('db.json')
db.truncate()

table1 = db.table('products')
table2 = db.table('specifications')

