from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3253_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3253_ret_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3253_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3253_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3253_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3253_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
