from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2357_enable_controls_0',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2357_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._248_GAME_INTRO_MUSHROOM_WAY_AREA_01, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2357_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._248_GAME_INTRO_MUSHROOM_WAY_AREA_01, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2357_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2357_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2357_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2357_action_queue_sync_4_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [12, 28]
            }
        ]
    },
    {
        "identifier": 'EVENT_2357_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2357_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 44, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2357_action_queue_async_5_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2357_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 838]
    },
    {
        "identifier": 'EVENT_2357_pause_7',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_2357_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2357_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2357_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2357_set_action_script_sync_12']
    },
    {
        "identifier": 'EVENT_2357_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_2357_pause_9']
    },
    {
        "identifier": 'EVENT_2357_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 839]
    },
    {
        "identifier": 'EVENT_2357_pause_13',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2357_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 832]
    },
    {
        "identifier": 'EVENT_2357_pause_15',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'EVENT_2357_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 839]
    },
    {
        "identifier": 'EVENT_2357_pause_17',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2357_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 832]
    },
    {
        "identifier": 'EVENT_2357_pause_19',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2357_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2357_remove_from_current_level_22']
    },
    {
        "identifier": 'EVENT_2357_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_2357_pause_19']
    },
    {
        "identifier": 'EVENT_2357_remove_from_current_level_22',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2357_remove_from_current_level_23',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2357_remove_from_current_level_24',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2357_remove_from_current_level_25',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2357_remove_from_current_level_26',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2357_circle_mask_nonstatic_27',
        "command": 'circle_mask_nonstatic',
        "args": [AreaObjects.MARIO, 24, 5]
    },
    {
        "identifier": 'EVENT_2357_pause_28',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_2357_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2357_remove_from_current_level_30',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2357_remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2357_display_intro_title_32',
        "command": 'display_intro_title',
        "args": [17, IntroTitles.SUPER_MARIO]
    },
    {
        "identifier": 'EVENT_2357_pause_33',
        "command": 'pause',
        "args": [150]
    },
    {
        "identifier": 'EVENT_2357_fade_out_to_black_async_duration_34',
        "command": 'fade_out_to_black_async_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2357_jmp_to_event_35',
        "command": 'jmp_to_event',
        "args": [129]
    },
    {
        "identifier": 'EVENT_2357_ret_36',
        "command": 'ret'
    }
]
