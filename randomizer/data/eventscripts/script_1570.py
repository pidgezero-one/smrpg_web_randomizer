from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1570_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a]
    },
    {
        "identifier": 'EVENT_1570_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7034, 0x7000]
    },
    {
        "identifier": 'EVENT_1570_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1570_disable_trigger_3',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1570_start_embedded_action_script_async_4',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1570_start_embedded_action_script_async_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1570_start_embedded_action_script_async_4_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1570_start_embedded_action_script_async_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1570_start_embedded_action_script_async_4_SUBSCRIPT_walk_1_step_west_3',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_1570_start_embedded_action_script_async_4_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1570_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1570_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_1570_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1570_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1570_pause_action_script_9',
        "command": 'pause_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_1570_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [72]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_set_short_mem_3',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7034]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_play_sound_8']
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 4]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_1570_action_queue_sync_11']
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_10_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1570_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1570_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_11_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_11_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1570_action_queue_sync_11_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1570_set_short_12',
        "command": 'set_short',
        "args": [0x700c, 0x0005]
    },
    {
        "identifier": 'EVENT_1570_start_loop_n_times_13',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1570_set_short_mem_14',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a]
    },
    {
        "identifier": 'EVENT_1570_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1570_pause_18']
    },
    {
        "identifier": 'EVENT_1570_create_packet_at_object_coords_jmp_if_null_16',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._017_SMALL_COIN_NOT_MOVING, AreaObjects.MARIO, 'EVENT_1570_pause_18']
    },
    {
        "identifier": 'EVENT_1570_dec_short_17',
        "command": 'dec_short',
        "args": [0x702a]
    },
    {
        "identifier": 'EVENT_1570_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1570_add_short_19',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'EVENT_1570_end_loop_20',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1570_pause_21',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1570_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1570_action_queue_async_22_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1570_resume_action_script_23',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1570_resume_action_script_24',
        "command": 'resume_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1570_resume_action_script_25',
        "command": 'resume_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_1570_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1570_ret_27',
        "command": 'ret'
    }
]
