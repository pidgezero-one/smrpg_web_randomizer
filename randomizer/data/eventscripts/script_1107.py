from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1107_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1107_action_queue_async_0_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_0_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_0_SUBSCRIPT_bounce_to_xy_with_height_2',
                "command": 'bounce_to_xy_with_height',
                "args": [12, 51, 0]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_0_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_0_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_0_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_1107_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_1107_set_7000_to_object_coord_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_7000_to_tapped_button_2',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_jmp_if_7000_any_bits_set_4',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1107_set_7000_to_pressed_button_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_1107_set_7000_to_tapped_button_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_7000_to_pressed_button_6',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_jmp_if_7000_any_bits_set_7',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 3], 'EVENT_1107_set_7000_to_object_coord_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_jmp_if_7000_any_bits_set_8',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1, 2], 'EVENT_1107_action_queue_async_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1107_action_queue_async_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_7000_to_object_coord_10',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 20, 'EVENT_1107_enable_controls_until_return_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_shadow_off_7',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_face_northeast_9',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_12_SUBSCRIPT_ret_11',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1107_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_1107_set_7000_to_tapped_button_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_shadow_on_2',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_shadow_off_10',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_14_SUBSCRIPT_ret_11',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1107_set_7000_to_object_coord_15',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 12, 'EVENT_1105_action_queue_sync_49'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_1107_set_7000_to_tapped_button_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1107_action_queue_async_18_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_18_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_18_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_18_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1107_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_1107_set_7000_to_tapped_button_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_enable_controls_until_return_20',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_async_21_SUBSCRIPT_ret_10',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1107_jmp_if_bit_clear_22',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 0, 'EVENT_1110_stop_sound_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1107_action_queue_sync_23_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_sync_23_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1107_action_queue_sync_23_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1107_action_queue_sync_23_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [22]
            },
            {
                "identifier": 'EVENT_1107_action_queue_sync_23_SUBSCRIPT_ret_4',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1107_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_25',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_27',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_29',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_31',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_33',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_35',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_37',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_pause_39',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_enable_controls_until_return_40',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_set_action_script_async_41',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_clear_bit_42',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1107_ret_43',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
