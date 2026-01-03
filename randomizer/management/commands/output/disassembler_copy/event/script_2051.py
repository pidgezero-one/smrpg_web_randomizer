
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2051_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 7, 'EVENT_2051_action_queue_sync_6']
    },
    {
        "identifier": 'EVENT_2051_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2051_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_1_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [11, 5, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2051_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2051_action_queue_async_2_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 16, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_2_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_2_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_2_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_2_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_2_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_2_SUBSCRIPT_shadow_on_6',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2051_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2051_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2052_pause_0']
    },
    {
        "identifier": 'EVENT_2051_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2051_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2051_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_6_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [15, 19, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_6_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_6_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_6_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_6_SUBSCRIPT_sequence_looping_on_6',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_6_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2051_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [13, 17, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_7_SUBSCRIPT_shadow_on_9',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2051_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [14, 18, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_sync_8_SUBSCRIPT_shadow_on_9',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2051_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [14, 19, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2051_action_queue_async_9_SUBSCRIPT_shadow_on_9',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2051_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 878]
    },
    {
        "identifier": 'EVENT_2051_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 879]
    },
    {
        "identifier": 'EVENT_2051_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 879]
    },
    {
        "identifier": 'EVENT_2051_apply_solidity_mod_13',
        "command": 'apply_solidity_mod',
        "args": [Rooms._398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2051_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2051_ret_15',
        "command": 'ret'
    }
]
