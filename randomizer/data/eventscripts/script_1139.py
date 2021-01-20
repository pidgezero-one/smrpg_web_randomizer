from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1139_run_dialog_0',
        "command": 'run_dialog',
        "args": [2843, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1139_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1139_action_queue_async_1_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_1_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_1_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_1_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_1_SUBSCRIPT_bounce_to_xy_with_height_4',
                "command": 'bounce_to_xy_with_height',
                "args": [14, 68, 0]
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_1_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1139_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1139_action_queue_async_2_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_2_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_2_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_2_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
        ]
    },
    {
        "identifier": 'EVENT_1139_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1139_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_3_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [16, 64, 0]
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_3_SUBSCRIPT_face_mario_2',
                "command": 'face_mario',
                "args": []
            },
            {
                "identifier": 'EVENT_1139_action_queue_async_3_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1139_pause_4',
        "command": 'pause',
        "args": [25],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1139_run_dialog_5',
        "command": 'run_dialog',
        "args": [2844, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1139_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1139_action_queue_async_6_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1139_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
