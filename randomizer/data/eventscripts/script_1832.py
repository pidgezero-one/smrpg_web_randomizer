from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1832_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1832_pause_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1832_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_set_7000_to_pressed_button_4',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_jmp_if_7000_any_bits_set_5',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 1, 2, 3], 'EVENT_1832_pause_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1832_pause_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1832_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_priority_set_9',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.LAYER_3], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.HALF_INTENSITY]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_pause_10',
        "command": 'pause',
        "args": [6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_priority_set_11',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.HALF_INTENSITY]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_1832_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_pause_13',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_jmp_if_mario_in_air_14',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1832_pause_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1832_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_1832_pause_0'],
        "subscript": []
    },
]
