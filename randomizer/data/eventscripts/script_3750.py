from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3750_set_bit_0',
        "command": 'set_bit',
        "args": [0x704a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3750_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS, RadialDirections.SOUTH, 17, 54, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3750_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [282],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3750_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
