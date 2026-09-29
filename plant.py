from models.tank import Tank
from models.valve import Valve


class Plant:

    def __init__(self, config):

        self.name = config["plant"]["name"]

        self.tanks = {}

        for tank_id, tank_config in config["tanks"].items():

            tank = Tank(
                tank_config["name"],
                tank_config["capacity_l"],
                tank_config["initial_volume_l"],
                tank_config["initial_temperature_c"]
            )

            self.tanks[tank_id] = tank

        self.valves = {}

        for valve_id, valve_config in config["valves"].items():

            valve = Valve(
                valve_config["name"]
            )

            self.valves[valve_id] = valve

    def get_tank(self, tank_id):
        return self.tanks[tank_id]

    def get_valve(self, valve_id):
        return self.valves[valve_id]