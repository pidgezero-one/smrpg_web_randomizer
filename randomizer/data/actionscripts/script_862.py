from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_862_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_862_shift_east_pixels_1',
        "command": 'shift_east_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_862_shift_west_pixels_2',
        "command": 'shift_west_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_862_shift_east_pixels_3',
        "command": 'shift_east_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_862_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_862_set_animation_speed_0']
    }
]
