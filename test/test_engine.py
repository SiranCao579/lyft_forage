import unittest
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


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


if __name__ == '__main__':
    unittest.main()
