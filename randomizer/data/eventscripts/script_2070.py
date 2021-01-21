from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2070_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 0, 'EVENT_2070_enter_area_6']
    },
    {
        "identifier": 'EVENT_2070_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 1, 'EVENT_2070_enter_area_6']
    },
    {
        "identifier": 'EVENT_2070_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 0, 'EVENT_2070_enter_area_6']
    },
    {
        "identifier": 'EVENT_2070_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2070_action_queue_async_3_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2070_run_dialog_4',
        "command": 'run_dialog',
        "args": [2973, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2070_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2059_stop_sound_77']
    },
    {
        "identifier": 'EVENT_2070_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._324_MONSTRO_TOWN_OUTSIDE, RadialDirections.SOUTHWEST, 7, 54, 4, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2070_ret_7',
        "command": 'ret'
    }
]
