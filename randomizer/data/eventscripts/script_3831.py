from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_disabled_0',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, 'EVENT_3831_set_7000_to_current_level_25']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_disabled_1',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, 'EVENT_3831_set_7000_to_current_level_25']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_disabled_2',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, 'EVENT_3831_set_7000_to_current_level_25']
    },
    {
        "identifier": 'EVENT_3831_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3831_action_queue_async_3_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_disabled_4',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, 'EVENT_3831_set_7000_to_current_level_34']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_disabled_5',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, 'EVENT_3831_set_7000_to_current_level_34']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_disabled_6',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, 'EVENT_3831_set_7000_to_current_level_34']
    },
    {
        "identifier": 'EVENT_3831_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3831_action_queue_async_7_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3831_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 6, 'EVENT_3831_jmp_if_bit_clear_10']
    },
    {
        "identifier": 'EVENT_3831_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3831_action_queue_async_9_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 42, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3831_action_queue_async_9_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3831_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x705e, 6, 'EVENT_3831_fade_in_from_black_async_12']
    },
    {
        "identifier": 'EVENT_3831_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 128]
    },
    {
        "identifier": 'EVENT_3831_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3831_run_event_as_subroutine_13',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_3831_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_enabled_15',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_1, Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, 'EVENT_3831_clear_bit_22']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_enabled_16',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_1, Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, 'EVENT_3831_clear_bit_22']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_enabled_17',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_1, Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, 'EVENT_3831_clear_bit_22']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_enabled_18',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_0, Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, 'EVENT_3831_clear_bit_22']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_enabled_19',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_0, Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, 'EVENT_3831_clear_bit_22']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_object_trigger_enabled_20',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_0, Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, 'EVENT_3831_clear_bit_22']
    },
    {
        "identifier": 'EVENT_3831_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3831_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_3831_play_sound_23',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_3831_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3831_set_7000_to_current_level_25',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3831_jmp_if_7000_equals_short_26',
        "command": 'jmp_if_7000_equals_short',
        "args": [484, 'EVENT_3831_apply_tile_mod_30']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_7000_equals_short_27',
        "command": 'jmp_if_7000_equals_short',
        "args": [492, 'EVENT_3831_apply_tile_mod_32']
    },
    {
        "identifier": 'EVENT_3831_apply_tile_mod_28',
        "command": 'apply_tile_mod',
        "args": [Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3831_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_3831_jmp_if_object_trigger_disabled_4']
    },
    {
        "identifier": 'EVENT_3831_apply_tile_mod_30',
        "command": 'apply_tile_mod',
        "args": [Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3831_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_3831_jmp_if_object_trigger_disabled_4']
    },
    {
        "identifier": 'EVENT_3831_apply_tile_mod_32',
        "command": 'apply_tile_mod',
        "args": [Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3831_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_3831_jmp_if_object_trigger_disabled_4']
    },
    {
        "identifier": 'EVENT_3831_set_7000_to_current_level_34',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3831_jmp_if_7000_equals_short_35',
        "command": 'jmp_if_7000_equals_short',
        "args": [484, 'EVENT_3831_apply_tile_mod_39']
    },
    {
        "identifier": 'EVENT_3831_jmp_if_7000_equals_short_36',
        "command": 'jmp_if_7000_equals_short',
        "args": [492, 'EVENT_3831_apply_tile_mod_41']
    },
    {
        "identifier": 'EVENT_3831_apply_tile_mod_37',
        "command": 'apply_tile_mod',
        "args": [Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3831_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_3831_jmp_if_bit_set_8']
    },
    {
        "identifier": 'EVENT_3831_apply_tile_mod_39',
        "command": 'apply_tile_mod',
        "args": [Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3831_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_3831_jmp_if_bit_set_8']
    },
    {
        "identifier": 'EVENT_3831_apply_tile_mod_41',
        "command": 'apply_tile_mod',
        "args": [Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3831_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_3831_jmp_if_bit_set_8']
    }
]
