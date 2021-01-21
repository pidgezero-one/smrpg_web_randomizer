from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1722_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7094, 2, 'EVENT_1722_action_queue_sync_2']
    },
    {
        "identifier": 'EVENT_1722_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_18]
    },
    {
        "identifier": 'EVENT_1722_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1722_action_queue_sync_2_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1722_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1722_action_queue_sync_3_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1722_fade_in_from_black_sync_4',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1722_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 0, 'EVENT_1722_jmp_if_bit_clear_8']
    },
    {
        "identifier": 'EVENT_1722_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_walk_1_step_south_5',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_jmp_if_mario_in_air_10',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1722_action_queue_async_6_SUBSCRIPT_pause_9']
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_6_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1722_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_1722_set_action_script_sync_10']
    },
    {
        "identifier": 'EVENT_1722_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 7, 'EVENT_1722_set_action_script_sync_10']
    },
    {
        "identifier": 'EVENT_1722_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_walk_1_step_south_3',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_floating_on_5',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1722_action_queue_async_9_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_1722_action_queue_async_9_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1722_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 823]
    },
    {
        "identifier": 'EVENT_1722_set_bit_11',
        "command": 'set_bit',
        "args": [0x7094, 3]
    },
    {
        "identifier": 'EVENT_1722_set_bit_12',
        "command": 'set_bit',
        "args": [0x707b, 7]
    },
    {
        "identifier": 'EVENT_1722_set_short_13',
        "command": 'set_short',
        "args": [0x702e, 0x0030]
    },
    {
        "identifier": 'EVENT_1722_set_short_14',
        "command": 'set_short',
        "args": [0x702c, 0x0046]
    },
    {
        "identifier": 'EVENT_1722_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [300]
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_set_short_5',
                "command": 'set_short',
                "args": [0x7034, 0x8006]
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_6',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._032_BLUE_CLOUD, AreaObjects.DUMMY_0X07, 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_shift_z_up_pixels_8',
                "command": 'shift_z_up_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1722_action_queue_sync_15_SUBSCRIPT_jmp_9',
                "command": 'jmp',
                "args": ['EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_2']
            }
        ]
    },
    {
        "identifier": 'EVENT_1722_ret_16',
        "command": 'ret'
    }
]
