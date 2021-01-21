from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1582_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 4, 'EVENT_1582_run_event_as_subroutine_4']
    },
    {
        "identifier": 'EVENT_1582_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 0, 'EVENT_1582_run_event_as_subroutine_4']
    },
    {
        "identifier": 'EVENT_1582_set_bit_2',
        "command": 'set_bit',
        "args": [0x7042, 2]
    },
    {
        "identifier": 'EVENT_1582_enable_trigger_in_level_3',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    },
    {
        "identifier": 'EVENT_1582_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_1582_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS, RadialDirections.SOUTH, 8, 100, 14, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1582_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 10]
    },
    {
        "identifier": 'EVENT_1582_ret_7',
        "command": 'ret'
    }
]
