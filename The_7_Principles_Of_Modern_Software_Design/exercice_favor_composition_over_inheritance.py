from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol, List


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


class RentPrice(Protocol):

    def get_total_prrice(self) -> int:
        ...



@dataclass
class PricePerDay():
    price_per_km: int
    price_per_day: int
    nb_days: int

    def get_total_prrice(self) -> int:
        return self.price_per_day*self.nb_days

@dataclass
class PricePerMonth():
    price_per_month: int
    nb_month: int

    def get_total_prrice(self) -> int:
        return self.price_per_day*self.nb_month



@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool
    rent_price: List[RentPrice] = field(default_factory=List)


@dataclass
class Car(Vehicle):
    number_of_seats: int = 5
    storage_capacity_litres: int = 200


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle = TruckCabStyle.REGULAR



@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    reserved: bool
    rent_price: List[RentPrice] = field(default_factory=List)


def main():
    pass


if __name__ == "__main__":
    main()
