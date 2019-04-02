import json
import hashlib


def a(path):
    with open(path, encoding='utf-8') as f:
        while True:
            countries_file = f.readline()
            if not countries_file:
                break
            yield print(hashlib.md5(countries_file.encode('utf-8')).hexdigest())


for item in a('countries.json'):
    print (item)