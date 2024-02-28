from car import Car
from car_enum import CarType, FuelType

class CarVariant(Car):
    def __init__(self,name:str,car_type: CarType, fuel_type: FuelType, price: int):
        super().__init__(car_type, fuel_type, price)
        self._name=name
    
    def description(self):
        return f"{self._name} is a car of type {self._cartype} with fuel type {self._fuel_type} available at price {self._price}"