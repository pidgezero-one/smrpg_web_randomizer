from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1876_mem_compare_0',
        "command": 'mem_compare',
        "args": [0x702c, 28]
    },
    {
        "identifier": 'EVENT_1876_jmp_if_loaded_memory_is_0_1',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_1876_jmp_if_bit_clear_10']
    },
    {
        "identifier": 'EVENT_1876_set_short_2',
        "command": 'set_short',
        "args": [0x702c, 0x001c]
    },
    {
        "identifier": 'EVENT_1876_set_3',
        "command": 'set',
        "args": [0x70a9, 28]
    },
    {
        "identifier": 'EVENT_1876_set_4',
        "command": 'set',
        "args": [0x70aa, 27]
    },
    {
        "identifier": 'EVENT_1876_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1876_action_queue_async_5_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_1876_action_queue_async_5_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0x24, 0x11, 0x12]
            },
            {
                "identifier": 'EVENT_1876_action_queue_async_5_SUBSCRIPT_set_7000_short_mem_to_700C_2',
                "command": 'set_7000_short_mem_to_700C',
                "args": [0x702a]
            }
        ]
    },
    {
        "identifier": 'EVENT_1876_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_1876_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 479]
    },
    {
        "identifier": 'EVENT_1876_pause_8',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1876_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 653]
    },
    {
        "identifier": 'EVENT_1876_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x707c, 0, 'EVENT_1876_ret_13']
    },
    {
        "identifier": 'EVENT_1876_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x707c, 0]
    },
    {
        "identifier": 'EVENT_1876_jmp_to_event_12',
        "command": 'jmp_to_event',
        "args": [1840]
    },
    {
        "identifier": 'EVENT_1876_ret_13',
        "command": 'ret'
    }
]
