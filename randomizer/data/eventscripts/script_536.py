from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_536_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 3, 'EVENT_536_run_event_as_subroutine_15']
    },
    {
        "identifier": 'EVENT_536_set_bit_1',
        "command": 'set_bit',
        "args": [0x7061, 3]
    },
    {
        "identifier": 'EVENT_536_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_536_run_dialog_3',
        "command": 'run_dialog',
        "args": [795, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_536_jmp_if_dialog_option_b_4',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_536_pause_20']
    },
    {
        "identifier": 'EVENT_536_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_536_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x24, 0x00, 0x10]
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_mem_700C_and_const_1',
                "command": 'mem_700C_and_const',
                "args": [0x00c0]
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_jmp_if_700C_equals_short_2',
                "command": 'jmp_if_700C_equals_short',
                "args": [0, 'EVENT_536_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_6']
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_jmp_if_700C_equals_short_3',
                "command": 'jmp_if_700C_equals_short',
                "args": [64, 'EVENT_536_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_8']
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_jmp_if_700C_equals_short_4',
                "command": 'jmp_if_700C_equals_short',
                "args": [128, 'EVENT_536_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_10']
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_jmp_if_700C_equals_short_5',
                "command": 'jmp_if_700C_equals_short',
                "args": [192, 'EVENT_536_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_12']
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_536_action_queue_async_6_SUBSCRIPT_pause_13']
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_jmp_9',
                "command": 'jmp',
                "args": ['EVENT_536_action_queue_async_6_SUBSCRIPT_pause_13']
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_jmp_11',
                "command": 'jmp',
                "args": ['EVENT_536_action_queue_async_6_SUBSCRIPT_pause_13']
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_536_action_queue_async_6_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_536_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_536_run_dialog_8',
        "command": 'run_dialog',
        "args": [798, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_536_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 2, 'EVENT_529_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_536_set_bit_10',
        "command": 'set_bit',
        "args": [0x7060, 5]
    },
    {
        "identifier": 'EVENT_536_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7060, 6]
    },
    {
        "identifier": 'EVENT_536_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7060, 7]
    },
    {
        "identifier": 'EVENT_536_set_bit_13',
        "command": 'set_bit',
        "args": [0x7061, 0]
    },
    {
        "identifier": 'EVENT_536_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_536_run_event_as_subroutine_15',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_536_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 0, 'EVENT_534_jmp_if_bit_set_0']
    },
    {
        "identifier": 'EVENT_536_run_dialog_17',
        "command": 'run_dialog',
        "args": [805, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_536_jmp_if_dialog_option_b_18',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_536_pause_20']
    },
    {
        "identifier": 'EVENT_536_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_536_pause_5']
    },
    {
        "identifier": 'EVENT_536_pause_20',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_536_set_action_script_async_21',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_536_remember_last_object_22',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_536_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_536_run_dialog_24',
        "command": 'run_dialog',
        "args": [804, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_536_ret_25',
        "command": 'ret'
    }
]
