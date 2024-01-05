import copy
from typing import Dict


class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        # fuel station with specified number of spots for each fuel type
        self.available_spots :Dict[str, int] = {
            "diesel" : diesel,
            "petrol" : petrol,
            "electric" : electric,
        }
        self.filled_spots = copy.copy(self.available_spots)

    def fuel_vehicle(self, fuel_type: str) -> bool:
        # checking if each fuel type available or not
        if self.filled_spots.get(fuel_type) > 0:
            self.filled_spots[fuel_type] -= 1
            return True
        else:
            return False
    
    def open_fuel_slot(self, fuel_type: str) -> bool:
        # checking if total spots of each fuel type is grater than filled spots 
        if self.filled_spots.get(fuel_type) < self.available_spots.get(fuel_type):
            self.filled_spots[fuel_type] += 1
            return True
        else:
            return False
#initializing class
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.fuel_vehicle('petrol'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.fuel_vehicle('electric'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.open_fuel_slot('diesel'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.open_fuel_slot('electric'))
print(fuel_station.open_fuel_slot('electric'))
print(fuel_station.available_spots)
print(fuel_station.filled_spots)