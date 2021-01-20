from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1698_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_sync_0_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_sync_1_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_async_2_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_set_3',
        "command": 'set',
        "args": [0x70ab, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.MEM_70AB, Rooms._078_BANDITS_WAY_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 474],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_7',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70AB],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_add_9',
        "command": 'add',
        "args": [0x70ab, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_end_loop_10',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_sync_11_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_async_12_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_set_short_13',
        "command": 'set_short',
        "args": [0x702c, 0x001a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_set_14',
        "command": 'set',
        "args": [0x70a9, 26],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_set_15',
        "command": 'set',
        "args": [0x70aa, 27],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_async_16_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_16_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0x24, 0x11, 0x12]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_16_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x702a, 0x700c]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_pause_action_script_17',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 479],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_19',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 653],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_run_background_event_21',
        "command": 'run_background_event',
        "args": [1699, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_jmp_if_bit_clear_22',
        "command": 'jmp_if_bit_clear',
        "args": [0x7077, 3, 'EVENT_1698_action_queue_async_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_23',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_24',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_25',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_26',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_run_event_as_subroutine_27',
        "command": 'run_event_as_subroutine',
        "args": [14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_28',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_action_script_29',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_ret_30',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_async_31_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_sync_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_32_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_32_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_32_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_sync_33_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_33_SUBSCRIPT_walk_1_step_north_1',
                "command": 'walk_1_step_north',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_33_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_set_bit_34',
        "command": 'set_bit',
        "args": [0x7077, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_run_event_as_subroutine_35',
        "command": 'run_event_as_subroutine',
        "args": [14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_action_script_36',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_sync_37_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_37_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_37_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_37_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_37_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_37_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_37_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_sync_37_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_pause_38',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_start_loop_n_times_39',
        "command": 'start_loop_n_times',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_action_script_40',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_async_41_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_41_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_41_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [27]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_42',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_43',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_end_loop_44',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_pause_action_script_45',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_shift_east_pixels_4',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_shadow_on_5',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_shift_east_pixels_6',
                "command": 'shift_east_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x20, 0xf7]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_46_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_1698_action_queue_async_49'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_async_48_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_48_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_48_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_48_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_48_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_48_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_48_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_async_49_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_49_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_49_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_49_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_49_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_49_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_49_SUBSCRIPT_shift_east_steps_6',
                "command": 'shift_east_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1698_action_queue_async_49_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1698_action_queue_sync_50_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_51',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_52',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_53',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_resume_action_script_54',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_stop_sound_55',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_stop_sound_56',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_stop_sound_57',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1698_ret_58',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
