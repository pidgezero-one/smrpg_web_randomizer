from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_689_pause_0',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'ACTION_689_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_689_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_689_shift_northwest_pixels_3',
        "command": 'shift_northwest_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_689_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_689_visibility_on_5',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_689_db_6',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_689_embedded_animation_routine_7',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0xf0, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80]
    },
    {
        "identifier": 'ACTION_689_embedded_animation_routine_8',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0xf0, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80]
    },
    {
        "identifier": 'ACTION_689_embedded_animation_routine_9',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0xf0, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_689_shift_z_down_steps_10',
        "command": 'shift_z_down_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_689_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_689_ret_12',
        "command": 'ret'
    }
]
