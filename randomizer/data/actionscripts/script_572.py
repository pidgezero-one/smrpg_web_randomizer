from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_572_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_572_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_572_pause_2',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_572_visibility_off_3',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_572_ret_4',
        "command": 'ret'
    }
]
