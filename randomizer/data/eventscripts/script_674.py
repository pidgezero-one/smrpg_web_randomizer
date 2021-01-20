from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_674_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_674_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_674_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_674_apply_tile_mod_3',
        "command": 'apply_tile_mod',
        "args": [Rooms._064_MARRYMORE_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_674_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
