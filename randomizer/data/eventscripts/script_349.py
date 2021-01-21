from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_349_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_349_enter_area_3']
    },
    {
        "identifier": 'EVENT_349_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_349_enter_area_3']
    },
    {
        "identifier": 'EVENT_349_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_349_enter_area_5']
    },
    {
        "identifier": 'EVENT_349_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM, RadialDirections.NORTHEAST, 13, 35, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_349_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_349_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._029_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM_TOADSTOOL_RETURNS, RadialDirections.NORTHEAST, 13, 35, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_349_ret_6',
        "command": 'ret'
    }
]
