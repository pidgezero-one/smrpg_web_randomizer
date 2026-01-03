
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    
    {
        "identifier": 'EVENT_3080_set_7000_to_70A0_short_mem_1',
        "command": 'copy_var_to_var',
        'args': [0x70a7, 0x7000]
    },
    {
        "identifier": 'EVENT_3080_mem_7000_and_const_12',
        "command": 'mem_7000_and_const',
        "args": [240]
    },
    {
        "identifier": 'EVENT_3080_mem_7000_decision',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 240, 'EVENT_3080_reset_7000___']
    },
    {
        "identifier": 'EVENT_3080_set_7000_to_70A0_short_mem__11',
        "command": 'copy_var_to_var',
        'args': [0x70a7, 0x7000]
    },
    {
        "identifier": 'EVENT_3080_mem_7000_and_const__12',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_3080_set_small_coin',
        "command": 'jmp',
        "args": ['EVENT_3080_add_coins_260']
    },





    {
        "identifier": 'EVENT_3080_reset_7000___',
        "command": "set_var_to_const",
        "args": [0x7000, 0]
    },
    {
        "identifier": 'EVENT_3080_check_multiplier',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70BC, 0, 'EVENT_3080_store_multiplier']
    },
    {
        "identifier": 'EVENT_3080_add_counter',
        "command": "add_const_to_var",
        "args": [0x7000, 15]
    },
    {
        "identifier": 'EVENT_3080_get_multiplier',
        "command": 'dec',
        "args": [0x70BC]
    },
    {
        "identifier": 'EVENT_3080_loop',
        "command": 'jmp',
        "args": ['EVENT_3080_check_multiplier']
    },
    {
        "identifier": 'EVENT_3080_store_multiplier',
        "command": 'copy_var_to_var',
        'args': [0x7000, 0x70BC]
    },


    {
        "identifier": 'EVENT_3080_set_7000_to_70A0_short_mem_11',
        "command": 'copy_var_to_var',
        'args': [0x70a7, 0x7000]
    },
    {
        "identifier": 'EVENT_3080_mem_7000_and_const__12_',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_3080_concat_multiplier',
        "command": 'add_var_to_7000',
        'args': [0x70BC]
    },
    {
        "identifier": 'EVENT_3080_store_multiplier_',
        "command": 'copy_var_to_var',
        'args': [0x7000, 0x70BC]
    },

    
    {
        "identifier": 'EVENT_3080_reset_7000_2',
        "command": "set_var_to_const",
        "args": [0x7000, 0]
    },


    {
        "identifier": 'EVENT_3080_use_multiplier',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70BC, 0, 'EVENT_3080_add_coins_260']
    },
    {
        "identifier": 'EVENT_3080_count_10s',
        "command": "add_const_to_var",
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_3080_dec_multiplier',
        "command": 'dec',
        "args": [0x70BC]
    },
    {
        "identifier": 'EVENT_3080_loop_2',
        "command": 'jmp',
        "args": ['EVENT_3080_use_multiplier']
    },

    
    {
        "identifier": 'EVENT_3080_add_coins_260',
        "command": 'add_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_3080_summon_to_current_level_261',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3080_run_dialog_262',
        "command": 'run_dialog',
        "args": [515, AreaObjects.MARIO, [_0x60Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_3080_disable_trigger_263',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3080_play_sound_264',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3080_disable_trigger_at_70A8_265',
        "command": 'disable_trigger_at_70A8'
    },
    {
        "identifier": 'EVENT_3080_set_action_script_sync_266',
        "command": 'set_action_script',
        'args': [AreaObjects.MEM_70A8, True, 7]
    },
    {
        "identifier": 'EVENT_3080_set_7010_to_object_xyz_267',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3080_set_7000_to_7000_short_mem_268',
        "command": 'copy_var_to_var',
        'args': [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_3080_add_269',
        "command": "add_const_to_var",
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3080_set_7000_short_mem_to_7000_270',
        "command": 'copy_var_to_var',
        'args': [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_3080_jmp_if_bit_set_271',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 3, 'EVENT_3080_clear_bit_273']
    },
    {
        "identifier": 'EVENT_3080_play_sound_272',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_3080_clear_bit_273',
        "command": 'clear_bit',
        "args": [0x704a, 3]
    },
    {
        "identifier": 'EVENT_3080_create_packet_at_7010_274',
        "command": 'create_packet_at_7010',
        "args": [NPCPackets._016_BIG_COIN, 'EVENT_3080_ret']
    },
    {
        "identifier": 'EVENT_3080_ret',
        "command": 'ret'
    }
]
