from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2495_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 6, 'EVENT_2495_ret_9']
    },
    {
        "identifier": 'EVENT_2495_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [2644]
    },
    {
        "identifier": 'EVENT_2495_set_bit_2',
        "command": 'set_bit',
        "args": [0x708c, 6]
    },
    {
        "identifier": 'EVENT_2495_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE]
    },
    {
        "identifier": 'EVENT_2495_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE]
    },
    {
        "identifier": 'EVENT_2495_remove_from_level_5',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE]
    },
    {
        "identifier": 'EVENT_2495_run_dialog_6',
        "command": 'run_dialog',
        "args": [3164, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2495_put_inventory_7',
        "command": 'put_inventory',
        "args": [items.RedEssence]
    },
    {
        "identifier": 'EVENT_2495_add_8',
        "command": 'add',
        "args": [0x70c8, 0x01]
    },
    {
        "identifier": 'EVENT_2495_ret_9',
        "command": 'ret'
    }
]
