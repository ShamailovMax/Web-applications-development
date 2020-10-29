from abc import ABC
from abc import abstractmethod


class Figure(ABC):

    FTYPE = None

    @classmethod
    def get_ftype(cls):
        return cls.FTYPE

    @abstractmethod
    def _area(self):
        pass
        # raise NotImplementedError
