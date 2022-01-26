class Tank:
    def __init__(self, air_type) -> None:
        self.volume_L = 0
        self.max_volume_L = 25
        self.air_type = air_type

        def release_air(self, volume_ml):
            amount = volume_ml / 1000
            if amount <= self.volume_L:
                self.volume_L -= amount
            else:
                pass