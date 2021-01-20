from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3773_freeze_camera_0',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3773_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3773_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3773_action_queue_async_2_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [17, 114]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_2_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3773_palette_set_morphs_3',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 142, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3773_pause_4',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3773_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3773_action_queue_async_5_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [19]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_turn_clockwise_45_degrees_n_times_11',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [31, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3773_action_queue_async_5_SUBSCRIPT_reset_properties_18',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3773_palette_set_6',
        "command": 'palette_set',
        "args": [84, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3773_unfreeze_camera_7',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3773_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
