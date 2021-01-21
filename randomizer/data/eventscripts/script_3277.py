from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3277_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3277_ret_4']
    },
    {
        "identifier": 'EVENT_3277_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3277_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3277_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3277_ret_4',
        "command": 'ret'
    }
]
