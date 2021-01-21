from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1697_mem_compare_0',
        "command": 'mem_compare',
        "args": [0x702c, 27]
    },
    {
        "identifier": 'EVENT_1697_jmp_if_loaded_memory_is_0_1',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_1696_jmp_if_bit_clear_10']
    },
    {
        "identifier": 'EVENT_1697_set_short_2',
        "command": 'set_short',
        "args": [0x702c, 0x001b]
    },
    {
        "identifier": 'EVENT_1697_set_3',
        "command": 'set',
        "args": [0x70a9, 27]
    },
    {
        "identifier": 'EVENT_1697_set_4',
        "command": 'set',
        "args": [0x70aa, 26]
    },
    {
        "identifier": 'EVENT_1697_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1697_action_queue_async_5_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_1697_action_queue_async_5_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0x24, 0x11, 0x12]
            },
            {
                "identifier": 'EVENT_1697_action_queue_async_5_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x702a, 0x700c]
            }
        ]
    },
    {
        "identifier": 'EVENT_1697_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1697_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 479]
    },
    {
        "identifier": 'EVENT_1697_pause_8',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1697_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 653]
    },
    {
        "identifier": 'EVENT_1697_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x707c, 0, 'EVENT_1697_ret_13']
    },
    {
        "identifier": 'EVENT_1697_run_event_as_subroutine_11',
        "command": 'run_event_as_subroutine',
        "args": [1840]
    },
    {
        "identifier": 'EVENT_1697_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x707c, 0]
    },
    {
        "identifier": 'EVENT_1697_ret_13',
        "command": 'ret'
    }
]
