from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3124_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_3124_ret_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 5, 'EVENT_3124_jmp_to_event_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3124_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3124_action_queue_sync_2_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3124_action_queue_sync_2_SUBSCRIPT_shift_z_down_steps_2',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3124_action_queue_sync_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3124_set_short_3',
        "command": 'set_short',
        "args": [0x700e, 0x009c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [35],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7064, 5, 'EVENT_3124_ret_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_set_bit_6',
        "command": 'set_bit',
        "args": [0x7057, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_set_short_8',
        "command": 'set_short',
        "args": [0x700a, 0x00ca],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_stop_sound_10',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_stop_sound_11',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3124_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [34],
        "subscript": []
    }
]
