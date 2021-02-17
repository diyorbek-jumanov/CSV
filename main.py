from tinydb import TinyDB, Query
from pprint import pprint

data1 = open('products.csv')
data2 = open('specifications.csv')

data1_text = data1.read()
pprint(data1_text)
data2_text = data2.read()
pprint(data2_text)