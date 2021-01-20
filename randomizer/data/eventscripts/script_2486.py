from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2486_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_0, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, 'EVENT_2486_ret_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2486_set_short_1',
        "command": 'set_short',
        "args": [0x7016, 0x0007],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2486_set_short_2',
        "command": 'set_short',
        "args": [0x7018, 0x0022],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2486_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2486_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT, RadialDirections.SOUTH, 24, 102, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2486_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
