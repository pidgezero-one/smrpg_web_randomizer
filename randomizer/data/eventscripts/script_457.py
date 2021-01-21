from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_457_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_457_action_queue_sync_0_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_0_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_457_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_457_action_queue_sync_1_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_1_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_1_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_457_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_457_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_2_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_457_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_457_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_3_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_3_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_457_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_457_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_457_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_457_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_5_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_457_action_queue_sync_5_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_457_remember_last_object_6',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_457_ret_7',
        "command": 'ret'
    }
]
