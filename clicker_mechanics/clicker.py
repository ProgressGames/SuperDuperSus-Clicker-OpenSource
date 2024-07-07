from clicker_mechanics.points import Points
from clicker_mechanics.autofarm import AutoFarm

class ClickerMechanics:
    def __init__(self):
        self.points = Points()
        self.auto_farm = AutoFarm(self.points)
    
    @property
    def count(self):
        return self.points.count

    def increase_count(self):
        self.points.increase(self.points.click_power)
    
    def buy_upgrade(self, cost, power_increase):
        return self.points.buy(cost, power_increase)

    def buy_auto_farm(self, cost):
        return self.auto_farm.buy(cost)

    def auto_farm_update(self):
        self.auto_farm.update()

    def get_state(self):
        return {
            "points": self.points.count,
            "click_power": self.points.click_power,
            "auto_farm_level": self.auto_farm.level
        }

    def set_state(self, state):
        self.points.set_count(state["points"])
        self.points.set_click_power(state["click_power"])
        self.auto_farm.set_level(state["auto_farm_level"])
