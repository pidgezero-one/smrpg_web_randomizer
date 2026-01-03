
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2059_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 0, 'EVENT_2059_run_dialog_84']
    },
    {
        "identifier": 'EVENT_2059_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 1, 'EVENT_2059_jmp_if_bit_set_11']
    },
    {
        "identifier": 'EVENT_2059_run_dialog_2',
        "command": 'run_dialog',
        "args": [2976, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_bounce_to_xy_with_height_4',
                "command": 'bounce_to_xy_with_height',
                "args": [15, 78, 0]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._081_STAR, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_3_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_4_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_6',
        "command": 'run_dialog',
        "args": [2975, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2059_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 0, 'EVENT_2059_action_queue_sync_15']
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_8_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_set_bit_9',
        "command": 'set_bit',
        "args": [0x7089, 1]
    },
    {
        "identifier": 'EVENT_2059_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2059_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 0, 'EVENT_2059_run_dialog_14']
    },
    {
        "identifier": 'EVENT_2059_run_dialog_12',
        "command": 'run_dialog',
        "args": [2974, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2059_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2059_run_dialog_14',
        "command": 'run_dialog',
        "args": [2973, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_bounce_to_xy_with_height_4',
                "command": 'bounce_to_xy_with_height',
                "args": [15, 78, 0]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._081_STAR, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._027_FOUND_AN_ITEM, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [30, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_reset_properties_18',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_15_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_16_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_16_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_16_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_set_action_script_async_17',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_18',
        "command": 'run_dialog',
        "args": [2972, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._030_SURPRISED_MONSTER, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_jump_to_height_silent_8',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_19_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_set_action_script_async_20',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_21',
        "command": 'run_dialog',
        "args": [2971, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_22_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_22_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_23',
        "command": 'run_dialog',
        "args": [2988, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_24_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_24_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_pause_25',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2059_fade_out_sound_to_volume_26',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_2059_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._122_SKY_TROOPAS_APPROACHING, 6]
    },
    {
        "identifier": 'EVENT_2059_fade_out_sound_to_volume_28',
        "command": 'fade_out_sound_to_volume',
        "args": [5, 100]
    },
    {
        "identifier": 'EVENT_2059_pause_29',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2059_pause_30',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2059_pause_31',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2059_pause_32',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2059_pause_33',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2059_play_sound_34',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_2059_pause_35',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2059_play_sound_36',
        "command": 'play_sound',
        "args": [Sounds._123_CHAIN_RUMBLING_NOISE, 6]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [13, 83, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_8',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_2, 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_shift_northeast_steps_11',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_shift_northeast_pixels_13',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_shift_northeast_pixels_16',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_sequence_looping_on_17',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_37_SUBSCRIPT_set_bit_18',
                "command": 'set_bit',
                "args": [0x7043, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [13, 83, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_8',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_3, 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_shift_northeast_steps_11',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_shift_northeast_pixels_13',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_shift_northeast_pixels_16',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_sequence_looping_on_17',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_38_SUBSCRIPT_set_bit_18',
                "command": 'set_bit',
                "args": [0x7043, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [14, 84, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_8',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_4, 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_shift_northeast_steps_11',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_shift_northeast_pixels_13',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_shift_northeast_pixels_16',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_sequence_looping_on_17',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_39_SUBSCRIPT_set_bit_18',
                "command": 'set_bit',
                "args": [0x7043, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_40_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_40_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_41_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_41_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_fade_out_sound_to_volume_42',
        "command": 'fade_out_sound_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_2059_pause_43',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_44',
        "command": 'run_dialog',
        "args": [3016, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_45',
        "command": 'run_dialog',
        "args": [3017, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_pause_46',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._134_SWIPE, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._134_SWIPE, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._134_SWIPE, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._134_SWIPE, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_shift_southeast_steps_12',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_47_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_48_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._133_CLOSE_HIT_DOOR, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_49_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_50',
        "command": 'run_dialog',
        "args": [3018, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_51',
        "command": 'run_dialog',
        "args": [3019, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_pause_52',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_53_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_pause_54',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_55',
        "command": 'run_dialog',
        "args": [3020, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_pause_56',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_57',
        "command": 'run_dialog',
        "args": [3021, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_pause_58',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_59_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_59_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_59_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_59_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_60',
        "command": 'run_dialog',
        "args": [3022, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_61_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_61_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_61_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_pause_62',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_63',
        "command": 'run_dialog',
        "args": [3023, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_play_sound_64',
        "command": 'play_sound',
        "args": [Sounds._124_ENGINE_STARTING, 6]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_65',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_65_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_66_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_67_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_68',
        "command": 'run_dialog',
        "args": [3024, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_set_69',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'EVENT_2059_clear_bit_70',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2059_play_sound_71',
        "command": 'play_sound',
        "args": [Sounds._123_CHAIN_RUMBLING_NOISE, 6]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_clear_bit_3',
                "command": 'clear_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_5',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_2, 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_72_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_4',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_3, 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_sync_73_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_4',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.NPC_4, 'EVENT_2059_action_queue_async_74_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._016_OPEN_DOOR, 6]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2059_action_queue_async_74_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_set_bit_75',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2059_pause_76',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_2059_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_sync_77_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_78_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_run_dialog_79',
        "command": 'run_dialog',
        "args": [3025, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2059_action_queue_async_80',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2059_action_queue_async_80_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2059_set_bit_81',
        "command": 'set_bit',
        "args": [0x708a, 0]
    },
    {
        "identifier": 'EVENT_2059_set_bit_82',
        "command": 'set_bit',
        "args": [0x7068, 0]
    },
    {
        "identifier": 'EVENT_2059_ret_83',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2059_run_dialog_84',
        "command": 'run_dialog',
        "args": [3026, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2059_ret_85',
        "command": 'ret'
    }
]
