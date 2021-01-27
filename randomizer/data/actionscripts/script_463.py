from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_463_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_463_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_463_pause_2',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'ACTION_463_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_463_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_463_sequence_looping_on_5',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_463_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_463_shift_southwest_pixels_7',
        "command": 'shift_southwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_463_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_463_floating_on_9',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_463_jump_to_height_10',
        "command": 'jump_to_height',
        "args": [0]
    },
    {
        "identifier": 'ACTION_463_shadow_on_11',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_463_pause_12',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_463_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_463_db_14',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_463_db_15',
        "command": 'db',
        "args": [0x24, 0x00, 0x02, 0x00, 0x02]
    },
    {
        "identifier": 'ACTION_463_db_16',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_463_pause_17',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_463_db_18',
        "command": 'db',
        "args": [0x24, 0x80, 0xfb, 0x70, 0xfe]
    },
    {
        "identifier": 'ACTION_463_db_19',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_463_pause_20',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_463_db_21',
        "command": 'db',
        "args": [0x24, 0x00, 0x01, 0x80, 0x03]
    },
    {
        "identifier": 'ACTION_463_db_22',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_463_pause_23',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_463_db_24',
        "command": 'db',
        "args": [0x24, 0x80, 0xfc, 0x70, 0xfe]
    },
    {
        "identifier": 'ACTION_463_db_25',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_463_pause_26',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_463_bpl_26_27_28_27',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_463_reset_properties_28',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_463_walk_to_xy_coords_29',
        "command": 'walk_to_xy_coords',
        "args": [17, 92]
    },
    {
        "identifier": 'ACTION_463_pause_30',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_463_set_sprite_sequence_31',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_463_db_32',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_463_db_33',
        "command": 'db',
        "args": [0x24, 0x80, 0x03, 0x90, 0x01]
    },
    {
        "identifier": 'ACTION_463_db_34',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_463_pause_35',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_463_db_36',
        "command": 'db',
        "args": [0x24, 0x00, 0xff, 0x00, 0xfd]
    },
    {
        "identifier": 'ACTION_463_db_37',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_463_pause_38',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_463_db_39',
        "command": 'db',
        "args": [0x24, 0x80, 0x04, 0x90, 0x01]
    },
    {
        "identifier": 'ACTION_463_db_40',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_463_pause_41',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_463_bpl_26_27_28_42',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_463_reset_properties_43',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_463_walk_to_xy_coords_44',
        "command": 'walk_to_xy_coords',
        "args": [23, 91]
    },
    {
        "identifier": 'ACTION_463_set_sprite_sequence_45',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_463_db_46',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_463_jmp_47',
        "command": 'jmp',
        "args": ['ACTION_463_db_18']
    }
]
