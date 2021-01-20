from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3681_start_battle_0',
        "command": 'start_battle',
        "args": [0x005c, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_set_bit_1',
        "command": 'set_bit',
        "args": [0x704a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [1011],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x704a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_set_7000_to_current_level_5',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 379, 'EVENT_3681_jmp_to_subroutine_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 380, 'EVENT_3681_jmp_to_subroutine_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": [0xa402],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._379_BEAN_VALLEY_BEANSTALKS_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_summon_to_current_level_12',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_jmp_to_subroutine_14',
        "command": 'jmp_to_subroutine',
        "args": [0xa402],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_remove_from_level_16',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_remove_from_current_level_17',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_summon_to_current_level_18',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3681_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_end_loop_11',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_start_loop_n_times_12',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_visibility_on_15',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_end_loop_17',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_start_loop_n_times_18',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_visibility_on_19',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_visibility_off_21',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3681_action_queue_async_20_SUBSCRIPT_end_loop_23',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3681_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
