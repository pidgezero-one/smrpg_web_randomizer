from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_503_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_503_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_503_set_7000_to_pressed_button_2',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_503_jmp_if_7000_any_bits_set_3',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 3, 6], 'EVENT_503_start_loop_n_times_5']
    },
    {
        "identifier": 'EVENT_503_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_503_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'EVENT_503_set_7000_to_pressed_button_6',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_503_jmp_if_7000_any_bits_set_7',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_503_remember_last_object_20']
    },
    {
        "identifier": 'EVENT_503_jmp_if_7000_any_bits_set_8',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_503_enable_controls_until_return_12']
    },
    {
        "identifier": 'EVENT_503_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_503_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_503_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_503_enable_controls_until_return_12',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_503_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_503_action_queue_sync_13_SUBSCRIPT_walk_to_xy_coords_9',
                "command": 'walk_to_xy_coords',
                "args": [8, 64]
            }
        ]
    },
    {
        "identifier": 'EVENT_503_jmp_if_object_not_in_level_14',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, 'EVENT_503_remember_last_object_20']
    },
    {
        "identifier": 'EVENT_503_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_503_remove_from_current_level_16',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_503_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_503_add_frog_coins_18',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_503_remove_from_level_19',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    },
    {
        "identifier": 'EVENT_503_remember_last_object_20',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_503_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_503_ret_22',
        "command": 'ret'
    }
]
