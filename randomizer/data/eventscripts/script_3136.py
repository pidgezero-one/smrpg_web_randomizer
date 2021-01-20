from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3136_run_background_event_with_pause_return_on_exit_0',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [3134, 0x701c, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3136_resume_background_event_1',
        "command": 'resume_background_event',
        "args": [0x701c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3136_set_short_2',
        "command": 'set_short',
        "args": [0x7016, 0x0005],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3136_set_short_3',
        "command": 'set_short',
        "args": [0x7018, 0x0014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3136_run_event_as_subroutine_4',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3136_set_bit_5',
        "command": 'set_bit',
        "args": [0x707d, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3136_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE, RadialDirections.SOUTH, 5, 90, 4, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3136_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3136_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
