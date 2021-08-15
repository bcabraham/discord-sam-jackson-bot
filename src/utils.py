import os
import json

ROOT_DIR = os.path.abspath(os.curdir)


def load_data(file_path) -> object:
    data_path = os.path.join(ROOT_DIR, file_path)

    with open(data_path) as data:
        contents = json.load(data)

        return contents
