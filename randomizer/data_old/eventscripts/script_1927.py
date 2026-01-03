
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1927_action_queue_async_9',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
        "subscript": [
            {
                "identifier": 'EVENT_1927_action_queue_async_9_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_39_SUBSCRIPT_walk',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_39_SUBSCRIPT_walk',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_39_SUBSCRIPT_walk',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_39_SUBSCRIPT_jump',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2278_action_queue_async_39_SUBSCRIPT_walk',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_1927_pause_13',
        "command": 'pause',
        "args": [150]
    },
    {
        "identifier": 'EVENT_1927_fade_out_to_black_async_44',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_1927_enter_area_54',
        "command": 'enter_area',
        "args": [Rooms._202_BOOSTER_TOWER_ENTRANCE, RadialDirections.SOUTHWEST, 5, 114, 15, []]
    },
    {
        "identifier": 'EVENT_1927_fade_out_to_black_async_44_',
        "command": 'jmp_to_event',
        "args": [1328]
    },
    {
        "identifier": 'EVENT_1927_ret_13',
        "command": 'ret'
    }
]
