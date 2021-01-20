from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3261_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3261_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3261_set_bit_7_offset_1',
        "command": 'set_bit_7_offset',
        "args": [0x0258],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3261_set_bit_7_offset_2',
        "command": 'set_bit_7_offset',
        "args": [0x025a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3261_apply_tile_mod_3',
        "command": 'apply_tile_mod',
        "args": [Rooms._176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3261_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3261_set_bit_5',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3261_clear_bit_7_offset_6',
        "command": 'clear_bit_7_offset',
        "args": [0x0258],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3261_clear_bit_7_offset_7',
        "command": 'clear_bit_7_offset',
        "args": [0x025a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3261_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
