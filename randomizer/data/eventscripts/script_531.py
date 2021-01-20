from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_531_close_dialog_0',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_531_db_1',
        "command": 'db',
        "args": [0xfd, 0x47],
        "subscript": []
    },
    {
        "identifier": 'EVENT_531_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_531_action_queue_async_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_531_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_531_run_event_as_subroutine_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_531_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_531_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_531_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [265],
        "subscript": []
    },
    {
        "identifier": 'EVENT_531_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
