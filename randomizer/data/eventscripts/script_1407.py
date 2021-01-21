from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1407_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 0, 'EVENT_1407_ret_4']
    },
    {
        "identifier": 'EVENT_1407_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_1407_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._016_MARIOS_PAD, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1407_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_1407_ret_4',
        "command": 'ret'
    }
]
