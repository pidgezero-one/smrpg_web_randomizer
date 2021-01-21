from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_65_pause_script_if_menu_open_0',
        "command": 'pause_script_if_menu_open'
    },
    {
        "identifier": 'EVENT_65_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 0, 'EVENT_65_action_queue_sync_6']
    },
    {
        "identifier": 'EVENT_65_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_65_action_queue_sync_2_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_2_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_2_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_65_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_shift_z_down_pixels_7',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_shift_z_down_pixels_11',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_shift_z_down_pixels_14',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_sequence_playback_on_17',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_jump_to_height_silent_18',
                "command": 'jump_to_height_silent',
                "args": [256]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_floating_on_19',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_65_action_queue_async_3_SUBSCRIPT_set_vram_priority_20',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_65_pause_4',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_65_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_65_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_65_action_queue_sync_6_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_6_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_6_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_6_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_65_action_queue_sync_6_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_65_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_jump_to_height_silent_7',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_walk_1_step_south_10',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_65_action_queue_async_7_SUBSCRIPT_set_solidity_bits_11',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_65_enable_controls_8',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_65_remember_last_object_9',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_65_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_65_move_script_to_main_thread_11',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_65_end_all_12',
        "command": 'end_all'
    }
]
