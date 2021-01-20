from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1887_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70af, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_1887_jmp_if_bit_set_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_jmp_fork_mario_on_object_3',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1745_freeze_all_npcs_until_return_43', 'EVENT_1887_jmp_if_bit_set_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7097, 4, 'EVENT_1887_jmp_to_subroutine_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [1745],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_1887_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_set_bit_7',
        "command": 'set_bit',
        "args": [0x7097, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_jmp_to_subroutine_9',
        "command": 'jmp_to_subroutine',
        "args": [0x4400],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1887_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1887_action_queue_sync_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_1887_action_queue_sync_10_SUBSCRIPT_summon_to_level_1',
                "command": 'summon_to_level',
                "args": [AreaObjects.NPC_6, Rooms._318_LANDS_END_DESERT_AREA_02]
            },
            {
                "identifier": 'EVENT_1887_action_queue_sync_10_SUBSCRIPT_object_memory_clear_bit_2',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1887_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
