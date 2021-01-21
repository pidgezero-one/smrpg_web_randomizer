from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_712_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_712_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 30, 'ACTION_712_pause_11']
    },
    {
        "identifier": 'ACTION_712_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 29, 'ACTION_712_db_7']
    },
    {
        "identifier": 'ACTION_712_db_3',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_712_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_712_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_712_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_712_db_7',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_712_embedded_animation_routine_8',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_712_embedded_animation_routine_9',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_712_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_712_pause_11',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_712_db_12',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_712_embedded_animation_routine_13',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_712_embedded_animation_routine_14',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_712_ret_15',
        "command": 'ret'
    }
]
