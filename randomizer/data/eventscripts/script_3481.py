from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3481_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3481_pause_1',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_3481_set_7000_to_object_coord_2',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3481_mem_7000_and_const_3',
        "command": 'mem_7000_and_const',
        "args": [0xff00]
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4352, 'EVENT_3481_set_7000_to_object_coord_9']
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7680, 'EVENT_3481_set_7000_to_object_coord_16']
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 10496, 'EVENT_3481_set_7000_to_object_coord_31']
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 14848, 'EVENT_3481_set_7000_to_object_coord_38']
    },
    {
        "identifier": 'EVENT_3481_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3481_pause_1']
    },
    {
        "identifier": 'EVENT_3481_set_7000_to_object_coord_9',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3481_mem_7000_and_const_10',
        "command": 'mem_7000_and_const',
        "args": [0xff00]
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_not_equals_short_11',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 4352, 'EVENT_3481_pause_1']
    },
    {
        "identifier": 'EVENT_3481_jmp_to_subroutine_12',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3481_pause_action_script_45']
    },
    {
        "identifier": 'EVENT_3481_db_13',
        "command": 'db',
        "args": [0xfd, 0x47]
    },
    {
        "identifier": 'EVENT_3481_enter_area_14',
        "command": 'enter_area',
        "args": [Rooms._070_MIDAS_RIVER_1ST_TUNNEL, RadialDirections.SOUTHEAST, 4, 24, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3481_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3481_set_7000_to_object_coord_16',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3481_mem_7000_and_const_17',
        "command": 'mem_7000_and_const',
        "args": [0xff00]
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3072, 'EVENT_3481_clear_bit_21']
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4608, 'EVENT_3481_set_bit_26']
    },
    {
        "identifier": 'EVENT_3481_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3481_pause_1']
    },
    {
        "identifier": 'EVENT_3481_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x7078, 3]
    },
    {
        "identifier": 'EVENT_3481_jmp_to_subroutine_22',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3481_pause_action_script_45']
    },
    {
        "identifier": 'EVENT_3481_db_23',
        "command": 'db',
        "args": [0xfd, 0x47]
    },
    {
        "identifier": 'EVENT_3481_enter_area_24',
        "command": 'enter_area',
        "args": [Rooms._071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT, RadialDirections.SOUTHEAST, 3, 57, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3481_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3481_set_bit_26',
        "command": 'set_bit',
        "args": [0x7078, 3]
    },
    {
        "identifier": 'EVENT_3481_jmp_to_subroutine_27',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3481_pause_action_script_45']
    },
    {
        "identifier": 'EVENT_3481_db_28',
        "command": 'db',
        "args": [0xfd, 0x47]
    },
    {
        "identifier": 'EVENT_3481_enter_area_29',
        "command": 'enter_area',
        "args": [Rooms._071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT, RadialDirections.SOUTHEAST, 16, 67, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3481_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3481_set_7000_to_object_coord_31',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3481_mem_7000_and_const_32',
        "command": 'mem_7000_and_const',
        "args": [0xff00]
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_not_equals_short_33',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 2048, 'EVENT_3481_pause_1']
    },
    {
        "identifier": 'EVENT_3481_jmp_to_subroutine_34',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3481_pause_action_script_45']
    },
    {
        "identifier": 'EVENT_3481_db_35',
        "command": 'db',
        "args": [0xfd, 0x47]
    },
    {
        "identifier": 'EVENT_3481_enter_area_36',
        "command": 'enter_area',
        "args": [Rooms._072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT, RadialDirections.SOUTHEAST, 28, 25, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3481_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3481_set_7000_to_object_coord_38',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3481_mem_7000_and_const_39',
        "command": 'mem_7000_and_const',
        "args": [0xff00]
    },
    {
        "identifier": 'EVENT_3481_jmp_if_var_not_equals_short_40',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 6912, 'EVENT_3481_pause_1']
    },
    {
        "identifier": 'EVENT_3481_jmp_to_subroutine_41',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3481_pause_action_script_45']
    },
    {
        "identifier": 'EVENT_3481_db_42',
        "command": 'db',
        "args": [0xfd, 0x47]
    },
    {
        "identifier": 'EVENT_3481_enter_area_43',
        "command": 'enter_area',
        "args": [Rooms._073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT, RadialDirections.SOUTHEAST, 10, 97, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3481_ret_44',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3481_pause_action_script_45',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_3481_play_sound_46',
        "command": 'play_sound',
        "args": [Sounds._032_UNDERGROUND_WARP, 6]
    },
    {
        "identifier": 'EVENT_3481_start_embedded_action_script_async_47',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3481_start_embedded_action_script_async_47_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3481_start_embedded_action_script_async_47_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3481_start_embedded_action_script_async_47_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3481_start_embedded_action_script_async_47_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3481_start_embedded_action_script_async_47_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3481_start_embedded_action_script_async_47_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3481_pixelate_layers_48',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 8, 196]
    },
    {
        "identifier": 'EVENT_3481_enable_controls_49',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3481_ret_50',
        "command": 'ret'
    }
]
