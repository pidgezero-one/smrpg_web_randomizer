from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_459_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_459_shadow_off_1',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_459_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_459_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_459_shift_southwest_pixels_4',
        "command": 'shift_southwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_459_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_459_floating_on_6',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_459_jump_to_height_7',
        "command": 'jump_to_height',
        "args": [0]
    },
    {
        "identifier": 'ACTION_459_shadow_on_8',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_459_pause_9',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_459_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_459_reset_properties_11',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_459_walk_to_xy_coords_12',
        "command": 'walk_to_xy_coords',
        "args": [22, 85]
    },
    {
        "identifier": 'ACTION_459_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_459_db_14',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_459_db_15',
        "command": 'db',
        "args": [0x24, 0x00, 0xff, 0xb0, 0x00]
    },
    {
        "identifier": 'ACTION_459_db_16',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_459_pause_17',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_459_db_18',
        "command": 'db',
        "args": [0x24, 0x80, 0xfe, 0x00, 0xff]
    },
    {
        "identifier": 'ACTION_459_db_19',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_459_pause_20',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_459_db_21',
        "command": 'db',
        "args": [0x24, 0x80, 0x01, 0x00, 0x01]
    },
    {
        "identifier": 'ACTION_459_db_22',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_459_pause_23',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_459_db_24',
        "command": 'db',
        "args": [0x24, 0x00, 0x01, 0x50, 0xff]
    },
    {
        "identifier": 'ACTION_459_db_25',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_459_pause_26',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_459_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_459_db_15']
    }
]
