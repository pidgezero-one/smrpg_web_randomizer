from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1858_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 4, 'EVENT_1858_enter_area_3']
    },
    {
        "identifier": 'EVENT_1858_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES, RadialDirections.SOUTHWEST, 14, 86, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1858_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1858_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, RadialDirections.SOUTHWEST, 14, 86, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1858_ret_4',
        "command": 'ret'
    }
]
