from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2523_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 5, 'EVENT_2523_freeze_camera_2']
    },
    {
        "identifier": 'EVENT_2523_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2523_freeze_camera_2',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2523_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2523_action_queue_async_3_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2523_action_queue_async_3_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2523_action_queue_async_3_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_2523_action_queue_async_3_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_2523_action_queue_async_3_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2523_pause_4',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2523_db_5',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2523_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._158_STAR_HILL_AREA_02, 11, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2523_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._125_ENTER_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2523_unfreeze_camera_8',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2523_pause_9',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2523_fade_out_to_black_async_duration_10',
        "command": 'fade_out_to_black_async_duration',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2523_enter_area_11',
        "command": 'enter_area',
        "args": [Rooms._157_STAR_HILL_AREA_03, RadialDirections.SOUTHWEST, 13, 24, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2523_ret_12',
        "command": 'ret'
    }
]
