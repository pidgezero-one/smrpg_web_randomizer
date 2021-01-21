from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_475_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_475_add_1',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_475_load_mem_2',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_475_pause_3',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_475_end_loop_4',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_475_visibility_on_5',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_475_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_475_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_475_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_714_turn_clockwise_45_degrees_12']
    }
]
