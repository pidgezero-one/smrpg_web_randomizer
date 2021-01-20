from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1075_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 6, 'EVENT_1075_run_dialog_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7051, 6, 'EVENT_1075_run_dialog_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_2',
        "command": 'run_dialog',
        "args": [2732, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_set_bit_3',
        "command": 'set_bit',
        "args": [0x7051, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_pause_4',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_5',
        "command": 'run_dialog',
        "args": [2719, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_jmp_if_dialog_option_b_6',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1075_run_dialog_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_set_bit_7',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": [0xbc99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_9',
        "command": 'run_dialog',
        "args": [2720, AreaObjects.NPC_12, [_0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_pause_10',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_pause_script_resume_on_next_dialog_page_a_11',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_pause_12',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1075_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 32, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_13_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_13_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_13_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1075_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 81],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._040_TADPOLE_POND_STAFF_SO, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_pause_16',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_pause_script_resume_on_next_dialog_page_a_17',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_pause_18',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_unsync_dialog_19',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._040_TADPOLE_POND_STAFF_SO, 4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_visibility_on_10',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._041_TADPOLE_POND_STAFF_LA, 4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_visibility_off_18',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_shift_northwest_steps_19',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_visibility_on_20',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_play_sound_23',
                "command": 'play_sound',
                "args": [Sounds._042_TADPOLE_POND_STAFF_TI, 4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_24',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_20_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [50]
            },
        ]
    },
    {
        "identifier": 'EVENT_1075_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._040_TADPOLE_POND_STAFF_SO, 4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_shift_southeast_steps_15',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_visibility_on_16',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_play_sound_19',
                "command": 'play_sound',
                "args": [Sounds._039_TADPOLE_POND_STAFF_FA, 4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_visibility_off_24',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_shift_southeast_steps_25',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_visibility_on_26',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_play_sound_29',
                "command": 'play_sound',
                "args": [Sounds._038_TADPOLE_POND_STAFF_MI, 4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_21_SUBSCRIPT_pause_31',
                "command": 'pause',
                "args": [25]
            },
        ]
    },
    {
        "identifier": 'EVENT_1075_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._037_TADPOLE_POND_STAFF_RE, 4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_shift_southeast_steps_14',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_visibility_on_15',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_play_sound_18',
                "command": 'play_sound',
                "args": [Sounds._036_TADPOLE_POND_STAFF_DO, 4]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1075_action_queue_async_22_SUBSCRIPT_visibility_off_23',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1075_close_dialog_23',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_24',
        "command": 'run_dialog',
        "args": [2717, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_27',
        "command": 'run_dialog',
        "args": [2721, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_ret_28',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_29',
        "command": 'run_dialog',
        "args": [3063, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_jmp_if_dialog_option_b_or_c_30',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_1075_run_dialog_34', 'EVENT_1075_run_dialog_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_31',
        "command": 'run_dialog',
        "args": [3064, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_pause_32',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_1078_pause_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_34',
        "command": 'run_dialog',
        "args": [3065, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_ret_35',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_run_dialog_36',
        "command": 'run_dialog',
        "args": [2721, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1075_ret_37',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
