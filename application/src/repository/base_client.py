from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def get (self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass


