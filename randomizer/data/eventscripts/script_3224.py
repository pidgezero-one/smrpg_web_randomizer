from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3224_set_short_0',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_set_short_1',
        "command": 'set_short',
        "args": [0x7026, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_set_short_2',
        "command": 'set_short',
        "args": [0x7028, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_set_short_3',
        "command": 'set_short',
        "args": [0x702a, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_set_short_4',
        "command": 'set_short',
        "args": [0x702c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_set_short_5',
        "command": 'set_short',
        "args": [0x702e, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_set_6',
        "command": 'set',
        "args": [0x70ac, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 6, 'EVENT_3224_run_event_as_subroutine_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_apply_solidity_mod_8',
        "command": 'apply_solidity_mod',
        "args": [Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_apply_tile_mod_9',
        "command": 'apply_tile_mod',
        "args": [Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_set_bit_10',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_jmp_to_event_11',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_run_event_as_subroutine_12',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_run_background_event_13',
        "command": 'run_background_event',
        "args": [3225, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3224_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
