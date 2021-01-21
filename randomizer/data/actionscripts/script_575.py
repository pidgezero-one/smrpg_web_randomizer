from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_575_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_575_shift_east_steps_1',
        "command": 'shift_east_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_575_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_575_shift_east_steps_1']
    }
]
