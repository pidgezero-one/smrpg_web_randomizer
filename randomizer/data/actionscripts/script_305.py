from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_305_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_305_shift_southeast_pixels_1',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_305_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_305_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_305_mem_700C_and_const_4',
        "command": 'mem_700C_and_const',
        "args": [0x0006]
    },
    {
        "identifier": 'ACTION_305_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_305_pause_9']
    },
    {
        "identifier": 'ACTION_305_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 2, 'ACTION_305_pause_10']
    },
    {
        "identifier": 'ACTION_305_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 4, 'ACTION_305_pause_11']
    },
    {
        "identifier": 'ACTION_305_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 6, 'ACTION_305_jump_to_subroutine_12']
    },
    {
        "identifier": 'ACTION_305_pause_9',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_305_pause_10',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_305_pause_11',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_305_jump_to_subroutine_12',
        "command": 'jump_to_subroutine',
        "args": [0x3801]
    },
    {
        "identifier": 'ACTION_305_transfer_xyzf_steps_13',
        "command": 'transfer_xyzf_steps',
        "args": [2, 4, 20, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_305_pause_14',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_305_jump_to_subroutine_15',
        "command": 'jump_to_subroutine',
        "args": [0x3801]
    },
    {
        "identifier": 'ACTION_305_transfer_xyzf_steps_16',
        "command": 'transfer_xyzf_steps',
        "args": [253, 254, 20, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_305_pause_17',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_305_jump_to_subroutine_18',
        "command": 'jump_to_subroutine',
        "args": [0x3801]
    },
    {
        "identifier": 'ACTION_305_transfer_xyzf_steps_19',
        "command": 'transfer_xyzf_steps',
        "args": [1, 254, 20, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_305_pause_20',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_305_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_305_jump_to_subroutine_12']
    }
]
