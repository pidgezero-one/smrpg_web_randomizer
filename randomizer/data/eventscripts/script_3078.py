from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3078_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3078_set_7000_to_70A0_short_mem_1',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a8]
    },
    {
        "identifier": 'EVENT_3078_set_70A0_short_mem_to_7000_2',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70b4]
    },
    {
        "identifier": 'EVENT_3078_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3078_set_7010_to_object_xyz_4',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3078_set_7000_to_7000_short_mem_5',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7014]
    },
    {
        "identifier": 'EVENT_3078_add_6',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3078_set_7000_short_mem_to_7000_7',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7014]
    },
    {
        "identifier": 'EVENT_3078_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7064, 6]
    },
    {
        "identifier": 'EVENT_3078_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3078_create_packet_at_7010_coords_jmp_if_null_10',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._004_MONSTER_FACE, 'EVENT_3078_pause_11']
    },
    {
        "identifier": 'EVENT_3078_pause_11',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3078_pause_12',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'EVENT_3078_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_3078_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700e, 156, 'EVENT_3078_start_battle_18']
    },
    {
        "identifier": 'EVENT_3078_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700e, 157, 'EVENT_3078_start_battle_20']
    },
    {
        "identifier": 'EVENT_3078_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700e, 158, 'EVENT_3078_jmp_if_bit_set_22']
    },
    {
        "identifier": 'EVENT_3078_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700e, 159, 'EVENT_3078_jmp_if_bit_set_22']
    },
    {
        "identifier": 'EVENT_3078_start_battle_18',
        "command": 'start_battle',
        "args": [0x009c, 21]
    },
    {
        "identifier": 'EVENT_3078_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_3078_jmp_if_bit_set_22']
    },
    {
        "identifier": 'EVENT_3078_start_battle_20',
        "command": 'start_battle',
        "args": [0x009d, 4]
    },
    {
        "identifier": 'EVENT_3078_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_3078_jmp_if_bit_set_22']
    },
    {
        "identifier": 'EVENT_3078_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3078_reset_and_choose_game_30']
    },
    {
        "identifier": 'EVENT_3078_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3078_set_bit_24',
        "command": 'set_bit',
        "args": [0x7064, 6]
    },
    {
        "identifier": 'EVENT_3078_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x25, 0x40, 0x00, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_jmp_if_bit_set_4',
                "command": 'jmp_if_bit_set',
                "args": [0x7040, 1, 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_object_memory_clear_bit_9']
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_object_memory_set_bit_6',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_ret_8',
                "command": 'ret'
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_object_memory_clear_bit_9',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_sequence_looping_off_10',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3078_action_queue_sync_25_SUBSCRIPT_ret_12',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3078_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x7064, 5]
    },
    {
        "identifier": 'EVENT_3078_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3078_ret_29']
    },
    {
        "identifier": 'EVENT_3078_set_bit_28',
        "command": 'set_bit',
        "args": [0x7064, 5]
    },
    {
        "identifier": 'EVENT_3078_ret_29',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3078_reset_and_choose_game_30',
        "command": 'reset_and_choose_game'
    }
]
