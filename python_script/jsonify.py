import os
import json

os.chdir('../data')

if __name__ == "__main__":
    new_dict = {}
    with open('language.json', 'r', encoding='utf-8') as f:
        languages = json.load(f)
    for each in languages:
        name = list(each.keys())[0]
        value = list(each.values())[0]
        new_dict[name] = value
    with open('language.json', 'w', encoding='utf-8') as f:
        json.load(new_dict)