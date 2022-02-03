from dataclasses import dataclass
from enum import Enum, auto


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


@dataclass
class VehicleInformation:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool


@dataclass
class VehiclePerDay:
    price_per_km: int
    price_per_day: int
    info: VehicleInformation


@dataclass
class VehiclePerMonth:
    price_per_month: int
    info: VehicleInformation

@dataclass
class CarPerDay():
    per_day: VehiclePerDay
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class CarPerMonth():
    per_day: VehiclePerDay
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class Truck:
    cab_style: TruckCabStyle
    info: VehicleInformation


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    price_per_month: int
    reserved: bool


def main():
    pass


if __name__ == "__main__":
    main()
