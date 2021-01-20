from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1647_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x707a, 7, 'EVENT_1647_jmp_if_bit_set_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_pause_1',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._049_BIG_SHELL_HIT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1647_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1647_action_queue_async_3_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1647_action_queue_async_3_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1647_action_queue_async_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_1647_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_pause_6',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_fade_out_to_black_async_duration_7',
        "command": 'fade_out_to_black_async_duration',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_enter_area_8',
        "command": 'enter_area',
        "args": [Rooms._290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING, RadialDirections.SOUTH, 19, 27, 12, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_set_bit_9',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_enable_controls_10',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_fade_in_from_black_sync_11',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1647_action_queue_async_12_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
        ]
    },
    {
        "identifier": 'EVENT_1647_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_1647_ret_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1647_action_queue_async_15_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [20, 39, 20]
            },
            {
                "identifier": 'EVENT_1647_action_queue_async_15_SUBSCRIPT_face_west_1',
                "command": 'face_west',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1647_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_run_dialog_17',
        "command": 'run_dialog',
        "args": [1135, AreaObjects.NPC_2, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_set_bit_18',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1647_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
