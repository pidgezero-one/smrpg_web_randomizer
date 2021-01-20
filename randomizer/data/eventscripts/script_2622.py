from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2622_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2622_action_queue_async_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2622_action_queue_async_0_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [1, 4]
            },
            {
                "identifier": 'EVENT_2622_action_queue_async_0_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2622_action_queue_async_0_SUBSCRIPT_walk_1_step_north_3',
                "command": 'walk_1_step_north',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2622_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2622_star_mask_expand_from_screen_center_2',
        "command": 'star_mask_expand_from_screen_center',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2622_pause_short_3',
        "command": 'pause_short',
        "args": [564],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2622_star_mask_shrink_to_screen_center_4',
        "command": 'star_mask_shrink_to_screen_center',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2622_pause_script_until_effect_done_5',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2622_jmp_to_event_6',
        "command": 'jmp_to_event',
        "args": [3798],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2622_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
