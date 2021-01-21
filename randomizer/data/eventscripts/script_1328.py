from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1328_play_music_default_volume_0',
        "command": 'play_music_default_volume',
        "args": [Music._13_ROAD_IS_FULL_OF_DANGERS]
    },
    {
        "identifier": 'EVENT_1328_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1328_action_queue_async_1_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1328_action_queue_async_1_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1328_action_queue_async_1_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1328_action_queue_async_1_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1328_action_queue_async_1_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1328_action_queue_async_1_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1328_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7053, 7, 'EVENT_1329_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_1328_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1328_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1328_ret_5',
        "command": 'ret'
    }
]
