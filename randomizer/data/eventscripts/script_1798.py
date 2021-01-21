from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1798_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704f, 4, 'EVENT_1798_run_dialog_4']
    },
    {
        "identifier": 'EVENT_1798_run_dialog_1',
        "command": 'run_dialog',
        "args": [1284, AreaObjects.MARIO, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1798_set_bit_2',
        "command": 'set_bit',
        "args": [0x704f, 4]
    },
    {
        "identifier": 'EVENT_1798_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_1798_run_dialog_duration_5']
    },
    {
        "identifier": 'EVENT_1798_run_dialog_4',
        "command": 'run_dialog',
        "args": [1285, AreaObjects.MARIO, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1798_run_dialog_duration_5',
        "command": 'run_dialog_duration',
        "args": [1234, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1798_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1798_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1798_action_queue_async_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1798_action_queue_async_6_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1798_action_queue_async_6_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1798_action_queue_async_6_SUBSCRIPT_shift_south_steps_4',
                "command": 'shift_south_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1798_action_queue_async_6_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1798_action_queue_async_6_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1798_action_queue_async_6_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1798_ret_7',
        "command": 'ret'
    }
]
