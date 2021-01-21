from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_927_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_927_shift_southeast_pixels_1',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_927_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_927_jump_to_subroutine_3',
        "command": 'jump_to_subroutine',
        "args": [0x3801]
    },
    {
        "identifier": 'ACTION_927_transfer_xyzf_steps_4',
        "command": 'transfer_xyzf_steps',
        "args": [0, 0, 20, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_927_pause_5',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_927_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_927_jump_to_subroutine_3']
    }
]
