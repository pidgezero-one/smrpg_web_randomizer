from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_473_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_473_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_473_add_2',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_473_load_mem_3',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_473_pause_4',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_473_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_473_shadow_on_6',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_473_db_7',
        "command": 'db',
        "args": [0x20, 0x05]
    },
    {
        "identifier": 'ACTION_473_embedded_animation_routine_8',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80]
    },
    {
        "identifier": 'ACTION_473_shift_northwest_steps_9',
        "command": 'shift_northwest_steps',
        "args": [14]
    },
    {
        "identifier": 'ACTION_473_walk_1_step_northeast_10',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_473_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [14]
    },
    {
        "identifier": 'ACTION_473_walk_1_step_southwest_12',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_473_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_473_shift_northwest_steps_9']
    }
]
