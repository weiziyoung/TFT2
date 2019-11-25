import json
import os

if __name__ == "__main__":
    os.chdir('../data')
    with open('champions.json', 'r') as f:
        champion_list = json.load(f)
        origin_dict = dict()
        class_dict = dict()
        for champion in champion_list:
            origins = champion['origin']
            for origin in origins:
                if origin_dict.get(origin):
                    origin_dict[origin]['champions'].append(champion['name'])
                else:
                    origin_dict[origin] = {
                        'bonus_num': [],
                        'scope': [],
                        'strength': [],
                        'champions': [champion['name']]
                    }
            classes = champion['class']
            for _class in classes:
                if class_dict.get(_class):
                    class_dict[_class]['champions'].append(champion['name'])
                else:
                    class_dict[_class] = {
                        'bonus_num': [],
                        'scope': [],
                        'strength': [],
                        'champions': [champion['name']]
                    }

    trait_dict = {}
    trait_dict.update(origin_dict)
    trait_dict.update(class_dict)

    with open('traits.json', 'w') as f:
        json.dump(trait_dict, f, indent='\t')
