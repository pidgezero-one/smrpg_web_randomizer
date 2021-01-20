from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1581_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_1581_ret_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1581_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1581_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 4, 'EVENT_1581_db_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1581_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1581_db_4',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1581_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._068_MIDAS_RIVER_BARREL_JUMPING_RIVER, 3, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1581_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
