from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2814_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7064, 0]
    },
    {
        "identifier": 'EVENT_2814_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7064, 1]
    },
    {
        "identifier": 'EVENT_2814_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7064, 2]
    },
    {
        "identifier": 'EVENT_2814_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7064, 3]
    },
    {
        "identifier": 'EVENT_2814_set_4',
        "command": 'set',
        "args": [0x70da, 0]
    },
    {
        "identifier": 'EVENT_2814_set_5',
        "command": 'set',
        "args": [0x70db, 0]
    },
    {
        "identifier": 'EVENT_2814_set_6',
        "command": 'set',
        "args": [0x70dc, 0]
    },
    {
        "identifier": 'EVENT_2814_set_7',
        "command": 'set',
        "args": [0x70dd, 0]
    },
    {
        "identifier": 'EVENT_2814_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._205_MUSHROOM_WAY_AREA_03]
    },
    {
        "identifier": 'EVENT_2814_remove_from_level_9',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._205_MUSHROOM_WAY_AREA_03]
    },
    {
        "identifier": 'EVENT_2814_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._205_MUSHROOM_WAY_AREA_03]
    },
    {
        "identifier": 'EVENT_2814_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2814_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2814_action_queue_async_11_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2814_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2814_run_background_event_13',
        "command": 'run_background_event',
        "args": [2813, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2814_run_background_event_14',
        "command": 'run_background_event',
        "args": [2809, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_2814_ret_15',
        "command": 'ret'
    }
]
