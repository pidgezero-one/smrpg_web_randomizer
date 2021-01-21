from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_307_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_307_shift_southeast_pixels_1',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_307_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_307_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_307_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 25, 'ACTION_307_jump_to_subroutine_6']
    },
    {
        "identifier": 'ACTION_307_pause_5',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_307_jump_to_subroutine_6',
        "command": 'jump_to_subroutine',
        "args": [0x3885]
    },
    {
        "identifier": 'ACTION_307_transfer_xyzf_steps_7',
        "command": 'transfer_xyzf_steps',
        "args": [0, 0, 10, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_307_pause_8',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_307_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_307_jump_to_subroutine_6']
    }
]
