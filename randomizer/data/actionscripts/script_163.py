from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_163_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_163_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [422, 'ACTION_163_shadow_on_3']
    },
    {
        "identifier": 'ACTION_163_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_163_shadow_on_3',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_163_set_priority_4',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_163_set_700C_to_pressed_button_5',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_163_add_6',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_163_load_mem_7',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_163_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_163_end_loop_9',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_163_sequence_looping_on_10',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_163_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_163_ret_12',
        "command": 'ret'
    }
]
