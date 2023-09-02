from model.car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:
    def create_calliope(self, last_service_date, current_mileage, last_service_mileage, tires_worn_condition):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tire = OctoprimeTire(tires_worn_condition)
        return Car(engine, battery, tire)

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage, tires_worn_condition):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tire = OctoprimeTire(tires_worn_condition)
        return Car(engine, battery, tire)

    def create_palindrome(self, last_service_date, warning_light_on, tires_worn_condition):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        tire = OctoprimeTire(tires_worn_condition)
        return Car(engine, battery, tire)

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage, tires_worn_condition):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tire = OctoprimeTire(tires_worn_condition)
        return Car(engine, battery, tire)

    def create_thovex(self, last_service_date, current_mileage, last_service_mileage, tires_worn_condition):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tire = OctoprimeTire(tires_worn_condition)
        return Car(engine, battery, tire)
