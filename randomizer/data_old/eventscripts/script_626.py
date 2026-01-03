
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_626_set_var_to_random_111',
        "command": 'set_var_to_random',
        "args": [0x7000, 101]
    },
    {
        "identifier": 'EVENT_626_mem_compare_val_112',
        "command": 'compare_var_to_const',
        'args': [0x7000, 80]
    },
    {
        "identifier": 'EVENT_626_jmp_if_comparison_result_is_lesser_113',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_626_grant_item_1_ret']
    },
    {
        "identifier": 'EVENT_626_grant_item_1_set',
        "command": "set_var_to_const",
        "args": [0x70A7, 117]
    },
    {
        "identifier": 'EVENT_626_grant_item_1_subroutine',
        "command": 'jmp_to_event',
        "args": [160]
    },
    {
        "identifier": 'EVENT_626_grant_item_1_ret',
        "command": 'ret'
    },
]
