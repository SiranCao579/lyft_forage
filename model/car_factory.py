from model.car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory:
    def create_calliope(self, last_service_date, current_mileage, last_service_mileage):
        calliope_engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope_battery = SpindlerBattery(last_service_date)
        return Car(calliope_engine, calliope_battery)

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage):
        glissade_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        glissade_battery = SpindlerBattery(last_service_date)
        return Car(glissade_engine, glissade_battery)

    def create_palindrome(self, last_service_date, warning_light_on):
        palindrome_engine = SternmanEngine(warning_light_on)
        palindrome_battery = SpindlerBattery(last_service_date)
        return Car(palindrome_engine, palindrome_battery)

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage):
        rorschach_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach_battery = NubbinBattery(last_service_date)
        return Car(rorschach_engine, rorschach_battery)

    def create_thovex(self, last_service_date, current_mileage, last_service_mileage):
        thovex_engine = CapuletEngine(current_mileage, last_service_mileage)
        thoves_battery = NubbinBattery(last_service_date)
        return Car(thovex_engine, thoves_battery)
