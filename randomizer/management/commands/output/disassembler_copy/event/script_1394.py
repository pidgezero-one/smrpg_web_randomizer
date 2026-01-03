
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1394_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 0, 'EVENT_1394_run_dialog_19']
    },
    {
        "identifier": 'EVENT_1394_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1394_run_dialog_2',
        "command": 'run_dialog',
        "args": [2760, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1394_pause_3',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1394_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_face_southwest_7D_1',
                "command": 'face_southwest_7D',
                "args": [0x00]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_turn_clockwise_45_degrees_n_times_2',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_turn_clockwise_45_degrees_n_times_4',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_turn_clockwise_45_degrees_n_times_6',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_4_SUBSCRIPT_shift_f_direction_pixels_10',
                "command": 'shift_f_direction_pixels',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_1394_pause_5',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1394_run_dialog_6',
        "command": 'run_dialog',
        "args": [2761, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1394_pause_script_resume_on_next_dialog_page_a_FD61_7',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1394_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1394_action_queue_async_8_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_8_SUBSCRIPT_face_southwest_7D_1',
                "command": 'face_southwest_7D',
                "args": [0x00]
            },
            {
                "identifier": 'EVENT_1394_action_queue_async_8_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_1394_pause_script_resume_on_next_dialog_page_a_FD61_9',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1394_unsync_dialog_10',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1394_close_dialog_11',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1394_reset_coords_12',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1394_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1394_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 146]
    },
    {
        "identifier": 'EVENT_1394_set_bit_15',
        "command": 'set_bit',
        "args": [0x7053, 0]
    },
    {
        "identifier": 'EVENT_1394_set_bit_16',
        "command": 'set_bit',
        "args": [0x7065, 0]
    },
    {
        "identifier": 'EVENT_1394_set_bit_17',
        "command": 'set_bit',
        "args": [0x706d, 1]
    },
    {
        "identifier": 'EVENT_1394_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1394_run_dialog_19',
        "command": 'run_dialog',
        "args": [2762, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1394_ret_20',
        "command": 'ret'
    }
]
