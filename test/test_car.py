import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from model.car_factory import CarFactory


class TestEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage_capulet = 30001
        current_mileage_willoughby = 60001
        last_service_mileage = 0
        warning_light_on = True

        capulet_engine = CapuletEngine(current_mileage_capulet, last_service_mileage)
        willoughby_engine = WilloughbyEngine(current_mileage_willoughby, last_service_mileage)
        sternman_engine = SternmanEngine(warning_light_on)
        self.assertTrue(capulet_engine.needs_service())
        self.assertTrue(willoughby_engine.needs_service())
        self.assertTrue(sternman_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage_capulet = 30000
        current_mileage_willoughby = 60000
        last_service_mileage = 0
        warning_light_on = False

        capulet_engine = CapuletEngine(current_mileage_capulet, last_service_mileage)
        willoughby_engine = WilloughbyEngine(current_mileage_willoughby, last_service_mileage)
        sternman_engine = SternmanEngine(warning_light_on)

        self.assertFalse(capulet_engine.needs_service())
        self.assertFalse(willoughby_engine.needs_service())
        self.assertFalse(sternman_engine.needs_service())


class TestBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date_spindler = today.replace(year=today.year - 3)
        last_service_date_nubbine = today.replace(year=today.year - 5)
        spindler_battery = SpindlerBattery(last_service_date_spindler)
        nubbin_battery = NubbinBattery(last_service_date_nubbine)

        self.assertTrue(spindler_battery.needs_service())
        self.assertTrue(nubbin_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler_battery = SpindlerBattery(last_service_date)
        nubbin_battery = NubbinBattery(last_service_date)

        self.assertFalse(spindler_battery.needs_service())
        self.assertFalse(nubbin_battery.needs_service())


# class TestPalindrome(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         warning_light_is_on = False
#
#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())
#
#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         warning_light_is_on = False
#
#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())
#
#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = True
#
#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())
#
#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = False
#
#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())
#
#
# class TestRorschach(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0
#
#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())
#
#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0
#
#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())
#
#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0
#
#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())
#
#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0
#
#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())
#
#
# class TestThovex(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0
#
#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())
#
#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0
#
#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())
#
#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0
#
#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())
#
#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0
#
#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
