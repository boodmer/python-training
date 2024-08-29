from abc import ABC, abstractmethod


class IBaseModel(ABC):
    @abstractmethod
    def find_one_by_id(cls, id: str):
        pass

    @abstractmethod
    def find(cls):
        pass

    @abstractmethod
    def save(self):
        pass
