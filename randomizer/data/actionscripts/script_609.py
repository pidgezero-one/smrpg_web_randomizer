from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_609_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_609_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_609_object_memory_set_bit_2',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_609_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_609_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'ACTION_609_pause_3']
    },
    {
        "identifier": 'ACTION_609_reset_properties_5',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_609_face_southwest_6',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_609_sequence_looping_off_7',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_609_sequence_playback_off_8',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_609_transfer_to_object_xy_9',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'ACTION_609_transfer_xyzf_pixels_10',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 0, 11, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_609_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_609_visibility_on_12',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_609_set_object_memory_bits_13',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[0, 2]]
    },
    {
        "identifier": 'ACTION_609_shift_z_up_pixels_14',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_609_pause_15',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_609_shift_z_down_pixels_16',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_609_pause_17',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_609_jmp_if_object_in_level_18',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_1, Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM, 'ACTION_609_shift_z_up_pixels_14']
    },
    {
        "identifier": 'ACTION_609_visibility_off_19',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_609_db_20',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_609_ret_21',
        "command": 'ret'
    }
]
