from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_616_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_616_jmp_if_bit_set_8']
    },
    {
        "identifier": 'EVENT_616_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_616_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_616_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_616_enter_area_6']
    },
    {
        "identifier": 'EVENT_616_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER, RadialDirections.SOUTHEAST, 5, 73, 4, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_616_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_616_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._064_MARRYMORE_OUTSIDE, RadialDirections.SOUTHEAST, 5, 73, 4, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_616_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_616_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 5, 'EVENT_616_jmp_if_bit_set_1']
    },
    {
        "identifier": 'EVENT_616_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 6, 'EVENT_616_jmp_if_bit_set_1']
    },
    {
        "identifier": 'EVENT_616_run_dialog_10',
        "command": 'run_dialog',
        "args": [997, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_616_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_616_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_616_action_queue_async_11_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_616_action_queue_async_11_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_616_action_queue_async_11_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_616_action_queue_async_11_SUBSCRIPT_pause_2']
            },
            {
                "identifier": 'EVENT_616_action_queue_async_11_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_616_action_queue_async_11_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_616_action_queue_async_11_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [6, 62]
            },
            {
                "identifier": 'EVENT_616_action_queue_async_11_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_616_run_dialog_12',
        "command": 'run_dialog',
        "args": [968, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_616_jmp_if_dialog_option_b_13',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_616_set_action_script_sync_18']
    },
    {
        "identifier": 'EVENT_616_set_action_script_async_14',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_616_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_616_run_dialog_16',
        "command": 'run_dialog',
        "args": [974, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_616_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_616_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_616_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_616_run_dialog_20',
        "command": 'run_dialog',
        "args": [996, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_616_pause_21',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_616_unsync_dialog_22',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_616_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_616_action_queue_async_23_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_616_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_616_jmp_if_bit_set_1']
    }
]
