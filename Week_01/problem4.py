class Thermostat:
    min_temp = 15.0
    max_temp = 30.0
    device_count = 0

    def __init__(self, location, initial_temp):
        self.location = location
        self.readings = []
        
        if initial_temp < Thermostat.min_temp or initial_temp > Thermostat.max_temp:
            print("Initial temperature out of range. Set to minimum.")
            self.current_temp = Thermostat.min_temp
        else:
            self.current_temp = initial_temp
        
        self.readings.append(self.current_temp)
        Thermostat.device_count += 1

    def set_temperature(self, new_temp):
        if new_temp < Thermostat.min_temp or new_temp > Thermostat.max_temp:
            print(f"Temperature {new_temp}°C is out of allowed range ({Thermostat.min_temp}-{Thermostat.max_temp})")
        else:
            self.current_temp = new_temp
            self.readings.append(self.current_temp)
    
    def get_average_temperature(self):
        return sum(self.readings) / len(self.readings)
    
    def display_status(self):
        print(f"Thermostat in {self.location}: {self.current_temp}°C")
        print(f"Reading count: {len(self.readings)}")
        print(f"average temperature: {self.get_average_temperature():.2f}°C")

    def is_comfortable(self):
        return 20 <= self.current_temp <= 25
    
living_room = Thermostat("Living Room", 22)
garage = Thermostat("Garage", 10)
living_room.set_temperature(26.5)
living_room.set_temperature(35)
living_room.display_status()
garage.display_status()
print(living_room.is_comfortable())
print(f"{Thermostat.device_count}")