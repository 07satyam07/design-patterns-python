from abc import ABC,abstractmethod
from car_enum import FuelType,CarType

class Car(ABC):
    def __init__(self,car_type:CarType,fuel_type:FuelType,price:int):
        self._cartype=car_type.value
        self._fuel_type=fuel_type.value
        self._price=price
    
    @abstractmethod
    def description(self):
        pass

    @property
    def fuel_type(self):
        return self._fuel_type
    
    @property
    def price(self):
        return self._price
    
    @property
    def car_type(self):
        return self.car_type
    
