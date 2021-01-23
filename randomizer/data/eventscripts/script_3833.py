from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3833_jmp_if_present_in_current_level_0',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_1, 'EVENT_3833_play_sound_12']
    },
    {
        "identifier": 'EVENT_3833_freeze_camera_1',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3833_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3833_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3833_action_queue_sync_2_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3833_set_3',
        "command": 'set',
        "args": [0x70a7, 32]
    },
    {
        "identifier": 'EVENT_3833_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [32]
    },
    {
        "identifier": 'EVENT_3833_inc_5',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_3833_disable_trigger_in_level_6',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT]
    },
    {
        "identifier": 'EVENT_3833_disable_trigger_in_level_7',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    },
    {
        "identifier": 'EVENT_3833_disable_trigger_in_level_8',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT]
    },
    {
        "identifier": 'EVENT_3833_remember_last_object_9',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3833_unfreeze_camera_10',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3833_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3833_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3833_summon_to_current_level_13',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_3833_set_7000_to_current_level_14',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3833_jmp_if_7000_equals_short_15',
        "command": 'jmp_if_7000_equals_short',
        "args": [484, 'EVENT_3833_apply_tile_mod_19']
    },
    {
        "identifier": 'EVENT_3833_jmp_if_7000_equals_short_16',
        "command": 'jmp_if_7000_equals_short',
        "args": [492, 'EVENT_3833_apply_tile_mod_21']
    },
    {
        "identifier": 'EVENT_3833_apply_tile_mod_17',
        "command": 'apply_tile_mod',
        "args": [Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3833_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3833_set_action_script_sync_22']
    },
    {
        "identifier": 'EVENT_3833_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3833_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3833_set_action_script_sync_22']
    },
    {
        "identifier": 'EVENT_3833_apply_tile_mod_21',
        "command": 'apply_tile_mod',
        "args": [Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3833_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 14]
    },
    {
        "identifier": 'EVENT_3833_ret_23',
        "command": 'ret'
    }
]
