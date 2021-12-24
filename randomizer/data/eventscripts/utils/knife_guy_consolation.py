from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [

    {
        "identifier": 'EVENT_2672_set_random_93',
        "command": 'set_random',
        "args": [0x7000, 21]
    },
    {
        "identifier": 'EVENT_2672_mem_compare_val_94',
        "command": 'mem_compare_val',
        "args": [3]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_comparison_result_is_lesser_95',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2672_jmp_if_bit_set_96']
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set__96',
        "command": 'jmp_to_event',
        "args": [5]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_96',
        "command": 'jmp_to_event',
        "args": [7]
    },
]
