from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3172_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3172_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x006a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3172_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3172_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS, RadialDirections.SOUTH, 2, 42, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3172_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3172_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
