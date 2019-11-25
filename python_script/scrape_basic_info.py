import requests
import json
import os

os.chdir('../data')
if __name__ == "__main__":
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    url = "https://blitz-cdn-plain.blitz.gg/blitz/tft/data-sets/champions.json"
    response = requests.get(url, headers=headers)
    champions_list = json.loads(response.text)
    saved_list = []
    for info in champions_list.values():
        name = info['name']
        if not info['set2']:
            continue
        set2 = info['set2']
        origins = set2['origin']
        classes = set2['class']
        cost = set2['cost']
        encode_name = name.replace(' ', '').replace('.', '').replace("'", '')
        if encode_name == 'LeBlanc':
            encode_name = 'Leblanc'
        if encode_name == 'KhaZix':
            encode_name = 'Khazix'
        avatar1 = f'https://blitz-cdn.blitz.gg/90x90/blitz/tft/champion_squares/set1/{encode_name}.png'
        avatar2 = f'https://blitz-cdn.blitz.gg/90x90/blitz/tft/champion_squares/set2/{encode_name}.png'
        response = requests.get(avatar1, headers=headers)
        if response.status_code == 200:
            with open(f"avatar/{name}.png", 'wb') as f:
                f.write(response.content)
                avatar = avatar1
        else:
            response = requests.get(avatar2, headers=headers)
            if response.status_code == 200:
                with open(f"avatar/{name}.png", 'wb') as f:
                    f.write(response.content)
                    avatar = avatar2
            else:
                print(name)
                raise Exception("download fail")

        champion_json = {
            "name": name,
            "origin": origins,
            "class": classes,
            "cost": cost,
            "avatar": avatar
        }
        print(champion_json)
        saved_list.append(champion_json)

        print('success')
    with open(f'champions.json', 'w', encoding='utf-8') as f:
        json.dump(saved_list, f, ensure_ascii=False, indent='\t')
