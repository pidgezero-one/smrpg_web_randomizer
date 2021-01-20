from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1896_set_bit_0',
        "command": 'set_bit',
        "args": [0x7096, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1896_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1896_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS, RadialDirections.SOUTH, 8, 35, 5, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1896_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
