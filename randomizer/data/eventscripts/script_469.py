from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_469_enable_controls_0',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_469_action_queue_async_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_469_unfreeze_camera_2',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_469_action_queue_async_3_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[2, 3]]
            },
        ]
    },
    {
        "identifier": 'EVENT_469_enable_controls_until_return_4',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_469_action_queue_async_5_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
        ]
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 505],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_7000_to_pressed_button_7',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_8',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_469_set_7000_to_pressed_button_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_9',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_469_set_7000_to_pressed_button_87'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_10',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_469_set_7000_to_pressed_button_91'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_11',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_469_set_7000_to_pressed_button_95'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_12',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 3], 'EVENT_469_set_action_script_sync_61'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_13',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 2], 'EVENT_469_set_action_script_sync_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_14',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1, 2], 'EVENT_469_set_action_script_sync_64'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_15',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1, 3], 'EVENT_469_set_action_script_sync_58'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_16',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_469_action_queue_async_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_17',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[6], 'EVENT_469_enable_controls_until_return_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_pause_18',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_469_enable_controls_until_return_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_469_action_queue_async_20_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_469_action_queue_async_20_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x703e, 0x700c]
            },
        ]
    },
    {
        "identifier": 'EVENT_469_set_7016_to_object_xyz_21',
        "command": 'set_7016_to_object_xyz',
        "args": [0x80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x701a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_var_not_equals_short_23',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_469_enable_controls_until_return_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_db_24',
        "command": 'db',
        "args": [0xfd, 0xca],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_var_equals_short_25',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_469_action_queue_async_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_var_equals_short_26',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 512, 'EVENT_469_action_queue_async_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_var_equals_short_27',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 531, 'EVENT_469_action_queue_async_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_var_equals_short_28',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 256, 'EVENT_469_action_queue_async_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_469_enable_controls_until_return_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_469_action_queue_async_30_SUBSCRIPT_run_away_shift_0',
                "command": 'run_away_shift',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_469_set_short_mem_31',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_add_32',
        "command": 'add',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_mem_7000_and_const_33',
        "command": 'mem_7000_and_const',
        "args": [0x0007],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_enable_controls_until_return_35',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_var_equals_short_36',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_469_set_action_script_sync_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_var_equals_short_37',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_469_set_action_script_sync_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 289],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 288],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_unsync_action_script_40',
        "command": 'unsync_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_pause_41',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_mario_in_air_42',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_469_pause_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_apply_solidity_mod_43',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 2, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_apply_solidity_mod_44',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 4, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_apply_solidity_mod_45',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 6, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_enable_controls_46',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_ret_47',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_48',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 498],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_49',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 497],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_unsync_action_script_50',
        "command": 'unsync_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_pause_51',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_mario_in_air_52',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_469_pause_51'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_apply_solidity_mod_53',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 2, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_apply_solidity_mod_54',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 4, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_apply_solidity_mod_55',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 6, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_enable_controls_56',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_ret_57',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_58',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 211],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_async_59',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 230],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_60',
        "command": 'jmp',
        "args": ['EVENT_469_set_7000_to_pressed_button_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_61',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 212],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_async_62',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 231],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_63',
        "command": 'jmp',
        "args": ['EVENT_469_set_7000_to_pressed_button_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_64',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 213],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_async_65',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 232],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_66',
        "command": 'jmp',
        "args": ['EVENT_469_set_7000_to_pressed_button_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_67',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 217],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_async_68',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 233],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_469_set_7000_to_pressed_button_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_70',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 218],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_async_71',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 234],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_72',
        "command": 'jmp',
        "args": ['EVENT_469_set_7000_to_pressed_button_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_73',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 219],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_async_74',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 235],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_469_set_7000_to_pressed_button_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_bit_76',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_77',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 220],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_async_78',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 236],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_79',
        "command": 'jmp',
        "args": ['EVENT_469_set_7000_to_pressed_button_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_sync_80',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 221],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_action_script_async_81',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 237],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_82',
        "command": 'jmp',
        "args": ['EVENT_469_set_7000_to_pressed_button_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_7000_to_pressed_button_83',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_84',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_469_set_action_script_sync_58'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_85',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_469_set_action_script_sync_61'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_86',
        "command": 'jmp',
        "args": ['EVENT_469_set_action_script_sync_70'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_7000_to_pressed_button_87',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_88',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_469_set_action_script_sync_64'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_89',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_469_set_action_script_sync_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_90',
        "command": 'jmp',
        "args": ['EVENT_469_set_action_script_sync_73'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_7000_to_pressed_button_91',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_92',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_469_set_action_script_sync_58'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_93',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_469_set_action_script_sync_64'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_94',
        "command": 'jmp',
        "args": ['EVENT_469_set_bit_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_set_7000_to_pressed_button_95',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_96',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_469_set_action_script_sync_61'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_7000_any_bits_set_97',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_469_set_action_script_sync_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_98',
        "command": 'jmp',
        "args": ['EVENT_469_set_action_script_sync_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_enable_controls_until_return_99',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_469_action_queue_sync_100_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
        ]
    },
    {
        "identifier": 'EVENT_469_start_embedded_action_script_async_101',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[2, 3]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_700C_to_object_coord_1',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_9, Coords.F]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x7032, 0x700c]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_if_700C_any_bits_set_3',
                "command": 'jmp_if_700C_any_bits_set',
                "args": [[0], 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_if_var_equals_short_5']
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_4',
                "command": 'jmp',
                "args": ['EVENT_469_pause_102']
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 3, 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_animation_speed_11']
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_animation_speed_14']
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_if_var_equals_short_7',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 7, 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_animation_speed_17']
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_10',
                "command": 'jmp',
                "args": ['EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_pause_19']
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_13',
                "command": 'jmp',
                "args": ['EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_pause_19']
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_jmp_16',
                "command": 'jmp',
                "args": ['EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_pause_19']
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_469_start_embedded_action_script_async_101_SUBSCRIPT_reset_properties_20',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_469_pause_102',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_if_mario_in_air_103',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_469_pause_102'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_remember_last_object_104',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_469_jmp_105',
        "command": 'jmp',
        "args": ['EVENT_469_enable_controls_until_return_4'],
        "subscript": []
    },
]
