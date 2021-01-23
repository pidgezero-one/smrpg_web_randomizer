from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2052_pause_0',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2052_run_dialog_1',
        "command": 'run_dialog',
        "args": [2977, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2052_pause_2',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2052_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._045_GOOMBA_TAUNT, 6]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_3_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_run_dialog_4',
        "command": 'run_dialog',
        "args": [2978, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2052_pause_5',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2052_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_async_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_6_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_6_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_6_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_6_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_pause_7',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2052_run_dialog_8',
        "command": 'run_dialog',
        "args": [2979, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2052_pause_9',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2052_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_10_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_10_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_10_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_pause_11',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2052_run_dialog_12',
        "command": 'run_dialog',
        "args": [2980, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2052_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [14, 16, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 6]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_13_SUBSCRIPT_fixed_f_coord_off_10',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_sync_14_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [15, 18, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_15_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_pause_16',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2052_run_dialog_17',
        "command": 'run_dialog',
        "args": [2981, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2052_pause_18',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_2052_run_dialog_19',
        "command": 'run_dialog',
        "args": [2982, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2052_pause_20',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2052_run_dialog_21',
        "command": 'run_dialog',
        "args": [2986, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2052_pause_script_resume_on_next_dialog_page_a_FD61_22',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_2052_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_async_23_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_unsync_dialog_24',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2052_close_dialog_25',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_2052_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_sync_26_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2052_action_queue_async_27_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_27_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_27_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2052_action_queue_async_27_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2052_set_bit_28',
        "command": 'set_bit',
        "args": [0x7088, 7]
    },
    {
        "identifier": 'EVENT_2052_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 878]
    },
    {
        "identifier": 'EVENT_2052_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 879]
    },
    {
        "identifier": 'EVENT_2052_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 879]
    },
    {
        "identifier": 'EVENT_2052_apply_solidity_mod_32',
        "command": 'apply_solidity_mod',
        "args": [Rooms._398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2052_ret_33',
        "command": 'ret'
    }
]
