from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_303_transfer_xyzf_pixels_0',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 248, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_303_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_303_pause_2',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_303_ret_3',
        "command": 'ret'
    }
]
