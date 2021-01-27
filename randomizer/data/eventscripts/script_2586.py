from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2586_set_7000_to_70A0_short_mem_0',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e2]
    },
    {
        "identifier": 'EVENT_2586_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2586_action_queue_async_1_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2586_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 7, 'EVENT_2586_run_dialog_5']
    },
    {
        "identifier": 'EVENT_2586_run_dialog_3',
        "command": 'run_dialog',
        "args": [3088, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2586_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2586_start_battle_6']
    },
    {
        "identifier": 'EVENT_2586_run_dialog_5',
        "command": 'run_dialog',
        "args": [3091, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2586_start_battle_6',
        "command": 'start_battle',
        "args": [0x0097, 10]
    },
    {
        "identifier": 'EVENT_2586_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_2586_set_temp_action_script_sync_14']
    },
    {
        "identifier": 'EVENT_2586_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_2586_stop_music_FD9F_17']
    },
    {
        "identifier": 'EVENT_2586_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2586_set_bit_10',
        "command": 'set_bit',
        "args": [0x708d, 7]
    },
    {
        "identifier": 'EVENT_2586_run_dialog_11',
        "command": 'run_dialog',
        "args": [3089, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2586_set_action_script_async_12',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 851]
    },
    {
        "identifier": 'EVENT_2586_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2586_set_temp_action_script_sync_14',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_9, 2]
    },
    {
        "identifier": 'EVENT_2586_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2586_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2586_stop_music_FD9F_17',
        "command": 'stop_music_FD9F'
    },
    {
        "identifier": 'EVENT_2586_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2586_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2586_action_queue_async_18_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2586_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x708d, 7]
    },
    {
        "identifier": 'EVENT_2586_set_7000_to_70A0_short_mem_20',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e2]
    },
    {
        "identifier": 'EVENT_2586_fade_in_from_black_async_21',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2586_run_dialog_22',
        "command": 'run_dialog',
        "args": [3090, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2586_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 851]
    },
    {
        "identifier": 'EVENT_2586_inc_24',
        "command": 'inc',
        "args": [0x70e2]
    },
    {
        "identifier": 'EVENT_2586_set_7000_to_70A0_short_mem_25',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e2]
    },
    {
        "identifier": 'EVENT_2586_jmp_if_7000_equals_short_26',
        "command": 'jmp_if_7000_equals_short',
        "args": [5, 'EVENT_2586_summon_to_level_35']
    },
    {
        "identifier": 'EVENT_2586_jmp_if_7000_equals_short_27',
        "command": 'jmp_if_7000_equals_short',
        "args": [6, 'EVENT_2586_summon_to_level_37']
    },
    {
        "identifier": 'EVENT_2586_jmp_if_7000_equals_short_28',
        "command": 'jmp_if_7000_equals_short',
        "args": [7, 'EVENT_2586_summon_to_level_39']
    },
    {
        "identifier": 'EVENT_2586_jmp_if_7000_equals_short_29',
        "command": 'jmp_if_7000_equals_short',
        "args": [8, 'EVENT_2586_summon_to_level_41']
    },
    {
        "identifier": 'EVENT_2586_jmp_if_7000_equals_short_30',
        "command": 'jmp_if_7000_equals_short',
        "args": [9, 'EVENT_2586_summon_to_level_43']
    },
    {
        "identifier": 'EVENT_2586_pause_31',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2586_set_action_script_async_32',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_2586_set_action_script_async_33',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2586_ret_34',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2586_summon_to_level_35',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP]
    },
    {
        "identifier": 'EVENT_2586_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_2586_pause_31']
    },
    {
        "identifier": 'EVENT_2586_summon_to_level_37',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP]
    },
    {
        "identifier": 'EVENT_2586_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_2586_pause_31']
    },
    {
        "identifier": 'EVENT_2586_summon_to_level_39',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP]
    },
    {
        "identifier": 'EVENT_2586_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_2586_pause_31']
    },
    {
        "identifier": 'EVENT_2586_summon_to_level_41',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP]
    },
    {
        "identifier": 'EVENT_2586_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_2586_pause_31']
    },
    {
        "identifier": 'EVENT_2586_summon_to_level_43',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP]
    },
    {
        "identifier": 'EVENT_2586_remove_from_level_44',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._405_BOOSTER_PASS_SECRET]
    },
    {
        "identifier": 'EVENT_2586_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_2586_pause_31']
    }
]
