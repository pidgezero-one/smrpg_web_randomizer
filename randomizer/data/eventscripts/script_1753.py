from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1753_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_2, Rooms._319_LANDS_END_DESERT_AREA_06, 'EVENT_1753_set_short_mem_9']
    },
    {
        "identifier": 'EVENT_1753_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1753_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 20, 'EVENT_1754_run_event_as_subroutine_3']
    },
    {
        "identifier": 'EVENT_1753_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [1544]
    },
    {
        "identifier": 'EVENT_1753_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._403_LANDS_END_DESERT_AREA_05, RadialDirections.SOUTH, 27, 60, 0, []]
    },
    {
        "identifier": 'EVENT_1753_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [1844]
    },
    {
        "identifier": 'EVENT_1753_set_6',
        "command": 'set',
        "args": [0x70a8, 21]
    },
    {
        "identifier": 'EVENT_1753_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [1545]
    },
    {
        "identifier": 'EVENT_1753_jmp_to_event_8',
        "command": 'jmp_to_event',
        "args": [1785]
    },
    {
        "identifier": 'EVENT_1753_set_short_mem_9',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1753_jmp_if_var_not_equals_short_10',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 20, 'EVENT_1753_run_event_as_subroutine_3']
    },
    {
        "identifier": 'EVENT_1753_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_1753_pause_14']
    },
    {
        "identifier": 'EVENT_1753_set_12',
        "command": 'set',
        "args": [0x70a8, 22]
    },
    {
        "identifier": 'EVENT_1753_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_1883_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_1753_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1753_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1753_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1754_run_event_as_subroutine_3']
    }
]
