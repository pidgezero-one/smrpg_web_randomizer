from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_457_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_457_shadow_off_1',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_457_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_457_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_457_shift_southwest_pixels_4',
        "command": 'shift_southwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_457_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_457_floating_on_6',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_457_jump_to_height_7',
        "command": 'jump_to_height',
        "args": [0]
    },
    {
        "identifier": 'ACTION_457_shadow_on_8',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_457_pause_9',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_457_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_457_db_11',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_457_db_12',
        "command": 'db',
        "args": [0x24, 0x00, 0x00, 0x80, 0x01]
    },
    {
        "identifier": 'ACTION_457_db_13',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_457_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_457_db_15',
        "command": 'db',
        "args": [0x24, 0x80, 0xfe, 0x00, 0x00]
    },
    {
        "identifier": 'ACTION_457_db_16',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_457_pause_17',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_457_db_18',
        "command": 'db',
        "args": [0x24, 0x00, 0xff, 0x00, 0x01]
    },
    {
        "identifier": 'ACTION_457_db_19',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_457_pause_20',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_457_bpl_26_27_28_21',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_457_pause_22',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_457_reset_properties_23',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_457_pause_24',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_457_walk_to_xy_coords_25',
        "command": 'walk_to_xy_coords',
        "args": [20, 95]
    },
    {
        "identifier": 'ACTION_457_set_sprite_sequence_26',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_457_db_27',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_457_db_28',
        "command": 'db',
        "args": [0x24, 0x30, 0x01, 0x00, 0x00]
    },
    {
        "identifier": 'ACTION_457_db_29',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_457_pause_30',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_457_db_31',
        "command": 'db',
        "args": [0x24, 0x00, 0x01, 0x00, 0xff]
    },
    {
        "identifier": 'ACTION_457_db_32',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_457_pause_33',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_457_bpl_26_27_28_34',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_457_pause_35',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_457_reset_properties_36',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_457_pause_37',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_457_walk_to_xy_coords_38',
        "command": 'walk_to_xy_coords',
        "args": [21, 88]
    },
    {
        "identifier": 'ACTION_457_set_sprite_sequence_39',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_457_db_40',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_457_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_457_db_15']
    }
]
