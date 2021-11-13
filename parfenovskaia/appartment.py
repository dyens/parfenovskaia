from dataclasses import dataclass, field
from typing import List

WALL_HEIGT = 200


@dataclass
class Door:
    width: float
    height: float = WALL_HEIGT - 61

    def area(self):
        return self.width * self.height


@dataclass
class Window:
    width: float
    height: float =  WALL_HEIGT - 17

    def area(self):
        return self.width * self.height

@dataclass
class Wall:
    width: float
    height: float = WALL_HEIGT
    doors: List[Door] = field(default_factory=lambda : list())
    windows: List[Window] = field(default_factory=lambda: list())

    def area(self, with_doors=False, with_windows=False):
        total = self.width * self.height
        if with_doors is False:
            doors_area = sum([door.area() for door in self.doors])
            total -= doors_area 
        if with_windows is False:
            windows_area = sum([window.area() for window in self.windows])
            total -= windows_area 
        return total
    
    
@dataclass
class Room:
    walls: List[Wall]

    def area(self, with_doors=False, with_windows=False):
        return sum([wall.area(with_doors, with_windows) for wall in self.walls])


@dataclass
class Appartment:
    rooms: List[Room]


    def area(self, with_doors=False, with_windows=False):
        return sum([room.area(with_doors, with_windows) for room in self.rooms])
