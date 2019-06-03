import json
import os


class Config():
    def __init__(self):
        self.env = "DEFAULT"
        self.save = ""

    def get_save_config(self):
        print("Get Saves")
        with open("saves/config.json", "r") as json_data:
            data = json.load(json_data)
            loaded_env = data[self.env]
            if self.env is "DEFAULT":
                save_number = 0
                self.save = os.path.join(
                    "saves", loaded_env[save_number]["DB_NAME"])
            else:
                self.save = os.path.join("saves", loaded_env["DB_NAME"])


config = Config()
