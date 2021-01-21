from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_1022_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._066_KICK_BALL_SHELL, 4]
    },
    {
        "identifier": 'ACTION_1022_db_1',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_1022_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_1022_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_1022_overwrite_solidity_4',
        "command": 'overwrite_solidity',
        "args": [[]]
    },
    {
        "identifier": 'ACTION_1022_object_memory_clear_bit_5',
        "command": 'object_memory_clear_bit',
        "args": [0x08, [3, 4]]
    },
    {
        "identifier": 'ACTION_1022_floating_off_6',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_1022_fixed_f_coord_on_7',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_1022_db_8',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_1022_embedded_animation_routine_9',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_1022_embedded_animation_routine_10',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_1022_db_11',
        "command": 'db',
        "args": [0xfd, 0x24, 0x00, 0x07]
    },
    {
        "identifier": 'ACTION_1022_jmp_if_random_above_128_12',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_1022_db_17']
    },
    {
        "identifier": 'ACTION_1022_jmp_if_random_above_128_13',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_1022_add_16']
    },
    {
        "identifier": 'ACTION_1022_add_14',
        "command": 'add',
        "args": [0x700c, 24]
    },
    {
        "identifier": 'ACTION_1022_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_1022_db_17']
    },
    {
        "identifier": 'ACTION_1022_add_16',
        "command": 'add',
        "args": [0x700c, 232]
    },
    {
        "identifier": 'ACTION_1022_db_17',
        "command": 'db',
        "args": [0xfd, 0x25]
    },
    {
        "identifier": 'ACTION_1022_db_18',
        "command": 'db',
        "args": [0x25, 0xa0, 0x08, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_1022_pause_19',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'ACTION_1022_bpl_26_27_28_20',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_1022_visibility_off_21',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_1022_end_all_22',
        "command": 'end_all'
    }
]
