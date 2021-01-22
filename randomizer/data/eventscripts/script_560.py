from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_560_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 189, 'EVENT_560_remove_from_current_level_34']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 83, 'EVENT_560_remove_from_current_level_41']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 84, 'EVENT_560_remove_from_current_level_49']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 301, 'EVENT_560_jmp_if_var_equals_byte_57']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 74, 'EVENT_560_jmp_if_bit_clear_69']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 34, 'EVENT_560_remove_from_current_level_95']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 195, 'EVENT_560_jmp_if_objects_less_than_xy_steps_apart_102']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 41, 'EVENT_560_jmp_if_objects_less_than_xy_steps_apart_111']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 315, 'EVENT_560_remove_from_current_level_119']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 324, 'EVENT_560_remove_from_current_level_126']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 254, 'EVENT_560_remove_from_current_level_133']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 414, 'EVENT_560_jmp_if_bit_set_140']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 409, 'EVENT_560_jmp_if_objects_less_than_xy_steps_apart_152']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 107, 'EVENT_560_remove_from_current_level_153']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 438, 'EVENT_560_action_queue_async_161']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 208, 'EVENT_560_jmp_if_bit_clear_236']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 422, 'EVENT_560_store_item_amount_7000_250']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 118, 'EVENT_560_freeze_all_npcs_until_return_273']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 418, 'EVENT_560_set_307']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 47, 'EVENT_560_jmp_if_bit_set_355']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 483, 'EVENT_560_jmp_if_bit_set_355']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_22',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 491, 'EVENT_560_jmp_if_bit_set_355']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_23',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 75, 'EVENT_560_set_373']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 272, 'EVENT_560_set_395']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_25',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 104, 'EVENT_560_set_422']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_26',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 86, 'EVENT_560_jmp_if_bit_set_28']
    },
    {
        "identifier": 'EVENT_560_ret_27',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 7, 'EVENT_560_ret_33']
    },
    {
        "identifier": 'EVENT_560_set_bit_29',
        "command": 'set_bit',
        "args": [0x7085, 7]
    },
    {
        "identifier": 'EVENT_560_set_30',
        "command": 'set',
        "args": [0x70a7, 9]
    },
    {
        "identifier": 'EVENT_560_set_short_31',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_32',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_34',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_35',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._189_MARIOS_PIPEHOUSE]
    },
    {
        "identifier": 'EVENT_560_set_36',
        "command": 'set',
        "args": [0x70a7, 162]
    },
    {
        "identifier": 'EVENT_560_set_37',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_38',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_39',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_40',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_41',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_42',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_43',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_12, Rooms._084_ROSE_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_560_set_44',
        "command": 'set',
        "args": [0x70a7, 163]
    },
    {
        "identifier": 'EVENT_560_set_45',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_46',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_47',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_48',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_49',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_50',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_51',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_12, Rooms._084_ROSE_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_560_set_52',
        "command": 'set',
        "args": [0x70a7, 163]
    },
    {
        "identifier": 'EVENT_560_set_53',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_54',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_55',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_56',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_57',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 20, 'EVENT_560_jmp_to_event_60']
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_58',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_560_set_61']
    },
    {
        "identifier": 'EVENT_560_jmp_to_event_59',
        "command": 'jmp_to_event',
        "args": [32]
    },
    {
        "identifier": 'EVENT_560_jmp_to_event_60',
        "command": 'jmp_to_event',
        "args": [32]
    },
    {
        "identifier": 'EVENT_560_set_61',
        "command": 'set',
        "args": [0x70a7, 166]
    },
    {
        "identifier": 'EVENT_560_set_bit_62',
        "command": 'set_bit',
        "args": [0x7055, 4]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_63',
        "command": 'run_event_as_subroutine',
        "args": [33]
    },
    {
        "identifier": 'EVENT_560_set_64',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_set_65',
        "command": 'set',
        "args": [0x70a7, 166]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_66',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_67',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_68',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_clear_69',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_560_set_bit_72']
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_clear_70',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_560_set_bit_79']
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_clear_71',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_560_set_bit_86']
    },
    {
        "identifier": 'EVENT_560_set_bit_72',
        "command": 'set_bit',
        "args": [0x7051, 4]
    },
    {
        "identifier": 'EVENT_560_set_73',
        "command": 'set',
        "args": [0x70a7, 151]
    },
    {
        "identifier": 'EVENT_560_set_74',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_75',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_76',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_pause_77',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_560_jmp_78',
        "command": 'jmp',
        "args": ['EVENT_1074_action_queue_async_185']
    },
    {
        "identifier": 'EVENT_560_set_bit_79',
        "command": 'set_bit',
        "args": [0x7054, 5]
    },
    {
        "identifier": 'EVENT_560_set_80',
        "command": 'set',
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_560_set_81',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_82',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_83',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_pause_84',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_560_jmp_85',
        "command": 'jmp',
        "args": ['EVENT_1074_action_queue_async_185']
    },
    {
        "identifier": 'EVENT_560_set_bit_86',
        "command": 'set_bit',
        "args": [0x7054, 6]
    },
    {
        "identifier": 'EVENT_560_set_bit_87',
        "command": 'set_bit',
        "args": [0x7093, 0]
    },
    {
        "identifier": 'EVENT_560_set_88',
        "command": 'set',
        "args": [0x70a7, 150]
    },
    {
        "identifier": 'EVENT_560_set_89',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_90',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_91',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_pause_92',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_560_jmp_93',
        "command": 'jmp',
        "args": ['EVENT_1074_action_queue_async_185']
    },
    {
        "identifier": 'EVENT_560_ret_94',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_95',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_96',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_16, Rooms._034_YOSTER_ISLE]
    },
    {
        "identifier": 'EVENT_560_set_97',
        "command": 'set',
        "args": [0x70a7, 161]
    },
    {
        "identifier": 'EVENT_560_set_98',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_99',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_100',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_101',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_objects_less_than_xy_steps_apart_102',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MARIO, AreaObjects.NPC_14, 0x03, 0x03, 'EVENT_560_set_208']
    },
    {
        "identifier": 'EVENT_560_set_bit_103',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_560_set_bit_104',
        "command": 'set_bit',
        "args": [0x7054, 0]
    },
    {
        "identifier": 'EVENT_560_set_105',
        "command": 'set',
        "args": [0x70a7, 141]
    },
    {
        "identifier": 'EVENT_560_set_106',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_107',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_108',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_109',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_109_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_109_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_ret_110',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_objects_less_than_xy_steps_apart_111',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MARIO, AreaObjects.NPC_6, 0x03, 0x03, 'EVENT_560_set_222']
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_112',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_113',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS]
    },
    {
        "identifier": 'EVENT_560_set_114',
        "command": 'set',
        "args": [0x70a7, 140]
    },
    {
        "identifier": 'EVENT_560_set_115',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_116',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_117',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_118',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_119',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_120',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH]
    },
    {
        "identifier": 'EVENT_560_set_121',
        "command": 'set',
        "args": [0x70a7, 142]
    },
    {
        "identifier": 'EVENT_560_set_122',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_123',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_124',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_125',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_126',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_127',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._324_MONSTRO_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_560_set_128',
        "command": 'set',
        "args": [0x70a7, 124]
    },
    {
        "identifier": 'EVENT_560_set_129',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_130',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_131',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_132',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_133',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_134',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._254_BEAN_VALLEY_SMILAX_AREA]
    },
    {
        "identifier": 'EVENT_560_set_135',
        "command": 'set',
        "args": [0x70a7, 158]
    },
    {
        "identifier": 'EVENT_560_set_136',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_137',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_138',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_139',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_140',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 6, 'EVENT_560_ret_151']
    },
    {
        "identifier": 'EVENT_560_set_bit_141',
        "command": 'set_bit',
        "args": [0x705f, 6]
    },
    {
        "identifier": 'EVENT_560_clear_bit_142',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_560_clear_bit_143',
        "command": 'clear_bit',
        "args": [0x704c, 1]
    },
    {
        "identifier": 'EVENT_560_set_144',
        "command": 'set',
        "args": [0x70ae, 16]
    },
    {
        "identifier": 'EVENT_560_pause_145',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_560_pause_146',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_560_set_147',
        "command": 'set',
        "args": [0x70a7, 132]
    },
    {
        "identifier": 'EVENT_560_set_148',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_149',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_jmp_to_event_150',
        "command": 'jmp_to_event',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_151',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_objects_less_than_xy_steps_apart_152',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MARIO, AreaObjects.NPC_6, 0x03, 0x03, 'EVENT_560_store_item_amount_7000_292']
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_153',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_154',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_155',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA]
    },
    {
        "identifier": 'EVENT_560_set_156',
        "command": 'set',
        "args": [0x70a7, 134]
    },
    {
        "identifier": 'EVENT_560_set_157',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_158',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_159',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_160',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_action_queue_async_161',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_161_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_161_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_161_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_162',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_pause_163',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_164',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_164_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_164_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_165',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_165_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_165_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_166',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_set_167',
        "command": 'set',
        "args": [0x70a7, 159]
    },
    {
        "identifier": 'EVENT_560_set_168',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_169',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_170',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_171',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_172',
        "command": 'set',
        "args": [0x70a7, 0]
    },
    {
        "identifier": 'EVENT_560_set_173',
        "command": 'set',
        "args": [0x70a7, 151]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_174',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_175',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_set_188']
    },
    {
        "identifier": 'EVENT_560_set_176',
        "command": 'set',
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_177',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_178',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_set_198']
    },
    {
        "identifier": 'EVENT_560_set_179',
        "command": 'set',
        "args": [0x70a7, 151]
    },
    {
        "identifier": 'EVENT_560_set_180',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_181',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_set_7000_to_current_level_182',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_183',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 74, 'EVENT_560_jmp_if_bit_set_351']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_184',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 47, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_185',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 483, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_186',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 491, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_ret_187',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_188',
        "command": 'set',
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_560_set_189',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_190',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_191',
        "command": 'remove_one_from_inventory',
        "args": [items.AltoCard]
    },
    {
        "identifier": 'EVENT_560_set_7000_to_current_level_192',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_193',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 74, 'EVENT_560_jmp_if_bit_set_351']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_194',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 47, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_195',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 483, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_196',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 491, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_ret_197',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_198',
        "command": 'set',
        "args": [0x70a7, 150]
    },
    {
        "identifier": 'EVENT_560_set_199',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_200',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_201',
        "command": 'remove_one_from_inventory',
        "args": [items.TenorCard]
    },
    {
        "identifier": 'EVENT_560_set_7000_to_current_level_202',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_203',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 74, 'EVENT_560_jmp_if_bit_set_351']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_204',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 47, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_205',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 483, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_206',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 491, 'EVENT_560_remove_one_from_inventory_371']
    },
    {
        "identifier": 'EVENT_560_ret_207',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_208',
        "command": 'set',
        "args": [0x70a7, 141]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_209',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_210',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_pause_213']
    },
    {
        "identifier": 'EVENT_560_run_dialog_211',
        "command": 'run_dialog',
        "args": [2801, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_560_ret_212',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_pause_213',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_560_play_sound_214',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_560_apply_tile_mod_215',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_216',
        "command": 'apply_solidity_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_217',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_218',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_14, Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM]
    },
    {
        "identifier": 'EVENT_560_pause_219',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_220',
        "command": 'remove_one_from_inventory',
        "args": [items.ElderKey]
    },
    {
        "identifier": 'EVENT_560_ret_221',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_222',
        "command": 'set',
        "args": [0x70a7, 140]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_223',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_224',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_pause_227']
    },
    {
        "identifier": 'EVENT_560_run_dialog_225',
        "command": 'run_dialog',
        "args": [2801, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_560_ret_226',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_pause_227',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_560_play_sound_228',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_560_apply_tile_mod_229',
        "command": 'apply_tile_mod',
        "args": [Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_230',
        "command": 'apply_solidity_mod',
        "args": [Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_231',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_232',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS]
    },
    {
        "identifier": 'EVENT_560_pause_233',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_234',
        "command": 'remove_one_from_inventory',
        "args": [items.RoomKey]
    },
    {
        "identifier": 'EVENT_560_ret_235',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_clear_236',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 2, 'EVENT_560_set_237']
    },
    {
        "identifier": 'EVENT_560_set_237',
        "command": 'set',
        "args": [0x70a7, 142]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_238',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_239',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_pause_242']
    },
    {
        "identifier": 'EVENT_560_run_dialog_240',
        "command": 'run_dialog',
        "args": [2801, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_560_ret_241',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_pause_242',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_560_play_sound_243',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_244',
        "command": 'apply_solidity_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_245',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_246',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    },
    {
        "identifier": 'EVENT_560_pause_247',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_248',
        "command": 'remove_one_from_inventory',
        "args": [items.ShedKey]
    },
    {
        "identifier": 'EVENT_560_ret_249',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_store_item_amount_7000_250',
        "command": 'store_item_amount_7000',
        "args": [items.TempleKey]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_not_equals_short_251',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_560_summon_to_current_level_at_marios_coords_254']
    },
    {
        "identifier": 'EVENT_560_run_dialog_252',
        "command": 'run_dialog',
        "args": [1235, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_560_ret_253',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_summon_to_current_level_at_marios_coords_254',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_255',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_walk_to_xy_coords_5',
                "command": 'walk_to_xy_coords',
                "args": [1, 118]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x20, 0xb1, 0x64]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_shift_z_up_pixels_11',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_255_SUBSCRIPT_shift_z_up_pixels_13',
                "command": 'shift_z_up_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_256',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_256_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_256_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_256_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_256_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_256_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_256_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_257',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_560_pause_258',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_560_play_sound_259',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_560_set_short_260',
        "command": 'set_short',
        "args": [0x7034, 0x0001]
    },
    {
        "identifier": 'EVENT_560_set_7010_to_object_xyz_261',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_16]
    },
    {
        "identifier": 'EVENT_560_start_loop_n_times_262',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'EVENT_560_pause_263',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_560_create_packet_at_7010_coords_jmp_if_null_264',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_560_pause_263']
    },
    {
        "identifier": 'EVENT_560_pause_265',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_560_add_short_266',
        "command": 'add_short',
        "args": [0x7034, 0x0003]
    },
    {
        "identifier": 'EVENT_560_end_loop_267',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_560_action_queue_async_268',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_268_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_268_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_268_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_268_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_268_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_268_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_268_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_268_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_269',
        "command": 'remove_one_from_inventory',
        "args": [items.TempleKey]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_270',
        "command": 'apply_solidity_mod',
        "args": [Rooms._422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_set_bit_271',
        "command": 'set_bit',
        "args": [0x7094, 6]
    },
    {
        "identifier": 'EVENT_560_ret_272',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_freeze_all_npcs_until_return_273',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_560_store_item_amount_7000_274',
        "command": 'store_item_amount_7000',
        "args": [items.CastleKey1]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_not_equals_short_275',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_560_play_sound_279']
    },
    {
        "identifier": 'EVENT_560_run_dialog_276',
        "command": 'run_dialog',
        "args": [3600, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_560_unfreeze_all_npcs_277',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_560_ret_278',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_play_sound_279',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_560_pause_280',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_560_play_sound_281',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_560_pause_282',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_283',
        "command": 'apply_solidity_mod',
        "args": [Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_284',
        "command": 'apply_solidity_mod',
        "args": [Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_285',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_286',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_287',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_288',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_11, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_289',
        "command": 'remove_one_from_inventory',
        "args": [items.CastleKey1]
    },
    {
        "identifier": 'EVENT_560_unfreeze_all_npcs_290',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_560_ret_291',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_store_item_amount_7000_292',
        "command": 'store_item_amount_7000',
        "args": [items.CastleKey2]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_not_equals_short_293',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_560_play_sound_296']
    },
    {
        "identifier": 'EVENT_560_run_dialog_294',
        "command": 'run_dialog',
        "args": [2811, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_560_ret_295',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_play_sound_296',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_560_pause_297',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_560_play_sound_298',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_560_pause_299',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_300',
        "command": 'apply_solidity_mod',
        "args": [Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_301',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_560_remove_from_current_level_302',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_303',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    },
    {
        "identifier": 'EVENT_560_remove_from_level_304',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_305',
        "command": 'remove_one_from_inventory',
        "args": [items.CastleKey2]
    },
    {
        "identifier": 'EVENT_560_ret_306',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_307',
        "command": 'set',
        "args": [0x70ae, 23]
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_308',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 7, 'EVENT_560_run_dialog_314']
    },
    {
        "identifier": 'EVENT_560_store_item_amount_7000_309',
        "command": 'store_item_amount_7000',
        "args": [items.Seed]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_not_equals_short_310',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_560_remove_one_from_inventory_316']
    },
    {
        "identifier": 'EVENT_560_store_item_amount_7000_311',
        "command": 'store_item_amount_7000',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_not_equals_short_312',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_560_remove_one_from_inventory_322']
    },
    {
        "identifier": 'EVENT_560_ret_313',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_run_dialog_314',
        "command": 'run_dialog',
        "args": [3103, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_ret_315',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_316',
        "command": 'remove_one_from_inventory',
        "args": [items.Seed]
    },
    {
        "identifier": 'EVENT_560_set_bit_317',
        "command": 'set_bit',
        "args": [0x708e, 5]
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_318',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 6, 'EVENT_560_jmp_if_bit_set_318']
    },
    {
        "identifier": 'EVENT_560_store_item_amount_7000_319',
        "command": 'store_item_amount_7000',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_not_equals_short_320',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_560_remove_one_from_inventory_322']
    },
    {
        "identifier": 'EVENT_560_ret_321',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_322',
        "command": 'remove_one_from_inventory',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_560_set_bit_323',
        "command": 'set_bit',
        "args": [0x708e, 6]
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_324',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 5, 'EVENT_560_freeze_camera_328']
    },
    {
        "identifier": 'EVENT_560_store_item_amount_7000_325',
        "command": 'store_item_amount_7000',
        "args": [items.Seed]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_not_equals_short_326',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_560_remove_one_from_inventory_316']
    },
    {
        "identifier": 'EVENT_560_ret_327',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_freeze_camera_328',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_560_set_bit_329',
        "command": 'set_bit',
        "args": [0x708e, 7]
    },
    {
        "identifier": 'EVENT_560_summon_to_level_330',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._417_GARDENERS_HOUSE_OUTSIDE]
    },
    {
        "identifier": 'EVENT_560_summon_to_level_331',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._417_GARDENERS_HOUSE_OUTSIDE]
    },
    {
        "identifier": 'EVENT_560_summon_to_level_332',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._418_GARDENERS_HOUSE]
    },
    {
        "identifier": 'EVENT_560_summon_to_level_333',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._418_GARDENERS_HOUSE]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_334',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_334_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_334_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [22, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_play_sound_335',
        "command": 'play_sound',
        "args": [Sounds._127_LIGHT_RATTLE, 6]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_336',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_336_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_336_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_337',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_338',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_560_pause_339',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_340',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_340_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_play_sound_341',
        "command": 'play_sound',
        "args": [Sounds._128_FLOATING_HOVERING, 6]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_342',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_342_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_342_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_342_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_342_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_343',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_560_summon_to_current_level_344',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_560_play_sound_345',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_560_pause_346',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_347',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 857]
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_348',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_560_unfreeze_camera_349',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_560_ret_350',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_351',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 6, 'EVENT_560_pause_92']
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_352',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 5, 'EVENT_560_pause_84']
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_353',
        "command": 'jmp_if_bit_set',
        "args": [0x7051, 4, 'EVENT_560_pause_77']
    },
    {
        "identifier": 'EVENT_560_ret_354',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_355',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 6, 'EVENT_560_set_361']
    },
    {
        "identifier": 'EVENT_560_set_bit_356',
        "command": 'set_bit',
        "args": [0x7089, 6]
    },
    {
        "identifier": 'EVENT_560_set_357',
        "command": 'set',
        "args": [0x70a7, 102]
    },
    {
        "identifier": 'EVENT_560_set_358',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_359',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_ret_360',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_361',
        "command": 'set',
        "args": [0x70a7, 128]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_362',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_363',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_set_367']
    },
    {
        "identifier": 'EVENT_560_open_shop_364',
        "command": 'open_shop',
        "args": [Shops._00_MUSHROOM_KINGDOM]
    },
    {
        "identifier": 'EVENT_560_fade_in_from_black_async_365',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_560_ret_366',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_367',
        "command": 'set',
        "args": [0x70a7, 130]
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_byte_368',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_560_set_172']
    },
    {
        "identifier": 'EVENT_560_set_369',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_370',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_371',
        "command": 'remove_one_from_inventory',
        "args": [items.RareFrogCoin]
    },
    {
        "identifier": 'EVENT_560_ret_372',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_373',
        "command": 'set',
        "args": [0x70a7, 130]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_374',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_375',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_set_380']
    },
    {
        "identifier": 'EVENT_560_set_376',
        "command": 'set',
        "args": [0x70a7, 166]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_377',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_378',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_play_sound_390']
    },
    {
        "identifier": 'EVENT_560_ret_379',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_380',
        "command": 'set',
        "args": [0x70a7, 6]
    },
    {
        "identifier": 'EVENT_560_set_381',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_382',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_383',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketPie]
    },
    {
        "identifier": 'EVENT_560_ret_384',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_385',
        "command": 'set',
        "args": [0x70a7, 6]
    },
    {
        "identifier": 'EVENT_560_set_386',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_387',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_388',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketJam]
    },
    {
        "identifier": 'EVENT_560_ret_389',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_play_sound_390',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_560_set_short_391',
        "command": 'set_short',
        "args": [0x7000, 0x000a]
    },
    {
        "identifier": 'EVENT_560_add_frog_coins_392',
        "command": 'add_frog_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_393',
        "command": 'remove_one_from_inventory',
        "args": [items.CricketJam]
    },
    {
        "identifier": 'EVENT_560_ret_394',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_395',
        "command": 'set',
        "args": [0x70a7, 135]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_396',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_397',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_560_set_399']
    },
    {
        "identifier": 'EVENT_560_ret_398',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_399',
        "command": 'set',
        "args": [0x70ae, 20]
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_400',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_560_pause_401',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_560_close_dialog_402',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_560_pause_403',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_560_store_02_to_0248_404',
        "command": 'store_02_to_0248'
    },
    {
        "identifier": 'EVENT_560_set_bit_405',
        "command": 'set_bit',
        "args": [0x707c, 4]
    },
    {
        "identifier": 'EVENT_560_pause_406',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_560_apply_tile_mod_407',
        "command": 'apply_tile_mod',
        "args": [Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_408',
        "command": 'apply_solidity_mod',
        "args": [Rooms._272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_pause_409',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_560_clear_bit_410',
        "command": 'clear_bit',
        "args": [0x707c, 4]
    },
    {
        "identifier": 'EVENT_560_store_00_to_0248_411',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_560_pause_412',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_clear_413',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 5, 'EVENT_560_action_queue_sync_414']
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_414',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_414_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_414_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_414_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_414_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_414_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_414_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_set_415',
        "command": 'set',
        "args": [0x70ae, 20]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_416',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_417',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_418',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [72]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [6, 24]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_walk_to_xy_coords_8',
                "command": 'walk_to_xy_coords',
                "args": [4, 20]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_418_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_set_bit_419',
        "command": 'set_bit',
        "args": [0x7056, 2]
    },
    {
        "identifier": 'EVENT_560_remove_one_from_inventory_420',
        "command": 'remove_one_from_inventory',
        "args": [items.BambinoBomb]
    },
    {
        "identifier": 'EVENT_560_ret_421',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_set_422',
        "command": 'set',
        "args": [0x70a7, 174]
    },
    {
        "identifier": 'EVENT_560_store_7000_item_quantity_to_70A7_423',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_560_jmp_if_var_equals_short_424',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_560_jmp_if_bit_set_435']
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_425',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 1, 'EVENT_560_run_dialog_433']
    },
    {
        "identifier": 'EVENT_560_run_dialog_426',
        "command": 'run_dialog',
        "args": [3300, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_427',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_560_ret_432']
    },
    {
        "identifier": 'EVENT_560_set_bit_428',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_560_apply_solidity_mod_429',
        "command": 'apply_solidity_mod',
        "args": [Rooms._104_GRATE_GUYS_CASINO_FRONT_DOOR, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_430',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_430_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_431',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_431_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_ret_432',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_run_dialog_433',
        "command": 'run_dialog',
        "args": [3301, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_ret_434',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_435',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 6, 'EVENT_560_run_dialog_438']
    },
    {
        "identifier": 'EVENT_560_run_dialog_436',
        "command": 'run_dialog',
        "args": [3298, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_ret_437',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_run_dialog_438',
        "command": 'run_dialog',
        "args": [3299, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_ret_439',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_stop_sound_440',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_560_stop_sound_441',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_560_stop_sound_442',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_560_stop_sound_443',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_560_stop_sound_444',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_560_ret_445',
        "command": 'ret'
    }
]
