from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3160_pause_script_if_menu_open_0',
        "command": 'pause_script_if_menu_open',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3160_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_0, Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, 'EVENT_3160_ret_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3160_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, RadialDirections.SOUTHWEST, 20, 25, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3160_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
