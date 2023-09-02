from abc import ABC
from tire import Tire


class CarriganTire(Tire, ABC):
    def __init__(self, tires_worn_condition):
        super().__init__(tires_worn_condition)

    def needs_service(self) -> bool:
        # should be serviced only when one or more
        # of the values in the tire wear array >= 0.9
        for wear in self.tires_worn_condition:
            if wear >= 0.9:
                return True
        return False
