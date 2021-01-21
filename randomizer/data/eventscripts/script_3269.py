from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3269_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3269_ret_6']
    },
    {
        "identifier": 'EVENT_3269_store_02_to_0248_1',
        "command": 'store_02_to_0248'
    },
    {
        "identifier": 'EVENT_3269_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3269_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3269_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3269_store_00_to_0248_5',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_3269_ret_6',
        "command": 'ret'
    }
]
