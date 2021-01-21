from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_618_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_618_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_618_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_618_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_618_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_618_action_queue_async_4_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_618_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 636]
    },
    {
        "identifier": 'EVENT_618_pause_6',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_618_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_618_action_queue_async_7_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_618_run_dialog_8',
        "command": 'run_dialog',
        "args": [1010, AreaObjects.NPC_5, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_618_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_618_action_queue_async_9_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_618_ret_10',
        "command": 'ret'
    }
]
