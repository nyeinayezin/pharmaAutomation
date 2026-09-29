class Valve:

    def __init__(self, name):
        self.name = name
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def get_status(self):
        return {
            "name": self.name,
            "is_open": self.is_open
        }

valve = Valve("XV_A_OUT")

print(valve.get_status())

valve.open()

print(valve.get_status())

valve.close()

print(valve.get_status())