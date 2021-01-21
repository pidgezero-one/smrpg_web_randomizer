from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1166_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 2, 'EVENT_1166_pause_3']
    },
    {
        "identifier": 'EVENT_1166_run_dialog_1',
        "command": 'run_dialog',
        "args": [2867, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1166_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1166_pause_3',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1166_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_1166_apply_solidity_mod_5',
        "command": 'apply_solidity_mod',
        "args": [Rooms._304_SEASIDE_TOWN_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1166_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1166_remove_from_level_7',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._304_SEASIDE_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_1166_pause_8',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1166_remove_one_from_inventory_9',
        "command": 'remove_one_from_inventory',
        "args": [items.ShedKey]
    },
    {
        "identifier": 'EVENT_1166_ret_10',
        "command": 'ret'
    }
]
