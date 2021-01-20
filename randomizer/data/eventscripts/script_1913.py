from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1913_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1913_ret_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1913_ret_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_set_7016_to_object_xyz_4',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_add_short_5',
        "command": 'add_short',
        "args": [0x701a, 0x0800],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_set_7000_to_pressed_button_6',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_if_7000_all_bits_clear_7',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[0, 1, 2, 3], 'EVENT_1913_action_queue_sync_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_set_7000_to_pressed_button_8',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_if_7000_any_bits_set_9',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[6], 'EVENT_1913_set_7000_to_object_coord_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_set_bit_10',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_set_7000_to_object_coord_11',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_1913_add_short_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_1913_add_short_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1913_add_short_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_add_short_15',
        "command": 'add_short',
        "args": [0x7016, 0xff40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_add_short_16',
        "command": 'add_short',
        "args": [0x7018, 0x00c0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_1913_action_queue_sync_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_add_short_18',
        "command": 'add_short',
        "args": [0x7018, 0xfe80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_1913_action_queue_sync_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_add_short_20',
        "command": 'add_short',
        "args": [0x7016, 0x0180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_add_short_21',
        "command": 'add_short',
        "args": [0x7018, 0xff40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_1913_action_queue_sync_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_add_short_23',
        "command": 'add_short',
        "args": [0x7016, 0x0180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1913_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_jmp_if_bit_clear_0',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 2, 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_db_2']
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_object_memory_clear_bit_3',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._078_CLICK, 4]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_floating_off_6',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_shift_z_down_steps_8',
                "command": 'shift_z_down_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_object_memory_set_bit_9',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_visibility_on_11',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_end_loop_15',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_1913_action_queue_sync_24_SUBSCRIPT_clear_bit_16',
                "command": 'clear_bit',
                "args": [0x7043, 0]
            },
        ]
    },
    {
        "identifier": 'EVENT_1913_ret_25',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
