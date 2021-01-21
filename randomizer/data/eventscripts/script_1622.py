from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1622_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'EVENT_1622_ret_10']
    },
    {
        "identifier": 'EVENT_1622_set_7000_to_tapped_button_1',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1622_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 4, 'EVENT_1622_ret_10']
    },
    {
        "identifier": 'EVENT_1622_set_7000_to_pressed_button_3',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1622_jmp_if_var_not_equals_short_4',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 4, 'EVENT_1622_ret_10']
    },
    {
        "identifier": 'EVENT_1622_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._032_UNDERGROUND_WARP, 6]
    },
    {
        "identifier": 'EVENT_1622_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_walk_to_xy_coords_4',
                "command": 'walk_to_xy_coords',
                "args": [3, 62]
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1622_action_queue_async_6_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1622_set_bit_7',
        "command": 'set_bit',
        "args": [0x7096, 5]
    },
    {
        "identifier": 'EVENT_1622_pixelate_layers_8',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 8, 196]
    },
    {
        "identifier": 'EVENT_1622_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._069_MIDAS_RIVER_WATERFALL, RadialDirections.SOUTH, 9, 108, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1622_ret_10',
        "command": 'ret'
    }
]
