from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2366_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [28, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_0_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_0_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_join_party_1',
        "command": 'join_party',
        "args": [AreaObjects.GENO]
    },
    {
        "identifier": 'EVENT_2366_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_sync_3_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_sync_4_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 34]
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=4, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_5_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [7, 16]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2366_pause_7',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2366_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 766]
    },
    {
        "identifier": 'EVENT_2366_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_10_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_10_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_10_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_10_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_10_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_pause_11',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_2366_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 767]
    },
    {
        "identifier": 'EVENT_2366_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_sync_14_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_pause_15',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2366_summon_to_current_level_16',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2366_pause_17',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2366_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_sync_18_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_18_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_18_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_pause_19',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2366_screen_flashes_with_colour_20',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.RED]
    },
    {
        "identifier": 'EVENT_2366_pause_21',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_2366_screen_flashes_with_colour_22',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.YELLOW]
    },
    {
        "identifier": 'EVENT_2366_pause_23',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_2366_screen_flashes_with_colour_24',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.RED]
    },
    {
        "identifier": 'EVENT_2366_pause_25',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_2366_screen_flashes_with_colour_26',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.YELLOW]
    },
    {
        "identifier": 'EVENT_2366_pause_27',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_28',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2366_screen_flashes_with_colour_29',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.RED]
    },
    {
        "identifier": 'EVENT_2366_freeze_camera_30',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2366_pause_31',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2366_circle_mask_nonstatic_32',
        "command": 'circle_mask_nonstatic',
        "args": [AreaObjects.NPC_11, 24, 5]
    },
    {
        "identifier": 'EVENT_2366_pause_33',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_34',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_35',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_36',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_37',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_38',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_39',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_40',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_41',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_42',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_43',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2366_remove_from_current_level_44',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14]
    },
    {
        "identifier": 'EVENT_2366_pause_45',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2366_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_sync_46_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_46_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_46_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_46_SUBSCRIPT_sequence_playback_off_3',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_46_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_sync_46_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2366_action_queue_async_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2366_action_queue_async_47_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2366_set_action_script_sync_48',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 854]
    },
    {
        "identifier": 'EVENT_2366_display_intro_title_49',
        "command": 'display_intro_title',
        "args": [17, IntroTitles.GENO]
    },
    {
        "identifier": 'EVENT_2366_pause_50',
        "command": 'pause',
        "args": [150]
    },
    {
        "identifier": 'EVENT_2366_fade_out_to_black_async_duration_51',
        "command": 'fade_out_to_black_async_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2366_jmp_to_event_52',
        "command": 'jmp_to_event',
        "args": [137]
    },
    {
        "identifier": 'EVENT_2366_ret_53',
        "command": 'ret'
    }
]
