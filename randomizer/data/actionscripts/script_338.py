from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_338_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_338_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_338_pause_2',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_338_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'ACTION_338_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_338_inc_palette_row_by_5',
        "command": 'inc_palette_row_by',
        "args": [2]
    },
    {
        "identifier": 'ACTION_338_visibility_on_6',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_338_floating_on_7',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_338_jump_to_height_silent_8',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_338_set_solidity_bits_9',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_338_set_vram_priority_10',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_338_pause_11',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_338_ret_12',
        "command": 'ret'
    }
]
