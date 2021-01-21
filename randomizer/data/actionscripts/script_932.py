from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_932_transfer_xyzf_pixels_0',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 0, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_932_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_932_pause_2',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_932_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_932_pause_2']
    },
    {
        "identifier": 'ACTION_932_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_932_pause_5',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_932_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_932_pause_7',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_932_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_932_transfer_xyzf_pixels_0']
    }
]
