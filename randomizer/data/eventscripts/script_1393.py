from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1393_set_bit_0',
        "command": 'set_bit',
        "args": [0x7052, 2]
    },
    {
        "identifier": 'EVENT_1393_set_bit_1',
        "command": 'set_bit',
        "args": [0x7053, 0]
    },
    {
        "identifier": 'EVENT_1393_set_bit_2',
        "command": 'set_bit',
        "args": [0x7053, 1]
    },
    {
        "identifier": 'EVENT_1393_set_bit_3',
        "command": 'set_bit',
        "args": [0x7053, 2]
    },
    {
        "identifier": 'EVENT_1393_set_bit_4',
        "command": 'set_bit',
        "args": [0x7053, 3]
    },
    {
        "identifier": 'EVENT_1393_set_bit_5',
        "command": 'set_bit',
        "args": [0x7065, 0]
    },
    {
        "identifier": 'EVENT_1393_set_bit_6',
        "command": 'set_bit',
        "args": [0x7065, 1]
    },
    {
        "identifier": 'EVENT_1393_set_bit_7',
        "command": 'set_bit',
        "args": [0x7065, 2]
    },
    {
        "identifier": 'EVENT_1393_set_bit_8',
        "command": 'set_bit',
        "args": [0x7065, 3]
    },
    {
        "identifier": 'EVENT_1393_set_bit_9',
        "command": 'set_bit',
        "args": [0x7068, 3]
    },
    {
        "identifier": 'EVENT_1393_set_bit_10',
        "command": 'set_bit',
        "args": [0x706d, 1]
    },
    {
        "identifier": 'EVENT_1393_set_bit_11',
        "command": 'set_bit',
        "args": [0x706d, 2]
    },
    {
        "identifier": 'EVENT_1393_set_bit_12',
        "command": 'set_bit',
        "args": [0x7070, 3]
    },
    {
        "identifier": 'EVENT_1393_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7056, 6]
    },
    {
        "identifier": 'EVENT_1393_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7056, 7]
    },
    {
        "identifier": 'EVENT_1393_join_party_15',
        "command": 'join_party',
        "args": [AreaObjects.DUMMY_0X05]
    },
    {
        "identifier": 'EVENT_1393_leave_party_16',
        "command": 'leave_party',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1393_join_party_17',
        "command": 'join_party',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1393_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_20',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_21',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_leave_party_22',
        "command": 'leave_party',
        "args": [AreaObjects.DUMMY_0X05]
    },
    {
        "identifier": 'EVENT_1393_put_inventory_23',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_1393_put_inventory_24',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_1393_put_inventory_25',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_1393_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_sync_26_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 13, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_26_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_26_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_26_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_26_SUBSCRIPT_ret_4',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_stop_sound_27',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_music_FDA2_28',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_1393_pause_action_script_29',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1393_jmp_if_bit_set_30',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 5, 'EVENT_1393_set_bit_32']
    },
    {
        "identifier": 'EVENT_1393_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_1393_enter_area_178']
    },
    {
        "identifier": 'EVENT_1393_set_bit_32',
        "command": 'set_bit',
        "args": [0x7070, 2]
    },
    {
        "identifier": 'EVENT_1393_set_bit_33',
        "command": 'set_bit',
        "args": [0x7070, 7]
    },
    {
        "identifier": 'EVENT_1393_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_1393_enter_area_178']
    },
    {
        "identifier": 'EVENT_1393_ret_35',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1393_stop_music_36',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_37',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_38',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_39',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_40',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_41',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_42',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_43',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_44',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_45',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_46',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_47',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_48',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_49',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_50',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_51',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_52',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_53',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_54',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_55',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_56',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_57',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_58',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_59',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_60',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_61',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_62',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_63',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_64',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_65',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_66',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_67',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_68',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_69',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_70',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_71',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_72',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_73',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_74',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_75',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_76',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_77',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_78',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_79',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_80',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_81',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_82',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_83',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_84',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_85',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_86',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_87',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_88',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_89',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_90',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_91',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_92',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_93',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_94',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_95',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_96',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_97',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_98',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_99',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_100',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_101',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_102',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_103',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_104',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_105',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_106',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_107',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_108',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_109',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_110',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_111',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_112',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_113',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_114',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_115',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_116',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_117',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_118',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_119',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_120',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_121',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_122',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_123',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_124',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_125',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_126',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_127',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_128',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_129',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_130',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_131',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_132',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_133',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_134',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_135',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_136',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_137',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_138',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_139',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_140',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_141',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_142',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_143',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_144',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_145',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_146',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_147',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_148',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_149',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_150',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_151',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_152',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_153',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_154',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_155',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_156',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_157',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_158',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_159',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_160',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_161',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_162',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_163',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_164',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_165',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_166',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_167',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_168',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_169',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_170',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_171',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_172',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_173',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_174',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_175',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_176',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_stop_music_177',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1393_enter_area_178',
        "command": 'enter_area',
        "args": [Rooms._189_MARIOS_PIPEHOUSE, RadialDirections.SOUTHEAST, 3, 13, 0, []]
    },
    {
        "identifier": 'EVENT_1393_palette_set_179',
        "command": 'palette_set',
        "args": [33, 7, [0]]
    },
    {
        "identifier": 'EVENT_1393_stop_music_FDA2_180',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_181',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_181_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_181_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 9, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_181_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_181_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_181_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_181_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_181_SUBSCRIPT_shadow_off_6',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_182',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_182_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_182_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_182_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_set_action_script_sync_183',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 95]
    },
    {
        "identifier": 'EVENT_1393_freeze_camera_184',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_185',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_185_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_fade_in_from_black_async_186',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1393_set_bit_187',
        "command": 'set_bit',
        "args": [0x7056, 4]
    },
    {
        "identifier": 'EVENT_1393_jmp_188',
        "command": 'jmp',
        "args": ['EVENT_1393_play_music_default_volume_242']
    },
    {
        "identifier": 'EVENT_1393_stop_sound_189',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_190',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_191',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_192',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_193',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_194',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_195',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_196',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_197',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_198',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_199',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_200',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_201',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_202',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_203',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_204',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_205',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_206',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_207',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_208',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_209',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_210',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_211',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_212',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_213',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_214',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_215',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_216',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_217',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_218',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_219',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_220',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_221',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_222',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_223',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_224',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_225',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_226',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_227',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_228',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_229',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_230',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_231',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_232',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_233',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_234',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_235',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_236',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_237',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_238',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_239',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_240',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_stop_sound_241',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1393_play_music_default_volume_242',
        "command": 'play_music_default_volume',
        "args": [Music._14_MARIOS_PAD]
    },
    {
        "identifier": 'EVENT_1393_pause_243',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1393_set_7000_to_tapped_button_244',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1393_pause_245',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1393_mem_7000_and_const_246',
        "command": 'mem_7000_and_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_1393_jmp_if_7000_equals_short_247',
        "command": 'jmp_if_7000_equals_short',
        "args": [128, 'EVENT_1393_pause_action_script_249']
    },
    {
        "identifier": 'EVENT_1393_jmp_248',
        "command": 'jmp',
        "args": ['EVENT_1393_set_7000_to_tapped_button_244']
    },
    {
        "identifier": 'EVENT_1393_pause_action_script_249',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_250',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_shadow_on_4',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [69]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_stop_sound_15',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_250_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_pause_251',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1393_remove_from_level_252',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._396_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_2F]
    },
    {
        "identifier": 'EVENT_1393_ret_253',
        "command": 'ret'
    }
]
