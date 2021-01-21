from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_388_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_388_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_388_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_388_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_388_db_4',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_388_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_388_embedded_animation_routine_6',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_388_embedded_animation_routine_7',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_388_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_388_set_700C_to_pressed_button_9',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 20, 'ACTION_388_shadow_on_18']
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 21, 'ACTION_388_shadow_on_31']
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_388_shadow_on_18']
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 23, 'ACTION_388_shadow_on_31']
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 24, 'ACTION_388_shift_z_down_steps_44']
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 25, 'ACTION_388_shift_z_down_steps_49']
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 26, 'ACTION_388_shift_z_down_steps_44']
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 27, 'ACTION_388_shift_z_down_steps_44']
    },
    {
        "identifier": 'ACTION_388_shadow_on_18',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_388_shift_z_down_steps_19',
        "command": 'shift_z_down_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_388_bpl_26_27_28_20',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_388_shadow_off_21',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_388_object_memory_clear_bit_22',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_388_pause_23',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_388_sequence_playback_on_24',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_388_set_700C_to_pressed_button_25',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_26',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 20, 'ACTION_388_set_sprite_sequence_29']
    },
    {
        "identifier": 'ACTION_388_set_sprite_sequence_27',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_388_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_388_set_sprite_sequence_29',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_388_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_388_shadow_on_31',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_388_shift_z_down_steps_32',
        "command": 'shift_z_down_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_388_bpl_26_27_28_33',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_388_shadow_off_34',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_388_object_memory_clear_bit_35',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_388_pause_36',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_388_sequence_playback_on_37',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_388_set_700C_to_pressed_button_38',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_388_jmp_if_var_equals_short_39',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 23, 'ACTION_388_set_sprite_sequence_42']
    },
    {
        "identifier": 'ACTION_388_set_sprite_sequence_40',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_388_ret_41',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_388_set_sprite_sequence_42',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_388_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_388_shift_z_down_steps_44',
        "command": 'shift_z_down_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_388_set_vram_priority_45',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_388_shift_z_down_pixels_46',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_388_visibility_off_47',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_388_ret_48',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_388_shift_z_down_steps_49',
        "command": 'shift_z_down_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_388_set_vram_priority_50',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_388_shift_z_down_pixels_51',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_388_visibility_off_52',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_388_ret_53',
        "command": 'ret'
    }
]
