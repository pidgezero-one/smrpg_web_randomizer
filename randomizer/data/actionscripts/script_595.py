from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_595_db_0',
        "command": 'db',
        "args": [0x9a]
    },
    {
        "identifier": 'ACTION_595_visibility_on_1',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_595_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_595_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_595_walk_1_step_southwest_4',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_595_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_595_walk_1_step_southwest_4']
    }
]
