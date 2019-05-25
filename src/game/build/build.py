from abc import ABC, abstractmethod
import json
import os


class Build(ABC):
    '''
    Abstract class for build scripts
    '''

    def __init__(self, file_name):
        cwd = os.getcwd()
        self.path = os.path.join(cwd, "game", "content", file_name)

    @abstractmethod
    def build(self):
        pass

    def importData(self):
        with open(self.path) as json_data:
            data = json.load(json_data)

        return data
