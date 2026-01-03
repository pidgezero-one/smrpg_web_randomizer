
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3819_jmp_if_object_trigger_disabled_0',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_2, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3819_jmp_to_subroutine_1',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3818_disable_trigger_21']
    },
    {
        "identifier": 'EVENT_3819_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3819_action_queue_async_2_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_2_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            }
        ]
    },
    {
        "identifier": 'EVENT_3819_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3819_jmp_if_mario_in_air_4',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3819_pause_3']
    },
    {
        "identifier": 'EVENT_3819_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [4, 94]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_5_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3819_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_3819_start_embedded_action_script_async_F1_7',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3819_start_embedded_action_script_async_F1_7_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3819_start_embedded_action_script_async_F1_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3819_start_embedded_action_script_async_F1_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3819_start_embedded_action_script_async_F1_7_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [4, 93]
            },
            {
                "identifier": 'EVENT_3819_start_embedded_action_script_async_F1_7_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3819_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 636]
    },
    {
        "identifier": 'EVENT_3819_pause_9',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3819_run_dialog_10',
        "command": 'run_dialog',
        "args": [3753, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3819_pause_11',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3819_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3819_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3819_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3819_action_queue_sync_12_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3819_action_queue_sync_12_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [13, 91, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3819_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3818_action_queue_sync_34']
    },
    {
        "identifier": 'EVENT_3819_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3819_action_queue_async_14_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3819_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 978]
    },
    {
        "identifier": 'EVENT_3819_set_16',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3819_add_max_FP_7000_17',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_3819_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3819_action_queue_async_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3819_action_queue_async_18_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3819_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3819_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3818_clear_bit_38']
    }
]
