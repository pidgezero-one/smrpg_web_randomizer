from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_77_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_77_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [21, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_77_pause_2',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_77_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_77_pause_4',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_77_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [13, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_77_ret_6',
        "command": 'ret'
    }
]
