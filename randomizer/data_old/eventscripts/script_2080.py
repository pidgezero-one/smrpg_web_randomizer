
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_2080_jmp_if_flag_shuffle_off",
        "command": "jmp_if_bit_clear",
        "args": [0x7060, 2, 'EVENT_2080_action_queue_async_1']
    },
    {
        "identifier": 'EVENT_2080_hide_note',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2080_show_guy_1',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_2, False],
        "subscript": [
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2080_action_queue_sync_0_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2080_show_guy_2',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, False],
        "subscript": [
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2080_action_queue_sync_0_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2080_show_guy_3',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, False],
        "subscript": [
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2080_action_queue_sync_0_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": "EVENT_2080_jmp",
        "command": "jmp",
        "args": ['EVENT_2080_fade_in_from_black_async_2']
    },
    {
        "identifier": 'EVENT_2080_action_queue_async_1',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, False],
        "subscript": [
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2080_action_queue_async_1_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_2080_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": "EVENT_2080_summoner", 
        "command": "run_event_as_subroutine", 
        "args": [91]
    },
    {
        "identifier": 'EVENT_2080_ret_3',
        "command": 'ret'
    }
]
