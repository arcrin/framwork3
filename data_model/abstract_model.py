import abc
import typing


class AbstractDataModel(abc.ABC):
    @abc.abstractmethod
    def add(self, data: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self) -> int:
        # for test, we are going to use a fixed key
        raise NotImplementedError
