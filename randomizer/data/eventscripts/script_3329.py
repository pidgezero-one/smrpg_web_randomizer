from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3329_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3329_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3329_jmp_if_7000_not_equals_short_2',
        "command": 'jmp_if_7000_not_equals_short',
        "args": [0, 'EVENT_3329_pause_0']
    },
    {
        "identifier": 'EVENT_3329_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_3329_pause_0']
    },
    {
        "identifier": 'EVENT_3329_enable_controls_4',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3329_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_3329_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_jmp_0',
                "command": 'jmp',
                "args": ['EVENT_3329_non_embedded_action_queue_9']
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_set_bit_2',
                "command": 'set_bit',
                "args": [0x7044, 4]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3329_action_queue_async_6_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_set_700C_to_object_coord_9',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_0, Coords.F, []]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_face_east_7C_10',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3329_action_queue_async_6_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x3a]
            }
        ]
    },
    {
        "identifier": 'EVENT_3329_enable_controls_7',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3329_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3329_pause_0']
    },
    {
        "identifier": 'EVENT_3329_non_embedded_action_queue_9',
        "command": 'non_embedded_action_queue',
        "subscript": [
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_face_southwest_7D_0',
                "command": 'face_southwest_7D',
                "args": [0x14]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_700C_to_object_coord_1',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_700C_equals_short_2',
                "command": 'jmp_if_700C_equals_short',
                "args": [7, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_10']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_700C_equals_short_3',
                "command": 'jmp_if_700C_equals_short',
                "args": [0, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_10']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_700C_equals_short_4',
                "command": 'jmp_if_700C_equals_short',
                "args": [1, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_12']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_700C_equals_short_5',
                "command": 'jmp_if_700C_equals_short',
                "args": [2, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_12']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_700C_equals_short_6',
                "command": 'jmp_if_700C_equals_short',
                "args": [3, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_14']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_700C_equals_short_7',
                "command": 'jmp_if_700C_equals_short',
                "args": [4, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_16']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_700C_equals_short_8',
                "command": 'jmp_if_700C_equals_short',
                "args": [5, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_16']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_700C_equals_short_9',
                "command": 'jmp_if_700C_equals_short',
                "args": [6, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_16']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [9, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_11',
                "command": 'jmp',
                "args": ['EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_17']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [8, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_13',
                "command": 'jmp',
                "args": ['EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_17']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [8, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_15',
                "command": 'jmp',
                "args": ['EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_17']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [9, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_17',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x69]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_18',
                "command": 'db',
                "args": [0x3a, 0x14, 0x00, 0x08, 0xa2, 0x40]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_19',
                "command": 'db',
                "args": [0x3a, 0x14, 0x00, 0x10, 0x9c, 0x40]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_20',
                "command": 'db',
                "args": [0x3a, 0x14, 0x00, 0x1c, 0x96, 0x40]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_21',
                "command": 'jump_to_height_silent',
                "args": [384]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_22',
                "command": 'jmp',
                "args": ['EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_28']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_23',
                "command": 'jump_to_height_silent',
                "args": [320]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_24',
                "command": 'jmp',
                "args": ['EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_28']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_25',
                "command": 'jump_to_height_silent',
                "args": [256]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_26',
                "command": 'jmp',
                "args": ['EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_28']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jump_to_height_silent_27',
                "command": 'jump_to_height_silent',
                "args": [192]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_28',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._047_BLUE_FIRE_TRAIL_FOLLOWS_OBJECT, AreaObjects.MARIO, 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_clear_solidity_bits_29']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_clear_solidity_bits_29',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_clear_solidity_bits_31',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_32',
                "command": 'db',
                "args": [0xc8, 0x14]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_db_33',
                "command": 'db',
                "args": [0xfd, 0xc7]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_animation_speed_34',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_run_away_shift_35',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_set_solidity_bits_36',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_pause_37',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_if_mario_in_air_38',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_pause_37']
            },
            {
                "identifier": 'EVENT_3329_non_embedded_action_queue_9_SUBSCRIPT_jmp_39',
                "command": 'jmp',
                "args": ['EVENT_3329_action_queue_async_6_SUBSCRIPT_set_solidity_bits_1']
            }
        ]
    }
]
