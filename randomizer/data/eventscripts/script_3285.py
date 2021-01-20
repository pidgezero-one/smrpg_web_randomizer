from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3285_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 6, 'EVENT_3285_jmp_if_bit_clear_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_set_bit_1',
        "command": 'set_bit',
        "args": [0x7055, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._131_SEA_AREA_04_BUNCH_OF_ZEOSTARS, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_3285_jmp_to_event_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_set_7000_to_current_level_4',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 133, 'EVENT_3285_set_short_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_set_short_6',
        "command": 'set_short',
        "args": [0x7022, 0x0005],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_3285_jmp_to_event_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_set_short_8',
        "command": 'set_short',
        "args": [0x7022, 0x0028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3285_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
]
