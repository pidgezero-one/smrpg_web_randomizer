from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2630_set_0',
        "command": 'set',
        "args": [0x70ae, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_1',
        "command": 'run_dialog',
        "args": [3293, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_dialog_option_b_2',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2631_pause_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_pause_3',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 0, 'EVENT_2630_store_frog_coin_amount_7000_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_bit_6',
        "command": 'set_bit',
        "args": [0x7046, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_7',
        "command": 'run_dialog',
        "args": [3314, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_dialog_option_b_8',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2630_pause_525'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_pause_9',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_store_frog_coin_amount_7000_11',
        "command": 'store_frog_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2630_run_dialog_523'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7045, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_15',
        "command": 'set',
        "args": [0x70ac, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_16',
        "command": 'set',
        "args": [0x70ad, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_17',
        "command": 'set',
        "args": [0x70ae, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_18',
        "command": 'set',
        "args": [0x70af, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_19',
        "command": 'set',
        "args": [0x70c0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_20',
        "command": 'set',
        "args": [0x70c1, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_21',
        "command": 'set',
        "args": [0x70c2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_22',
        "command": 'set',
        "args": [0x70c3, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_23',
        "command": 'set',
        "args": [0x70c4, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_24',
        "command": 'set',
        "args": [0x70c5, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_25',
        "command": 'set',
        "args": [0x70c7, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_26',
        "command": 'set',
        "args": [0x70eb, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_async_27_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_run_dialog_28',
        "command": 'run_dialog',
        "args": [3280, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_random_29',
        "command": 'set_random',
        "args": [0x7000, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_30',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2630_add_66'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_31',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2630_add_63'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_32',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2630_add_60'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_33',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2630_add_57'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_34',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2630_add_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_35',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2630_add_51'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_36',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2630_add_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_37',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2630_add_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_38',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8, 'EVENT_2630_add_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_39',
        "command": 'add',
        "args": [0x70eb, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_40',
        "command": 'add',
        "args": [0x70ac, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_42',
        "command": 'add',
        "args": [0x70c7, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_43',
        "command": 'add',
        "args": [0x70ac, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_45',
        "command": 'add',
        "args": [0x70c5, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_46',
        "command": 'add',
        "args": [0x70ac, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_48',
        "command": 'add',
        "args": [0x70c4, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_49',
        "command": 'add',
        "args": [0x70ac, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_50',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_51',
        "command": 'add',
        "args": [0x70c3, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_52',
        "command": 'add',
        "args": [0x70ac, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_54',
        "command": 'add',
        "args": [0x70c2, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_55',
        "command": 'add',
        "args": [0x70ac, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_56',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_57',
        "command": 'add',
        "args": [0x70c1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_58',
        "command": 'add',
        "args": [0x70ac, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_60',
        "command": 'add',
        "args": [0x70c0, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_61',
        "command": 'add',
        "args": [0x70ac, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_62',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_63',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_64',
        "command": 'add',
        "args": [0x70ac, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_65',
        "command": 'jmp',
        "args": ['EVENT_2630_set_random_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_66',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_67',
        "command": 'add',
        "args": [0x70ac, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_random_68',
        "command": 'set_random',
        "args": [0x7000, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_69',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2630_add_105'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_70',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2630_add_102'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_71',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2630_add_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_72',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2630_add_96'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_73',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2630_add_93'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_74',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2630_add_90'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_75',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2630_add_87'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_76',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2630_add_84'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_77',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8, 'EVENT_2630_add_81'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_78',
        "command": 'add',
        "args": [0x70eb, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_79',
        "command": 'add',
        "args": [0x70ac, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_80',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_81',
        "command": 'add',
        "args": [0x70c7, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_82',
        "command": 'add',
        "args": [0x70ac, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_83',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_84',
        "command": 'add',
        "args": [0x70c5, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_85',
        "command": 'add',
        "args": [0x70ac, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_86',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_87',
        "command": 'add',
        "args": [0x70c4, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_88',
        "command": 'add',
        "args": [0x70ac, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_89',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_90',
        "command": 'add',
        "args": [0x70c3, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_91',
        "command": 'add',
        "args": [0x70ac, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_92',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_93',
        "command": 'add',
        "args": [0x70c2, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_94',
        "command": 'add',
        "args": [0x70ac, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_95',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_96',
        "command": 'add',
        "args": [0x70c1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_97',
        "command": 'add',
        "args": [0x70ac, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_98',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_99',
        "command": 'add',
        "args": [0x70c0, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_100',
        "command": 'add',
        "args": [0x70ac, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_101',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_102',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_103',
        "command": 'add',
        "args": [0x70ac, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_104',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_105',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_106',
        "command": 'add',
        "args": [0x70ac, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_107',
        "command": 'run_dialog',
        "args": [3291, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_108_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_pause_109',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_async_110',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_async_110_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_110_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_110_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_110_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_110_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_110_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_110_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_110_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=6, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_set_random_111',
        "command": 'set_random',
        "args": [0x7000, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_112',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2630_add_148'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_113',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2630_add_145'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_114',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2630_add_142'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_115',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2630_add_139'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_116',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2630_add_136'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_117',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2630_add_133'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_118',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2630_add_130'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_119',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2630_add_127'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_120',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8, 'EVENT_2630_add_124'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_121',
        "command": 'add',
        "args": [0x70eb, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_122',
        "command": 'add',
        "args": [0x70ad, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_123',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_124',
        "command": 'add',
        "args": [0x70c7, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_125',
        "command": 'add',
        "args": [0x70ad, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_126',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_127',
        "command": 'add',
        "args": [0x70c5, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_128',
        "command": 'add',
        "args": [0x70ad, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_129',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_130',
        "command": 'add',
        "args": [0x70c4, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_131',
        "command": 'add',
        "args": [0x70ad, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_132',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_133',
        "command": 'add',
        "args": [0x70c3, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_134',
        "command": 'add',
        "args": [0x70ad, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_135',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_136',
        "command": 'add',
        "args": [0x70c2, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_137',
        "command": 'add',
        "args": [0x70ad, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_138',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_139',
        "command": 'add',
        "args": [0x70c1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_140',
        "command": 'add',
        "args": [0x70ad, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_141',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_142',
        "command": 'add',
        "args": [0x70c0, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_143',
        "command": 'add',
        "args": [0x70ad, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_144',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_145',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_146',
        "command": 'add',
        "args": [0x70ad, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_147',
        "command": 'jmp',
        "args": ['EVENT_2630_set_short_mem_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_148',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_149',
        "command": 'add',
        "args": [0x70ad, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_150',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_151',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_152',
        "command": 'run_dialog',
        "args": [3292, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_async_153',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_153_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_pause_154',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_async_155',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_155_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=6, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_set_random_156',
        "command": 'set_random',
        "args": [0x7000, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_157',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2630_add_211'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_158',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2630_add_206'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_159',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2630_add_201'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_160',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2630_add_196'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_161',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2630_add_191'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_162',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2630_add_186'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_163',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2630_add_181'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_164',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2630_add_176'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_165',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8, 'EVENT_2630_add_171'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_166',
        "command": 'add',
        "args": [0x70eb, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_167',
        "command": 'add',
        "args": [0x70ad, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_168',
        "command": 'set',
        "args": [0x7000, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_169',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_170',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_171',
        "command": 'add',
        "args": [0x70c7, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_172',
        "command": 'add',
        "args": [0x70ad, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_173',
        "command": 'set',
        "args": [0x7000, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_174',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_175',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_176',
        "command": 'add',
        "args": [0x70c5, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_177',
        "command": 'add',
        "args": [0x70ad, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_178',
        "command": 'set',
        "args": [0x7000, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_179',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_180',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_181',
        "command": 'add',
        "args": [0x70c4, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_182',
        "command": 'add',
        "args": [0x70ad, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_183',
        "command": 'set',
        "args": [0x7000, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_184',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_185',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_186',
        "command": 'add',
        "args": [0x70c3, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_187',
        "command": 'add',
        "args": [0x70ad, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_188',
        "command": 'set',
        "args": [0x7000, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_189',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_190',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_191',
        "command": 'add',
        "args": [0x70c2, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_192',
        "command": 'add',
        "args": [0x70ad, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_193',
        "command": 'set',
        "args": [0x7000, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_194',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_195',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_196',
        "command": 'add',
        "args": [0x70c1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_197',
        "command": 'add',
        "args": [0x70ad, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_198',
        "command": 'set',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_199',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_200',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_201',
        "command": 'add',
        "args": [0x70c0, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_202',
        "command": 'add',
        "args": [0x70ad, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_203',
        "command": 'set',
        "args": [0x7000, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_204',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_205',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_206',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_207',
        "command": 'add',
        "args": [0x70ad, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_208',
        "command": 'set',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_209',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_210',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_211',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_212',
        "command": 'add',
        "args": [0x70ad, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_213',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_214',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_stop_embedded_action_script_215',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_stop_embedded_action_script_216',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_bit_set_217',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_218',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 21, 'EVENT_2630_set_bit_357'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_219',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 20, 'EVENT_2630_set_bit_357'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_220',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 19, 'EVENT_2630_set_bit_357'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_221',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 18, 'EVENT_2630_set_random_353'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_222',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 17, 'EVENT_2630_set_random_353'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_223',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 16, 'EVENT_2630_set_random_353'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_224',
        "command": 'run_dialog',
        "args": [3276, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_sync_225',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_225_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_set_random_226',
        "command": 'set_random',
        "args": [0x7000, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_227',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2630_jmp_if_var_equals_byte_343'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_228',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2630_jmp_if_var_equals_byte_332'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_229',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2630_jmp_if_var_equals_byte_320'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_230',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2630_jmp_if_var_equals_byte_308'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_231',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2630_jmp_if_var_equals_byte_296'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_232',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2630_jmp_if_var_equals_byte_284'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_233',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2630_jmp_if_var_equals_byte_272'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_234',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2630_jmp_if_var_equals_byte_260'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_235',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8, 'EVENT_2630_jmp_if_var_equals_byte_248'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_236',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70eb, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_237',
        "command": 'add',
        "args": [0x70ac, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_238',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_239',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_240',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_243'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_241',
        "command": 'add',
        "args": [0x70eb, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_242',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_243',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_start_loop_n_times_244',
        "command": 'start_loop_n_times',
        "args": [9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_245',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_end_loop_246',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_247',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_248',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c7, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_249',
        "command": 'add',
        "args": [0x70ac, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_250',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_251',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_252',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_255'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_253',
        "command": 'add',
        "args": [0x70c7, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_254',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_255',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_start_loop_n_times_256',
        "command": 'start_loop_n_times',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_257',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_end_loop_258',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_259',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_260',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c5, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_261',
        "command": 'add',
        "args": [0x70ac, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_262',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_263',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_264',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_267'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_265',
        "command": 'add',
        "args": [0x70c5, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_266',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_267',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_start_loop_n_times_268',
        "command": 'start_loop_n_times',
        "args": [7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_269',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_end_loop_270',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_271',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_272',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c4, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_273',
        "command": 'add',
        "args": [0x70ac, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_274',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_275',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_276',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_279'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_277',
        "command": 'add',
        "args": [0x70c4, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_278',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_279',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_start_loop_n_times_280',
        "command": 'start_loop_n_times',
        "args": [6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_281',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_end_loop_282',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_283',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_284',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c3, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_285',
        "command": 'add',
        "args": [0x70ac, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_286',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_287',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_288',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_291'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_289',
        "command": 'add',
        "args": [0x70c3, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_290',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_291',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_start_loop_n_times_292',
        "command": 'start_loop_n_times',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_293',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_end_loop_294',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_295',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_296',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_297',
        "command": 'add',
        "args": [0x70ac, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_298',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_299',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_300',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_303'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_301',
        "command": 'add',
        "args": [0x70c2, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_302',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_303',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_start_loop_n_times_304',
        "command": 'start_loop_n_times',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_305',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_end_loop_306',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_307',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_308',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_309',
        "command": 'add',
        "args": [0x70ac, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_310',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_311',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_312',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_315'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_313',
        "command": 'add',
        "args": [0x70c1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_314',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_315',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_start_loop_n_times_316',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_317',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_end_loop_318',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_319',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_320',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_321',
        "command": 'add',
        "args": [0x70ac, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_322',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_323',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_324',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_327'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_325',
        "command": 'add',
        "args": [0x70c0, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_326',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_327',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_start_loop_n_times_328',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_329',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_end_loop_330',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_331',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_332',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_333',
        "command": 'add',
        "args": [0x70ac, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_334',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_335',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_336',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_339'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_337',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_338',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_339',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_340',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_341',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_342',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_343',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 3, 'EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_344',
        "command": 'add',
        "args": [0x70ac, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_345',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_346',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_347',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_jmp_if_random_above_128_350'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_348',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_349',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_if_bit_set_359'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_random_above_128_350',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2630_set_bit_469'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_351',
        "command": 'dec',
        "args": [0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_352',
        "command": 'jmp',
        "args": ['EVENT_2630_action_queue_sync_225'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_random_353',
        "command": 'set_random',
        "args": [0x7000, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_354',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2630_set_bit_357'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_355',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2630_set_bit_357'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_356',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_224'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_bit_357',
        "command": 'set_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_358',
        "command": 'run_dialog',
        "args": [3277, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_bit_set_359',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'EVENT_2630_set_bit_466'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_stop_embedded_action_script_360',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_361',
        "command": 'run_dialog',
        "args": [3278, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_362',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_363',
        "command": 'run_dialog',
        "args": [3279, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_dialog_option_b_364',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2630_set_bit_466'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_sync_365',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2630_action_queue_sync_365_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=6, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_set_random_366',
        "command": 'set_random',
        "args": [0x7000, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_367',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2630_jmp_if_var_equals_byte_457'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_368',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2630_jmp_if_var_equals_byte_448'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_369',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2630_jmp_if_var_equals_byte_439'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_370',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2630_jmp_if_var_equals_byte_430'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_371',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2630_jmp_if_var_equals_byte_421'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_372',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2630_jmp_if_var_equals_byte_412'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_373',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2630_jmp_if_var_equals_byte_403'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_374',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2630_jmp_if_var_equals_byte_394'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_short_375',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8, 'EVENT_2630_jmp_if_var_equals_byte_385'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_376',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70eb, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_377',
        "command": 'add',
        "args": [0x70eb, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_378',
        "command": 'set',
        "args": [0x7000, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_379',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_380',
        "command": 'add',
        "args": [0x70ad, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_381',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_382',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_383',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_384',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_385',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c7, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_386',
        "command": 'add',
        "args": [0x70c7, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_387',
        "command": 'set',
        "args": [0x7000, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_388',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_389',
        "command": 'add',
        "args": [0x70ad, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_390',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_391',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_392',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_393',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_394',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c5, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_395',
        "command": 'add',
        "args": [0x70c5, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_396',
        "command": 'set',
        "args": [0x7000, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_397',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_398',
        "command": 'add',
        "args": [0x70ad, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_399',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_400',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_401',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_402',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_403',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c4, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_404',
        "command": 'add',
        "args": [0x70c4, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_405',
        "command": 'set',
        "args": [0x7000, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_406',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_407',
        "command": 'add',
        "args": [0x70ad, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_408',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_409',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_410',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_411',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_412',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c3, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_413',
        "command": 'add',
        "args": [0x70c3, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_414',
        "command": 'set',
        "args": [0x7000, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_415',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_416',
        "command": 'add',
        "args": [0x70ad, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_417',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_418',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_419',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_420',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_421',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_422',
        "command": 'add',
        "args": [0x70c2, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_423',
        "command": 'set',
        "args": [0x7000, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_424',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_425',
        "command": 'add',
        "args": [0x70ad, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_426',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_427',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_428',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_429',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_430',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_431',
        "command": 'add',
        "args": [0x70c1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_432',
        "command": 'set',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_433',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_434',
        "command": 'add',
        "args": [0x70ad, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_435',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_436',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_437',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_438',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_439',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_440',
        "command": 'add',
        "args": [0x70c0, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_441',
        "command": 'set',
        "args": [0x7000, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_442',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_443',
        "command": 'add',
        "args": [0x70ad, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_444',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_445',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_446',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_447',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_448',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_449',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_450',
        "command": 'set',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_451',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_452',
        "command": 'add',
        "args": [0x70ad, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_453',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_454',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_455',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_456',
        "command": 'jmp',
        "args": ['EVENT_2630_jmp_465'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_var_equals_byte_457',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 3, 'EVENT_2630_action_queue_sync_365'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_458',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_459',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_460',
        "command": 'run_dialog',
        "args": [3281, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_461',
        "command": 'add',
        "args": [0x70ad, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_462',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_463',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_464',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_async_471'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_465',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_bit_466',
        "command": 'set_bit',
        "args": [0x7045, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_bit_set_467',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2630_run_dialog_476'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_468',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_bit_469',
        "command": 'set_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_470',
        "command": 'jmp',
        "args": ['EVENT_2630_stop_embedded_action_script_215'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_async_471',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_async_471_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_471_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_run_dialog_472',
        "command": 'run_dialog',
        "args": [3282, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_473',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_sync_474',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_sync_474_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_jmp_475',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_495'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_476',
        "command": 'run_dialog',
        "args": [3283, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_477',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_mem_compare_478',
        "command": 'mem_compare',
        "args": [0x7000, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_greater_or_equal_479',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2630_action_queue_sync_505'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_480',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_async_481',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_async_481_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_481_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_run_dialog_482',
        "command": 'run_dialog',
        "args": [3284, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_short_mem_483',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_async_484',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_async_484_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._152_SLIP_HIT, 4]
            },
            {
                "identifier": 'EVENT_2630_action_queue_async_484_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_run_dialog_485',
        "command": 'run_dialog',
        "args": [3285, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_sync_486',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_sync_486_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_action_queue_sync_487',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_sync_487_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_mem_compare_488',
        "command": 'mem_compare',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_loaded_memory_is_0_489',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_2630_run_dialog_500'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_comparison_result_is_lesser_490',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2630_run_dialog_495'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_491',
        "command": 'run_dialog',
        "args": [3287, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_play_sound_492',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_frog_coins_493',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_494',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_512'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_495',
        "command": 'run_dialog',
        "args": [3288, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_play_sound_496',
        "command": 'play_sound',
        "args": [Sounds._105_SURPRISE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_497',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_frog_coins_7000_498',
        "command": 'dec_frog_coins_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_499',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_512'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_500',
        "command": 'run_dialog',
        "args": [3289, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_play_sound_501',
        "command": 'play_sound',
        "args": [Sounds._105_SURPRISE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_502',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_dec_frog_coins_7000_503',
        "command": 'dec_frog_coins_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_504',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_512'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_action_queue_sync_505',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2630_action_queue_sync_505_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2630_run_dialog_506',
        "command": 'run_dialog',
        "args": [3284, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_507',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_508',
        "command": 'run_dialog',
        "args": [3286, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_play_sound_509',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_add_frog_coins_510',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_511',
        "command": 'jmp',
        "args": ['EVENT_2630_run_dialog_512'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_512',
        "command": 'run_dialog',
        "args": [3319, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_dialog_option_b_513',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2630_pause_517'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_pause_514',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_515',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_516',
        "command": 'jmp',
        "args": ['EVENT_2630_store_frog_coin_amount_7000_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_pause_517',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_518',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_519',
        "command": 'run_dialog',
        "args": [3313, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_520',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_enable_controls_521',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_ret_522',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_523',
        "command": 'run_dialog',
        "args": [3290, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_ret_524',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_pause_525',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_526',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_run_dialog_527',
        "command": 'run_dialog',
        "args": [3297, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_if_dialog_option_b_528',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2631_pause_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_pause_529',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_set_action_script_async_530',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2630_jmp_531',
        "command": 'jmp',
        "args": ['EVENT_2630_store_frog_coin_amount_7000_11'],
        "subscript": []
    }
]
