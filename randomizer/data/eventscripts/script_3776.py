from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3776_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._099_ROSE_TOWN_GENO_AWAKENS_IN_INN_1F, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3776_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._099_ROSE_TOWN_GENO_AWAKENS_IN_INN_1F, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3776_fade_in_from_black_sync_duration_2',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3776_pause_3',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3776_set_bit_4',
        "command": 'set_bit',
        "args": [0x7049, 2]
    },
    {
        "identifier": 'EVENT_3776_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_3776_pause_script_until_effect_done_6',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3776_pause_7',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3776_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3776_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 142]
    },
    {
        "identifier": 'EVENT_3776_pause_10',
        "command": 'pause',
        "args": [52]
    },
    {
        "identifier": 'EVENT_3776_play_music_default_volume_11',
        "command": 'play_music_default_volume',
        "args": [Music._48_GENO_AWAKENS]
    },
    {
        "identifier": 'EVENT_3776_pause_12',
        "command": 'pause',
        "args": [17]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_13',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_pause_14',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_15_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 28, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_resume_action_script_16',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_pause_17',
        "command": 'pause',
        "args": [63]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_18',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_19_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_19_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 17, 2, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_pause_20',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3776_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 143]
    },
    {
        "identifier": 'EVENT_3776_pause_short_22',
        "command": 'pause_short',
        "args": [422]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_23',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_24_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_pause_25',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3776_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 120]
    },
    {
        "identifier": 'EVENT_3776_pause_27',
        "command": 'pause',
        "args": [121]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_28',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_bpl_26_27_28_1',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x24, 0x98, 0x00, 0x70, 0x00]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [13]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [13]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_pause_30',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3776_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 120]
    },
    {
        "identifier": 'EVENT_3776_pause_32',
        "command": 'pause',
        "args": [61]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_33',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_bpl_26_27_28_1',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0x20, 0x07, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x24, 0xc0, 0xfe, 0xa0, 0x00]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_pause_35',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3776_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 120]
    },
    {
        "identifier": 'EVENT_3776_pause_37',
        "command": 'pause',
        "args": [61]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_38',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_bpl_26_27_28_1',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x24, 0x68, 0xff, 0x90, 0xff]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [13]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_pause_40',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3776_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 120]
    },
    {
        "identifier": 'EVENT_3776_pause_42',
        "command": 'pause',
        "args": [61]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_43',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_bpl_26_27_28_1',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0x20, 0x07, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x24, 0x40, 0x01, 0x60, 0xff]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_pause_45',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3776_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 120]
    },
    {
        "identifier": 'EVENT_3776_pause_47',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_48',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_shift_z_up_pixels_11',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_shift_z_up_pixels_13',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_set_action_script_sync_50',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 120]
    },
    {
        "identifier": 'EVENT_3776_pause_51',
        "command": 'pause',
        "args": [110]
    },
    {
        "identifier": 'EVENT_3776_pause_action_script_52',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_53_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [180]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_shift_z_down_steps_11',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_54_SUBSCRIPT_dec_z_coord_1_step_13',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [428]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_on_11',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_on_15',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_off_17',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_start_loop_n_times_19',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_on_20',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_off_22',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_end_loop_24',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_start_loop_n_times_25',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_on_26',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_off_28',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_29',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_end_loop_30',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_start_loop_n_times_31',
                "command": 'start_loop_n_times',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_on_32',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_33',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_visibility_off_34',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_pause_35',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_55_SUBSCRIPT_end_loop_36',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [428]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_on_13',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_off_15',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_on_17',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_start_loop_n_times_19',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_off_20',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_on_22',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_end_loop_24',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_start_loop_n_times_25',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_off_26',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_on_28',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_29',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_end_loop_30',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_start_loop_n_times_31',
                "command": 'start_loop_n_times',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_off_32',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_33',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_visibility_on_34',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_pause_35',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_56_SUBSCRIPT_end_loop_36',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_pause_57',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_3776_db_58',
        "command": 'db',
        "args": [0xfd, 0x8f, 0x00]
    },
    {
        "identifier": 'EVENT_3776_pause_short_59',
        "command": 'pause_short',
        "args": [394]
    },
    {
        "identifier": 'EVENT_3776_fade_out_to_colour_duration_60',
        "command": 'fade_out_to_colour_duration',
        "args": [120, Colours.WHITE]
    },
    {
        "identifier": 'EVENT_3776_pause_61',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3776_remove_from_current_level_62',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_3776_remove_from_level_63',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._085_ROSE_TOWN_DURING_BOWYER_INN_1F]
    },
    {
        "identifier": 'EVENT_3776_remove_from_level_64',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._085_ROSE_TOWN_DURING_BOWYER_INN_1F]
    },
    {
        "identifier": 'EVENT_3776_pause_script_until_effect_done_65',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3776_db_66',
        "command": 'db',
        "args": [0xfd, 0x8f, 0x01]
    },
    {
        "identifier": 'EVENT_3776_pause_67',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_3776_fade_in_from_colour_duration_68',
        "command": 'fade_in_from_colour_duration',
        "args": [40, Colours.WHITE]
    },
    {
        "identifier": 'EVENT_3776_pause_script_until_effect_done_69',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3776_remember_last_object_70',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3776_pause_71',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_shift_z_up_pixels_12',
                "command": 'shift_z_up_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_shift_z_down_pixels_14',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_shift_z_down_pixels_17',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_set_animation_speed_19',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_reset_properties_22',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_72_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [90]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_walk_1_step_southwest_3',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_shift_northwest_pixels_8',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_shift_north_pixels_10',
                "command": 'shift_north_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_shift_west_pixels_12',
                "command": 'shift_west_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_shift_northwest_pixels_17',
                "command": 'shift_northwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_shift_west_pixels_19',
                "command": 'shift_west_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_shift_north_pixels_21',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_face_northwest_22',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_reset_properties_23',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_animation_speed_25',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_sprite_sequence_26',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_sprite_sequence_28',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_pause_29',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_animation_speed_30',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_set_sprite_sequence_31',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_73_SUBSCRIPT_shift_northwest_pixels_32',
                "command": 'shift_northwest_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 6]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 6]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_stop_sound_20',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3776_action_queue_sync_75_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_remember_last_object_76',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3776_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [27, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [29, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [29, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [27, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_animation_speed_19',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_shift_southwest_steps_22',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3776_action_queue_async_77_SUBSCRIPT_visibility_off_23',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3776_fade_out_to_black_sync_duration_78',
        "command": 'fade_out_to_black_sync_duration',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3776_fade_out_music_79',
        "command": 'fade_out_music'
    },
    {
        "identifier": 'EVENT_3776_pause_script_until_effect_done_80',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3776_pause_81',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3776_set_bit_82',
        "command": 'set_bit',
        "args": [0x7084, 6]
    },
    {
        "identifier": 'EVENT_3776_jmp_to_event_83',
        "command": 'jmp_to_event',
        "args": [736]
    }
]
