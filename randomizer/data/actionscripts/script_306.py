from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_306_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_306_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_306_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_306_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [24, 'ACTION_306_jump_to_subroutine_5']
    },
    {
        "identifier": 'ACTION_306_pause_4',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_306_jump_to_subroutine_5',
        "command": 'jump_to_subroutine',
        "args": [0x3885]
    },
    {
        "identifier": 'ACTION_306_transfer_xyzf_steps_6',
        "command": 'transfer_xyzf_steps',
        "args": [0, 0, 10, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_306_pause_7',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_306_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_306_jump_to_subroutine_5']
    },
    {
        "identifier": 'ACTION_306_visibility_on_9',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_306_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_306_db_11',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_306_embedded_animation_routine_12',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x08, 0x00, 0x01, 0xf0, 0xff, 0x00, 0x10, 0x80]
    },
    {
        "identifier": 'ACTION_306_embedded_animation_routine_13',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x04, 0x00, 0x01, 0xf8, 0xff, 0x00, 0x10, 0x80]
    },
    {
        "identifier": 'ACTION_306_shift_z_down_steps_14',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_306_bpl_26_27_28_15',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_306_visibility_off_16',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_306_ret_17',
        "command": 'ret'
    }
]
