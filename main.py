from core.config_loader import ConfigLoader
from plant import Plant


config_loader = ConfigLoader("config/plant_config.json")

config = config_loader.load()

plant = Plant(config)

print(plant.name)
print(plant.tanks)
tank_a = plant.get_tank("Tank_A")
tank_b = plant.get_tank("Tank_B")

#print(tank_a.get_status())
#print(plant.tanks.keys())
valve_a_out = plant.get_valve("XV_A_OUT")

print(valve_a_out.get_status())

valve_a_out.open()

print(valve_a_out.get_status())