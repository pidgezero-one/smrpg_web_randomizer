from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_292_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_292_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_292_set_priority_2',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_292_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_292_jmp_if_random_above_66_4',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_291_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_292_jump_to_subroutine_5',
        "command": 'jump_to_subroutine',
        "args": [0x3586]
    },
    {
        "identifier": 'ACTION_292_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_291_set_animation_speed_0']
    }
]
