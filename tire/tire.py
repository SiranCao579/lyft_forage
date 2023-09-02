from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, tires_worn_condition):
        self.tires_worn_condition = tires_worn_condition

    @abstractmethod
    def needs_service(self) -> bool:
        pass
