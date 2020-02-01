from tracker.utils.path_util import ProjectPaths
import json
import pandas as pd
import pathlib

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
#print(ProjectPaths().dbt_seeds)
pd.DataFrame(cards_list, columns=column_names).to_csv(ProjectPaths().dbt_seeds.joinpath('cards.csv'))
