import json


def load_json(file_path: str):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


class Config:
    CONFIG = load_json("./config.json")
