from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_229_sequence_playback_off_0',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_229_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_229_walk_1_step_northwest_2',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_229_ret_3',
        "command": 'ret'
    }
]
