from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self) -> bool:
        pass
