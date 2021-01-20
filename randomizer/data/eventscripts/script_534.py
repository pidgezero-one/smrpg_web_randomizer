from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_534_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 2, 'EVENT_534_ret_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_534_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 2, 'EVENT_534_play_sound_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_534_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_534_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_534_add_frog_coins_4',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_534_set_bit_5',
        "command": 'set_bit',
        "args": [0x705d, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_534_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_534_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_534_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
