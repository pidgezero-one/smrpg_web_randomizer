from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_960_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_960_jump_to_height_1',
        "command": 'jump_to_height',
        "args": [80]
    },
    {
        "identifier": 'ACTION_960_walk_1_step_southeast_2',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_960_ret_3',
        "command": 'ret'
    }
]
