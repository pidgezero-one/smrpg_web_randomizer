from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1839_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [1840]
    },
    {
        "identifier": 'EVENT_1839_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1839_ret_7']
    },
    {
        "identifier": 'EVENT_1839_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1839_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_1839_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1839_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1839_action_queue_sync_4_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1839_action_queue_sync_4_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1839_action_queue_sync_4_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1839_action_queue_sync_4_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1839_pause_5',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_1839_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1839_action_queue_sync_6_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1839_action_queue_sync_6_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1839_action_queue_sync_6_SUBSCRIPT_jmp_2',
                "command": 'jmp',
                "args": ['EVENT_1839_non_embedded_action_queue_8']
            }
        ]
    },
    {
        "identifier": 'EVENT_1839_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1839_non_embedded_action_queue_8',
        "command": 'non_embedded_action_queue',
        "subscript": [
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_down_steps_3',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_up_steps_5',
                "command": 'shift_z_up_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_down_steps_7',
                "command": 'shift_z_down_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_up_steps_10',
                "command": 'shift_z_up_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_southwest_steps_11',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_northeast_steps_12',
                "command": 'shift_northeast_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_up_steps_13',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_down_steps_14',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_northwest_steps_15',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_down_steps_16',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_southeast_steps_17',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_up_steps_18',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_play_sound_19',
                "command": 'play_sound',
                "args": [Sounds._113_OPEN_CHAMBER_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_northwest_steps_22',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_down_steps_23',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_southwest_steps_24',
                "command": 'shift_southwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_shift_z_up_steps_25',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_play_sound_26',
                "command": 'play_sound',
                "args": [Sounds._113_OPEN_CHAMBER_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1839_non_embedded_action_queue_8_SUBSCRIPT_jmp_28',
                "command": 'jmp',
                "args": ['EVENT_1839_non_embedded_action_queue_8']
            }
        ]
    }
]
