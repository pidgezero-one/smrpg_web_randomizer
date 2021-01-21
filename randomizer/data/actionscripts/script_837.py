from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_837_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_837_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_837_shift_northeast_steps_2',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_837_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_837_walk_1_step_southwest_4',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_837_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_837_ret_6',
        "command": 'ret'
    }
]
