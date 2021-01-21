from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_466_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_466_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_466_walk_1_step_south_2',
        "command": 'walk_1_step_south'
    },
    {
        "identifier": 'ACTION_466_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_466_walk_1_step_south_2']
    }
]
