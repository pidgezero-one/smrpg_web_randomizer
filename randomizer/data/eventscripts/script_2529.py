from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2529_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._110_ABSTRACT_MUSIC, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_run_dialog_1',
        "command": 'run_dialog',
        "args": [3115, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 7, 'EVENT_2529_ret_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_set_bit_4',
        "command": 'set_bit',
        "args": [0x708b, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_summon_to_current_level_at_marios_coords_5',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2529_action_queue_async_6_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_6_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_6_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_6_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2529_freeze_camera_7',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_pause_8',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2529_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_9_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_9_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_9_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_9_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2529_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2529_action_queue_sync_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_10_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_10_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_10_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_10_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_2529_action_queue_sync_10_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2529_run_dialog_11',
        "command": 'run_dialog',
        "args": [3120, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_stop_embedded_action_script_12',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_pause_13',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2529_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2529_run_dialog_16',
        "command": 'run_dialog',
        "args": [3121, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_pause_script_resume_on_next_dialog_page_a_17',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2529_action_queue_sync_18_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2529_unsync_dialog_19',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_walk_1_step_southwest_3',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_set_priority_6',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_set_priority_8',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_walk_1_step_northeast_9',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_20_SUBSCRIPT_face_southwest_11',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2529_run_dialog_21',
        "command": 'run_dialog',
        "args": [3122, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2529_action_queue_async_22_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_22_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2529_action_queue_async_22_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2529_remove_from_current_level_23',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_unfreeze_camera_24',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2529_ret_25',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
