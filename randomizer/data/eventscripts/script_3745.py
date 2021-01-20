from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3745_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_1_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [27, 29, 16, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_1_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_1_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_1_SUBSCRIPT_shadow_off_5',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_1_SUBSCRIPT_clear_solidity_bits_6',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_fade_in_from_black_sync_2',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_pause_3',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_pause_script_until_effect_done_4',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_fade_out_to_black_async_5',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, RadialDirections.SOUTHEAST, 19, 95, 10, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_7_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [19, 95, 27, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_7_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_7_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_7_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_7_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x25, 0x00, 0x00, 0x08, 0x00]
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_fade_in_from_black_sync_8',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_9_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3745_action_queue_async_9_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_9_SUBSCRIPT_bpl_26_27_28_2',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_9_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 976],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_pause_11',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_pause_script_until_effect_done_12',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_fade_out_to_black_async_13',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_enter_area_14',
        "command": 'enter_area',
        "args": [Rooms._373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD, RadialDirections.SOUTHEAST, 27, 91, 6, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_15_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_15_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [27, 91, 16, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_15_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_15_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_15_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x00, 0x0c, 0x00]
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_fade_in_from_black_sync_16',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_17_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_17_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3745_action_queue_async_17_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_17_SUBSCRIPT_bpl_26_27_28_2',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_17_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_17_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_17_SUBSCRIPT_shadow_off_5',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 976],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_pause_19',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_pause_script_until_effect_done_20',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_fade_out_to_black_async_21',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_enter_area_22',
        "command": 'enter_area',
        "args": [Rooms._374_NIMBUS_LAND_FALL_FROM_PLATFORM_4TH, RadialDirections.SOUTHEAST, 27, 115, 6, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_23_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_23_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [27, 115, 16, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_23_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_23_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_23_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_23_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x25, 0x00, 0x00, 0x0e, 0x00]
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_fade_in_from_black_sync_24',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_pause_25',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_pause_script_until_effect_done_26',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_fade_out_to_black_async_27',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_set_bit_28',
        "command": 'set_bit',
        "args": [0x704a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_enter_area_29',
        "command": 'enter_area',
        "args": [Rooms._370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS, RadialDirections.SOUTHEAST, 20, 50, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_30_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_30_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [20, 50, 0, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_30_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_30_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_fade_in_from_black_sync_31',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_32_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_32_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3745_action_queue_async_32_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_32_SUBSCRIPT_stop_sound_2',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_32_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_32_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 976],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3745_action_queue_async_34_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_34_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3745_action_queue_async_34_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_3745_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3745_ret_36',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
