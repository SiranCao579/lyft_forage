from abc import ABC
from tire.tire import Tire


class OctoprimeTire(Tire, ABC):
    def __init__(self, tires_worn_condition):
        super().__init__(tires_worn_condition)

    def needs_service(self) -> bool:
        # should be serviced only when the sum of all values >= 3
        return sum(self.tires_worn_condition) >= 3
