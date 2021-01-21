from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_924_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_924_jmp_if_700C_any_bits_set_1',
        "command": 'jmp_if_700C_any_bits_set',
        "args": [[0, 1], 'ACTION_924_set_sprite_sequence_4']
    },
    {
        "identifier": 'ACTION_924_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_924_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_924_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_924_ret_5',
        "command": 'ret'
    }
]
