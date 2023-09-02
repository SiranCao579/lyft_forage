from abc import ABC
from battery.battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return self.current_date > service_threshold_date
