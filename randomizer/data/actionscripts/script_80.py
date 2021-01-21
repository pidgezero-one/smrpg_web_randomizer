from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_80_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_80_start_loop_n_times_1',
        "command": 'start_loop_n_times',
        "args": [8]
    },
    {
        "identifier": 'ACTION_80_visibility_on_2',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_80_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_80_pause_4',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_80_visibility_off_5',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_80_shift_southeast_steps_6',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_80_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_80_start_loop_n_times_8',
        "command": 'start_loop_n_times',
        "args": [8]
    },
    {
        "identifier": 'ACTION_80_visibility_on_9',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_80_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_80_pause_11',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_80_visibility_off_12',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_80_shift_northwest_steps_13',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_80_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_80_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_80_set_animation_speed_0']
    }
]
