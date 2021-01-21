from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2445_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_2445_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_2445_fade_in_from_black_async_12']
    },
    {
        "identifier": 'EVENT_2445_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2445_freeze_camera_3',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2445_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2445_action_queue_async_4_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_4_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_4_SUBSCRIPT_face_south_2',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_4_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_4_SUBSCRIPT_sequence_playback_off_4',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_4_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2445_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2445_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2445_action_queue_async_6_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_6_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2445_action_queue_async_6_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_6_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_6_SUBSCRIPT_shadow_on_4',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_6_SUBSCRIPT_walk_1_step_south_5',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_6_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2445_action_queue_async_6_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2445_action_queue_async_6_SUBSCRIPT_pause_6']
            }
        ]
    },
    {
        "identifier": 'EVENT_2445_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2445_unfreeze_camera_8',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2445_enable_controls_until_return_9',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2445_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_2445_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2445_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2445_ret_13',
        "command": 'ret'
    }
]
