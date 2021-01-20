from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1823_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [33],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_run_dialog_2',
        "command": 'run_dialog',
        "args": [1177, AreaObjects.MARIO, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_put_inventory_3',
        "command": 'put_inventory',
        "args": [0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_set_7000_to_current_level_4',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 321, 'EVENT_1823_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_freeze_camera_6',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1823_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1823_action_queue_sync_7_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1823_action_queue_sync_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1823_set_short_8',
        "command": 'set_short',
        "args": [0x701c, 0x0028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_run_background_event_with_pause_return_on_exit_9',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1543, 0x701c, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_load_600f_10',
        "command": 'load_600f',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1823_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
