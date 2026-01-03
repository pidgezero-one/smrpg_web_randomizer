
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3951_enter_area_280',
        "command": 'enter_area',
        "args": [Rooms._375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, RadialDirections.NORTHWEST, 4, 48, 0, []]
    },
    {
        "identifier": 'EVENT_3951_run_star_piece_sequence_281',
        "command": 'run_star_piece_sequence',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3951_palette_set_282',
        "command": 'palette_set',
        "args": [163, 1, [3]]
    },
    {
        "identifier": 'EVENT_3951_palette_set_283',
        "command": 'palette_set',
        "args": [164, 1, [0, 3]]
    },
    {
        "identifier": 'EVENT_3951_palette_set_284',
        "command": 'palette_set',
        "args": [166, 1, [1, 3]]
    },
    {
        "identifier": 'EVENT_3951_palette_set_285',
        "command": 'palette_set',
        "args": [167, 1, [0, 1, 3]]
    },
    {
        "identifier": 'EVENT_3951_palette_set_286',
        "command": 'palette_set',
        "args": [165, 1, [0, 2, 3]]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_287',
        "command": 'action_queue',
        'args': [AreaObjects.SCREEN_FOCUS, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_287_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_287_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_287_SUBSCRIPT_walk_1_step_north_2',
                "command": 'walk_1_step_north'
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_288',
        "command": 'action_queue',
        'args': [AreaObjects.LAYER_2, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_288_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_288_SUBSCRIPT_walk_1_step_west_1',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_288_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_289',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_289_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 90, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_289_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_289_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_289_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_290',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_290_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [16, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_290_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_291',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_291_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_291_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_292',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_292_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_292_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_293',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_2, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_293_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_293_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_293_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_action_queue_async_294',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, False],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_async_294_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 208, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3951_action_queue_async_294_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_pause_295',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3951_fade_in_from_colour_duration_296',
        "command": 'fade_in_from_colour_duration',
        "args": [60, Colours.WHITE]
    },
    {
        "identifier": 'EVENT_3951_pause_script_until_effect_done_297',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3951_pause_298',
        "command": 'pause',
        "args": [170]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_299',
        "command": 'action_queue',
        'args': [AreaObjects.SCREEN_FOCUS, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_299_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_299_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_299_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_299_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_299_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_299_SUBSCRIPT_shift_south_steps_5',
                "command": 'shift_south_steps',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_pause_300',
        "command": 'pause',
        "args": [328]
    },
    {
        "identifier": 'EVENT_3951_action_queue_sync_301',
        "command": 'action_queue',
        'args': [AreaObjects.LAYER_2, True],
        "subscript": [
            {
                "identifier": 'EVENT_3951_action_queue_sync_301_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3951_action_queue_sync_301_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3951_pause_302',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3951_set_action_script_sync_303',
        "command": 'set_action_script',
        'args': [AreaObjects.MARIO, True, 229]
    },
    {
        "identifier": 'EVENT_3951_set_action_script_sync_304',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_0, True, 229]
    },
    {
        "identifier": 'EVENT_3951_set_action_script_sync_305',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_1, True, 229]
    },
    {
        "identifier": 'EVENT_3951_set_action_script_sync_306',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_2, True, 229]
    },
    {
        "identifier": 'EVENT_3951_set_action_script_sync_307',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_4, True, 229]
    },
    {
        "identifier": 'EVENT_3951_remember_last_object_308',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3951_apply_tile_mod_309',
        "command": 'apply_tile_mod',
        "args": [Rooms._375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3951_pause_310',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3951_apply_tile_mod_311',
        "command": 'apply_tile_mod',
        "args": [Rooms._375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3951_pause_312',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_3951_db_313',
        "command": 'db',
        "args": [0x5f]
    },
    {
        "identifier": 'EVENT_3951_pause_314',
        "command": 'pause',
        "args": [404]
    },
    {
        "identifier": 'EVENT_3951_palette_set_morphs_315',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 161, 1]
    },
    {
        "identifier": 'EVENT_3951_palette_set_morphs_316',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 162, 5]
    },
    {
        "identifier": 'EVENT_3951_palette_set_morphs_317',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 84, 8]
    },
    {
        "identifier": 'EVENT_3951_palette_set_morphs_318',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 85, 10]
    },
    {
        "identifier": 'EVENT_3951_palette_set_morphs_319',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 86, 11]
    },
    {
        "identifier": 'EVENT_3951_palette_set_morphs_320',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 141, 9]
    },
    {
        "identifier": 'EVENT_3951_palette_set_morphs_321',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 140, 13]
    },
    {
        "identifier": 'EVENT_3951_pause_script_until_effect_done_322',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3951_pause_323',
        "command": 'pause',
        "args": [216]
    },
    {
        "identifier": 'EVENT_3951_apply_tile_mod_324',
        "command": 'apply_tile_mod',
        "args": [Rooms._269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3951_apply_tile_mod_325',
        "command": 'apply_tile_mod',
        "args": [Rooms._269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3951_apply_tile_mod_326',
        "command": 'apply_tile_mod',
        "args": [Rooms._269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3951_fade_out_to_black_sync_duration_327',
        "command": 'fade_out_to_black_sync_duration',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3951_pause_script_until_effect_done_328',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3951_pause_329',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3951_play_music_default_volume_330',
        "command": 'play_music_default_volume',
        "args": [Music._71_ENDING_PART_2]
    },
    {
        "identifier": 'EVENT_3951_pause_331',
        "command": 'pause',
        "args": [130]
    },
    {
        "identifier": 'EVENT_3951_run_event_sequence_332',
        "command": 'run_event_sequence',
        "args": [EventSequences._13_RUN_STAR_PIECE_END_SEQUENCE, 0x00]
    },
    {
        "identifier": 'EVENT_3951_pause_333',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3951_enter_area_334',
        "command": 'enter_area',
        "args": [Rooms._269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, RadialDirections.SOUTHWEST, 17, 40, 2, []]
    },
    {
        "identifier": 'EVENT_3951_jmp_to_event_335',
        "command": 'jmp_to_event',
        "args": [3804]
    }
]
