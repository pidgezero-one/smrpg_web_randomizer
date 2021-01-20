from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_295_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_295_enter_area_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_295_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_295_enter_area_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_295_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, RadialDirections.SOUTHWEST, 12, 82, 9, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_295_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_295_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._191_MUSHROOM_KINGDOM_OUTSIDE, RadialDirections.SOUTHWEST, 12, 82, 9, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_295_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]