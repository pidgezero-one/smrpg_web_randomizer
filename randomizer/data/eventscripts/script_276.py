from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_276_set_7016_to_object_xyz_0',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_276_add_short_1',
        "command": 'add_short',
        "args": [0x7016, 0xf900],
        "subscript": []
    },
    {
        "identifier": 'EVENT_276_add_short_2',
        "command": 'add_short',
        "args": [0x7018, 0xf900],
        "subscript": []
    },
    {
        "identifier": 'EVENT_276_db_3',
        "command": 'db',
        "args": [0xfd, 0xc7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_276_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_jmp_if_bit_set_0',
                "command": 'jmp_if_bit_set',
                "args": [0x7049, 2, 'EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_6']
            },
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_jmp_if_bit_set_1',
                "command": 'jmp_if_bit_set',
                "args": [0x7049, 6, 'EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_4']
            },
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_jmp_3',
                "command": 'jmp',
                "args": ['EVENT_276_action_queue_async_4_SUBSCRIPT_db_7']
            },
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_jmp_5',
                "command": 'jmp',
                "args": ['EVENT_276_action_queue_async_4_SUBSCRIPT_db_7']
            },
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x98]
            },
            {
                "identifier": 'EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_276_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7049, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_276_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7049, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_276_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
