from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_23_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_23_add_z_coord_1_step_1',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_23_dec_z_coord_1_step_2',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_23_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_23_set_animation_speed_0']
    }
]
