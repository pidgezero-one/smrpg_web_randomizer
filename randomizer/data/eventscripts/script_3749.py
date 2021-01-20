from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3749_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 0, 'EVENT_3749_run_event_as_subroutine_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 7, 'EVENT_3749_jmp_if_bit_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_set_bit_3',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._061_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA_RIGHT_BEFORE_FIGHT, RadialDirections.NORTHEAST, 11, 59, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7090, 2, 'EVENT_3749_enter_area_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_3749_set_bit_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_set_bit_8',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, RadialDirections.NORTHEAST, 11, 59, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_set_bit_11',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_enter_area_12',
        "command": 'enter_area',
        "args": [Rooms._438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, RadialDirections.NORTHEAST, 11, 59, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_enter_area_14',
        "command": 'enter_area',
        "args": [Rooms._430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA, RadialDirections.NORTHEAST, 11, 59, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_run_event_as_subroutine_16',
        "command": 'run_event_as_subroutine',
        "args": [65],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3749_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
