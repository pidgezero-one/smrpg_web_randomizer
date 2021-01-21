from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2317_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 0, 'EVENT_2317_jmp_if_bit_clear_2']
    },
    {
        "identifier": 'EVENT_2317_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 690]
    },
    {
        "identifier": 'EVENT_2317_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 1, 'EVENT_2317_freeze_camera_4']
    },
    {
        "identifier": 'EVENT_2317_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 690]
    },
    {
        "identifier": 'EVENT_2317_freeze_camera_4',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2317_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2317_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_5_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [0, 76]
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_5_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_5_SUBSCRIPT_shift_east_pixels_3',
                "command": 'shift_east_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2317_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2317_action_queue_sync_6_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_6_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [4, 111]
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_6_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_6_SUBSCRIPT_shift_z_down_steps_4',
                "command": 'shift_z_down_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [7, 6, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2317_action_queue_sync_6_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2317_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2317_action_queue_async_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_7_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_7_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2317_set_bit_8',
        "command": 'set_bit',
        "args": [0x708e, 0]
    },
    {
        "identifier": 'EVENT_2317_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2317_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x24, 0x1c, 0x00, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [14, 6, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [160]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_overwrite_solidity_10',
                "command": 'overwrite_solidity',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2317_action_queue_async_10_SUBSCRIPT_shift_northwest_pixels_11',
                "command": 'shift_northwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2317_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2317_unfreeze_camera_12',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2317_ret_13',
        "command": 'ret'
    }
]
