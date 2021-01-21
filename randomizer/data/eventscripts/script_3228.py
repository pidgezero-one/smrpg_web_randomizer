from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3228_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3228_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3228_clear_bit_16']
    },
    {
        "identifier": 'EVENT_3228_set_7000_to_tapped_button_2',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_3228_jmp_if_7000_all_bits_clear_3',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3228_clear_bit_16']
    },
    {
        "identifier": 'EVENT_3228_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_3228_start_embedded_action_script_async_15']
    },
    {
        "identifier": 'EVENT_3228_set_7000_to_object_coord_5',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3228_jmp_if_var_not_equals_short_6',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 17, 'EVENT_3228_start_embedded_action_script_async_15']
    },
    {
        "identifier": 'EVENT_3228_set_7000_to_object_coord_7',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3228_jmp_if_var_not_equals_short_8',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 121, 'EVENT_3228_start_embedded_action_script_async_15']
    },
    {
        "identifier": 'EVENT_3228_jmp_if_object_trigger_disabled_9',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_2, Rooms._179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, 'EVENT_3228_start_embedded_action_script_async_15']
    },
    {
        "identifier": 'EVENT_3228_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3228_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3228_action_queue_sync_11_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3228_action_queue_sync_11_SUBSCRIPT_object_memory_clear_bit_1',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3228_action_queue_sync_11_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3228_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3228_action_queue_sync_12_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3228_action_queue_sync_12_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3228_action_queue_sync_12_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3228_action_queue_sync_12_SUBSCRIPT_end_all_3',
                "command": 'end_all'
            }
        ]
    },
    {
        "identifier": 'EVENT_3228_set_bit_13',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_3228_set_bit_14',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_3228_start_embedded_action_script_async_15',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_15_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_3228_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3228_set_7000_to_pressed_button_17',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_3228_jmp_if_7000_all_bits_clear_18',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[6], 'EVENT_3228_set_7000_to_pressed_button_20']
    },
    {
        "identifier": 'EVENT_3228_set_bit_19',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3228_set_7000_to_pressed_button_20',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_3228_jmp_if_7000_all_bits_clear_21',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[0, 1, 2, 3], 'EVENT_3228_pause_0']
    },
    {
        "identifier": 'EVENT_3228_start_embedded_action_script_async_22',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 7, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_set_700C_to_object_coord_3']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_set_700C_to_object_coord_3',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_south_pixels_16']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_southeast_pixels_14']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 2, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_east_pixels_12']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_var_equals_short_7',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 3, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_northeast_pixels_26']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_var_equals_short_8',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 4, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_north_pixels_24']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_var_equals_short_9',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_northwest_pixels_22']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_var_equals_short_10',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 6, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_west_pixels_20']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_jmp_if_var_equals_short_11',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 7, 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_southwest_pixels_18']
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_east_pixels_12',
                "command": 'shift_east_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_ret_13',
                "command": 'ret'
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_southeast_pixels_14',
                "command": 'shift_southeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_ret_15',
                "command": 'ret'
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_south_pixels_16',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_ret_17',
                "command": 'ret'
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_southwest_pixels_18',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_ret_19',
                "command": 'ret'
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_west_pixels_20',
                "command": 'shift_west_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_ret_21',
                "command": 'ret'
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_northwest_pixels_22',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_ret_23',
                "command": 'ret'
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_north_pixels_24',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_ret_25',
                "command": 'ret'
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_shift_northeast_pixels_26',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3228_start_embedded_action_script_async_22_SUBSCRIPT_ret_27',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3228_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_3228_pause_0']
    }
]
