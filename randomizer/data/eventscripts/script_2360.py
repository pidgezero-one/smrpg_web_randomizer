from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2360_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2360_action_queue_async_0_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2360_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2360_action_queue_async_1_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_1_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_1_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_1_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [14, 9, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_1_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_1_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2360_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2360_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_2360_pause_4',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'EVENT_2360_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2360_action_queue_async_5_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_5_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_5_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_5_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_5_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2360_action_queue_async_5_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_5_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2360_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2360_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2360_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2360_action_queue_async_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2360_action_queue_async_7_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2360_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._010_TRAMPOLINE, 6]
    },
    {
        "identifier": 'EVENT_2360_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2360_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2360_action_queue_sync_9_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2360_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2360_action_queue_sync_10_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2360_action_queue_sync_10_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2360_action_queue_sync_10_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x24, 0x00, 0xff, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_2360_action_queue_sync_10_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0x00, 0x0c, 0xf0, 0xff]
            },
            {
                "identifier": 'EVENT_2360_action_queue_sync_10_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2360_action_queue_sync_10_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2360_pause_11',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2360_fade_out_to_black_async_duration_12',
        "command": 'fade_out_to_black_async_duration',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2360_stop_embedded_action_script_13',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2360_stop_embedded_action_script_14',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_2360_jmp_if_var_equals_byte_15',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 220, 'EVENT_2360_set_32']
    },
    {
        "identifier": 'EVENT_2360_jmp_if_var_equals_byte_16',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 239, 'EVENT_2360_jmp_if_bit_set_38']
    },
    {
        "identifier": 'EVENT_2360_set_bit_17',
        "command": 'set_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2360_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2360_enter_area_24']
    },
    {
        "identifier": 'EVENT_2360_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'EVENT_2360_enter_area_26']
    },
    {
        "identifier": 'EVENT_2360_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 2, 'EVENT_2360_enter_area_28']
    },
    {
        "identifier": 'EVENT_2360_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 4, 'EVENT_2360_enter_area_30']
    },
    {
        "identifier": 'EVENT_2360_enter_area_22',
        "command": 'enter_area',
        "args": [Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, RadialDirections.SOUTH, 14, 99, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_2362_set_118']
    },
    {
        "identifier": 'EVENT_2360_enter_area_24',
        "command": 'enter_area',
        "args": [Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, RadialDirections.SOUTH, 4, 124, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_2362_set_40']
    },
    {
        "identifier": 'EVENT_2360_enter_area_26',
        "command": 'enter_area',
        "args": [Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, RadialDirections.SOUTH, 9, 111, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_2362_set_66']
    },
    {
        "identifier": 'EVENT_2360_enter_area_28',
        "command": 'enter_area',
        "args": [Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, RadialDirections.SOUTH, 14, 121, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_2362_set_92']
    },
    {
        "identifier": 'EVENT_2360_enter_area_30',
        "command": 'enter_area',
        "args": [Rooms._222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, RadialDirections.SOUTH, 19, 110, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_2362_set_144']
    },
    {
        "identifier": 'EVENT_2360_set_32',
        "command": 'set',
        "args": [0x70c0, 238]
    },
    {
        "identifier": 'EVENT_2360_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'EVENT_2360_enter_area_36']
    },
    {
        "identifier": 'EVENT_2360_enter_area_34',
        "command": 'enter_area',
        "args": [Rooms._220_SMITHY_FACTORY_AREA_02_WSAVE_POINT, RadialDirections.SOUTH, 5, 75, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_35',
        "command": 'jmp',
        "args": ['EVENT_2359_set_24']
    },
    {
        "identifier": 'EVENT_2360_enter_area_36',
        "command": 'enter_area',
        "args": [Rooms._220_SMITHY_FACTORY_AREA_02_WSAVE_POINT, RadialDirections.SOUTH, 10, 67, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_37',
        "command": 'jmp',
        "args": ['EVENT_2359_set_37']
    },
    {
        "identifier": 'EVENT_2360_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2360_enter_area_41']
    },
    {
        "identifier": 'EVENT_2360_enter_area_39',
        "command": 'enter_area',
        "args": [Rooms._239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, RadialDirections.NORTHEAST, 21, 53, 7, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_2409_jmp_if_bit_clear_57']
    },
    {
        "identifier": 'EVENT_2360_enter_area_41',
        "command": 'enter_area',
        "args": [Rooms._239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, RadialDirections.NORTHEAST, 29, 37, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2360_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_2409_jmp_if_bit_clear_37']
    }
]
