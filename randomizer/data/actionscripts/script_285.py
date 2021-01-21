from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_285_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_285_pause_1',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_285_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_285_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_285_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_285_add_5',
        "command": 'add',
        "args": [0x700c, 65512]
    },
    {
        "identifier": 'ACTION_285_load_mem_6',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_285_pause_7',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'ACTION_285_end_loop_8',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_285_transfer_to_xyzf_9',
        "command": 'transfer_to_xyzf',
        "args": [25, 35, 19, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_285_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_285_face_southwest_11',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_285_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_285_shift_z_down_steps_13',
        "command": 'shift_z_down_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_285_clear_solidity_bits_14',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_285_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_285_walk_to_xy_coords_16',
        "command": 'walk_to_xy_coords',
        "args": [5, 75]
    },
    {
        "identifier": 'ACTION_285_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_285_shift_z_up_steps_18',
        "command": 'shift_z_up_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_285_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_285_face_northeast_20',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_285_set_solidity_bits_21',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_285_walk_to_xy_coords_22',
        "command": 'walk_to_xy_coords',
        "args": [25, 35]
    },
    {
        "identifier": 'ACTION_285_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_285_face_southwest_11']
    }
]
