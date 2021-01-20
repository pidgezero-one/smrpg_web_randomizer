from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3218_stop_all_background_events_0',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3218_jmp_if_bit_set_53'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_3218_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 6, 'EVENT_3218_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_4',
        "command": 'run_dialog',
        "args": [1659, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_bit_5',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3218_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_background_event_7',
        "command": 'run_background_event',
        "args": [3225, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_9',
        "command": 'run_dialog',
        "args": [1706, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_short_mem_10',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_11',
        "command": 'add',
        "args": [0x7000, 1701],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_12',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_short_mem_13',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_14',
        "command": 'add',
        "args": [0x7000, 1713],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_15',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_17',
        "command": 'add',
        "args": [0x7000, 1725],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_18',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_20',
        "command": 'add',
        "args": [0x7000, 1737],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_21',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_23',
        "command": 'add',
        "args": [0x7000, 1749],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_24',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_26',
        "command": 'add',
        "args": [0x7000, 1761],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_27',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_28',
        "command": 'run_dialog',
        "args": [1707, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_29',
        "command": 'set',
        "args": [0x70ac, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_bit_30',
        "command": 'set_bit',
        "args": [0x7042, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_var_not_equals_short_31',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 4, 'EVENT_3218_jmp_if_var_not_equals_short_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_32',
        "command": 'add',
        "args": [0x70ac, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_var_not_equals_short_33',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 2, 'EVENT_3218_jmp_if_var_not_equals_short_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_34',
        "command": 'add',
        "args": [0x70ac, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_var_not_equals_short_35',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 0, 'EVENT_3218_jmp_if_var_not_equals_short_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_36',
        "command": 'add',
        "args": [0x70ac, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_var_not_equals_short_37',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 2, 'EVENT_3218_jmp_if_var_not_equals_short_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_38',
        "command": 'add',
        "args": [0x70ac, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_var_not_equals_short_39',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 3, 'EVENT_3218_jmp_if_var_not_equals_short_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_40',
        "command": 'add',
        "args": [0x70ac, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_var_not_equals_short_41',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 0, 'EVENT_3218_jmp_if_var_not_equals_byte_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_add_42',
        "command": 'add',
        "args": [0x70ac, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_var_not_equals_byte_43',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70ac, 6, 'EVENT_3218_play_sound_56'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_play_sound_44',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 6, 'EVENT_3218_jmp_if_bit_set_59'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 351],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3218_action_queue_async_47_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3218_action_queue_async_47_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3218_action_queue_async_47_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3218_action_queue_async_47_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3218_play_sound_48',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_apply_solidity_mod_49',
        "command": 'apply_solidity_mod',
        "args": [Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_apply_tile_mod_50',
        "command": 'apply_tile_mod',
        "args": [Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_bit_51',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_bit_52',
        "command": 'set_bit',
        "args": [0x7042, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_bit_set_53',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 6, 'EVENT_3218_jmp_if_bit_set_59'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_dialog_54',
        "command": 'run_dialog',
        "args": [1660, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_ret_55',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_play_sound_56',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_run_background_event_57',
        "command": 'run_background_event',
        "args": [3225, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_ret_58',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_jmp_if_bit_set_59',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3218_ret_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_play_sound_60',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_apply_solidity_mod_61',
        "command": 'apply_solidity_mod',
        "args": [Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_apply_tile_mod_62',
        "command": 'apply_tile_mod',
        "args": [Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_bit_63',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_set_bit_64',
        "command": 'set_bit',
        "args": [0x7042, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3218_ret_65',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
