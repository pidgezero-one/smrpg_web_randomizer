from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3072_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3072_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3072_set_7000_to_70A0_short_mem_2',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_3072_disable_event_trigger_for_object_at_70A8_3',
        "command": 'disable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'EVENT_3072_mem_7000_and_const_4',
        "command": 'mem_7000_and_const',
        "args": [0x00f0]
    },
    {
        "identifier": 'EVENT_3072_set_70A0_short_mem_to_7000_5',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70b4]
    },
    {
        "identifier": 'EVENT_3072_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7]
    },
    {
        "identifier": 'EVENT_3072_set_7010_to_object_xyz_7',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3072_set_7000_to_7000_short_mem_8',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7014]
    },
    {
        "identifier": 'EVENT_3072_add_9',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3072_set_7000_short_mem_to_7000_10',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7014]
    },
    {
        "identifier": 'EVENT_3072_jmp_if_var_equals_byte_11',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 0, 'EVENT_3072_play_sound_16']
    },
    {
        "identifier": 'EVENT_3072_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 16, 'EVENT_3072_enable_controls_23']
    },
    {
        "identifier": 'EVENT_3072_jmp_if_var_equals_byte_13',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 32, 'EVENT_3072_play_sound_39']
    },
    {
        "identifier": 'EVENT_3072_jmp_if_var_equals_byte_14',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 48, 'EVENT_3072_play_sound_44']
    },
    {
        "identifier": 'EVENT_3072_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3072_ret_47']
    },
    {
        "identifier": 'EVENT_3072_play_sound_16',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3072_create_packet_at_7010_coords_jmp_if_null_17',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._001_MUSHROOM, 'EVENT_3072_ret_47']
    },
    {
        "identifier": 'EVENT_3072_restore_all_hp_18',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_3072_restore_all_fp_19',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_3072_set_short_20',
        "command": 'set_short',
        "args": [0x7020, 0x0008]
    },
    {
        "identifier": 'EVENT_3072_run_background_event_with_pause_21',
        "command": 'run_background_event_with_pause',
        "args": [3075, 0x7020, [12, 13]]
    },
    {
        "identifier": 'EVENT_3072_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3072_ret_47']
    },
    {
        "identifier": 'EVENT_3072_enable_controls_23',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3072_play_sound_24',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3072_create_packet_at_7010_coords_jmp_if_null_25',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._003_SUPER_STAR, 'EVENT_3072_ret_47']
    },
    {
        "identifier": 'EVENT_3072_stop_music_FDA0_26',
        "command": 'stop_music_FDA0'
    },
    {
        "identifier": 'EVENT_3072_set_short_27',
        "command": 'set_short',
        "args": [0x7022, 0x0226]
    },
    {
        "identifier": 'EVENT_3072_run_background_event_with_pause_28',
        "command": 'run_background_event_with_pause',
        "args": [3076, 0x7022, [12, 13]]
    },
    {
        "identifier": 'EVENT_3072_set_bit_29',
        "command": 'set_bit',
        "args": [0x7076, 0]
    },
    {
        "identifier": 'EVENT_3072_set_7000_to_70A0_short_mem_30',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_3072_mem_7000_and_const_31',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_3072_set_experience_packet_7000_32',
        "command": 'set_experience_packet_7000'
    },
    {
        "identifier": 'EVENT_3072_mario_glows_33',
        "command": 'mario_glows'
    },
    {
        "identifier": 'EVENT_3072_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x707c, 3]
    },
    {
        "identifier": 'EVENT_3072_clear_bit_35',
        "command": 'clear_bit',
        "args": [0x7064, 4]
    },
    {
        "identifier": 'EVENT_3072_clear_bit_36',
        "command": 'clear_bit',
        "args": [0x707c, 2]
    },
    {
        "identifier": 'EVENT_3072_create_packet_at_object_coords_jmp_if_null_37',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._022_SPARKLES_MOVE_N, AreaObjects.MARIO, 'EVENT_3072_jmp_38']
    },
    {
        "identifier": 'EVENT_3072_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_3072_ret_47']
    },
    {
        "identifier": 'EVENT_3072_play_sound_39',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3072_create_packet_at_7010_coords_jmp_if_null_40',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 'EVENT_3072_ret_47']
    },
    {
        "identifier": 'EVENT_3072_set_41',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3072_add_max_FP_7000_42',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_3072_jmp_43',
        "command": 'jmp',
        "args": ['EVENT_3072_ret_47']
    },
    {
        "identifier": 'EVENT_3072_play_sound_44',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_3072_create_packet_at_7010_coords_jmp_if_null_45',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._019_FROG_COIN, 'EVENT_3072_ret_47']
    },
    {
        "identifier": 'EVENT_3072_add_frog_coins_46',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3072_ret_47',
        "command": 'ret'
    }
]
