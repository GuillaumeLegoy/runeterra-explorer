from tracker.utils.path_util import ProjectPaths
import json
import pandas as pd

column_names = [
    'region',
    'name',
    'cost',
    'attack',
    'health'
]

cards_list = []

with open(ProjectPaths().cards) as cards_file:
    cards = json.load(cards_file)

    for c in cards:
        current_card = [
            c['regionRef'],
            c['name'],
            c['cost'],
            c['attack'],
            c['health']
        ]

        cards_list.append(current_card)

print(pd.DataFrame(cards_list, columns=column_names))
