from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_829_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_829_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_829_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_829_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_829_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 28, 'ACTION_829_shift_f_direction_steps_9']
    },
    {
        "identifier": 'ACTION_829_shift_f_direction_steps_5',
        "command": 'shift_f_direction_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_829_pause_6',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_829_turn_clockwise_45_degrees_n_times_7',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_829_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_829_shift_f_direction_steps_5']
    },
    {
        "identifier": 'ACTION_829_shift_f_direction_steps_9',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_829_pause_10',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_829_turn_clockwise_45_degrees_n_times_11',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_829_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_829_shift_f_direction_steps_9']
    }
]
