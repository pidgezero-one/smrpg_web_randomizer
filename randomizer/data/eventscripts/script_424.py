from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_424_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_424_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x0064],
        "subscript": []
    },
    {
        "identifier": 'EVENT_424_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_424_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._129_PIPE_VAULT_AREA_05, RadialDirections.SOUTHWEST, 25, 100, 1, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_424_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [269],
        "subscript": []
    }
]
