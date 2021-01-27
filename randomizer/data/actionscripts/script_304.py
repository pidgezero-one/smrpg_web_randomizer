from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_304_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_304_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_304_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_304_mem_700C_and_const_3',
        "command": 'mem_700C_and_const',
        "args": [0x0006]
    },
    {
        "identifier": 'ACTION_304_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_304_pause_8']
    },
    {
        "identifier": 'ACTION_304_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_304_pause_9']
    },
    {
        "identifier": 'ACTION_304_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [4, 'ACTION_304_pause_10']
    },
    {
        "identifier": 'ACTION_304_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [6, 'ACTION_304_jump_to_subroutine_11']
    },
    {
        "identifier": 'ACTION_304_pause_8',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_304_pause_9',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_304_pause_10',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_304_jump_to_subroutine_11',
        "command": 'jump_to_subroutine',
        "args": [0x3801]
    },
    {
        "identifier": 'ACTION_304_transfer_xyzf_steps_12',
        "command": 'transfer_xyzf_steps',
        "args": [2, 4, 20, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_304_pause_13',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_304_jump_to_subroutine_14',
        "command": 'jump_to_subroutine',
        "args": [0x3801]
    },
    {
        "identifier": 'ACTION_304_transfer_xyzf_steps_15',
        "command": 'transfer_xyzf_steps',
        "args": [253, 254, 20, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_304_pause_16',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_304_jump_to_subroutine_17',
        "command": 'jump_to_subroutine',
        "args": [0x3801]
    },
    {
        "identifier": 'ACTION_304_transfer_xyzf_steps_18',
        "command": 'transfer_xyzf_steps',
        "args": [1, 254, 20, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_304_pause_19',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_304_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_304_jump_to_subroutine_11']
    },
    {
        "identifier": 'ACTION_304_visibility_on_21',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_304_set_sprite_sequence_22',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_304_db_23',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_304_embedded_animation_routine_24',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x00, 0x00, 0x10, 0x80]
    },
    {
        "identifier": 'ACTION_304_embedded_animation_routine_25',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x01, 0x04, 0x00, 0x00, 0x10, 0x80]
    },
    {
        "identifier": 'ACTION_304_shift_z_up_steps_26',
        "command": 'shift_z_up_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_304_bpl_26_27_28_27',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_304_visibility_off_28',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_304_ret_29',
        "command": 'ret'
    }
]
