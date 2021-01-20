from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2563_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 4, 'EVENT_2563_freeze_camera_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_set_bit_1',
        "command": 'set_bit',
        "args": [0x708c, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_set_bit_2',
        "command": 'set_bit',
        "args": [0x707f, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._049_BIG_SHELL_HIT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_freeze_camera_4',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_pause_5',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_async_6_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [26, 29]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_6_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_pause_7',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._127_LIGHT_RATTLE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_summon_to_current_level_9',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._128_FLOATING_HOVERING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2563_action_queue_sync_12_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2563_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_sync_13_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_sync_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2563_action_queue_sync_14_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_pause_15',
        "command": 'pause',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_summon_to_current_level_16',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_17_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_pause_18',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_pause_20',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_async_21_SUBSCRIPT_shift_south_steps_0',
                "command": 'shift_south_steps',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_pause_22',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_sync_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_2563_action_queue_sync_23_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_run_dialog_24',
        "command": 'run_dialog',
        "args": [3162, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_stop_embedded_action_script_25',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_set_action_script_async_26',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_unfreeze_camera_27',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_2563_ret_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_freeze_camera_29',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_sync_30_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_sync_31_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_sync_32_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [26, 30]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_overwrite_solidity_8',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_floating_off_9',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_shadow_off_11',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_db_13',
                "command": 'db',
                "args": [0x24, 0x80, 0x01, 0x80, 0x01]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_db_14',
                "command": 'db',
                "args": [0x25, 0x00, 0x0c, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [31]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_bpl_26_27_28_16',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_shadow_off_17',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=6, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_33_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [24]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_sync_34_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2563_action_queue_async_35_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_35_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_35_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x24, 0x20, 0x00, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_35_SUBSCRIPT_shift_north_steps_3',
                "command": 'shift_north_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2563_action_queue_async_35_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2563_fade_out_to_black_async_36',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_jmp_to_event_37',
        "command": 'jmp_to_event',
        "args": [3615],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2563_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
