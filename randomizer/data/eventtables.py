from types import SimpleNamespace

controller_direction_table = {
    0: 'LEFT',
    1: 'RIGHT',
    2: 'DOWN',
    3: 'UP',
    4: 'X',
    5: 'A',
    6: 'Y',
    7: 'B'
}

ControllerDirections = SimpleNamespace()
for i in controller_direction_table:
    setattr(ControllerDirections, controller_direction_table[i], i)

radial_direction_table = {
    0x00: 'EAST',
    0x02: 'SOUTHEAST',
    0x04: 'SOUTH',
    0x06: 'SOUTHWEST',
    0x08: 'WEST',
    0x0A: 'NORTHWEST',
    0x0C: 'NORTH',
    0x0E: 'NORTHEAST'
}

RadialDirections = SimpleNamespace()
for i in radial_direction_table:
    setattr(RadialDirections, radial_direction_table[i], i)
