from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2600_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708f, 4, 'EVENT_2600_ret_15']
    },
    {
        "identifier": 'EVENT_2600_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_2600_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7]
    },
    {
        "identifier": 'EVENT_2600_set_7010_to_object_xyz_3',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2600_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2600_create_packet_at_7010_coords_jmp_if_null_5',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._001_MUSHROOM, 'EVENT_2600_ret_15']
    },
    {
        "identifier": 'EVENT_2600_restore_all_hp_6',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2600_restore_all_fp_7',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2600_set_short_8',
        "command": 'set_short',
        "args": [0x7020, 0x0008]
    },
    {
        "identifier": 'EVENT_2600_run_background_event_with_pause_9',
        "command": 'run_background_event_with_pause',
        "args": [3075, 0x7020, [12, 13]]
    },
    {
        "identifier": 'EVENT_2600_set_bit_10',
        "command": 'set_bit',
        "args": [0x708f, 4]
    },
    {
        "identifier": 'EVENT_2600_inc_11',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_2600_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._237_SMITHY_FACTORY_AREA_05_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2600_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._237_SMITHY_FACTORY_AREA_05_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2600_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._237_SMITHY_FACTORY_AREA_05_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2600_ret_15',
        "command": 'ret'
    }
]
