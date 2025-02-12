from abc import ABC
import exceptions


class Vehicle(ABC):
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel != 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance: float):
        """Допустим мы передаём значения в км и на 100 км идёт расход 10 литров.
        То есть ли мы укажем, что мы хотим проехать 200 км у нас должно быть
        как минимум 20 литров топлива."""
        if self.fuel < distance / 10:
            self.fuel -= (distance / 10)
        else:
            raise exceptions.NotEnoughFuel

