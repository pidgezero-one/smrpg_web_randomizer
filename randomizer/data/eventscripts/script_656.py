from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_656_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_656_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_656_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_656_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_656_action_queue_async_3_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_656_run_dialog_4',
        "command": 'run_dialog',
        "args": [2538, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_656_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_656_action_queue_async_5_SUBSCRIPT_walk_1_step_south_0',
                "command": 'walk_1_step_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_656_ret_6',
        "command": 'ret'
    }
]
