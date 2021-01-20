from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3717_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_3, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 6, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_freeze_all_npcs_until_return_2',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3717_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_3_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_3_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_3_SUBSCRIPT_walk_to_xy_coords_4',
                "command": 'walk_to_xy_coords',
                "args": [15, 112]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_3_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3717_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3717_action_queue_async_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_4_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_4_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_4_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_4_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_4_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_4_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3717_pause_5',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_reset_properties_12',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_reset_properties_18',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_face_northwest_19',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3717_action_queue_async_6_SUBSCRIPT_set_solidity_bits_20',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3717_pause_7',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_pause_9',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_unfreeze_all_npcs_10',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3717_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
