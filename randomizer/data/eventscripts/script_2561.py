from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2561_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_2304_ret_0']
    },
    {
        "identifier": 'EVENT_2561_enable_controls_1',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2561_freeze_camera_2',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2561_unfreeze_all_npcs_3',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_2561_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6]
    },
    {
        "identifier": 'EVENT_2561_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_700C_to_object_coord_2',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_12']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_14']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 2, 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_16']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 3, 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_18']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_if_var_equals_short_7',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 4, 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_20']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_if_var_equals_short_8',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_22']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_if_var_equals_short_9',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 6, 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_24']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_11',
                "command": 'jmp',
                "args": ['EVENT_2561_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_25']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_13',
                "command": 'jmp',
                "args": ['EVENT_2561_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_25']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_15',
                "command": 'jmp',
                "args": ['EVENT_2561_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_25']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_17',
                "command": 'jmp',
                "args": ['EVENT_2561_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_25']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_19',
                "command": 'jmp',
                "args": ['EVENT_2561_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_25']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_21',
                "command": 'jmp',
                "args": ['EVENT_2561_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_25']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_jmp_23',
                "command": 'jmp',
                "args": ['EVENT_2561_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_25']
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_24',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_25',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_priority_26',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_animation_speed_27',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_shift_z_up_steps_28',
                "command": 'shift_z_up_steps',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_run_away_transfer_29',
                "command": 'run_away_transfer'
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_face_south_30',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2561_action_queue_async_5_SUBSCRIPT_set_solidity_bits_31',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2561_fade_out_to_black_async_6',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_2561_open_save_menu_7',
        "command": 'open_save_menu'
    }
]
