from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1672_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [1840],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1672_jmp_fork_mario_on_object_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_jmp_fork_mario_on_object_2',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1672_ret_3', 'EVENT_1672_play_sound_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1672_action_queue_sync_5_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1672_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1672_action_queue_sync_5_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1672_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1672_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_jmp_fork_mario_on_object_8',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1672_jmp_if_bit_set_10', 'EVENT_1672_ret_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1672_ret_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_1672_ret_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1672_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1672_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1672_action_queue_async_12_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1672_action_queue_async_12_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1672_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1672_action_queue_sync_13_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1672_action_queue_sync_13_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1672_action_queue_sync_13_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1672_action_queue_sync_13_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1672_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
