from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_458_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_458_action_queue_async_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_458_action_queue_async_0_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [7, 65]
            },
            {
                "identifier": 'EVENT_458_action_queue_async_0_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_458_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7061, 7]
    },
    {
        "identifier": 'EVENT_458_db_2',
        "command": 'db',
        "args": [0xfd, 0x45]
    },
    {
        "identifier": 'EVENT_458_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_458_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_458_enable_controls_5',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_458_start_embedded_action_script_async_6',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_6_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, []]
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_6_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [10, 81, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_6_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_6_SUBSCRIPT_object_memory_set_bit_3',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_6_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_6_SUBSCRIPT_clear_solidity_bits_5',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_458_start_embedded_action_script_async_7',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 6, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_7_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_7_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_7_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [10, 81, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_458_start_embedded_action_script_async_7_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_458_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": [0x42a2]
    },
    {
        "identifier": 'EVENT_458_fade_in_from_black_sync_duration_9',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_458_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_458_jmp_to_event_13']
    },
    {
        "identifier": 'EVENT_458_run_background_event_11',
        "command": 'run_background_event',
        "args": [465, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_458_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_458_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [3601]
    }
]
