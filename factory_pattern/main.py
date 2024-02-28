from car_variant import CarVariant
from car_enum import CarType,FuelType


harrier=CarVariant(
    name="harrier",
    car_type=CarType.SUV,
    fuel_type=FuelType.PETROL,
    price=2655522
)

print(harrier.description())