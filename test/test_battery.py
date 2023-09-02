import unittest
from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


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


if __name__ == '__main__':
    unittest.main()
