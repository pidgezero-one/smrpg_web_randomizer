
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_291_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_291_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_291_set_priority_2',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_291_shift_northwest_steps_3',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_291_jmp_if_random_above_66_4',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_291_set_priority_6', 'ACTION_291_set_priority_6']
    },
    {
        "identifier": 'ACTION_291_jmp_to_subroutine_5',
        "command": 'jmp_to_subroutine',
        "args": ['ACTION_293_object_memory_modify_bits_0']
    },
    {
        "identifier": 'ACTION_291_set_priority_6',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_291_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_291_jmp_if_random_above_66_8',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_291_set_priority_10', 'ACTION_291_set_priority_10']
    },
    {
        "identifier": 'ACTION_291_jmp_to_subroutine_9',
        "command": 'jmp_to_subroutine',
        "args": ['ACTION_293_object_memory_modify_bits_0']
    },
    {
        "identifier": 'ACTION_291_set_priority_10',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_291_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_291_jmp_if_random_above_66_12',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_291_set_priority_14', 'ACTION_291_set_priority_14']
    },
    {
        "identifier": 'ACTION_291_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": ['ACTION_293_object_memory_modify_bits_0']
    },
    {
        "identifier": 'ACTION_291_set_priority_14',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_291_shift_southwest_steps_15',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_291_jmp_if_random_above_66_16',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_291_set_animation_speed_0', 'ACTION_291_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_291_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": ['ACTION_293_object_memory_modify_bits_0']
    },
    {
        "identifier": 'ACTION_291_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_291_set_animation_speed_0']
    }
]
