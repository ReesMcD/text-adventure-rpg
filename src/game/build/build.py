from abc import ABC, abstractmethod
import json
import os


class Build(ABC):
    '''
    Abstract class for build scripts
    '''

    def __init__(self, file_name):
        cwd = os.getcwd()
        game_path = "game"
        content_path = "content"
        self.path = os.path.join(cwd, game_path, content_path, file_name)

    @abstractmethod
    def build(self):
        pass

    def importData(self):
        with open(self.path) as json_data:
            data = json.load(json_data)

        return dict(data)
