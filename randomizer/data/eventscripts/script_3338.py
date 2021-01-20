from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3338_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 7, 'EVENT_3338_open_location_184'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._013_BARREL_VOLCANO_FALLING_INTO_VOLCANO, RadialDirections.SOUTH, 4, 48, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_stop_music_3',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_5_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [4, 54]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_5_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_set_short_6',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_7',
        "command": 'set_short',
        "args": [0x7026, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_8',
        "command": 'set_short',
        "args": [0x7028, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_9',
        "command": 'set_short',
        "args": [0x702a, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_10',
        "command": 'set_short',
        "args": [0x702c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_11',
        "command": 'set_short',
        "args": [0x7010, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_12',
        "command": 'set_short',
        "args": [0x7012, 0x002c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_13',
        "command": 'set_short',
        "args": [0x7014, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_db_14',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_15',
        "command": 'set',
        "args": [0x70af, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_create_packet_at_7010_coords_jmp_if_null_16',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._046_AXEM_RED_MINI, 'EVENT_3338_pause_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_17',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7034, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_add_20',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_create_packet_at_7010_coords_jmp_if_null_21',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._046_AXEM_RED_MINI, 'EVENT_3338_pause_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_22',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_24',
        "command": 'set_short_mem',
        "args": [0x7036, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_add_25',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_create_packet_at_7010_coords_jmp_if_null_26',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._046_AXEM_RED_MINI, 'EVENT_3338_pause_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_27',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x7038, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_add_30',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_create_packet_at_7010_coords_jmp_if_null_31',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._046_AXEM_RED_MINI, 'EVENT_3338_pause_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_32',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x703a, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_add_35',
        "command": 'add',
        "args": [0x70af, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_create_packet_at_7010_coords_jmp_if_null_36',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._046_AXEM_RED_MINI, 'EVENT_3338_pause_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_37',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_38',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_39',
        "command": 'set_short_mem',
        "args": [0x703c, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_fade_in_from_black_async_40',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_41',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [140]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_bpl_26_27_28_12',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_floating_off_13',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_42_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_pause_43',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_44',
        "command": 'set_short',
        "args": [0x7028, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_45',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_46',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7038],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_stop_sound_47',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_48',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_49',
        "command": 'jmp',
        "args": ['EVENT_3338_action_queue_sync_89'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_stop_sound_50',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_stop_sound_51',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_52_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_52_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_52_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_52_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_52_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_52_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_52_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_53',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_54',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_55_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_55_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_55_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_55_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_run_dialog_56',
        "command": 'run_dialog',
        "args": [1825, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_57',
        "command": 'set_short',
        "args": [0x7026, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_58',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_59',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7036],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_60',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_61_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_61_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_61_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_61_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_61_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_61_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_61_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_62',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_63',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_64_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_64_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_64_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_64_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_set_short_65',
        "command": 'set_short',
        "args": [0x702a, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_66',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_67',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_68',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_69_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_69_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_69_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_69_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_69_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_69_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_69_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_run_dialog_70',
        "command": 'run_dialog',
        "args": [1828, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_71',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_72',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_73_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_73_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_73_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_73_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_run_dialog_74',
        "command": 'run_dialog',
        "args": [1829, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_75',
        "command": 'set_short',
        "args": [0x702c, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_76',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_77',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_78',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_79_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_79_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_79_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_79_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_79_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_79_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_79_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_run_dialog_80',
        "command": 'run_dialog',
        "args": [1830, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_81',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_mem_82',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_83',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_83_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_83_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_83_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_83_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_run_dialog_84',
        "command": 'run_dialog',
        "args": [1831, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_85',
        "command": 'set_short',
        "args": [0x7026, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_86',
        "command": 'set_short',
        "args": [0x7028, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_87',
        "command": 'set_short',
        "args": [0x702a, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_88',
        "command": 'set_short',
        "args": [0x702c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_89_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_89_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_89_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_90',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_90_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x5b]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_90_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_90_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_action_queue_async_91',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_async_91_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [95]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_91_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_91_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_91_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_set_action_script_sync_92',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_2, 942],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_action_script_sync_93',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 942],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_94',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_95',
        "command": 'set_short',
        "args": [0x7026, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_96',
        "command": 'set_short',
        "args": [0x7028, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_97',
        "command": 'set_short',
        "args": [0x702a, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_98',
        "command": 'set_short',
        "args": [0x702c, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_99',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_100',
        "command": 'set',
        "args": [0x70ab, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_101_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_101_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_102_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_102_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_102_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_102_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_102_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_103_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_103_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_103_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_103_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_103_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_104',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_104_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_104_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [47]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_104_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_104_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_104_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_set_short_105',
        "command": 'set_short',
        "args": [0x7024, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_106',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_107',
        "command": 'set_short',
        "args": [0x7026, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_108',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_109',
        "command": 'set_short',
        "args": [0x7028, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_110',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_111',
        "command": 'set_short',
        "args": [0x702a, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_112',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_113',
        "command": 'set_short',
        "args": [0x702c, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_async_114',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_async_114_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_114_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_114_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_114_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_114_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x00, 0x03, 0xe8, 0xff]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_114_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_114_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_114_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_start_battle_115',
        "command": 'start_battle',
        "args": [0x00b6, 39],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_stop_music_116',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_117',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_118',
        "command": 'set_short',
        "args": [0x7026, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_119',
        "command": 'set_short',
        "args": [0x7028, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_120',
        "command": 'set_short',
        "args": [0x702a, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_121',
        "command": 'set_short',
        "args": [0x702c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_if_bit_set_122',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3338_reset_and_choose_game_186'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_bit_123',
        "command": 'set_bit',
        "args": [0x707d, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_restore_all_hp_124',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_restore_all_fp_125',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_play_sound_126',
        "command": 'play_sound',
        "args": [Sounds._091_TUMBLING_BOULDERS, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_stop_music_127',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_fade_in_from_black_async_128',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_129',
        "command": 'jmp',
        "args": ['EVENT_3338_pause_175'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_play_music_default_volume_130',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_131_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_131_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_131_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_131_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_131_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_131_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_132',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_132_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_132_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_132_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_132_SUBSCRIPT_jmp_if_bit_clear_3',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 0, 'EVENT_3338_action_queue_sync_132_SUBSCRIPT_shift_south_pixels_1']
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_action_queue_sync_133',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_sync_133_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_133_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3338_action_queue_sync_133_SUBSCRIPT_set_bit_2',
                "command": 'set_bit',
                "args": [0x7044, 0]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_set_random_134',
        "command": 'set_random',
        "args": [0x7010, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_random_135',
        "command": 'set_random',
        "args": [0x7012, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_add_short_136',
        "command": 'add_short',
        "args": [0x7012, 0x0020],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_137',
        "command": 'set_short',
        "args": [0x7014, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_db_138',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_screen_flashes_with_colour_139',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_140',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_create_packet_at_7010_coords_jmp_if_null_141',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, 'EVENT_3338_screen_flashes_with_colour_139'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_142',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_if_random_above_128_143',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_3338_set_random_134'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_random_144',
        "command": 'set_random',
        "args": [0x7010, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_random_145',
        "command": 'set_random',
        "args": [0x7012, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_add_short_146',
        "command": 'add_short',
        "args": [0x7012, 0x0020],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_147',
        "command": 'set_short',
        "args": [0x7014, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_db_148',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_create_packet_at_7010_coords_jmp_if_null_149',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._025_BLUE_CLOUD_SFX, 'EVENT_3338_screen_flashes_with_colour_139'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_150',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_if_random_above_128_151',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_3338_set_random_134'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_screen_flashes_with_colour_152',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_153',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_if_bit_clear_154',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 0, 'EVENT_3338_set_random_134'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_fade_out_sound_to_volume_155',
        "command": 'fade_out_sound_to_volume',
        "args": [4, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_156',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_play_music_default_volume_157',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_158',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_159',
        "command": 'set_short',
        "args": [0x7010, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_160',
        "command": 'set_short',
        "args": [0x7012, 0x0022],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_161',
        "command": 'set_short',
        "args": [0x7014, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_db_162',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_163',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_create_packet_at_7010_coords_jmp_if_null_164',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._048_STAR_PIECE_MINI, 'EVENT_3338_pause_163'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_165',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_if_bit_clear_166',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_3338_pause_165'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_167',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_play_music_default_volume_168',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_169',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_170',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_if_bit_clear_171',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 6, 'EVENT_3338_pause_170'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_172',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_run_star_piece_sequence_173',
        "command": 'run_star_piece_sequence',
        "args": [6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_run_dialog_174',
        "command": 'run_dialog',
        "args": [1839, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_pause_175',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_enter_area_176',
        "command": 'enter_area',
        "args": [Rooms._391_VOLCANO_POSTCD_AREA_04, RadialDirections.SOUTH, 4, 16, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_fade_in_from_black_async_177',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_set_short_178',
        "command": 'set_short',
        "args": [0x700a, 0x00df],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_jmp_to_event_179',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_action_queue_async_180',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3338_action_queue_async_180_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_180_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_180_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_180_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_180_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_180_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_180_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 6]
            },
            {
                "identifier": 'EVENT_3338_action_queue_async_180_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
        ]
    },
    {
        "identifier": 'EVENT_3338_pause_181',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_open_location_182',
        "command": 'open_location',
        "args": [Locations._050_BARREL_VOLCANO, [6, 7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_ret_183',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_open_location_184',
        "command": 'open_location',
        "args": [Locations._050_BARREL_VOLCANO, [6, 7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_ret_185',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3338_reset_and_choose_game_186',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
]
