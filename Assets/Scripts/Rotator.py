
from Infernux import *


class Rotator(InxComponent):
    speed = 90.0       # degrees per second

    def start(self):
        pass

    def update(self, delta_time: float):
        rotation = self.transform.euler_angles
        rotation[1] += self.speed * delta_time
        self.transform.euler_angles = rotation
