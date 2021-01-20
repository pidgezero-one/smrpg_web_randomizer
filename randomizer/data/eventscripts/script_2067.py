from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2067_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [5, 9]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_0_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2067_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_2067_action_queue_sync_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2067_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2067_action_queue_sync_2_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2067_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_sync_2_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2067_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_shadow_on_6',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_3_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2067_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_9',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_jump_to_height_silent_12',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._121_AXEM_RANGER_TELEPORT, 4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southeast_pixels_14',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_visibility_off_15',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southeast_pixels_16',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_visibility_on_17',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southeast_pixels_18',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_20',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_face_northwest_22',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_24',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_jump_to_height_silent_26',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_play_sound_27',
                "command": 'play_sound',
                "args": [Sounds._121_AXEM_RANGER_TELEPORT, 4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_28',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_visibility_off_29',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_30',
                "command": 'shift_southwest_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_visibility_on_31',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_32',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_33',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_34',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_35',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_face_northeast_36',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_37',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_38',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_39',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_jump_to_height_silent_40',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_play_sound_41',
                "command": 'play_sound',
                "args": [Sounds._121_AXEM_RANGER_TELEPORT, 4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_northwest_pixels_42',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_visibility_off_43',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_northwest_pixels_44',
                "command": 'shift_northwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_visibility_on_45',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_shift_northwest_pixels_46',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_47',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_48',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_49',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_face_northeast_50',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_4_SUBSCRIPT_pause_51',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2067_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2067_action_queue_sync_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2067_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2067_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_sync_6_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2067_action_queue_sync_6_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_sync_6_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2067_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._121_AXEM_RANGER_TELEPORT, 4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_face_southeast_11',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_fixed_f_coord_on_13',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._121_AXEM_RANGER_TELEPORT, 4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_northeast_pixels_16',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_visibility_off_17',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_northeast_pixels_18',
                "command": 'shift_northeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_visibility_on_19',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_northeast_pixels_20',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_fixed_f_coord_off_22',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_face_southwest_24',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_fixed_f_coord_on_26',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_play_sound_28',
                "command": 'play_sound',
                "args": [Sounds._121_AXEM_RANGER_TELEPORT, 4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_southeast_pixels_29',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_visibility_off_30',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_southeast_pixels_31',
                "command": 'shift_southeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_visibility_on_32',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_shift_southeast_pixels_33',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_pause_34',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_face_southwest_35',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_set_solidity_bits_36',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_7_SUBSCRIPT_fixed_f_coord_off_37',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2067_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_2067_action_queue_async_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2067_run_dialog_9',
        "command": 'run_dialog',
        "args": [3047, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2067_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2067_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_10_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_10_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_10_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_10_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2067_action_queue_async_10_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2067_set_bit_11',
        "command": 'set_bit',
        "args": [0x708a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2067_set_short_12',
        "command": 'set_short',
        "args": [0x700a, 0x00e2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2067_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2067_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
