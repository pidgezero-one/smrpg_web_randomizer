from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_39_shadow_on_0',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_39_start_loop_n_times_1',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_39_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_39_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_39_pause_2']
    },
    {
        "identifier": 'ACTION_39_transfer_to_xyzf_4',
        "command": 'transfer_to_xyzf',
        "args": [29, 29, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_39_set_priority_5',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_39_set_vram_priority_6',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_39_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_39_visibility_on_8',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_39_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_39_jump_to_height_10',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_39_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_39_visibility_off_12',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_39_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_39_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_39_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_39_jmp_if_bit_clear_16',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'ACTION_39_pause_15']
    },
    {
        "identifier": 'ACTION_39_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_39_set_vram_priority_18',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_39_visibility_on_19',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_39_db_20',
        "command": 'db',
        "args": [0x97, 0x17]
    },
    {
        "identifier": 'ACTION_39_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'ACTION_39_db_20']
    },
    {
        "identifier": 'ACTION_39_jump_to_height_22',
        "command": 'jump_to_height',
        "args": [120]
    },
    {
        "identifier": 'ACTION_39_set_animation_speed_23',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_39_walk_1_step_northwest_24',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_39_shift_northwest_pixels_25',
        "command": 'shift_northwest_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_39_floating_off_26',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_39_ret_27',
        "command": 'ret'
    }
]
