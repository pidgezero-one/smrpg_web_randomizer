from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1894_pause_0',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_1894_start_battle_1',
        "command": 'start_battle',
        "args": [0x00b8, 40]
    },
    {
        "identifier": 'EVENT_1894_stop_sound_2',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1894_set_bit_3',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_1894_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_1894_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_1894_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_1894_apply_solidity_mod_7',
        "command": 'apply_solidity_mod',
        "args": [Rooms._103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1894_apply_tile_mod_8',
        "command": 'apply_tile_mod',
        "args": [Rooms._103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1894_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1894_restore_all_hp_10',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_1894_restore_all_fp_11',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_1894_set_bit_12',
        "command": 'set_bit',
        "args": [0x7096, 0]
    },
    {
        "identifier": 'EVENT_1894_ret_13',
        "command": 'ret'
    }
]
