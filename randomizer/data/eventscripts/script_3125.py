from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3125_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x0008]
    },
    {
        "identifier": 'EVENT_3125_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x0064]
    },
    {
        "identifier": 'EVENT_3125_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66]
    },
    {
        "identifier": 'EVENT_3125_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS, RadialDirections.SOUTH, 29, 35, 10, []]
    },
    {
        "identifier": 'EVENT_3125_set_bit_4',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_3125_enable_controls_5',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3125_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3125_action_queue_sync_6_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3125_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [1590]
    }
]
