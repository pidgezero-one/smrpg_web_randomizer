from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_319_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_319_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_319_set_palette_row_2',
        "command": 'set_palette_row',
        "args": [4]
    },
    {
        "identifier": 'ACTION_319_pause_3',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_319_create_packet_at_object_coords_jmp_if_null_4',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._024_BOMB_EXPLOSION_SFX, AreaObjects.DUMMY_0X07, 'ACTION_319_visibility_on_5']
    },
    {
        "identifier": 'ACTION_319_visibility_on_5',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_319_object_memory_clear_bit_6',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_319_set_solidity_bits_7',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_319_start_loop_n_times_8',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_319_shadow_on_9',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_319_walk_1_step_southeast_10',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_319_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_319_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 4]
    },
    {
        "identifier": 'ACTION_319_visibility_off_13',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_319_object_memory_set_bit_14',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_319_ret_15',
        "command": 'ret'
    }
]
