import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from model.car_factory import CarFactory


class TestCar(unittest.TestCase):

    def test_car_should_be_serviced_all_conditions_met(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 30001
        last_service_mileage = 0
        warning_light_on = True
        tires_worn_condition = [1, 1, 1, 1]
        factory = CarFactory()

        calliope = factory.create_calliope(last_service_date, current_mileage, last_service_mileage, tires_worn_condition)
        palindrome = factory.create_palindrome(last_service_date, warning_light_on, tires_worn_condition)
        self.assertTrue(calliope.needs_service())
        self.assertTrue(palindrome.needs_service())

    def test_car_should_be_serviced_one_condition_met(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 30000
        last_service_mileage = 0
        warning_light_on = False
        tires_worn_condition = [1, 1, 1, 1]
        factory = CarFactory()

        calliope = factory.create_calliope(last_service_date, current_mileage, last_service_mileage,
                                           tires_worn_condition)
        palindrome = factory.create_palindrome(last_service_date, warning_light_on, tires_worn_condition)
        self.assertTrue(calliope.needs_service())
        self.assertTrue(palindrome.needs_service())

    def test_car_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 30000
        last_service_mileage = 0
        warning_light_on = False
        tires_worn_condition = [0, 0, 0, 0]
        factory = CarFactory()

        calliope = factory.create_calliope(last_service_date, current_mileage, last_service_mileage,
                                           tires_worn_condition)
        palindrome = factory.create_palindrome(last_service_date, warning_light_on, tires_worn_condition)
        self.assertFalse(calliope.needs_service())
        self.assertFalse(palindrome.needs_service())


if __name__ == '__main__':
    unittest.main()
