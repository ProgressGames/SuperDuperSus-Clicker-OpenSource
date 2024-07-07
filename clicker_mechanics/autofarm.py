class AutoFarm:
    def __init__(self, points):
        self.points = points
        self.level = 0

    def buy(self, cost):
        if self.points.count >= cost:
            self.points.decrease(cost)
            self.level += 1
            return True
        return False

    def update(self):
        self.points.increase(self.level)

    def set_level(self, level):
        self.level = level
