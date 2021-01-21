from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_502_bpl_26_27_28_0',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_502_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_502_start_loop_n_times_2',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_502_jump_to_height_silent_3',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_502_shift_northeast_pixels_4',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_502_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_502_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_502_pause_5']
    },
    {
        "identifier": 'ACTION_502_pause_7',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_502_end_loop_8',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_502_set_bit_9',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_502_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_500_db_0']
    }
]
