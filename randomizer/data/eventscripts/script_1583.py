from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1583_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_1583_action_queue_sync_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1583_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1583_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._319_LANDS_END_DESERT_AREA_06, RadialDirections.SOUTH, 8, 110, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1583_set_3',
        "command": 'set',
        "args": [0x70a8, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1583_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [1545],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1583_jmp_to_event_5',
        "command": 'jmp_to_event',
        "args": [1783],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1583_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1583_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_sync_6_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_sync_6_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_1583_action_queue_sync_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_sync_6_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_1583_action_queue_sync_6_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1583_action_queue_sync_6_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1583_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_shift_z_down_pixels_6',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_shift_z_down_pixels_8',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_shift_z_down_pixels_10',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_shift_z_down_pixels_13',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_sequence_playback_on_16',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_jump_to_height_silent_17',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_solidity_bits_18',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_set_vram_priority_19',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_walk_1_step_south_20',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1583_action_queue_async_7_SUBSCRIPT_jmp_if_mario_in_air_22',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1583_action_queue_async_7_SUBSCRIPT_pause_21']
            }
        ]
    },
    {
        "identifier": 'EVENT_1583_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
