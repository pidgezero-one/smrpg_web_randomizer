from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3625_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 17, 'EVENT_3625_jmp_if_present_in_current_level_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 325, 'EVENT_3625_jmp_if_present_in_current_level_64'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 114, 'EVENT_3625_jmp_if_present_in_current_level_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 498, 'EVENT_3625_jmp_if_present_in_current_level_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 499, 'EVENT_3625_jmp_if_present_in_current_level_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 97, 'EVENT_3625_jmp_if_present_in_current_level_75'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 98, 'EVENT_3625_jmp_if_present_in_current_level_86'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 87, 'EVENT_3625_jmp_if_present_in_current_level_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 33, 'EVENT_3625_jmp_if_present_in_current_level_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 125, 'EVENT_3625_jmp_if_present_in_current_level_117'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 9, 'EVENT_3625_jmp_if_present_in_current_level_127'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_12',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_0, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_14',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_15',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_16',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_17',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._344_NIMBUS_LAND_ITEM_SHOP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_18',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_19',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_20',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_play_sound_21',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_summon_to_current_level_22',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_24',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_25',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_4, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_26',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_27',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_28',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_29',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_30',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_4, Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_31',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_6, Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_32',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_33',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_34',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_35',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_36',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_37',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_38',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_39',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_40',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_41',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._498_NIMBUS_CASTLE_AREA_10_____DUMMY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_42',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_43',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_44',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_45',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_46',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_47',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_48',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_49',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_50',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._498_NIMBUS_CASTLE_AREA_10_____DUMMY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_51',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_52',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_53',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_54',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_0, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_55',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_56',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_57',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_58',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_59',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_60',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_61',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_62',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_63',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_64',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_6, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_65',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_66',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_67',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_68',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_69',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_70',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_4, Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_71',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_6, Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_72',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_73',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_74',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_75',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_2, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_76',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_77',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_78',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_79',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_80',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_81',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_2, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_82',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._098_ROSE_TOWN_TREASURE_HOUSE_2F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_83',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_84',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_85',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_86',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_87',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_88',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_89',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_90',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_91',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_92',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_2, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_93',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._098_ROSE_TOWN_TREASURE_HOUSE_2F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_94',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_95',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_96',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_97',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_5, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_98',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_99',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_100',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_101',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_102',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_103',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_5, Rooms._087_ROSE_TOWN_ITEM_SHOP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_104',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_105',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_106',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_107',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_108',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_109',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_110',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_111',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_112',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_113',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_114',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_115',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_116',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_117',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_10, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_118',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_119',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_120',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_121',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_122',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_123',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_10, Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_124',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_125',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_126',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_if_present_in_current_level_127',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_0, 'EVENT_3625_play_sound_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_jmp_to_subroutine_128',
        "command": 'jmp_to_subroutine',
        "args": [0x86f3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_set_129',
        "command": 'set',
        "args": [0x70a7, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_130',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_add_131',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_run_event_as_subroutine_132',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_disable_trigger_in_level_133',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._009_MARRYMORE_INN_REGULAR_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_remember_last_object_134',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_unfreeze_camera_135',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_ret_136',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_freeze_camera_137',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3625_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3625_action_queue_sync_138_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3625_action_queue_sync_138_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3625_action_queue_sync_138_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3625_action_queue_sync_138_SUBSCRIPT_shift_z_down_steps_3',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3625_ret_139',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
