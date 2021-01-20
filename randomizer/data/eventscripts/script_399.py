from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_399_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 7, 'EVENT_399_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 3, 'EVENT_399_run_dialog_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_jmp_if_object_trigger_disabled_2',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT, 'EVENT_399_run_dialog_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_jmp_if_object_trigger_disabled_3',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT, 'EVENT_399_run_dialog_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_jmp_if_object_trigger_disabled_4',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_2, Rooms._331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT, 'EVENT_399_run_dialog_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_run_dialog_5',
        "command": 'run_dialog',
        "args": [650, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_run_dialog_7',
        "command": 'run_dialog',
        "args": [689, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_run_dialog_9',
        "command": 'run_dialog',
        "args": [3756, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_run_dialog_11',
        "command": 'run_dialog',
        "args": [3749, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_run_dialog_12',
        "command": 'run_dialog',
        "args": [3750, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_pause_13',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_399_action_queue_async_14_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_399_action_queue_async_14_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_399_action_queue_async_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_399_action_queue_async_14_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_399_set_bit_15',
        "command": 'set_bit',
        "args": [0x7099, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_399_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
