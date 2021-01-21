from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2798_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2798_freeze_camera_2']
    },
    {
        "identifier": 'EVENT_2798_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2798_freeze_camera_2',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2798_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2798_action_queue_async_3_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2798_action_queue_async_3_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2798_action_queue_async_3_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_2798_action_queue_async_3_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2798_action_queue_async_3_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_2798_action_queue_async_3_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2798_pause_4',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2798_db_5',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2798_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._145_STAR_HILL_AREA_01, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2798_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._125_ENTER_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2798_unfreeze_camera_8',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2798_pause_9',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2798_fade_out_to_black_async_duration_10',
        "command": 'fade_out_to_black_async_duration',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2798_open_location_11',
        "command": 'open_location',
        "args": [Locations._031_STAR_HILL, [6, 7]]
    },
    {
        "identifier": 'EVENT_2798_ret_12',
        "command": 'ret'
    }
]
