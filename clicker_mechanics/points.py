class Points:
    def __init__(self):
        self._count = 0
        self._click_power = 1

    @property
    def count(self):
        return self._count

    @property
    def click_power(self):
        return self._click_power

    def increase(self, amount):
        self._count += amount

    def decrease(self, amount):
        self._count -= amount

    def buy(self, cost, power_increase):
        if self._count >= cost:
            self._count -= cost
            self._click_power += power_increase
            return True
        return False

    def set_count(self, count):
        self._count = count

    def set_click_power(self, click_power):
        self._click_power = click_power
