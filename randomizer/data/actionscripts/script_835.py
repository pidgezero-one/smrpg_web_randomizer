from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_835_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_835_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_835_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_835_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_835_walk_1_step_southeast_4',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_835_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [16]
    },
    {
        "identifier": 'ACTION_835_ret_6',
        "command": 'ret'
    }
]
