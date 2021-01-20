from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3693_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7042, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7042, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7042, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7042, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7042, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_3693_enter_area_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, RadialDirections.SOUTHWEST, 4, 48, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_enter_area_8',
        "command": 'enter_area',
        "args": [Rooms._438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, RadialDirections.SOUTHWEST, 4, 48, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3693_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
