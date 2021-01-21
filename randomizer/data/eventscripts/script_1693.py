from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1693_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_1693_ret_21']
    },
    {
        "identifier": 'EVENT_1693_set_7000_to_tapped_button_1',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1693_jmp_if_7000_all_bits_clear_2',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_1693_ret_21']
    },
    {
        "identifier": 'EVENT_1693_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1693_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_1693_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._154_BIG_SQUISH, 6]
    },
    {
        "identifier": 'EVENT_1693_pause_5',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1693_store_02_to_0248_6',
        "command": 'store_02_to_0248'
    },
    {
        "identifier": 'EVENT_1693_apply_tile_mod_7',
        "command": 'apply_tile_mod',
        "args": [Rooms._423_BELOME_TEMPLE_AREA_06_BELOMES_FORTUNE_ROOM_WELEVATING_PLATFORM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1693_store_00_to_0248_8',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_1693_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1693_add_10',
        "command": 'add',
        "args": [0x70ad, 0x01]
    },
    {
        "identifier": 'EVENT_1693_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad]
    },
    {
        "identifier": 'EVENT_1693_add_12',
        "command": 'add',
        "args": [0x7000, 5]
    },
    {
        "identifier": 'EVENT_1693_set_random_13',
        "command": 'set_random',
        "args": [0x702a, 20]
    },
    {
        "identifier": 'EVENT_1693_mem_compare_14',
        "command": 'mem_compare',
        "args": [0x7000, 0x702a]
    },
    {
        "identifier": 'EVENT_1693_jmp_if_comparison_result_is_lesser_15',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1693_clear_bit_18']
    },
    {
        "identifier": 'EVENT_1693_set_bit_16',
        "command": 'set_bit',
        "args": [0x704e, 7]
    },
    {
        "identifier": 'EVENT_1693_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_1693_set_bit_19']
    },
    {
        "identifier": 'EVENT_1693_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x704e, 7]
    },
    {
        "identifier": 'EVENT_1693_set_bit_19',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1693_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_inc_palette_row_by_0',
                "command": 'inc_palette_row_by',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1693_action_queue_async_20_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1693_ret_21',
        "command": 'ret'
    }
]
