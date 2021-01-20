from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3374_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_3374_jmp_if_bit_set_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_enable_controls_until_return_1',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3374_jmp_if_mario_in_air_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3374_jmp_if_mario_in_air_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3374_jmp_if_mario_in_air_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_3374_jmp_if_mario_in_air_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_3374_jmp_if_mario_in_air_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_pause_7',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3374_jmp_if_bit_set_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_jmp_if_mario_in_air_9',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3374_action_queue_async_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_enable_controls_until_return_10',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3374_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3374_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3374_action_queue_async_11_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3374_action_queue_async_11_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3374_action_queue_async_11_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3374_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_3374_jmp_if_bit_set_0'],
        "subscript": []
    },
]
