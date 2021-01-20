from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1824_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_pause_1',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_set_2',
        "command": 'set',
        "args": [0x70a9, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_set_short_3',
        "command": 'set_short',
        "args": [0x700c, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1824_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1824_action_queue_async_5_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1824_action_queue_async_5_SUBSCRIPT_walk_f_direction_16_pixels_2',
                "command": 'walk_f_direction_16_pixels',
                "args": []
            },
            {
                "identifier": 'EVENT_1824_action_queue_async_5_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1824_add_6',
        "command": 'add',
        "args": [0x70a9, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_add_short_7',
        "command": 'add_short',
        "args": [0x700c, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_end_loop_8',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_unfreeze_all_npcs_9',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_set_short_10',
        "command": 'set_short',
        "args": [0x7038, 0x0880],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_set_short_11',
        "command": 'set_short',
        "args": [0x703a, 0x1c80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_set_short_12',
        "command": 'set_short',
        "args": [0x703c, 0x0500],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_run_background_event_13',
        "command": 'run_background_event',
        "args": [1828, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1824_jmp_to_event_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_set_15',
        "command": 'set',
        "args": [0x70cb, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7095, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1824_jmp_to_event_17',
        "command": 'jmp_to_event',
        "args": [1829],
        "subscript": []
    }
]
