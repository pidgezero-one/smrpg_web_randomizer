from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2347_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7048, 1, 'EVENT_2347_ret_19']
    },
    {
        "identifier": 'EVENT_2347_set_bit_1',
        "command": 'set_bit',
        "args": [0x7048, 1]
    },
    {
        "identifier": 'EVENT_2347_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2347_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_2_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2347_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x25, 0x40, 0x00, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_bpl_26_27_28_14',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_3_SUBSCRIPT_sequence_looping_off_16',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2347_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [44]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2347_action_queue_sync_4_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2347_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2347_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2347_action_queue_async_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2347_action_queue_async_6_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2347_action_queue_async_6_SUBSCRIPT_pause_5']
            },
            {
                "identifier": 'EVENT_2347_action_queue_async_6_SUBSCRIPT_jmp_2',
                "command": 'jmp',
                "args": ['EVENT_2347_action_queue_async_6_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_2347_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2347_action_queue_async_6_SUBSCRIPT_face_south_4',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2347_action_queue_async_6_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [24]
            }
        ]
    },
    {
        "identifier": 'EVENT_2347_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 401]
    },
    {
        "identifier": 'EVENT_2347_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2347_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 385]
    },
    {
        "identifier": 'EVENT_2347_set_10',
        "command": 'set',
        "args": [0x70a7, 125]
    },
    {
        "identifier": 'EVENT_2347_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2347_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2347_remove_from_level_13',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2347_summon_to_level_14',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2347_disable_trigger_in_level_15',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_2347_run_dialog_16',
        "command": 'run_dialog',
        "args": [3166, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2347_put_inventory_17',
        "command": 'put_inventory',
        "args": [items.GoodieBag]
    },
    {
        "identifier": 'EVENT_2347_inc_18',
        "command": 'inc',
        "args": [0x70c8]
    },
    {
        "identifier": 'EVENT_2347_ret_19',
        "command": 'ret'
    }
]
