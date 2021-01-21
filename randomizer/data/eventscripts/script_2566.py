from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2566_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 0, 'EVENT_2566_ret_9']
    },
    {
        "identifier": 'EVENT_2566_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [2644]
    },
    {
        "identifier": 'EVENT_2566_set_bit_2',
        "command": 'set_bit',
        "args": [0x708d, 0]
    },
    {
        "identifier": 'EVENT_2566_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._224_FOREST_MAZE_AREA_01]
    },
    {
        "identifier": 'EVENT_2566_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._224_FOREST_MAZE_AREA_01]
    },
    {
        "identifier": 'EVENT_2566_remove_from_level_5',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._224_FOREST_MAZE_AREA_01]
    },
    {
        "identifier": 'EVENT_2566_run_dialog_6',
        "command": 'run_dialog',
        "args": [3155, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2566_put_inventory_7',
        "command": 'put_inventory',
        "args": [items.KerokeroCola]
    },
    {
        "identifier": 'EVENT_2566_add_8',
        "command": 'add',
        "args": [0x70c8, 0x01]
    },
    {
        "identifier": 'EVENT_2566_ret_9',
        "command": 'ret'
    }
]
