from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_461_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_461_shadow_off_1',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_461_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_461_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_461_shift_southwest_pixels_4',
        "command": 'shift_southwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_461_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_461_floating_on_6',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_461_jump_to_height_7',
        "command": 'jump_to_height',
        "args": [0]
    },
    {
        "identifier": 'ACTION_461_shadow_on_8',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_461_pause_9',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_461_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_461_reset_properties_11',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_461_walk_to_xy_coords_12',
        "command": 'walk_to_xy_coords',
        "args": [22, 85]
    },
    {
        "identifier": 'ACTION_461_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_461_db_14',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_461_db_15',
        "command": 'db',
        "args": [0x24, 0x00, 0xfe, 0x00, 0x02]
    },
    {
        "identifier": 'ACTION_461_db_16',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_17',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_bpl_26_27_28_18',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_461_reset_properties_19',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_461_walk_to_xy_coords_20',
        "command": 'walk_to_xy_coords',
        "args": [20, 95]
    },
    {
        "identifier": 'ACTION_461_set_sprite_sequence_21',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_461_db_22',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_461_db_23',
        "command": 'db',
        "args": [0x24, 0x00, 0x02, 0x20, 0x00]
    },
    {
        "identifier": 'ACTION_461_db_24',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_25',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_db_26',
        "command": 'db',
        "args": [0x24, 0x00, 0x02, 0x80, 0xfe]
    },
    {
        "identifier": 'ACTION_461_db_27',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_28',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_bpl_26_27_28_29',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_461_reset_properties_30',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_461_walk_to_xy_coords_31',
        "command": 'walk_to_xy_coords',
        "args": [22, 89]
    },
    {
        "identifier": 'ACTION_461_set_sprite_sequence_32',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_461_db_33',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_461_db_34',
        "command": 'db',
        "args": [0x24, 0x00, 0xfe, 0x00, 0x00]
    },
    {
        "identifier": 'ACTION_461_db_35',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_36',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_db_37',
        "command": 'db',
        "args": [0x24, 0x00, 0xfe, 0x00, 0x00]
    },
    {
        "identifier": 'ACTION_461_db_38',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_39',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_db_40',
        "command": 'db',
        "args": [0x24, 0x80, 0xff, 0x80, 0x01]
    },
    {
        "identifier": 'ACTION_461_db_41',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_42',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_bpl_26_27_28_43',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_461_reset_properties_44',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_461_walk_to_xy_coords_45',
        "command": 'walk_to_xy_coords',
        "args": [20, 98]
    },
    {
        "identifier": 'ACTION_461_set_sprite_sequence_46',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_461_db_47',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_461_db_48',
        "command": 'db',
        "args": [0x24, 0x00, 0x02, 0x00, 0xff]
    },
    {
        "identifier": 'ACTION_461_db_49',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_50',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_db_51',
        "command": 'db',
        "args": [0x24, 0x00, 0x02, 0x00, 0xff]
    },
    {
        "identifier": 'ACTION_461_db_52',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_53',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_db_54',
        "command": 'db',
        "args": [0x24, 0x90, 0xff, 0x00, 0x01]
    },
    {
        "identifier": 'ACTION_461_db_55',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_56',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_db_57',
        "command": 'db',
        "args": [0x24, 0x00, 0x00, 0x00, 0xfe]
    },
    {
        "identifier": 'ACTION_461_db_58',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_461_pause_59',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_461_bpl_26_27_28_60',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_461_reset_properties_61',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_461_jmp_62',
        "command": 'jmp',
        "args": ['ACTION_461_walk_to_xy_coords_12']
    }
]
