from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_550_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7060, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_550_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_550_set_7000_to_object_coord_2',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'EVENT_550_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_550_mem_compare_4',
        "command": 'mem_compare',
        "args": [0x7026, 3]
    },
    {
        "identifier": 'EVENT_550_jmp_if_comparison_result_is_lesser_5',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_550_set_bit_8']
    },
    {
        "identifier": 'EVENT_550_mem_compare_6',
        "command": 'mem_compare',
        "args": [0x7026, 6]
    },
    {
        "identifier": 'EVENT_550_jmp_if_comparison_result_is_lesser_7',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_550_set_bit_8',
        "command": 'set_bit',
        "args": [0x7060, 0]
    },
    {
        "identifier": 'EVENT_550_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_550_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_550_action_queue_sync_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_550_action_queue_sync_9_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_550_action_queue_sync_9_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_550_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_550_action_queue_sync_9_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_550_action_queue_sync_9_SUBSCRIPT_object_memory_clear_bit_6',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_550_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 638]
    },
    {
        "identifier": 'EVENT_550_ret_11',
        "command": 'ret'
    }
]
