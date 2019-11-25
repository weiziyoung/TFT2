import json

with open('../data/champions.json', 'r', encoding='utf-8') as f:
    champion_list = json.load(f)

with open('../data/traits.json', 'r', encoding='utf-8') as f:
    trait_list = json.load(f)

name_dict = {}
for each in champion_list:
    name_dict[each['name']] = ""
for each in trait_list:
    name_dict[each['name']] = ''

with open('../data/language.json', 'w', encoding='utf-8') as f:
    json.dump(name_dict, f, indent='\t', ensure_ascii=False)
# dic = {}
#
# with open("../data/language.json", 'r') as f:
#     l = json.load(f)
#
# for each in l:
#     key = list(each.keys())[0]
#     value = list(each.values())[0]
#     dic[key] = value
#
# with open("../data/language_copy.json", "w") as f:
#     json.dump(dic, f, indent='\t', ensure_ascii=False)