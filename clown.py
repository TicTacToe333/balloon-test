from tank import Tank
from balloon import Balloon

class Clown:
    def __init__(self):
        self.tank = Tank()
        self.money = 0

    def buy_balloon(self, cost):
        balloon = Balloon("Red")
        balloon.fill(self.tank.release_air(500))
        self.money += cost
        return balloon