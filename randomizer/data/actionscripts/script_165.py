from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_165_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._012_DIZZINESS, 4]
    },
    {
        "identifier": 'ACTION_165_sequence_playback_off_1',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_165_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_165_walk_1_step_southeast_3',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_165_ret_4',
        "command": 'ret'
    }
]
