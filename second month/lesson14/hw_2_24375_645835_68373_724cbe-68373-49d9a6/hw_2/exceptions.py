"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self, message="Низкий уровень топлива!"):
        super().__init__(message)

class NotEnoughFuel(Exception):
    def __init__(self, message="Недостаточно топлива!"):
        super().__init__(message)

class CargoOverload(Exception):
    def __init__(self, message="Перегруз!"):
        super().__init__(message)