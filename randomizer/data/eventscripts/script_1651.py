from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1651_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, RadialDirections.SOUTHWEST, 30, 43, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._338_MOLEVILLE_DYNA_AND_MITES_HOUSE, RadialDirections.SOUTHWEST, 4, 41, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1651_action_queue_async_3_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_3_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_3_SUBSCRIPT_transfer_xyzf_steps_2',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 20, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_1651_circle_mask_expand_from_screen_center_4',
        "command": 'circle_mask_expand_from_screen_center',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1651_action_queue_sync_5_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1651_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 38, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1651_action_queue_sync_5_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1651_action_queue_sync_5_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1651_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1651_action_queue_async_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [2, 38, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_6_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_6_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_6_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_6_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1651_pause_script_until_effect_done_7',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1651_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_8_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_8_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_8_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1651_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 650],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_run_dialog_10',
        "command": 'run_dialog',
        "args": [1104, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 650],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_run_dialog_12',
        "command": 'run_dialog',
        "args": [1105, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1651_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_13_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_13_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_13_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1651_action_queue_async_13_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1651_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 650],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1651_run_dialog_15',
        "command": 'run_dialog',
        "args": [1106, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
]
