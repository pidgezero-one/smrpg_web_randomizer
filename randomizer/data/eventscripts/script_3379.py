from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3379_set_0',
        "command": 'set',
        "args": [0x70b7, 48]
    },
    {
        "identifier": 'EVENT_3379_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3379_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 40, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3379_apply_tile_mod_3',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 46, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3379_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e8]
    },
    {
        "identifier": 'EVENT_3379_mem_7000_shift_left_5',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_3379_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_3376_mem_7000_and_const_56']
    }
]
