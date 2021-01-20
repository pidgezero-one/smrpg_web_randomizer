from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1692_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7050, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_short_2',
        "command": 'set_short',
        "args": [0x7034, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_7010_to_object_xyz_3',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_pause_5',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_create_packet_at_7010_coords_jmp_if_null_6',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1692_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_pause_7',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_add_short_8',
        "command": 'add_short',
        "args": [0x7034, 0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_end_loop_9',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_remove_from_level_11',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_remove_from_level_13',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_disable_trigger_in_level_15',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_6, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_disable_trigger_in_level_16',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_7, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_disable_trigger_in_level_17',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_8, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_disable_trigger_in_level_18',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_9, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_run_dialog_19',
        "command": 'run_dialog',
        "args": [1249, AreaObjects.BOWSER, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_short_mem_20',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_mem_7000_and_const_21',
        "command": 'mem_7000_and_const',
        "args": [0x000f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_var_equals_short_22',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 9, 'EVENT_1692_run_dialog_duration_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_var_equals_short_23',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 13, 'EVENT_1692_run_dialog_duration_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_1692_run_dialog_duration_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_var_equals_short_25',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 14, 'EVENT_1692_run_dialog_duration_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_var_equals_short_26',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_1692_run_dialog_duration_56'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_var_equals_short_27',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 11, 'EVENT_1692_run_dialog_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_run_dialog_duration_28',
        "command": 'run_dialog_duration',
        "args": [1242, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_ret_29',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_run_dialog_duration_30',
        "command": 'run_dialog_duration',
        "args": [1243, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_short_mem_31',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_add_32',
        "command": 'add',
        "args": [0x7000, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_random_33',
        "command": 'set_random',
        "args": [0x702a, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_mem_compare_34',
        "command": 'mem_compare',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_comparison_result_is_lesser_35',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1692_summon_to_level_40'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_summon_to_level_36',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_enable_trigger_in_level_37',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_6, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_run_dialog_duration_39',
        "command": 'run_dialog_duration',
        "args": [1244, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_summon_to_level_40',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_enable_trigger_in_level_41',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_7, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_ret_42',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_run_dialog_duration_43',
        "command": 'run_dialog_duration',
        "args": [1245, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_summon_to_level_44',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_summon_to_level_45',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_summon_to_level_46',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_ret_47',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_run_dialog_duration_48',
        "command": 'run_dialog_duration',
        "args": [1246, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_short_mem_49',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_add_50',
        "command": 'add',
        "args": [0x7000, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_random_51',
        "command": 'set_random',
        "args": [0x702a, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_mem_compare_52',
        "command": 'mem_compare',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_comparison_result_is_lesser_53',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1692_summon_to_level_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_summon_to_level_54',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_ret_55',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_run_dialog_duration_56',
        "command": 'run_dialog_duration',
        "args": [1247, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_short_mem_57',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ad],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_add_58',
        "command": 'add',
        "args": [0x7000, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_set_random_59',
        "command": 'set_random',
        "args": [0x702a, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_mem_compare_60',
        "command": 'mem_compare',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_jmp_if_comparison_result_is_lesser_61',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1692_summon_to_level_66'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_summon_to_level_62',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_enable_trigger_in_level_63',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_8, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_ret_64',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_run_dialog_duration_65',
        "command": 'run_dialog_duration',
        "args": [1248, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_summon_to_level_66',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_enable_trigger_in_level_67',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_9, Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1692_ret_68',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
