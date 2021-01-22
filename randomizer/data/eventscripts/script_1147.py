from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1147_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_sync_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_11',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_shift_northwest_steps_12',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_face_northwest_14',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_15',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_shift_southwest_steps_16',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_start_loop_n_times_18',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_face_southwest_19',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_20',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_shift_southeast_steps_21',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_22',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_face_southeast_23',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_24',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_shift_northeast_steps_25',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_26',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_face_northeast_27',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_28',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_shift_northwest_steps_29',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_30',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_face_northwest_31',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_32',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_shift_southwest_steps_33',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_end_loop_34',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_set_animation_speed_35',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_bounce_to_xy_with_height_36',
                "command": 'bounce_to_xy_with_height',
                "args": [6, 26, 0]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_1_SUBSCRIPT_visibility_off_37',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_11',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_shift_southwest_steps_12',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_face_southwest_14',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_15',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_shift_southeast_steps_16',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_start_loop_n_times_18',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_face_southeast_19',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_20',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_shift_northeast_steps_21',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_off_22',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_face_northeast_23',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_24',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_shift_northwest_steps_25',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_off_26',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_face_northwest_27',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_28',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_shift_southwest_steps_29',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_off_30',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_face_southwest_31',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_32',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_shift_southeast_steps_33',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_end_loop_34',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_set_animation_speed_35',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_bounce_to_xy_with_height_36',
                "command": 'bounce_to_xy_with_height',
                "args": [6, 26, 0]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_2_SUBSCRIPT_visibility_off_37',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_11',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_12',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_face_northeast_14',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_15',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_shift_northwest_steps_16',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_start_loop_n_times_18',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_face_northwest_19',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_20',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_shift_southwest_steps_21',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_off_22',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_face_southwest_23',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_24',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_shift_southeast_steps_25',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_off_26',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_face_southeast_27',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_28',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_29',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_off_30',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_face_northeast_31',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_32',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_shift_northwest_steps_33',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_end_loop_34',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_set_animation_speed_35',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_bounce_to_xy_with_height_36',
                "command": 'bounce_to_xy_with_height',
                "args": [6, 26, 0]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_3_SUBSCRIPT_visibility_off_37',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_face_southwest_10',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_11',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_shift_southeast_steps_12',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_face_southeast_14',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_15',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_shift_northeast_steps_16',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._089_LIT_FUSE, 6]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_start_loop_n_times_19',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_face_northeast_20',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_21',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_shift_northwest_steps_22',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_23',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_face_northwest_24',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_25',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_26',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_27',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_face_southwest_28',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_29',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_shift_southeast_steps_30',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_31',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_face_southeast_32',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_33',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_shift_northeast_steps_34',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_end_loop_35',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_set_animation_speed_36',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_bounce_to_xy_with_height_37',
                "command": 'bounce_to_xy_with_height',
                "args": [6, 26, 0]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_4_SUBSCRIPT_visibility_off_38',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._148_SURGING_ELECTRICITY, 6]
    },
    {
        "identifier": 'EVENT_1147_fade_out_music_to_volume_6',
        "command": 'fade_out_music_to_volume',
        "args": [8, 0]
    },
    {
        "identifier": 'EVENT_1147_palette_set_morphs_7',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.NOTHING, 2, 214, 11]
    },
    {
        "identifier": 'EVENT_1147_pause_8',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_9',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_pause_10',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_11',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_pause_12',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_13',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_15',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_pause_16',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_17',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_async_18_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_18_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_18_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 527]
    },
    {
        "identifier": 'EVENT_1147_pause_20',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_21',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_pause_22',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_23',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 527]
    },
    {
        "identifier": 'EVENT_1147_pause_25',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1147_start_loop_n_times_26',
        "command": 'start_loop_n_times',
        "args": [6]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_27',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_pause_28',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1147_end_loop_29',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1147_remove_from_current_level_30',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_1147_pause_action_script_31',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1147_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_async_32_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_32_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_32_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._091_TUMBLING_BOULDERS, 6]
    },
    {
        "identifier": 'EVENT_1147_pause_34',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_35',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_pause_36',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1147_screen_flashes_with_colour_37',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE]
    },
    {
        "identifier": 'EVENT_1147_pause_38',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1147_start_battle_39',
        "command": 'start_battle',
        "args": [0x00b4, 37]
    },
    {
        "identifier": 'EVENT_1147_jmp_if_bit_clear_40',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_1147_play_music_default_volume_42']
    },
    {
        "identifier": 'EVENT_1147_reset_and_choose_game_41',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1147_play_music_default_volume_42',
        "command": 'play_music_default_volume',
        "args": [Music._05_SEASIDE_TOWN]
    },
    {
        "identifier": 'EVENT_1147_enter_area_43',
        "command": 'enter_area',
        "args": [Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, RadialDirections.NORTHWEST, 8, 30, 0, []]
    },
    {
        "identifier": 'EVENT_1147_set_bit_44',
        "command": 'set_bit',
        "args": [0x7086, 0]
    },
    {
        "identifier": 'EVENT_1147_remove_from_level_45',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP]
    },
    {
        "identifier": 'EVENT_1147_remove_from_level_46',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP]
    },
    {
        "identifier": 'EVENT_1147_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_sync_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_47_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [0, 8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_sync_48_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [4, 22]
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_jmp_to_subroutine_49',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1163_action_queue_sync_0']
    },
    {
        "identifier": 'EVENT_1147_jmp_50',
        "command": 'jmp',
        "args": ['EVENT_1147_pause_script_until_effect_done_61']
    },
    {
        "identifier": 'EVENT_1147_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_async_51_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [4, 20]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_51_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_51_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_51_SUBSCRIPT_shift_north_steps_3',
                "command": 'shift_north_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_51_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_pause_52',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_1147_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_sync_53_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_1147_action_queue_sync_53_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_action_queue_async_54',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_async_54_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_pause_55',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1147_db_56',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_1147_pause_script_until_effect_done_57',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_1147_pause_58',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1147_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_turn_clockwise_45_degrees_n_times_2',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 6]
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_face_south_9',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_fixed_f_coord_on_10',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1147_action_queue_async_59_SUBSCRIPT_sequence_playback_off_11',
                "command": 'sequence_playback_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1147_db_60',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_1147_pause_script_until_effect_done_61',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_1147_set_action_script_sync_62',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1147_restore_all_hp_63',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_1147_restore_all_fp_64',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_1147_set_short_65',
        "command": 'set_short',
        "args": [0x700a, 0x00d6]
    },
    {
        "identifier": 'EVENT_1147_jmp_to_event_66',
        "command": 'jmp_to_event',
        "args": [720]
    },
    {
        "identifier": 'EVENT_1147_ret_67',
        "command": 'ret'
    }
]
