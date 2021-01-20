from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3237_jmp_to_subroutine_0',
        "command": 'jmp_to_subroutine',
        "args": [0x3171],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_add_short_1',
        "command": 'add_short',
        "args": [0x702e, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 5, 'EVENT_3232_jmp_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_set_short_3',
        "command": 'set_short',
        "args": [0x702e, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_3237_clear_bit_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3237_end_all_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_set_temp_action_script_sync_7',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 337],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3237_end_all_11',
        "command": 'end_all',
        "args": [],
        "subscript": []
    }
]
