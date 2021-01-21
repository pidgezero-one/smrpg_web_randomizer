from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_926_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_926_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_926_jump_to_subroutine_2',
        "command": 'jump_to_subroutine',
        "args": [0x3801]
    },
    {
        "identifier": 'ACTION_926_transfer_xyzf_steps_3',
        "command": 'transfer_xyzf_steps',
        "args": [0, 0, 20, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_926_pause_4',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_926_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_926_jump_to_subroutine_2']
    }
]
