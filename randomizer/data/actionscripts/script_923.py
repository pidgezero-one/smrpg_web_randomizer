from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_923_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_923_shadow_off_1',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_923_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_923_mem_700C_and_const_3',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_923_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_923_db_10']
    },
    {
        "identifier": 'ACTION_923_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_923_pause_9']
    },
    {
        "identifier": 'ACTION_923_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_923_pause_8']
    },
    {
        "identifier": 'ACTION_923_pause_7',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_923_pause_8',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_923_pause_9',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_923_db_10',
        "command": 'db',
        "args": [0x20, 0x05]
    },
    {
        "identifier": 'ACTION_923_embedded_animation_routine_11',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x80]
    },
    {
        "identifier": 'ACTION_923_embedded_animation_routine_12',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_923_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_923_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_923_pause_13']
    }
]
