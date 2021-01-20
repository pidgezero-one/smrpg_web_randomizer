from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1280_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, RadialDirections.NORTHEAST, 4, 19, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_sync_1_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_2_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_2_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_2_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_async_3_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 20, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_3_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_fade_in_from_black_async_duration_4',
        "command": 'fade_in_from_black_async_duration',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_pause_5',
        "command": 'pause',
        "args": [100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_6_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_6_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_run_dialog_7',
        "command": 'run_dialog',
        "args": [2823, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_async_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_8_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_8_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_8_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [5]
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_run_dialog_9',
        "command": 'run_dialog',
        "args": [2824, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_pause_script_resume_on_next_dialog_page_a_10',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_async_11_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [37]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_11_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_unsync_dialog_12',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_close_dialog_13',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_run_dialog_15',
        "command": 'run_dialog',
        "args": [2825, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_16_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_16_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_16_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_16_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_run_dialog_17',
        "command": 'run_dialog',
        "args": [2826, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_pause_18',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_enter_area_19',
        "command": 'enter_area',
        "args": [Rooms._202_BOOSTER_TOWER_ENTRANCE, RadialDirections.NORTHEAST, 2, 120, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_freeze_camera_20',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_sync_21_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_21_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_21_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_21_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_21_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1280_action_queue_sync_21_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1280_action_queue_async_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1280_action_queue_async_22_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [40]
            },
        ]
    },
    {
        "identifier": 'EVENT_1280_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 519],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_1329_action_queue_sync_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1280_ret_25',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
