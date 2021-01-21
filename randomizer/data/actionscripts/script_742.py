from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_742_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_742_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_742_walk_1_step_southeast_2',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_742_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_742_walk_1_step_northwest_4',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_742_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_742_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_742_sequence_looping_on_0']
    }
]
