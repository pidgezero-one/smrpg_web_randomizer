from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_298_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_298_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 1, 'EVENT_298_action_queue_async_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_298_run_dialog_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_freeze_camera_4',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_run_dialog_5',
        "command": 'run_dialog',
        "args": [535, AreaObjects.NPC_4, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_298_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_298_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [286],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_298_action_queue_async_8_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_298_action_queue_async_8_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_298_action_queue_async_8_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_298_action_queue_async_8_SUBSCRIPT_pause_1']
            },
        ]
    },
    {
        "identifier": 'EVENT_298_pause_9',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_298_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_298_action_queue_async_10_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_298_action_queue_async_10_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_298_action_queue_async_10_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_298_pause_11',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_run_dialog_12',
        "command": 'run_dialog',
        "args": [536, AreaObjects.NPC_4, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_298_action_queue_async_13_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_298_unfreeze_camera_14',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_run_dialog_16',
        "command": 'run_dialog',
        "args": [580, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_298_action_queue_async_18_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_4, Coords.F]
            },
            {
                "identifier": 'EVENT_298_action_queue_async_18_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x7024, 0x700c]
            },
            {
                "identifier": 'EVENT_298_action_queue_async_18_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_298_action_queue_async_18_SUBSCRIPT_add_3',
                "command": 'add',
                "args": [0x700c, 4]
            },
            {
                "identifier": 'EVENT_298_action_queue_async_18_SUBSCRIPT_mem_700C_and_const_4',
                "command": 'mem_700C_and_const',
                "args": [0x0007]
            },
            {
                "identifier": 'EVENT_298_action_queue_async_18_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_298_action_queue_async_18_SUBSCRIPT_face_east_6',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_298_run_dialog_19',
        "command": 'run_dialog',
        "args": [588, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_298_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_298_action_queue_async_20_SUBSCRIPT_set_short_mem_0',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7024]
            },
            {
                "identifier": 'EVENT_298_action_queue_async_20_SUBSCRIPT_face_east_1',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_298_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
