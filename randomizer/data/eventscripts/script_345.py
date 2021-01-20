from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_345_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_345_run_dialog_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 4, 'EVENT_345_run_dialog_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_run_dialog_2',
        "command": 'run_dialog',
        "args": [715, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_run_dialog_4',
        "command": 'run_dialog',
        "args": [718, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_jmp_if_dialog_option_b_5',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_345_pause_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_pause_6',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [3587],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_remember_last_object_9',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_pause_10',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_run_dialog_11',
        "command": 'run_dialog',
        "args": [719, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_pause_12',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x24, 0x00, 0x10]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_mem_700C_and_const_1',
                "command": 'mem_700C_and_const',
                "args": [0x00c0]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_jmp_if_var_equals_short_2',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_12']
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 64, 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_6']
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 128, 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_6']
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 192, 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_12']
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_jmp_11',
                "command": 'jmp',
                "args": ['EVENT_345_action_queue_async_13_SUBSCRIPT_pause_17']
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_face_south_19',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_345_action_queue_async_13_SUBSCRIPT_reset_properties_20',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_345_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_pause_15',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_run_dialog_16',
        "command": 'run_dialog',
        "args": [720, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_pause_17',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_345_action_queue_async_18_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_345_pause_19',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_set_action_script_async_20',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_remember_last_object_21',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_run_dialog_23',
        "command": 'run_dialog',
        "args": [2320, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_345_ret_24',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
