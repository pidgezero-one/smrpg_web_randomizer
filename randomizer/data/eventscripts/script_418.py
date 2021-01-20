from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_418_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_418_set_short_1',
        "command": 'set_short',
        "args": [0x7016, 0x0005],
        "subscript": []
    },
    {
        "identifier": 'EVENT_418_set_short_2',
        "command": 'set_short',
        "args": [0x7018, 0x0036],
        "subscript": []
    },
    {
        "identifier": 'EVENT_418_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_418_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._127_PIPE_VAULT_AREA_02, RadialDirections.SOUTHWEST, 30, 18, 7, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_418_jmp_to_event_5',
        "command": 'jmp_to_event',
        "args": [270],
        "subscript": []
    }
]
