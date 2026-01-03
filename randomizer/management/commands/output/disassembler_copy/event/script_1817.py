
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1817_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1817_jmp_if_mario_in_air_1',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1817_pause_0']
    },
    {
        "identifier": 'EVENT_1817_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1817_set_7016_to_object_xyz_3',
        "command": 'set_7016_to_object_xyz',
        "args": [0x80]
    },
    {
        "identifier": 'EVENT_1817_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1817_action_queue_async_4_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._123_CHAIN_RUMBLING_NOISE, 4]
            },
            {
                "identifier": 'EVENT_1817_action_queue_async_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1817_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1817_action_queue_async_4_SUBSCRIPT_shift_z_down_steps_3',
                "command": 'shift_z_down_steps',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1817_action_queue_async_4_SUBSCRIPT_run_away_shift_4',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_1817_action_queue_async_4_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1817_action_queue_async_4_SUBSCRIPT_stop_sound_6',
                "command": 'stop_sound'
            }
        ]
    },
    {
        "identifier": 'EVENT_1817_set_5',
        "command": 'set',
        "args": [0x70ab, 21]
    },
    {
        "identifier": 'EVENT_1817_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1817_run_dialog_7',
        "command": 'run_dialog',
        "args": [1262, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1817_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1817_action_queue_sync_8_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._123_CHAIN_RUMBLING_NOISE, 4]
            },
            {
                "identifier": 'EVENT_1817_action_queue_sync_8_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1817_action_queue_sync_8_SUBSCRIPT_fade_out_sound_to_volume_2',
                "command": 'fade_out_sound_to_volume',
                "args": [3, 0]
            },
            {
                "identifier": 'EVENT_1817_action_queue_sync_8_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [24, 113]
            },
            {
                "identifier": 'EVENT_1817_action_queue_sync_8_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1817_action_queue_sync_8_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1817_action_queue_sync_8_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1817_action_queue_sync_8_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1817_set_9',
        "command": 'set',
        "args": [0x70ab, 0]
    },
    {
        "identifier": 'EVENT_1817_run_event_as_subroutine_10',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1817_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1817_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1817_ret_13',
        "command": 'ret'
    }
]
