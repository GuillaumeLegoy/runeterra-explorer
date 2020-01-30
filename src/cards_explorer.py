from path_util import ProjectPaths
import json


with open(ProjectPaths().globals) as cards_file:
    print(json.load(cards_file))
