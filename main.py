from tinydb import TinyDB, Query
from pprint import pprint

def document(dt_txt):
    doc_list = dt_txt.split('\n')
    doc_keys = doc_list[0].split(',')[1:]

    for row in doc_list[1:]:
        doc_full = dict()
        for i, x in enumerate(row.split(',')[1:]):
            print(i, x)
        


data1 = open('products.csv')
data2 = open('specifications.csv')

data1_text = data1.read()
data2_text = data2.read()

document(data1_text)