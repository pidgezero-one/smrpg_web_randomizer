from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1680_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x144a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1680_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1680_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, RadialDirections.SOUTH, 4, 83, 9, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1680_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x704f, 2, 'EVENT_1680_action_queue_sync_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1680_set_bit_4',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1680_enable_controls_5',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1680_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1680_action_queue_sync_6_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1680_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [1770],
        "subscript": []
    }
]
