from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_451_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_451_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7045, 7, 'ACTION_451_pause_3']
    },
    {
        "identifier": 'ACTION_451_pause_2',
        "command": 'pause',
        "args": [176]
    },
    {
        "identifier": 'ACTION_451_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_451_db_4',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x03, 0x9f, 0x57]
    },
    {
        "identifier": 'ACTION_451_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_451_pause_3']
    },
    {
        "identifier": 'ACTION_451_sequence_looping_on_6',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_451_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_451_pause_8',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_451_walk_1_step_southwest_9',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_451_walk_1_step_southeast_10',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_451_shift_northeast_steps_11',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_451_walk_1_step_southwest_12',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_451_walk_1_step_northwest_13',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_451_shift_southwest_steps_14',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_451_shift_southeast_steps_15',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_451_shift_northeast_steps_16',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_451_walk_1_step_northwest_17',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_451_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_451_walk_1_step_southwest_12']
    }
]
