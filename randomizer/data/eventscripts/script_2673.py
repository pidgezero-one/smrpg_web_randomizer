from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2673_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_2673_ret_6']
    },
    {
        "identifier": 'EVENT_2673_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_2673_ret_6']
    },
    {
        "identifier": 'EVENT_2673_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_2673_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_2673_jmp_5']
    },
    {
        "identifier": 'EVENT_2673_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_78']
    },
    {
        "identifier": 'EVENT_2673_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_68']
    },
    {
        "identifier": 'EVENT_2673_ret_6',
        "command": 'ret'
    }
]
