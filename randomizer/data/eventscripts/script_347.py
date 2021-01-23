from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_347_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_347_action_queue_async_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_347_action_queue_async_0_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_347_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 2, 'EVENT_347_pause_action_script_13']
    },
    {
        "identifier": 'EVENT_347_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_347_pause_action_script_6']
    },
    {
        "identifier": 'EVENT_347_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_347_pause_action_script_6']
    },
    {
        "identifier": 'EVENT_347_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_347_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_347_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_347_start_embedded_action_script_async_F1_7',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_347_start_embedded_action_script_async_F1_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 64, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_347_start_embedded_action_script_async_F1_7_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_347_start_embedded_action_script_async_F1_7_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_347_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 119]
    },
    {
        "identifier": 'EVENT_347_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x705d, 1, 'EVENT_347_fade_in_from_black_async_11']
    },
    {
        "identifier": 'EVENT_347_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_347_action_queue_async_10_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 63, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_347_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_347_action_queue_async_10_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_347_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_347_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_347_pause_action_script_13',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_347_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_347_action_queue_sync_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 66, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_347_action_queue_sync_14_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_347_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_347_action_queue_async_15_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 57, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_347_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_347_action_queue_async_15_SUBSCRIPT_object_memory_clear_bit_2',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_347_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_347_ret_17',
        "command": 'ret'
    }
]
