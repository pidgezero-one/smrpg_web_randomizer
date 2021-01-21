from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_353_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_353_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_353_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702e, 1, 'ACTION_353_play_sound_10']
    },
    {
        "identifier": 'ACTION_353_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702e, 16, 'ACTION_353_play_sound_7']
    },
    {
        "identifier": 'ACTION_353_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 4]
    },
    {
        "identifier": 'ACTION_353_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_353_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_353_set_animation_speed_12']
    },
    {
        "identifier": 'ACTION_353_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 4]
    },
    {
        "identifier": 'ACTION_353_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_353_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_353_set_animation_speed_12']
    },
    {
        "identifier": 'ACTION_353_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 4]
    },
    {
        "identifier": 'ACTION_353_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_353_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_353_add_z_coord_1_step_13',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_353_start_loop_n_times_14',
        "command": 'start_loop_n_times',
        "args": [8]
    },
    {
        "identifier": 'ACTION_353_visibility_on_15',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_353_pause_16',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_353_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_353_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_353_end_loop_19',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_353_pause_20',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_353_mem_compare_21',
        "command": 'mem_compare',
        "args": [0x702a, 96]
    },
    {
        "identifier": 'ACTION_353_jmp_if_comparison_result_is_greater_or_equal_22',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_353_pause_20']
    },
    {
        "identifier": 'ACTION_353_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_352_object_memory_clear_bit_0']
    }
]
