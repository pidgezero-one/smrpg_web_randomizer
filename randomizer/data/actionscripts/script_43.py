from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_43_pause_0',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_43_set_short_1',
        "command": 'set_short',
        "args": [0x7016, 0x3c80]
    },
    {
        "identifier": 'ACTION_43_set_short_2',
        "command": 'set_short',
        "args": [0x7018, 0x0e00]
    },
    {
        "identifier": 'ACTION_43_set_short_3',
        "command": 'set_short',
        "args": [0x701a, 0x0360]
    },
    {
        "identifier": 'ACTION_43_db_4',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_43_set_priority_5',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_43_shadow_on_6',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_43_set_vram_priority_7',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_43_visibility_on_8',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_43_pause_9',
        "command": 'pause',
        "args": [14]
    },
    {
        "identifier": 'ACTION_43_sequence_looping_on_10',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_43_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_43_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_43_floating_on_13',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_43_db_14',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_43_db_15',
        "command": 'db',
        "args": [0x25, 0x60, 0x03, 0xe0, 0xff]
    },
    {
        "identifier": 'ACTION_43_walk_to_xy_coords_16',
        "command": 'walk_to_xy_coords',
        "args": [26, 26]
    },
    {
        "identifier": 'ACTION_43_bpl_26_27_28_17',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_43_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_43_jump_to_height_19',
        "command": 'jump_to_height',
        "args": [108]
    },
    {
        "identifier": 'ACTION_43_shift_east_steps_20',
        "command": 'shift_east_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_43_start_loop_n_times_21',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_43_visibility_on_22',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_43_pause_23',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_43_visibility_off_24',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_43_pause_25',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_43_end_loop_26',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_43_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_43_pause_28',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_43_jmp_if_bit_clear_29',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'ACTION_43_pause_28']
    },
    {
        "identifier": 'ACTION_43_pause_30',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_43_set_short_31',
        "command": 'set_short',
        "args": [0x7016, 0x2e80]
    },
    {
        "identifier": 'ACTION_43_set_short_32',
        "command": 'set_short',
        "args": [0x7018, 0x0900]
    },
    {
        "identifier": 'ACTION_43_set_short_33',
        "command": 'set_short',
        "args": [0x701a, 0x0360]
    },
    {
        "identifier": 'ACTION_43_db_34',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_43_visibility_on_35',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_43_pause_36',
        "command": 'pause',
        "args": [14]
    },
    {
        "identifier": 'ACTION_43_sequence_looping_on_37',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_43_set_sprite_sequence_38',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_43_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_43_db_40',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_43_db_41',
        "command": 'db',
        "args": [0x25, 0x60, 0x03, 0xe0, 0xff]
    },
    {
        "identifier": 'ACTION_43_walk_to_xy_coords_42',
        "command": 'walk_to_xy_coords',
        "args": [19, 18]
    },
    {
        "identifier": 'ACTION_43_bpl_26_27_28_43',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_43_play_sound_44',
        "command": 'play_sound',
        "args": [Sounds._065_THWOMP_STOMP, 4]
    },
    {
        "identifier": 'ACTION_43_jump_to_height_45',
        "command": 'jump_to_height',
        "args": [108]
    },
    {
        "identifier": 'ACTION_43_jmp_if_bit_set_46',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 6, 'ACTION_43_shift_west_steps_49']
    },
    {
        "identifier": 'ACTION_43_shift_east_steps_47',
        "command": 'shift_east_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_43_jmp_48',
        "command": 'jmp',
        "args": ['ACTION_719_clear_solidity_bits_0']
    },
    {
        "identifier": 'ACTION_43_shift_west_steps_49',
        "command": 'shift_west_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_43_start_loop_n_times_50',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_43_visibility_on_51',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_43_pause_52',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_43_visibility_off_53',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_43_pause_54',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_43_end_loop_55',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_43_ret_56',
        "command": 'ret'
    }
]
