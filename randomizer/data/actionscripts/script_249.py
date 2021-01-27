from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_249_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_249_pause_1',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_249_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._146_MACHINE_TRANSFORM, 4]
    },
    {
        "identifier": 'ACTION_249_pause_3',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_249_visibility_off_4',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_249_set_bit_5',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_249_ret_6',
        "command": 'ret'
    }
]
