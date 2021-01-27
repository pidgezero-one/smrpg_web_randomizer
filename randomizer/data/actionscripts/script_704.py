from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_704_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_704_walk_1_step_northwest_1',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_704_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_704_walk_1_step_northwest_1']
    },
    {
        "identifier": 'ACTION_704_ret_3',
        "command": 'ret'
    }
]