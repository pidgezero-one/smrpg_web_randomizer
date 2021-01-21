from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_962_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_962_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_962_shift_southwest_pixels_2',
        "command": 'shift_southwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_962_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_962_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_962_pause_3']
    },
    {
        "identifier": 'ACTION_962_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_962_pause_6',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_962_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_962_pause_8',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_962_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_962_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_962_pause_3']
    }
]
