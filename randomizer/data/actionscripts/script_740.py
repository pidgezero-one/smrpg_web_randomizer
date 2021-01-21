from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_740_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_740_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_740_walk_1_step_southeast_2',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_740_walk_1_step_northeast_3',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_740_walk_1_step_northwest_4',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_740_walk_1_step_southwest_5',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_740_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_740_sequence_looping_on_0']
    }
]
