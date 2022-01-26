from operator import truediv


class Balloon:
    def __init__(self):
        self.popped = False
        self.sealed = False
        self.color =  None
        self.volume_ml = 0
        self.max_volume_ml = None
        self.update_time_ms = 0
    
    def pop(self):
        self.popped = True
        self.volume_ml = 0

    def decrease_air(self, delta_ms):
        pass

    def update(self, time_ms):
        delta_ms = time_ms - self.update_time_ms

        if self.popped:
            self.volume_ml = 0
        elif not self.sealed and self.volume_ml > 0:
            self.decrease_air(delta_ms)
        
        self.update_time_ms = time_ms

    def fill(self, volume_ml):
        self.volume_ml += volume_ml
        if self.volume_ml > self.max_volume_ml:
            self.pop()