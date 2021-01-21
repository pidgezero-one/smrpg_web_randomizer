from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1919_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1919_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6]
    },
    {
        "identifier": 'EVENT_1919_jmp_if_var_equals_byte_2',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 21, 'EVENT_1919_action_queue_async_7']
    },
    {
        "identifier": 'EVENT_1919_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1919_action_queue_async_3_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1919_action_queue_async_3_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1919_action_queue_async_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1919_action_queue_async_3_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1919_jmp_to_subroutine_4',
        "command": 'jmp_to_subroutine',
        "args": [0x6513]
    },
    {
        "identifier": 'EVENT_1919_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1919_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1919_action_queue_sync_5_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1919_action_queue_sync_5_SUBSCRIPT_object_memory_clear_bit_2',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1919_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1919_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1919_action_queue_async_7_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1919_action_queue_async_7_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1919_action_queue_async_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1919_action_queue_async_7_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1919_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": [0x6513]
    },
    {
        "identifier": 'EVENT_1919_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1919_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1919_action_queue_sync_9_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1919_action_queue_sync_9_SUBSCRIPT_object_memory_clear_bit_2',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1919_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1919_enable_controls_until_return_11',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1919_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1919_jmp_if_mario_in_air_13',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1919_ret_15']
    },
    {
        "identifier": 'EVENT_1919_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_1919_pause_12']
    },
    {
        "identifier": 'EVENT_1919_ret_15',
        "command": 'ret'
    }
]
