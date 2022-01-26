class Balloon:
    def __init__(self):
        self.popped = False
        self.sealed = False
        self.color =  None
        self.volume_ml = 0
        self.max_volume_ml = None
        self.update_time_ms = 0
    
    def pop():
        pass

    def decrease_air(self,delta_ms):
        pass

    def update(time_ms):
        delta_ms = time_ms - self.update_time_ms

        if self.popped:
            self.volume_ml = 0
        elif not self.sealed and self.volume_ml > 0:
            self.decrease_air(delta_ms)
        
        self.update_time_ms = time_ms