class Tank:

    def __init__(self, name, capacity_l, volume_l, temperature_c):

        self.name = name
        self.capacity_l = capacity_l
        self.volume_l = volume_l
        self.temperature_c = temperature_c

    @property
    def level_percent(self):
        return (self.volume_l / self.capacity_l) * 100

    def get_status(self):
        return {
            "name": self.name,
            "capacity_l": self.capacity_l,
            "volume_l": self.volume_l,
            "level_percent": self.level_percent,
            "temperature_c": self.temperature_c
        }