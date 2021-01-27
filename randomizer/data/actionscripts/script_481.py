from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_481_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_481_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_481_pause_2',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'ACTION_481_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_481_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_481_sequence_looping_on_5',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_481_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_481_shift_southwest_pixels_7',
        "command": 'shift_southwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_481_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_481_floating_on_9',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_481_jump_to_height_10',
        "command": 'jump_to_height',
        "args": [0]
    },
    {
        "identifier": 'ACTION_481_shadow_on_11',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_481_pause_12',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_481_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_481_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_481_db_15',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_481_start_loop_n_times_16',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_481_db_17',
        "command": 'db',
        "args": [0x24, 0xc0, 0x00, 0xa0, 0x00]
    },
    {
        "identifier": 'ACTION_481_db_18',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_481_pause_19',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_481_end_loop_20',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_481_start_loop_n_times_21',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_481_db_22',
        "command": 'db',
        "args": [0x24, 0xa0, 0xff, 0x40, 0x00]
    },
    {
        "identifier": 'ACTION_481_db_23',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_481_pause_24',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_481_end_loop_25',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_481_start_loop_n_times_26',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_481_db_27',
        "command": 'db',
        "args": [0x24, 0xa0, 0xff, 0xc0, 0xff]
    },
    {
        "identifier": 'ACTION_481_db_28',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_481_pause_29',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_481_end_loop_30',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_481_start_loop_n_times_31',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_481_db_32',
        "command": 'db',
        "args": [0x24, 0x60, 0x00, 0xc0, 0xff]
    },
    {
        "identifier": 'ACTION_481_db_33',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_481_pause_34',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_481_end_loop_35',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_481_start_loop_n_times_36',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_481_db_37',
        "command": 'db',
        "args": [0x24, 0x60, 0x00, 0x40, 0x00]
    },
    {
        "identifier": 'ACTION_481_db_38',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_481_pause_39',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_481_end_loop_40',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_481_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_481_start_loop_n_times_21']
    }
]
