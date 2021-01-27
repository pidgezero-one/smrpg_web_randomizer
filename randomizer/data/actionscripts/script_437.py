from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_437_shift_xy_pixels_0',
        "command": 'shift_xy_pixels',
        "args": [16, 248]
    },
    {
        "identifier": 'ACTION_437_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x0d, [6]]
    },
    {
        "identifier": 'ACTION_437_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_437_db_3',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_437_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_437_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x20, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_437_embedded_animation_routine_6',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x00, 0x0c, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80]
    },
    {
        "identifier": 'ACTION_437_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_437_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_437_pause_7']
    }
]
