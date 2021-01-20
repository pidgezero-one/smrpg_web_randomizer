from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1787_set_0',
        "command": 'set',
        "args": [0x70ad, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7094, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7050, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7050, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_set_4',
        "command": 'set',
        "args": [0x70ac, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._319_LANDS_END_DESERT_AREA_06],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_summon_to_level_6',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._402_LANDS_END_DESERT_AREA_03],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._403_LANDS_END_DESERT_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._404_LANDS_END_DESERT_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._318_LANDS_END_DESERT_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1787_action_queue_async_10_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x97, 0x17]
            },
            {
                "identifier": 'EVENT_1787_action_queue_async_10_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0, 1]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1787_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1787_set_short_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_run_event_as_subroutine_12',
        "command": 'run_event_as_subroutine',
        "args": [1844],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_set_short_14',
        "command": 'set_short',
        "args": [0x7024, 0x0017],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_set_bit_15',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1787_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
