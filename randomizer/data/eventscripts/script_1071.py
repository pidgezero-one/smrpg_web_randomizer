from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 1, 'EVENT_1071_ret_39']
    },
    {
        "identifier": 'EVENT_1071_set_1',
        "command": 'set',
        "args": [0x7000, 0]
    },
    {
        "identifier": 'EVENT_1071_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [7, 48]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_set_priority_9',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_2_SUBSCRIPT_set_vram_priority_10',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1071_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1071_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_async_3_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 32, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1071_freeze_camera_4',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 2, 'EVENT_1071_set_short_33']
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1071_jmp_if_bit_clear_9']
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 6, 'EVENT_1071_jmp_if_bit_clear_9']
    },
    {
        "identifier": 'EVENT_1071_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1071_action_queue_async_8_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [14, 25]
            },
            {
                "identifier": 'EVENT_1071_action_queue_async_8_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1071_action_queue_async_8_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1071_action_queue_async_8_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_1071_jmp_if_bit_clear_12']
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 157]
    },
    {
        "identifier": 'EVENT_1071_pause_11',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_12',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_1071_jmp_if_bit_clear_15']
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 157]
    },
    {
        "identifier": 'EVENT_1071_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_1071_jmp_if_bit_clear_18']
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 157]
    },
    {
        "identifier": 'EVENT_1071_pause_17',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_18',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_1071_jmp_if_bit_clear_21']
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 157]
    },
    {
        "identifier": 'EVENT_1071_pause_20',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'EVENT_1071_jmp_if_bit_clear_24']
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 157]
    },
    {
        "identifier": 'EVENT_1071_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_24',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 5, 'EVENT_1071_jmp_if_bit_clear_27']
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 157]
    },
    {
        "identifier": 'EVENT_1071_pause_26',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_27',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 6, 'EVENT_1071_jmp_if_bit_clear_30']
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 157]
    },
    {
        "identifier": 'EVENT_1071_pause_29',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1071_jmp_if_bit_clear_30',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 7, 'EVENT_1071_set_short_33']
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 157]
    },
    {
        "identifier": 'EVENT_1071_pause_32',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1071_set_short_33',
        "command": 'set_short',
        "args": [0x7010, 0x0003]
    },
    {
        "identifier": 'EVENT_1071_set_34',
        "command": 'set',
        "args": [0x70a9, 20]
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 515]
    },
    {
        "identifier": 'EVENT_1071_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1071_action_queue_sync_36_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 43, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_36_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_36_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1071_action_queue_sync_36_SUBSCRIPT_ret_3',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1071_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 570]
    },
    {
        "identifier": 'EVENT_1071_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_0']
    },
    {
        "identifier": 'EVENT_1071_ret_39',
        "command": 'ret'
    }
]
