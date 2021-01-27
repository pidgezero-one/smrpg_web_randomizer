from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1886_set_7000_to_70A0_short_mem_0',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70a8]
    },
    {
        "identifier": 'EVENT_1886_set_70A0_short_mem_to_7000_1',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_1886_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_1886_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_1886_jmp_fork_mario_on_object_3',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1745_freeze_all_npcs_until_return_43', 'EVENT_1886_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_1886_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7097, 3, 'EVENT_1886_jmp_to_subroutine_9']
    },
    {
        "identifier": 'EVENT_1886_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [1745]
    },
    {
        "identifier": 'EVENT_1886_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_1886_ret_8']
    },
    {
        "identifier": 'EVENT_1886_set_bit_7',
        "command": 'set_bit',
        "args": [0x7097, 3]
    },
    {
        "identifier": 'EVENT_1886_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1886_jmp_to_subroutine_9',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1745_freeze_all_npcs_until_return_60']
    },
    {
        "identifier": 'EVENT_1886_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1886_action_queue_sync_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_1886_action_queue_sync_10_SUBSCRIPT_summon_to_level_1',
                "command": 'summon_to_level',
                "args": [AreaObjects.NPC_3, Rooms._404_LANDS_END_DESERT_AREA_04]
            },
            {
                "identifier": 'EVENT_1886_action_queue_sync_10_SUBSCRIPT_object_memory_clear_bit_2',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1886_ret_11',
        "command": 'ret'
    }
]
