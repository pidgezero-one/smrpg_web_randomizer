from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1801_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._085_FLOWER, 4]
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_clear_solidity_bits_9',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1801_action_queue_async_0_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1801_set_1',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_1801_add_max_FP_7000_2',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_1801_ret_3',
        "command": 'ret'
    }
]
