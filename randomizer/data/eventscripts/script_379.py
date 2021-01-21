from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_379_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 0, 'EVENT_379_run_dialog_20']
    },
    {
        "identifier": 'EVENT_379_set_bit_1',
        "command": 'set_bit',
        "args": [0x7083, 0]
    },
    {
        "identifier": 'EVENT_379_set_2',
        "command": 'set',
        "args": [0x70a7, 85]
    },
    {
        "identifier": 'EVENT_379_set_3',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_379_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_379_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_379_stop_sound_6',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_379_stop_sound_7',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_379_stop_sound_8',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_379_stop_sound_9',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_379_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_379_pause_action_script_11',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_12_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_379_action_queue_async_12_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_379_action_queue_async_12_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_379_action_queue_async_13_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [27, 49]
            },
            {
                "identifier": 'EVENT_379_action_queue_async_13_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_379_action_queue_async_13_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_379_run_dialog_14',
        "command": 'run_dialog',
        "args": [2559, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_15_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_16_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_379_action_queue_async_16_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_17_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_379_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_379_action_queue_async_18_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_379_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_379_run_dialog_20',
        "command": 'run_dialog',
        "args": [655, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_379_ret_21',
        "command": 'ret'
    }
]
