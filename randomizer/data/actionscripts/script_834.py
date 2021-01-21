from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_834_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_834_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_834_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_834_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [16]
    },
    {
        "identifier": 'ACTION_834_ret_4',
        "command": 'ret'
    }
]
