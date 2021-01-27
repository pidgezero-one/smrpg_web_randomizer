from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_617_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_617_jmp_if_700C_not_equals_short_1',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [21, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_617_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 6, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_617_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 5, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_617_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 3, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_617_transfer_to_xyzf_5',
        "command": 'transfer_to_xyzf',
        "args": [23, 59, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_617_shift_west_pixels_6',
        "command": 'shift_west_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_617_face_southwest_7',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_617_sequence_looping_off_8',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_617_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_617_visibility_off_10',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_617_object_memory_set_bit_11',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_617_clear_solidity_bits_12',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_617_sequence_playback_off_13',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_617_ret_14',
        "command": 'ret'
    }
]
