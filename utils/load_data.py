import os.path

from settings import DATA_PATH
import json


class ProjectData:

    with open(os.path.join(DATA_PATH, 'installations', 'meaning_of_life.json')) as f:
        MEANING_OF_LIFE = json.load(f)

    with open(os.path.join(DATA_PATH, 'installations', 'what_do_you_do.json')) as f:
        WHAT_DO_YOU_DO = json.load(f)
