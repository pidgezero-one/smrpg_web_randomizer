from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_325_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 3, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_325_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_325_action_queue_async_1_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_325_run_dialog_2',
        "command": 'run_dialog',
        "args": [651, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_325_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_325_action_queue_async_3_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_325_action_queue_async_3_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_325_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_325_action_queue_async_4_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_325_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
