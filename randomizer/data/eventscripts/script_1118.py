from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1118_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1118_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1118_action_queue_async_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1118_action_queue_async_1_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1118_action_queue_async_1_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1118_action_queue_async_1_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1118_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1118_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._011_WHOOSH_AWAY, 6]
    },
    {
        "identifier": 'EVENT_1118_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1118_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1118_action_queue_sync_4_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1118_action_queue_sync_4_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1118_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1118_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1118_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1118_action_queue_sync_6_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1118_action_queue_sync_6_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1118_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1118_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1118_action_queue_sync_7_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1118_action_queue_sync_7_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1118_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1118_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1118_action_queue_sync_8_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1118_action_queue_sync_8_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1118_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1118_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1118_action_queue_async_9_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1118_action_queue_async_9_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_11',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_13',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_15',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_16',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_17',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_18',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_19',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_20',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_21',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_22',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_23',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_24',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_25',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP]
    },
    {
        "identifier": 'EVENT_1118_remove_from_level_26',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP]
    },
    {
        "identifier": 'EVENT_1118_set_bit_27',
        "command": 'set_bit',
        "args": [0x7086, 1]
    },
    {
        "identifier": 'EVENT_1118_stop_sound_28',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_30',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_40',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_41',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_42',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_43',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_44',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_45',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_46',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_47',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_48',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_49',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_50',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_51',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_52',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_53',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_54',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_55',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_56',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_57',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_58',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_59',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_60',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_61',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_62',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_63',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_64',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_stop_sound_65',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1118_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1118_action_queue_async_66_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1118_action_queue_async_66_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1118_action_queue_async_66_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1118_action_queue_async_66_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_1118_ret_67',
        "command": 'ret'
    }
]
