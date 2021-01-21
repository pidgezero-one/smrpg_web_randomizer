from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2515_pause_0',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2515_db_1',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2515_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._158_STAR_HILL_AREA_02, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2515_apply_solidity_mod_3',
        "command": 'apply_solidity_mod',
        "args": [Rooms._158_STAR_HILL_AREA_02, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2515_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._126_EMERGE_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2515_store_00_to_0248_5',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_2515_ret_6',
        "command": 'ret'
    }
]
