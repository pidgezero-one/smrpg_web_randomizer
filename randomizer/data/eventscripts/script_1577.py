from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1577_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1577_ret_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1577_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1577_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1577_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 4, 'EVENT_1577_db_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1577_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1577_db_5',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1577_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._068_MIDAS_RIVER_BARREL_JUMPING_RIVER, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1577_set_bit_7',
        "command": 'set_bit',
        "args": [0x7078, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1577_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
