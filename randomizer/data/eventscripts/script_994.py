from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_994_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._244_GAME_INTRO_YOSTER_ISLE_TALK_TO_YOSHI__RUN_AROUND, RadialDirections.SOUTHWEST, 16, 64, 0, []]
    },
    {
        "identifier": 'EVENT_994_fade_in_from_black_sync_1',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_994_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_994_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_994_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_994_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_994_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_994_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_994_action_queue_async_6_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_994_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [110]
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_floating_off_4',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [5, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_dec_z_coord_1_step_9',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_994_action_queue_async_7_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_994_move_script_to_main_thread_8',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_994_db_9',
        "command": 'db',
        "args": [0xfd, 0x45]
    },
    {
        "identifier": 'EVENT_994_pause_action_script_10',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_994_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [5, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [5, 6, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 6, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_8',
                "command": 'shift_northeast_steps',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_994_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_994_action_queue_sync_12_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_12_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, []]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_12_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_12_SUBSCRIPT_shift_south_steps_3',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_12_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_12_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_994_action_queue_sync_12_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_994_pause_13',
        "command": 'pause',
        "args": [190]
    },
    {
        "identifier": 'EVENT_994_fade_out_to_black_sync_duration_14',
        "command": 'fade_out_to_black_sync_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_994_pause_script_until_effect_done_15',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_994_jmp_to_event_16',
        "command": 'jmp_to_event',
        "args": [139]
    }
]
