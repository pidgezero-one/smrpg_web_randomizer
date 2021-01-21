from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_674_pause_0',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'ACTION_674_jump_to_subroutine_1',
        "command": 'jump_to_subroutine',
        "args": [0x7b75]
    },
    {
        "identifier": 'ACTION_674_face_northwest_2',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_674_sequence_looping_off_3',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_674_pause_4',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_674_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_674_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_674_shift_z_up_pixels_7',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_674_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_674_shift_z_down_pixels_9',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_674_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_674_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_674_pause_12',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_674_jump_to_subroutine_13',
        "command": 'jump_to_subroutine',
        "args": [0x7b92]
    },
    {
        "identifier": 'ACTION_674_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_674_set_bit_15',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_674_ret_16',
        "command": 'ret'
    }
]
