from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_174_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_174_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_174_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_174_add_3',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_174_load_mem_4',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_174_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_174_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_174_add_z_coord_1_step_7',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_174_pause_8',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_174_dec_z_coord_1_step_9',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_174_pause_10',
        "command": 'pause',
        "args": [27]
    },
    {
        "identifier": 'ACTION_174_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_174_add_z_coord_1_step_7']
    }
]
