from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1785_summon_to_level_0',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._319_LANDS_END_DESERT_AREA_06]
    },
    {
        "identifier": 'EVENT_1785_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._402_LANDS_END_DESERT_AREA_03]
    },
    {
        "identifier": 'EVENT_1785_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._403_LANDS_END_DESERT_AREA_05]
    },
    {
        "identifier": 'EVENT_1785_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._404_LANDS_END_DESERT_AREA_04]
    },
    {
        "identifier": 'EVENT_1785_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._318_LANDS_END_DESERT_AREA_02]
    },
    {
        "identifier": 'EVENT_1785_set_bit_5',
        "command": 'set_bit',
        "args": [0x704f, 6]
    },
    {
        "identifier": 'EVENT_1785_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1785_action_queue_async_6_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x97, 0x14]
            },
            {
                "identifier": 'EVENT_1785_action_queue_async_6_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [1]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1785_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1785_set_short_10']
    },
    {
        "identifier": 'EVENT_1785_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [1844]
    },
    {
        "identifier": 'EVENT_1785_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1785_set_short_10',
        "command": 'set_short',
        "args": [0x7024, 0x0014]
    },
    {
        "identifier": 'EVENT_1785_set_short_11',
        "command": 'set_short',
        "args": [0x7026, 0x0014]
    },
    {
        "identifier": 'EVENT_1785_set_bit_12',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_1785_ret_13',
        "command": 'ret'
    }
]
