from parfenovskaia.appartment import Door, Wall, Room, Appartment, Window, PAPER_LENGTH, WALL_HEIGT
import math


COLOR_CONS = 9 / 60.

kitchen = Room(
    walls=[
        Wall(width=361),
        Wall(width=142 + 155 + 15, windows=[Window(155)]),
        Wall(width=406),
        Wall(width=137, doors=[Door(96)]),
        Wall(width=86),
        Wall(width=103),
        Wall(width=41),
        Wall(width=72),
])

room1 = Room(
    walls=[
        Wall(width=480),
        Wall(width=100 + 155 + 57, windows=[Window(155)]),
        Wall(width=480),
        Wall(width=159 + 106 + 47, doors=[Door(106)]),
])
 
room2 = Room(
    walls=[
        Wall(width=600),
        Wall(width=79.5 + 175 + 43.5, windows=[Window(175)]),
        Wall(width=600),
        Wall(width=173 + 106 + 19, doors=[Door(106)]),
])


hallway = Room(
    walls=[
        Wall(width = 46.5 + 86 + 61 + 83.5, doors=[Door(86), Door(83.5)]),
        Wall(width = 12 + 96.5 + 20, doors=[Door(96.5)]),
        Wall(width=73),
        Wall(width=56 + 107.5 + 200 + 107 + 13, doors=[Door(107.5), Door(107)]),
        Wall(width=61.5 + 86 + 56, doors=[Door(86)]),
        Wall(width=141),
        Wall(width=78),
        Wall(width=21.5),
        Wall(width=79),
        Wall(width=185.5 + 95 + 171.5, doors=[Door(95)]),
])

wardrobe = Room(
    walls=[
        Wall(width=56 + 86 + 63, doors=[Door(86)]),
        Wall(width=150),
        Wall(width=205),
        Wall(width=150),
])


appartment = Appartment(
    # rooms=[kitchen, room1, room2, hallway]
    rooms=[wardrobe, room1, room2, hallway]
)


number_of_lanes_in_roll = math.floor(PAPER_LENGTH / WALL_HEIGT)
print('number of lanes in roll:', number_of_lanes_in_roll)

def print_area(el, name):
    print('=' * 50)
    print(name)
    print('=' * 50)
    print('all:', el.area() / 100 / 100)
    print('with_doors:', el.area(with_doors=True) / 100 / 100)
    print('with_windows:', el.area(with_windows=True) / 100 / 100)
    print('with_all:', el.area(with_doors=True, with_windows=True) / 100 / 100)
    print('paper_lanes:', el.paper_lanes())
    print('paper_rolls:', el.paper_lanes() / number_of_lanes_in_roll)
    print('color_cons:', el.area() / 100 / 100 *  COLOR_CONS)

    
print_area(appartment, 'total')
print_area(kitchen, 'kitchen')
print_area(room1, 'room1')
print_area(room2, 'room2')
print_area(hallway, 'hallway')
print_area(wardrobe, 'wardrobe')
