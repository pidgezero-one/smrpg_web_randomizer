from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1686_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7050, 6, 'EVENT_1686_ret_30']
    },
    {
        "identifier": 'EVENT_1686_set_7000_to_tapped_button_1',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1686_jmp_if_7000_all_bits_clear_2',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_1686_ret_30']
    },
    {
        "identifier": 'EVENT_1686_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1686_action_queue_sync_3_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_1686_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1686_ret_30']
    },
    {
        "identifier": 'EVENT_1686_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1686_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1686_pause_5']
    },
    {
        "identifier": 'EVENT_1686_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._154_BIG_SQUISH, 6]
    },
    {
        "identifier": 'EVENT_1686_pause_8',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1686_store_02_to_0248_9',
        "command": 'store_02_to_0248'
    },
    {
        "identifier": 'EVENT_1686_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1686_store_00_to_0248_11',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_1686_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1686_set_bit_13',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1686_jmp_if_var_not_equals_short_14',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 0, 'EVENT_1686_jmp_if_var_not_equals_short_20']
    },
    {
        "identifier": 'EVENT_1686_set_short_15',
        "command": 'set_short',
        "args": [0x7024, 0x0002]
    },
    {
        "identifier": 'EVENT_1686_set_7000_to_70A0_short_mem_16',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_1686_add_17',
        "command": 'add',
        "args": [0x7000, 32]
    },
    {
        "identifier": 'EVENT_1686_set_70A0_short_mem_to_7000_18',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_1686_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_1685_set_7000_to_7000_short_mem_39']
    },
    {
        "identifier": 'EVENT_1686_jmp_if_var_not_equals_short_20',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 0, 'EVENT_1686_set_7000_to_70A0_short_mem_26']
    },
    {
        "identifier": 'EVENT_1686_set_short_21',
        "command": 'set_short',
        "args": [0x7026, 0x0008]
    },
    {
        "identifier": 'EVENT_1686_set_7000_to_70A0_short_mem_22',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_1686_add_23',
        "command": 'add',
        "args": [0x7000, 32]
    },
    {
        "identifier": 'EVENT_1686_set_70A0_short_mem_to_7000_24',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_1686_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_1685_set_7000_to_7000_short_mem_39']
    },
    {
        "identifier": 'EVENT_1686_set_7000_to_70A0_short_mem_26',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_1686_add_27',
        "command": 'add',
        "args": [0x7000, 32]
    },
    {
        "identifier": 'EVENT_1686_set_70A0_short_mem_to_7000_28',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_1686_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1685_set_29']
    },
    {
        "identifier": 'EVENT_1686_ret_30',
        "command": 'ret'
    }
]
