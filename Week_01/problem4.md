Problem 4 (Medium): Smart Thermostat System
Create a Thermostat class that monitors and controls room temperature with safety constraints and historical tracking.

Requirements:

Design a Thermostat class with the following capabilities:

1. Class-level Configuration:

Define temperature safety limits (min_temp = 15.0°C, max_temp = 30.0°C) as class variables
Track how many thermostats have been created using device_count

2. Instance Management:

Each thermostat should have a location identifier and track its current_temp
Maintain a history of all temperature readings in a readings list
When creating a thermostat, validate the initial_temp against safety limits. If the initial temperature is out of range, set it to min_temp

3. Core Methods:

set_temperature(new_temp) - Attempt to change temperature with validation (reject and keep current temperature if out of range)
get_average_temp() - Calculate the average of all historical readings
display_status() - Show current state including location, temperature, reading count, and average
is_comfortable() - Determine if current temperature is in a comfortable range (20-25°C)

4. Test Scenario: Create two thermostats:

One for “Living Room” starting at 22.0°C
One for “Garage” starting at 10.0°C (out of safe range)

5. Demonstrate:

Adjusting the Living Room to 26.5°C
Attempting to set Living Room to 35.0°C (should be rejected)
Displaying status for both devices
Checking comfort status of the Living Room
Displaying the total thermostat count

Expected Output
```
Temperature set to 22.0°C

Initial temperature out of range. Set to minimum.

Temperature set to 26.5°C

Temperature 35.0°C is out of allowed range (15.0-30.0)

Thermostat in Living Room: 26.5°C
Reading count: 2
Average temperature: 24.25°C

Thermostat in Garage: 15.0°C
Reading count: 1
Average temperature: 15.0°C

False

2
```