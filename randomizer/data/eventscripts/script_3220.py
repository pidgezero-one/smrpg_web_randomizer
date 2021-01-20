from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3220_set_7000_to_object_coord_0',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A8, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3220_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3220_clear_bit_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3220_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_jump_to_height_silent_9',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_face_southeast_11',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_fixed_f_coord_on_12',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_play_sound_14',
                "command": 'play_sound',
                "args": [Sounds._109_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_sequence_looping_off_15',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_sequence_playback_off_16',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_set_solidity_bits_17',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_object_memory_clear_bit_18',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_ret_19',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_set_short_mem_20',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7032]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_face_east_21',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_sequence_looping_off_22',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_sequence_playback_off_23',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_object_memory_clear_bit_24',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_2_SUBSCRIPT_ret_25',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3220_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3220_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3220_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.F]
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_jmp_if_var_equals_short_1',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_8']
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_jmp_if_var_equals_short_2',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_8']
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 2, 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_8']
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_15']
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 4, 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_15']
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 6, 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_15']
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_3220_action_queue_sync_5_SUBSCRIPT_ret_21']
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_sequence_looping_off_11',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_off_12',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_set_bit_13',
                "command": 'set_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_jmp_14',
                "command": 'jmp',
                "args": ['EVENT_3220_action_queue_sync_5_SUBSCRIPT_ret_21']
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_15',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_sequence_looping_on_16',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_sequence_looping_off_18',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_off_19',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_set_bit_20',
                "command": 'set_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3220_action_queue_sync_5_SUBSCRIPT_ret_21',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3220_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_if_var_equals_short_1',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_9']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_if_var_equals_short_2',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_9']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 2, 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_9']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_21']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 4, 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_21']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 6, 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_21']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_object_memory_clear_bit_7',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_8',
                "command": 'jmp',
                "args": ['EVENT_3220_action_queue_async_6_SUBSCRIPT_sequence_looping_off_37']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_10',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_12',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_14',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_16',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_18',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_20',
                "command": 'jmp',
                "args": ['EVENT_3220_action_queue_async_6_SUBSCRIPT_object_memory_clear_bit_32']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_22',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_24',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_26',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_28',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_30',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_31',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_object_memory_clear_bit_32',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_700C_to_object_coord_33',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.Y, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_jmp_if_var_not_equals_short_34',
                "command": 'jmp_if_var_not_equals_short',
                "args": [0x700c, 21, 'EVENT_3220_action_queue_async_6_SUBSCRIPT_sequence_looping_off_37']
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_set_bit_35',
                "command": 'set_bit',
                "args": [0x7044, 5]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_object_memory_set_bit_36',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_sequence_looping_off_37',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3220_action_queue_async_6_SUBSCRIPT_sequence_playback_off_38',
                "command": 'sequence_playback_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3220_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_3220_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3220_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 336],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3220_add_9',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3220_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3220_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
