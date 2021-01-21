from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1867_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1867_action_queue_async_0_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 25, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_0_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1867_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7095, 5, 'EVENT_1867_jmp_to_event_7']
    },
    {
        "identifier": 'EVENT_1867_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7095, 3, 'EVENT_1867_jmp_to_event_7']
    },
    {
        "identifier": 'EVENT_1867_fade_in_from_black_sync_3',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1867_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 28, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1867_action_queue_async_4_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1867_set_bit_5',
        "command": 'set_bit',
        "args": [0x7095, 5]
    },
    {
        "identifier": 'EVENT_1867_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1867_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [15]
    }
]
