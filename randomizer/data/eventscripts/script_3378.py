from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3378_set_0',
        "command": 'set',
        "args": [0x70b7, 32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3378_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3378_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 39, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3378_apply_tile_mod_3',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 45, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3378_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3378_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3376_mem_7000_and_const_56'],
        "subscript": []
    }
]
