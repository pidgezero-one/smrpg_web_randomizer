from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2073_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7093, 3, 'EVENT_2073_ret_14']
    },
    {
        "identifier": 'EVENT_2073_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_2073_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 7]
    },
    {
        "identifier": 'EVENT_2073_set_7010_to_object_xyz_3',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2073_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_2073_add_5',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_2073_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_2073_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_2073_create_packet_at_7010_coords_jmp_if_null_8',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._019_FROG_COIN, 'EVENT_2073_create_packet_at_7010_coords_jmp_if_null_8']
    },
    {
        "identifier": 'EVENT_2073_add_frog_coins_9',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2073_set_bit_10',
        "command": 'set_bit',
        "args": [0x7093, 3]
    },
    {
        "identifier": 'EVENT_2073_summon_to_level_11',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._267_MONSTRO_TOWN_ENTRANCE]
    },
    {
        "identifier": 'EVENT_2073_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._267_MONSTRO_TOWN_ENTRANCE]
    },
    {
        "identifier": 'EVENT_2073_add_13',
        "command": 'add',
        "args": [0x70c8, 0x01]
    },
    {
        "identifier": 'EVENT_2073_ret_14',
        "command": 'ret'
    }
]
