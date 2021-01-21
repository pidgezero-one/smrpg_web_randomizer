from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3134_set_7000_to_object_coord_0',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3134_move_script_to_background_thread_2_1',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_3134_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 256, 'EVENT_3134_set_short_11']
    },
    {
        "identifier": 'EVENT_3134_run_dialog_3',
        "command": 'run_dialog',
        "args": [1583, AreaObjects.MARIO, [_0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3134_set_short_4',
        "command": 'set_short',
        "args": [0x7024, 0x012c]
    },
    {
        "identifier": 'EVENT_3134_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3134_set_7000_to_pressed_button_6',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_3134_jmp_if_7000_any_bits_set_7',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 1, 2, 3, 4, 7], 'EVENT_3134_close_dialog_10']
    },
    {
        "identifier": 'EVENT_3134_dec_short_8',
        "command": 'dec_short',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_3134_jmp_if_loaded_memory_is_not_0_9',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3134_pause_5']
    },
    {
        "identifier": 'EVENT_3134_close_dialog_10',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3134_set_short_11',
        "command": 'set_short',
        "args": [0x701c, 0x012c]
    },
    {
        "identifier": 'EVENT_3134_stop_background_event_12',
        "command": 'stop_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_3134_move_script_to_main_thread_13',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_3134_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_15',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_16',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES]
    },
    {
        "identifier": 'EVENT_3134_remove_from_level_17',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_18',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_19',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_20',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_21',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_22',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_23',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_24',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_25',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_26',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_27',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_28',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_29',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_30',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_31',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_32',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_33',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_34',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_35',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_36',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_37',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_38',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_39',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_40',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    },
    {
        "identifier": 'EVENT_3134_summon_to_level_41',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    },
    {
        "identifier": 'EVENT_3134_clear_bit_42',
        "command": 'clear_bit',
        "args": [0x7055, 1]
    },
    {
        "identifier": 'EVENT_3134_apply_solidity_mod_43',
        "command": 'apply_solidity_mod',
        "args": [Rooms._056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, 0, []]
    },
    {
        "identifier": 'EVENT_3134_apply_solidity_mod_44',
        "command": 'apply_solidity_mod',
        "args": [Rooms._056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, 1, []]
    },
    {
        "identifier": 'EVENT_3134_apply_solidity_mod_45',
        "command": 'apply_solidity_mod',
        "args": [Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, 0, []]
    },
    {
        "identifier": 'EVENT_3134_apply_solidity_mod_46',
        "command": 'apply_solidity_mod',
        "args": [Rooms._057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, 1, []]
    },
    {
        "identifier": 'EVENT_3134_apply_solidity_mod_47',
        "command": 'apply_solidity_mod',
        "args": [Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, 0, []]
    },
    {
        "identifier": 'EVENT_3134_apply_solidity_mod_48',
        "command": 'apply_solidity_mod',
        "args": [Rooms._058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, 1, []]
    },
    {
        "identifier": 'EVENT_3134_set_bit_49',
        "command": 'set_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_3134_ret_50',
        "command": 'ret'
    }
]
