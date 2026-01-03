
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_262_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_262_transfer_xyzf_pixels_1',
        "command": 'transfer_xyzf_pixels',
        "args": [251, 1, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_262_ret_2',
        "command": 'ret'
    }
]
