from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2306_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 2, 'EVENT_2306_ret_15']
    },
    {
        "identifier": 'EVENT_2306_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2306_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2306_action_queue_sync_1_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2306_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2306_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 7]
    },
    {
        "identifier": 'EVENT_2306_set_bit_4',
        "command": 'set_bit',
        "args": [0x7059, 2]
    },
    {
        "identifier": 'EVENT_2306_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2306_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._100_BOOSTER_PASS_AREA_01]
    },
    {
        "identifier": 'EVENT_2306_inc_7',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_2306_set_7010_to_object_xyz_8',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2306_set_7000_to_7000_short_mem_9',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7014]
    },
    {
        "identifier": 'EVENT_2306_add_10',
        "command": 'add',
        "args": [0x7000, 512]
    },
    {
        "identifier": 'EVENT_2306_set_7000_short_mem_to_7000_11',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7014]
    },
    {
        "identifier": 'EVENT_2306_create_packet_at_7010_coords_jmp_if_null_12',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 'EVENT_2306_ret_15']
    },
    {
        "identifier": 'EVENT_2306_set_13',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_2306_add_max_FP_7000_14',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_2306_ret_15',
        "command": 'ret'
    }
]
