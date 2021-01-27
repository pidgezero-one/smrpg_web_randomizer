from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_315_shadow_on_0',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_315_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_315_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_315_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'ACTION_315_shadow_on_0']
    },
    {
        "identifier": 'ACTION_315_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_315_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 4]
    },
    {
        "identifier": 'ACTION_315_ret_6',
        "command": 'ret'
    }
]
