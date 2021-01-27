from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2574_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 2, 'EVENT_2574_ret_16']
    },
    {
        "identifier": 'EVENT_2574_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2574_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2574_action_queue_sync_1_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2574_action_queue_sync_1_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2574_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_2574_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 7]
    },
    {
        "identifier": 'EVENT_2574_set_7010_to_object_xyz_4',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2574_set_7000_to_7000_short_mem_5',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7014]
    },
    {
        "identifier": 'EVENT_2574_add_6',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_2574_set_7000_short_mem_to_7000_7',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7014]
    },
    {
        "identifier": 'EVENT_2574_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_2574_create_packet_at_7010_coords_jmp_if_null_9',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._019_FROG_COIN, 'EVENT_2574_set_bit_11']
    },
    {
        "identifier": 'EVENT_2574_add_frog_coins_10',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2574_set_bit_11',
        "command": 'set_bit',
        "args": [0x708d, 2]
    },
    {
        "identifier": 'EVENT_2574_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2574_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2574_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    },
    {
        "identifier": 'EVENT_2574_inc_15',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_2574_ret_16',
        "command": 'ret'
    }
]
