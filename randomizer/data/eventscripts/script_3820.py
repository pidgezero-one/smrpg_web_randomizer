from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3820_jmp_if_object_trigger_disabled_0',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_jmp_to_subroutine_1',
        "command": 'jmp_to_subroutine',
        "args": [0xd837],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_set_short_2',
        "command": 'set_short',
        "args": [0x7022, 0x0008],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_run_background_event_with_pause_3',
        "command": 'run_background_event_with_pause',
        "args": [3075, 0x7022, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3820_action_queue_async_4_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3820_action_queue_async_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3820_action_queue_async_4_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            },
        ]
    },
    {
        "identifier": 'EVENT_3820_pause_5',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3820_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3820_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3820_action_queue_async_7_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [5, 97]
            },
            {
                "identifier": 'EVENT_3820_action_queue_async_7_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3820_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_start_embedded_action_script_async_9',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3820_start_embedded_action_script_async_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3820_start_embedded_action_script_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3820_start_embedded_action_script_async_9_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3820_start_embedded_action_script_async_9_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [6, 96]
            },
            {
                "identifier": 'EVENT_3820_start_embedded_action_script_async_9_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3820_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_pause_11',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_run_dialog_12',
        "command": 'run_dialog',
        "args": [3754, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_pause_13',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3820_action_queue_sync_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3820_action_queue_sync_14_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3820_action_queue_sync_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3820_action_queue_sync_14_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [13, 91, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3820_jmp_to_subroutine_15',
        "command": 'jmp_to_subroutine',
        "args": [0xd86f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3820_action_queue_sync_16_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3820_action_queue_sync_16_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3820_action_queue_sync_16_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3820_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3820_action_queue_async_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3820_action_queue_async_17_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3820_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 978],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_restore_all_hp_19',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_restore_all_fp_20',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3820_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3818_clear_bit_64'],
        "subscript": []
    },
]
