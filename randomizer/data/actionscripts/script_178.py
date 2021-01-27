from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_178_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_178_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_178_set_random_2',
        "command": 'set_random',
        "args": [0x700c, 255]
    },
    {
        "identifier": 'ACTION_178_load_mem_3',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_178_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_178_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_178_jmp_if_random_above_66_6',
        "command": 'jmp_if_random_above_66',
        "args": [0x241d, 'ACTION_178_transfer_to_xyzf_31']
    },
    {
        "identifier": 'ACTION_178_transfer_to_xyzf_7',
        "command": 'transfer_to_xyzf',
        "args": [11, 52, 17, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_178_visibility_on_8',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_178_overwrite_solidity_9',
        "command": 'overwrite_solidity',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_178_db_10',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_178_db_11',
        "command": 'db',
        "args": [0x24, 0x80, 0xfb, 0x00, 0x01]
    },
    {
        "identifier": 'ACTION_178_db_12',
        "command": 'db',
        "args": [0x25, 0x00, 0x00, 0x60, 0xff]
    },
    {
        "identifier": 'ACTION_178_pause_13',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_178_db_14',
        "command": 'db',
        "args": [0x24, 0xe0, 0xff, 0x80, 0x00]
    },
    {
        "identifier": 'ACTION_178_pause_15',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_178_bpl_26_27_28_16',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_178_overwrite_solidity_17',
        "command": 'overwrite_solidity',
        "args": [[]]
    },
    {
        "identifier": 'ACTION_178_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_178_play_sound_42']
    },
    {
        "identifier": 'ACTION_178_transfer_to_xyzf_19',
        "command": 'transfer_to_xyzf',
        "args": [3, 48, 17, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_178_visibility_on_20',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_178_overwrite_solidity_21',
        "command": 'overwrite_solidity',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_178_db_22',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_178_db_23',
        "command": 'db',
        "args": [0x24, 0x80, 0x03, 0x00, 0x04]
    },
    {
        "identifier": 'ACTION_178_db_24',
        "command": 'db',
        "args": [0x25, 0x00, 0x00, 0x60, 0xff]
    },
    {
        "identifier": 'ACTION_178_pause_25',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_178_db_26',
        "command": 'db',
        "args": [0x24, 0x20, 0x00, 0x80, 0x00]
    },
    {
        "identifier": 'ACTION_178_pause_27',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_178_bpl_26_27_28_28',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_178_overwrite_solidity_29',
        "command": 'overwrite_solidity',
        "args": [[]]
    },
    {
        "identifier": 'ACTION_178_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_178_play_sound_42']
    },
    {
        "identifier": 'ACTION_178_transfer_to_xyzf_31',
        "command": 'transfer_to_xyzf',
        "args": [10, 66, 0, RadialDirections.SOUTH]
    },
    {
        "identifier": 'ACTION_178_visibility_on_32',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_178_overwrite_solidity_33',
        "command": 'overwrite_solidity',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_178_db_34',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_178_db_35',
        "command": 'db',
        "args": [0x24, 0x80, 0xfe, 0x80, 0xfe]
    },
    {
        "identifier": 'ACTION_178_db_36',
        "command": 'db',
        "args": [0x25, 0x00, 0x00, 0x60, 0xff]
    },
    {
        "identifier": 'ACTION_178_pause_37',
        "command": 'pause',
        "args": [38]
    },
    {
        "identifier": 'ACTION_178_db_38',
        "command": 'db',
        "args": [0x24, 0xe0, 0xff, 0x00, 0xff]
    },
    {
        "identifier": 'ACTION_178_pause_39',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_178_bpl_26_27_28_40',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_178_overwrite_solidity_41',
        "command": 'overwrite_solidity',
        "args": [[]]
    },
    {
        "identifier": 'ACTION_178_play_sound_42',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
    },
    {
        "identifier": 'ACTION_178_set_sprite_sequence_43',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_178_pause_44',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_178_start_loop_n_times_45',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_178_visibility_off_46',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_178_pause_47',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_178_visibility_on_48',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_178_pause_49',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_178_end_loop_50',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_178_visibility_off_51',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_178_shirt_to_xy_coords_52',
        "command": 'shirt_to_xy_coords',
        "args": [14, 122]
    },
    {
        "identifier": 'ACTION_178_jmp_53',
        "command": 'jmp',
        "args": ['ACTION_178_set_random_2']
    }
]
