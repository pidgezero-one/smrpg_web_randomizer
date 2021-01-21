from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_700_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_700_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_700_shift_northwest_steps_2',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_700_walk_1_step_southwest_3',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_700_shift_southeast_steps_4',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_700_walk_1_step_northeast_5',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_700_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_700_sequence_looping_on_0']
    }
]
