from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1739_set_7016_to_object_xyz_0',
        "command": 'set_7016_to_object_xyz',
        "args": [0x93]
    },
    {
        "identifier": 'EVENT_1739_add_short_1',
        "command": 'add_short',
        "args": [0x7016, 0xfffc]
    },
    {
        "identifier": 'EVENT_1739_mem_compare_2',
        "command": 'mem_compare',
        "args": [0x7016, 32768]
    },
    {
        "identifier": 'EVENT_1739_jmp_if_comparison_result_is_lesser_3',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1739_add_short_5']
    },
    {
        "identifier": 'EVENT_1739_set_short_4',
        "command": 'set_short',
        "args": [0x7016, 0x0000]
    },
    {
        "identifier": 'EVENT_1739_add_short_5',
        "command": 'add_short',
        "args": [0x7018, 0xfff0]
    },
    {
        "identifier": 'EVENT_1739_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x701a]
    },
    {
        "identifier": 'EVENT_1739_mem_7000_xor_const_7',
        "command": 'mem_7000_xor_const',
        "args": [0xffff]
    },
    {
        "identifier": 'EVENT_1739_inc_8',
        "command": 'inc',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1739_add_short_mem_9',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7018]
    },
    {
        "identifier": 'EVENT_1739_mem_compare_val_10',
        "command": 'mem_compare_val',
        "args": [32768]
    },
    {
        "identifier": 'EVENT_1739_jmp_if_comparison_result_is_lesser_11',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1739_set_short_mem_13']
    },
    {
        "identifier": 'EVENT_1739_set_12',
        "command": 'set',
        "args": [0x7000, 0]
    },
    {
        "identifier": 'EVENT_1739_set_short_mem_13',
        "command": 'set_short_mem',
        "args": [0x7018, 0x7000]
    },
    {
        "identifier": 'EVENT_1739_set_short_14',
        "command": 'set_short',
        "args": [0x701a, 0x0000]
    },
    {
        "identifier": 'EVENT_1739_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_jmp_if_bit_set_0',
                "command": 'jmp_if_bit_set',
                "args": [0x7094, 4, 'EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_4']
            },
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_jmp_if_bit_set_1',
                "command": 'jmp_if_bit_set',
                "args": [0x7094, 5, 'EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_6']
            },
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_jmp_3',
                "command": 'jmp',
                "args": ['EVENT_1739_action_queue_async_15_SUBSCRIPT_db_7']
            },
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_jmp_5',
                "command": 'jmp',
                "args": ['EVENT_1739_action_queue_async_15_SUBSCRIPT_db_7']
            },
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x98]
            },
            {
                "identifier": 'EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1739_ret_16',
        "command": 'ret'
    }
]
