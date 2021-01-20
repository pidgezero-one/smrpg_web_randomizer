from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2117_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2117_action_queue_async_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2117_action_queue_async_0_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2117_action_queue_async_0_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2117_action_queue_async_0_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2117_action_queue_async_0_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2117_action_queue_async_0_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_2117_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
