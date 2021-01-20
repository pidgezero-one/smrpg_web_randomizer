from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2541_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_freeze_camera_1',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2541_action_queue_sync_2_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_2_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_2_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2541_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2541_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_3_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2541_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2541_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_4_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2541_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2541_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_5_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_5_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2541_action_queue_sync_5_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2541_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2541_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2541_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2541_action_queue_async_6_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_2541_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 405],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 846],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 847],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 194],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_jmp_if_object_in_level_12',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, 'EVENT_2541_action_queue_async_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_run_background_event_13',
        "command": 'run_background_event',
        "args": [2802, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2541_action_queue_async_14_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2541_action_queue_async_14_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2541_action_queue_async_14_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2541_action_queue_async_14_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_2541_action_queue_async_14_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_2541_unfreeze_camera_15',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2541_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
