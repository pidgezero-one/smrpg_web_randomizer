from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_427_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x001a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_427_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x0038],
        "subscript": []
    },
    {
        "identifier": 'EVENT_427_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_427_set_bit_3',
        "command": 'set_bit',
        "args": [0x7066, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_427_set_bit_4',
        "command": 'set_bit',
        "args": [0x706e, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_427_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, RadialDirections.SOUTH, 5, 20, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_427_jmp_to_event_6',
        "command": 'jmp_to_event',
        "args": [270],
        "subscript": []
    },
    {
        "identifier": 'EVENT_427_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
