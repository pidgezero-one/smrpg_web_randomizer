from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_808_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_808_walk_1_step_northeast_1',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_808_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_808_set_animation_speed_0']
    }
]
