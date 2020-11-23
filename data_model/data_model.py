from .abstract_model import AbstractDataModel


class DataModel(AbstractDataModel):
    def __init__(self):
        self._dict = {}

    def add(self, data: int):
        self._dict['test'] = data

    def get(self) -> int:
        return self._dict['test']
