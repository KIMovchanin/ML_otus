from base import Vehicle
import exceptions

class Plane(Vehicle):
    def __init__(self, cargo=0, max_cargo=0):
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, custom_cargo):
        if (custom_cargo + self.cargo) < self.max_cargo:
            print("Перегруза нет, полёт возможен.")
            self.cargo += custom_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        print(f"Груз снят с борта. Грузоподъёмность самолёта равна {self.max_cargo} килограмм.")
        return prev_cargo
