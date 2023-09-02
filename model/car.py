from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import Battery
from tire.tire import Tire


class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
