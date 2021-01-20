from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2356_pause_0',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_async_1',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 390],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_summon_to_current_level_2',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_3_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_pause_4',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_5_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7043, 7]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_5_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_5_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_5_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_5_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_5_SUBSCRIPT_shift_south_steps_5',
                "command": 'shift_south_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_5_SUBSCRIPT_floating_off_6',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 90, 16, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_6_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_6_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_6_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 388],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 388],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_9',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_bit_10',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_11',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_async_12',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 390],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_summon_to_current_level_13',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_14_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_pause_15',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7044, 0]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_shift_west_steps_6',
                "command": 'shift_west_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_16_SUBSCRIPT_floating_off_8',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_17_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 82, 16, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_17_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_17_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_17_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_17_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 388],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 388],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_20',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_bit_21',
        "command": 'set_bit',
        "args": [0x7044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_22',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 390],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_summon_to_current_level_24',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_25_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_pause_26',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7044, 1]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_shift_south_steps_6',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_27_SUBSCRIPT_floating_off_8',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_28_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 85, 18, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_28_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_28_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_28_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 388],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 388],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_31',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_bit_32',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_short_33',
        "command": 'pause_short',
        "args": [592],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_enable_controls_34',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_disable_trigger_35',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_disable_trigger_36',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_disable_trigger_37',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_disable_trigger_38',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_jmp_if_present_in_current_level_39',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_0, 'EVENT_2356_jmp_if_present_in_current_level_46'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_sync_40_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 83]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_40_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_40_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._060_DYNAMITE_BOMB_EXPLOSION, 4]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_40_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_pause_action_script_41',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_async_42',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 192],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_43',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_current_level_44',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_45',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_jmp_if_present_in_current_level_46',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_2356_jmp_if_present_in_current_level_53'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_sync_47_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [14, 90]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_47_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_47_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._060_DYNAMITE_BOMB_EXPLOSION, 4]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_47_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_pause_action_script_48',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_async_49',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 192],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_50',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_current_level_51',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_52',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_jmp_if_present_in_current_level_53',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_3, 'EVENT_2356_jmp_if_present_in_current_level_60'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_sync_54_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 82]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_54_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_54_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._060_DYNAMITE_BOMB_EXPLOSION, 4]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_54_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_54_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_54_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_pause_action_script_55',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_async_56',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 192],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_57',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_current_level_58',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_59',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_jmp_if_present_in_current_level_60',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_2, 'EVENT_2356_remove_from_current_level_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_sync_61_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 85]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_61_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_61_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._060_DYNAMITE_BOMB_EXPLOSION, 4]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_61_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_pause_action_script_62',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_set_action_script_async_63',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_2, 192],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_64',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_current_level_65',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_66_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [10, 60]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_run_dialog_67',
        "command": 'run_dialog',
        "args": [3081, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_68_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_pause_script_resume_on_next_dialog_page_a_69',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_70_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_unsync_dialog_71',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_72_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2356_action_queue_async_72_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_play_sound_73',
        "command": 'play_sound',
        "args": [Sounds._076_BOOSTERS_TRAIN_HORN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_74',
        "command": 'pause',
        "args": [72],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_sync_75_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._074_BOOSTERS_TRAIN, 6]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_75_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_75_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_75_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_75_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_75_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_75_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_sync_76_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2356_action_queue_sync_76_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_run_dialog_77',
        "command": 'run_dialog',
        "args": [3086, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_stop_embedded_action_script_78',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_pause_79',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_play_sound_80',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2356_action_queue_async_81_SUBSCRIPT_shift_south_steps_0',
                "command": 'shift_south_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2356_set_bit_82',
        "command": 'set_bit',
        "args": [0x708b, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_83',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_84',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_85',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_86',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_87',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_88',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_89',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_remove_from_level_90',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_enable_controls_91',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2356_ret_92',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
