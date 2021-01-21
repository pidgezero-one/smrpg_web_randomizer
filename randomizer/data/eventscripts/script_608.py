from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_608_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_608_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_608_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_608_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_608_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_608_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_608_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_608_action_queue_sync_8']
    },
    {
        "identifier": 'EVENT_608_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_608_action_queue_sync_8']
    },
    {
        "identifier": 'EVENT_608_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_608_action_queue_sync_8']
    },
    {
        "identifier": 'EVENT_608_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_608_action_queue_sync_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 71, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_608_action_queue_sync_7_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_608_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_608_action_queue_sync_8_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_608_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_608_action_queue_sync_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_608_apply_solidity_mod_10',
        "command": 'apply_solidity_mod',
        "args": [Rooms._011_MARRYMORE_INN_3F, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_608_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 0, 'EVENT_608_remove_from_current_level_22']
    },
    {
        "identifier": 'EVENT_608_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_608_enable_controls_until_return_13',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_608_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_608_ret_21']
    },
    {
        "identifier": 'EVENT_608_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_608_ret_21']
    },
    {
        "identifier": 'EVENT_608_set_bit_16',
        "command": 'set_bit',
        "args": [0x7042, 2]
    },
    {
        "identifier": 'EVENT_608_apply_tile_mod_17',
        "command": 'apply_tile_mod',
        "args": [Rooms._011_MARRYMORE_INN_3F, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_608_apply_solidity_mod_18',
        "command": 'apply_solidity_mod',
        "args": [Rooms._011_MARRYMORE_INN_3F, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_608_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_608_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_608_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_608_action_queue_async_20_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_608_action_queue_async_20_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_608_action_queue_async_20_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [16, 101, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_608_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_608_remove_from_current_level_22',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_608_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_608_ret_24',
        "command": 'ret'
    }
]
