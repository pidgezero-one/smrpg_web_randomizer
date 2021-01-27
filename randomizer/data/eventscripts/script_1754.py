from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1754_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_2, Rooms._319_LANDS_END_DESERT_AREA_06, 'EVENT_1754_set_7000_to_7000_short_mem_11']
    },
    {
        "identifier": 'EVENT_1754_set_7000_to_7000_short_mem_1',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_1754_jmp_if_7000_not_equals_short_2',
        "command": 'jmp_if_7000_not_equals_short',
        "args": [21, 'EVENT_1753_run_event_as_subroutine_3']
    },
    {
        "identifier": 'EVENT_1754_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [1544]
    },
    {
        "identifier": 'EVENT_1754_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._263_LANDS_END_UNDERGROUND_AREA_01, RadialDirections.SOUTH, 5, 91, 15, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1754_set_bit_5',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_1754_enable_controls_6',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1754_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1754_action_queue_async_7_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1754_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7050, 3, 'EVENT_1754_ret_10']
    },
    {
        "identifier": 'EVENT_1754_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_16, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    },
    {
        "identifier": 'EVENT_1754_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1754_set_7000_to_7000_short_mem_11',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_1754_jmp_if_7000_equals_short_12',
        "command": 'jmp_if_7000_equals_short',
        "args": [21, 'EVENT_1753_jmp_if_bit_set_11']
    },
    {
        "identifier": 'EVENT_1754_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_1753_run_event_as_subroutine_3']
    },
    {
        "identifier": 'EVENT_1754_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_1753_run_event_as_subroutine_3']
    }
]
