from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2225_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7093, 7, 'EVENT_2225_ret_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 2, 'EVENT_2225_start_battle_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_2_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_2225_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2225_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_3_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_3_SUBSCRIPT_shift_north_steps_3',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_3_SUBSCRIPT_shift_north_steps_5',
                "command": 'shift_north_steps',
                "args": [11]
            },
        ]
    },
    {
        "identifier": 'EVENT_2225_pause_4',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_pause_5',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_freeze_camera_6',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [12, 46, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_overwrite_solidity_4',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x24, 0xe0, 0xfd, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x25, 0x00, 0x0d, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [44]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_bpl_26_27_28_9',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2225_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2225_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_8_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_8_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_8_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2225_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2225_fade_out_music_to_volume_9',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_start_battle_10',
        "command": 'start_battle',
        "args": [0x00d2, 29],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2225_restore_all_hp_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_jmp_to_event_12',
        "command": 'jmp_to_event',
        "args": [3819],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_restore_all_hp_13',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_restore_all_fp_14',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_set_bit_15',
        "command": 'set_bit',
        "args": [0x7054, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_enter_area_16',
        "command": 'enter_area',
        "args": [Rooms._400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM, RadialDirections.NORTHEAST, 2, 66, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_set_short_17',
        "command": 'set_short',
        "args": [0x700a, 0x00e4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_jmp_to_event_18',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_start_battle_19',
        "command": 'start_battle',
        "args": [0x00ba, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_jmp_if_bit_clear_20',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2225_restore_all_hp_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_jmp_to_event_21',
        "command": 'jmp_to_event',
        "args": [3819],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_restore_all_hp_22',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_set_bit_23',
        "command": 'set_bit',
        "args": [0x7093, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_set_bit_24',
        "command": 'set_bit',
        "args": [0x7068, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_enter_area_25',
        "command": 'enter_area',
        "args": [Rooms._400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM, RadialDirections.NORTHEAST, 2, 66, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 5, 'EVENT_2225_set_short_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_set_bit_27',
        "command": 'set_bit',
        "args": [0x7070, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_set_short_28',
        "command": 'set_short',
        "args": [0x700a, 0x00e5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_jmp_to_event_29',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_stop_sound_30',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2225_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
