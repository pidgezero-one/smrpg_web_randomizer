from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1538_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1538_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1538_run_background_event_2',
        "command": 'run_background_event',
        "args": [1706, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1538_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1538_action_queue_async_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1538_action_queue_async_3_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1538_action_queue_async_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1538_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [3153],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1538_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
