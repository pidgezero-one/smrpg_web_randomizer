from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2525_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 6, 'EVENT_2525_freeze_camera_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_freeze_camera_2',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2525_action_queue_async_3_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2525_action_queue_async_3_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2525_action_queue_async_3_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_2525_action_queue_async_3_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2525_action_queue_async_3_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2525_pause_4',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_db_5',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._157_STAR_HILL_AREA_03, 13, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._125_ENTER_DEEP_WATER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_unfreeze_camera_8',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_pause_9',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_fade_out_to_black_async_duration_10',
        "command": 'fade_out_to_black_async_duration',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_enter_area_11',
        "command": 'enter_area',
        "args": [Rooms._159_STAR_HILL_AREA_04, RadialDirections.SOUTHWEST, 26, 110, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2525_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
