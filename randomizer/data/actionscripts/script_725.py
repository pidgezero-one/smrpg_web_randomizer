from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_725_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_725_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_725_object_memory_set_bit_2',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_725_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_725_jmp_if_object_in_level_4',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_0, Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, 'ACTION_725_ret_27']
    },
    {
        "identifier": 'ACTION_725_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM, 'ACTION_725_ret_27']
    },
    {
        "identifier": 'ACTION_725_set_short_6',
        "command": 'set_short',
        "args": [0x7024, 0x0384]
    },
    {
        "identifier": 'ACTION_725_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'ACTION_725_set_bit_11']
    },
    {
        "identifier": 'ACTION_725_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_725_dec_short_9',
        "command": 'dec_short',
        "args": [0x7024]
    },
    {
        "identifier": 'ACTION_725_jmp_if_loaded_memory_is_not_0_10',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['ACTION_725_jmp_if_bit_set_7']
    },
    {
        "identifier": 'ACTION_725_set_bit_11',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_725_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'ACTION_725_remove_from_level_13',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'ACTION_725_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_725_visibility_on_15',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_725_object_memory_clear_bit_16',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_725_set_solidity_bits_17',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_725_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._048_MINECART_START, 4]
    },
    {
        "identifier": 'ACTION_725_walk_to_xy_coords_19',
        "command": 'walk_to_xy_coords',
        "args": [2, 124]
    },
    {
        "identifier": 'ACTION_725_fade_out_sound_to_volume_20',
        "command": 'fade_out_sound_to_volume',
        "args": [1, 0]
    },
    {
        "identifier": 'ACTION_725_visibility_off_21',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_725_object_memory_set_bit_22',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_725_clear_solidity_bits_23',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_725_db_24',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_725_summon_to_level_25',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM]
    },
    {
        "identifier": 'ACTION_725_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_725_ret_27',
        "command": 'ret'
    }
]
