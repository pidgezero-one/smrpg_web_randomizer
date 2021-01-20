from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3645_set_bit_0',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3645_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE, RadialDirections.SOUTH, 24, 18, 2, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3645_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [282],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3645_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
