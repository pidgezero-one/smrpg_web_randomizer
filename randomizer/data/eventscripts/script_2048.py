from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2048_set_bit_0',
        "command": 'set_bit',
        "args": [0x7093, 5]
    },
    {
        "identifier": 'EVENT_2048_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 6, 'EVENT_2048_set_bit_9']
    },
    {
        "identifier": 'EVENT_2048_set_7000_to_70A0_short_mem_2',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70bd]
    },
    {
        "identifier": 'EVENT_2048_jmp_if_7000_equals_short_3',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2048_action_queue_async_5']
    },
    {
        "identifier": 'EVENT_2048_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2048_action_queue_async_4_SUBSCRIPT_load_mem_0',
                "command": 'load_mem',
                "args": [0x7000]
            },
            {
                "identifier": 'EVENT_2048_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2048_action_queue_async_4_SUBSCRIPT_end_loop_2',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2048_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2048_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2048_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_2079_enable_controls_until_return_0']
    },
    {
        "identifier": 'EVENT_2048_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2048_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2048_set_bit_9',
        "command": 'set_bit',
        "args": [0x7088, 6]
    },
    {
        "identifier": 'EVENT_2048_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2048_action_queue_async_10_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 62, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2048_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2048_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_2079_enable_controls_until_return_0']
    },
    {
        "identifier": 'EVENT_2048_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2048_ret_13',
        "command": 'ret'
    }
]
