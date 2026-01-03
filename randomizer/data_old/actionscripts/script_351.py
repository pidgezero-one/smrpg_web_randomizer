
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_351_jmp_if_var_equals_const_0',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70df, 50, 'ACTION_351_set_animation_speed_28']
    },
    {
        "identifier": 'ACTION_351_db_19',
        "command": 'db',
        "args": [0xc8, 0x00]
    },
    {
        "identifier": 'ACTION_351_transfer_to_7016_7018_20',
        "command": 'transfer_to_7016_7018'
    },
    {
        "identifier": 'ACTION_351_set_priority_21',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_351_set_vram_priority_22',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_351_visibility_on_23',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_351_pause_24',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_351_visibility_off_25',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_351_pause_26',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_351_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_351_visibility_on_23']
    },
    {
        "identifier": 'ACTION_351_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_351_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_351_walk_1_step_f_direction_30',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_351_turn_random_direction_31',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_351_walk_1_step_f_direction_32',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_351_jmp_if_random_above_128_33',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_351_set_animation_speed_28']
    },
    {
        "identifier": 'ACTION_351_face_mario_34',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_351_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_351_set_animation_speed_36',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_351_walk_1_step_f_direction_37',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_351_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_351_set_animation_speed_28']
    }
]
