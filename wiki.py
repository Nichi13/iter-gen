import json


class Iter_countries():
    def __init__(self, path):
        self.count = 0
        self.count_of_countries = 250
        self.path = path
        self.result = {}

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, encoding='utf-8') as countries_json:
            countries_file = json.load(countries_json)
            name = (countries_file[self.count]['name']['common'])
            name_list = []
            name_list.append(name.split())
            name_str = '_'.join(name_list[0])
            link = 'https://en.wikipedia.org/wiki/' + name_str
            self.result[name_str] = link
            with open('data.txt', 'w', encoding='utf8') as file:
                json.dump(self.result, file, ensure_ascii=False)
        self.count += 1
        if self.count > self.count_of_countries-1:
            raise StopIteration
        return self.count


if __name__ == '__main__':
    for item in Iter_countries('countries.json'):
        print(item)
