from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_832_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_832_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_832_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_832_set_vram_priority_3',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_832_sequence_playback_off_4',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_832_shirt_to_xy_coords_5',
        "command": 'shirt_to_xy_coords',
        "args": [13, 24]
    },
    {
        "identifier": 'ACTION_832_db_6',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_832_db_7',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_832_walk_1_step_southeast_8',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_832_sequence_playback_on_9',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_832_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_832_pause_11',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_832_bpl_26_27_28_12',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_832_reset_properties_13',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_832_object_memory_modify_bits_14',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_832_set_vram_priority_15',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_832_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_832_shift_southeast_steps_17',
        "command": 'shift_southeast_steps',
        "args": [12]
    },
    {
        "identifier": 'ACTION_832_shift_southwest_steps_18',
        "command": 'shift_southwest_steps',
        "args": [16]
    },
    {
        "identifier": 'ACTION_832_ret_19',
        "command": 'ret'
    }
]
