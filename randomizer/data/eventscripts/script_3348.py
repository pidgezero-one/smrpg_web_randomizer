from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3348_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3348_action_queue_sync_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3348_action_queue_sync_0_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3348_action_queue_sync_0_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3348_action_queue_sync_0_SUBSCRIPT_shift_z_down_steps_3',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3348_action_queue_sync_0_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3348_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_mem_7000_and_const_2',
        "command": 'mem_7000_and_const',
        "args": [0x0007],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_add_3',
        "command": 'add',
        "args": [0x7000, 512],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_dec_4',
        "command": 'dec',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_set_mem_704x_at_7000_bit_5',
        "command": 'set_mem_704x_at_7000_bit',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 513, 'EVENT_3348_set_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 514, 'EVENT_3348_set_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 515, 'EVENT_3348_set_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 516, 'EVENT_3348_set_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 517, 'EVENT_3348_set_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_set_11',
        "command": 'set',
        "args": [0x70a7, 32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_3348_run_event_as_subroutine_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_set_13',
        "command": 'set',
        "args": [0x70a7, 29],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_3348_run_event_as_subroutine_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_set_15',
        "command": 'set',
        "args": [0x70a7, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3348_run_event_as_subroutine_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_set_17',
        "command": 'set',
        "args": [0x70a7, 31],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3348_run_event_as_subroutine_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_set_19',
        "command": 'set',
        "args": [0x70a7, 131],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3348_run_event_as_subroutine_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_set_21',
        "command": 'set',
        "args": [0x70a7, 131],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_run_event_as_subroutine_22',
        "command": 'run_event_as_subroutine',
        "args": [33],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_set_23',
        "command": 'set',
        "args": [0x7000, 1586],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_run_event_as_subroutine_24',
        "command": 'run_event_as_subroutine',
        "args": [3829],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3348_ret_25',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
