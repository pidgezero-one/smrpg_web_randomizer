from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2660_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 3, 'EVENT_2660_ret_14']
    },
    {
        "identifier": 'EVENT_2660_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2660_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 7]
    },
    {
        "identifier": 'EVENT_2660_set_bit_3',
        "command": 'set_bit',
        "args": [0x7046, 3]
    },
    {
        "identifier": 'EVENT_2660_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    },
    {
        "identifier": 'EVENT_2660_remove_from_level_5',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    },
    {
        "identifier": 'EVENT_2660_inc_6',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_2660_set_7010_to_object_xyz_7',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2660_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_2660_add_9',
        "command": 'add',
        "args": [0x7000, 512]
    },
    {
        "identifier": 'EVENT_2660_set_short_mem_10',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_2660_create_packet_at_7010_coords_jmp_if_null_11',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 'EVENT_2660_ret_14']
    },
    {
        "identifier": 'EVENT_2660_set_12',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_2660_add_max_FP_7000_13',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_2660_ret_14',
        "command": 'ret'
    }
]
