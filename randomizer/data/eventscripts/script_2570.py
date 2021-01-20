from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2570_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_2570_action_queue_sync_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2570_action_queue_sync_0_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2570_action_queue_sync_0_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2570_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2570_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2570_action_queue_sync_1_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2570_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2570_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2570_action_queue_async_2_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2570_jmp_if_object_trigger_disabled_3',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_10, Rooms._405_BOOSTER_PASS_SECRET, 'EVENT_2570_jmp_if_object_trigger_disabled_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2570_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2570_jmp_if_object_trigger_disabled_5',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_11, Rooms._405_BOOSTER_PASS_SECRET, 'EVENT_2570_jmp_if_object_trigger_disabled_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2570_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2570_jmp_if_object_trigger_disabled_7',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_12, Rooms._405_BOOSTER_PASS_SECRET, 'EVENT_2570_run_background_event_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2570_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_12, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2570_run_background_event_9',
        "command": 'run_background_event',
        "args": [2571, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2570_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2570_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
