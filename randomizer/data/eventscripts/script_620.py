from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_620_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 2, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_620_jmp_if_bit_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_620_jmp_if_bit_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_set_7000_to_object_coord_8',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_5, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 64, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_620_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_620_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_620_action_queue_async_10_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_620_action_queue_async_10_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_620_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
