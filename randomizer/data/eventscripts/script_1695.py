from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1695_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_1695_set_short_2']
    },
    {
        "identifier": 'EVENT_1695_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [255]
    },
    {
        "identifier": 'EVENT_1695_set_short_2',
        "command": 'set_short',
        "args": [0x700e, 0x0007]
    },
    {
        "identifier": 'EVENT_1695_start_battle_700E_3',
        "command": 'start_battle_700E'
    },
    {
        "identifier": 'EVENT_1695_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1695_fade_in_from_black_sync_9']
    },
    {
        "identifier": 'EVENT_1695_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1695_reset_and_choose_game_12']
    },
    {
        "identifier": 'EVENT_1695_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1695_action_queue_async_6_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1695_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1695_action_queue_async_6_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1695_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1695_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1695_fade_in_from_black_sync_9',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1695_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1695_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1695_action_queue_async_10_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1695_action_queue_async_10_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1695_action_queue_async_10_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1695_action_queue_async_10_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1695_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1695_reset_and_choose_game_12',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1695_ret_13',
        "command": 'ret'
    }
]
