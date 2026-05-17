
from Infernux import *


class Bouncer(InxComponent):
    bounce_speed = 6.0

    def start(self):
        pass

    def on_collision_enter(self, collision):
        rb = self.game_object.get_component(Rigidbody)
        if rb:
            vel = rb.velocity
            rb.velocity = Vector3(vel.x, self.bounce_speed, vel.z)
