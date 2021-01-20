from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_499_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 0, 'EVENT_499_run_event_as_subroutine_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_499_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_499_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._055_PIPE_VAULT_ENTRANCE, RadialDirections.SOUTH, 17, 18, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_499_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [269],
        "subscript": []
    },
    {
        "identifier": 'EVENT_499_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_499_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
