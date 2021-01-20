from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2358_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2358_clear_bit_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2358_set_7000_to_object_coord_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2358_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_set_7000_to_object_coord_5',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 18, 'EVENT_2358_set_7000_to_object_coord_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_set_7000_to_object_coord_9',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 121, 'EVENT_2358_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2358_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
