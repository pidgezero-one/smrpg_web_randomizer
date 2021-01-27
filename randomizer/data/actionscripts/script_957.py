from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_957_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_957_shift_west_pixels_1',
        "command": 'shift_west_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_957_visibility_off_2',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_957_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_957_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_957_visibility_off_2']
    },
    {
        "identifier": 'ACTION_957_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_957_visibility_on_6',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_957_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_957_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._146_MACHINE_TRANSFORM, 4]
    },
    {
        "identifier": 'ACTION_957_pause_9',
        "command": 'pause',
        "args": [36]
    },
    {
        "identifier": 'ACTION_957_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_957_visibility_off_2']
    }
]
