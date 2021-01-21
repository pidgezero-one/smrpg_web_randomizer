from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_513_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_513_shift_southwest_steps_1',
        "command": 'shift_southwest_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_513_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_513_visibility_off_3',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_513_ret_4',
        "command": 'ret'
    }
]
