from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2659_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 4, 'EVENT_2659_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2659_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [2644],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2659_set_bit_2',
        "command": 'set_bit',
        "args": [0x7046, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2659_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2659_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2659_run_dialog_5',
        "command": 'run_dialog',
        "args": [3155, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2659_put_inventory_6',
        "command": 'put_inventory',
        "args": [items.KerokeroCola],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2659_add_7',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2659_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
