from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3074_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_1',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 240, 'EVENT_3074_play_sound_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_disable_event_trigger_for_object_at_70A8_2',
        "command": 'disable_event_trigger_for_object_at_70A8',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_mem_7000_and_const_6',
        "command": 'mem_7000_and_const',
        "args": [0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x70b4, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_add_8',
        "command": 'add',
        "args": [0x7000, 288],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_mem_704x_at_7000_bit_set_9',
        "command": 'jmp_if_mem_704x_at_7000_bit_set',
        "args": ['EVENT_3074_jmp_if_var_equals_byte_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_mem_704x_at_7000_bit_10',
        "command": 'set_mem_704x_at_7000_bit',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_mem_7000_and_const_12',
        "command": 'mem_7000_and_const',
        "args": [0x000f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_13',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 1, 'EVENT_3074_set_short_mem_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_14',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 2, 'EVENT_3074_set_short_mem_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_15',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 3, 'EVENT_3074_set_short_mem_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x70da, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_3074_jmp_if_var_equals_byte_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x70db, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_3074_jmp_if_var_equals_byte_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_20',
        "command": 'set_short_mem',
        "args": [0x70dc, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_3074_jmp_if_var_equals_byte_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x70dd, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_23',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 1, 'EVENT_3074_jmp_if_var_not_equals_byte_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_24',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 2, 'EVENT_3074_jmp_if_var_not_equals_byte_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_25',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 3, 'EVENT_3074_jmp_if_var_not_equals_byte_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_not_equals_byte_26',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70da, 1, 'EVENT_3074_set_temp_action_script_sync_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3074_set_action_script_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_not_equals_byte_28',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70db, 1, 'EVENT_3074_set_temp_action_script_sync_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_3074_set_action_script_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_not_equals_byte_30',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70dc, 1, 'EVENT_3074_set_temp_action_script_sync_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_3074_set_action_script_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_not_equals_byte_32',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70dd, 1, 'EVENT_3074_set_temp_action_script_sync_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_3074_set_7010_to_object_xyz_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_temp_action_script_sync_35',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_7010_to_object_xyz_36',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70AA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_37',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_add_38',
        "command": 'add',
        "args": [0x7000, 608],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_39',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_short_mem_40',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_mem_7000_and_const_41',
        "command": 'mem_7000_and_const',
        "args": [0x00f0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_short_42',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 240, 'EVENT_3074_play_sound_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_short_43',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 160, 'EVENT_3074_play_sound_46'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_short_44',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_3074_play_sound_61'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_play_sound_46',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_create_packet_at_7010_coords_jmp_if_null_47',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._016_BIG_COIN, 'EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_action_script_sync_48',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 906],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_add_coins_49',
        "command": 'add_coins',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_50',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 1, 'EVENT_3074_dec_55'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_51',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 2, 'EVENT_3074_dec_57'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_52',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 3, 'EVENT_3074_dec_59'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_dec_53',
        "command": 'dec',
        "args": [0x70da],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_54',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_dec_55',
        "command": 'dec',
        "args": [0x70db],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_56',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_dec_57',
        "command": 'dec',
        "args": [0x70dc],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_58',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_dec_59',
        "command": 'dec',
        "args": [0x70dd],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_60',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_play_sound_61',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_create_packet_at_7010_coords_jmp_if_null_62',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._018_SMALL_COIN, 'EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 906],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_add_coins_64',
        "command": 'add_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_65',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 1, 'EVENT_3074_dec_70'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_66',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 2, 'EVENT_3074_dec_72'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_if_var_equals_byte_67',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 3, 'EVENT_3074_dec_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_dec_68',
        "command": 'dec',
        "args": [0x70da],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_dec_70',
        "command": 'dec',
        "args": [0x70db],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_71',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_dec_72',
        "command": 'dec',
        "args": [0x70dc],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_73',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_dec_74',
        "command": 'dec',
        "args": [0x70dd],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_play_sound_76',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_create_packet_at_7010_coords_jmp_if_null_77',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._018_SMALL_COIN, 'EVENT_3074_ret_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_set_action_script_sync_78',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 906],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_add_coins_79',
        "command": 'add_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3074_ret_80',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
