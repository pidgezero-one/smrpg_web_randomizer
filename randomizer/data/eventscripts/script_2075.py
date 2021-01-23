from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2075_run_dialog_0',
        "command": 'run_dialog',
        "args": [3335, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_2075_set_1',
        "command": 'set',
        "args": [0x70a7, 138]
    },
    {
        "identifier": 'EVENT_2075_store_7000_item_quantity_to_70A7_2',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_2075_jmp_if_7000_equals_short_3',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2075_ret_13']
    },
    {
        "identifier": 'EVENT_2075_pause_4',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2075_run_dialog_5',
        "command": 'run_dialog',
        "args": [3336, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2075_pause_6',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2075_apply_solidity_mod_7',
        "command": 'apply_solidity_mod',
        "args": [Rooms._324_MONSTRO_TOWN_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2075_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._081_STAR, 6]
    },
    {
        "identifier": 'EVENT_2075_pause_9',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2075_run_dialog_10',
        "command": 'run_dialog',
        "args": [3337, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2075_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2075_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._324_MONSTRO_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_2075_ret_13',
        "command": 'ret'
    }
]
