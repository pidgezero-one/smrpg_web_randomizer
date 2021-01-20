from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3349_jmp_if_var_not_equals_byte_0',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70b6, 0, 'EVENT_3349_ret_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3349_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._452_BOWSERS_KEEP_AREA_06_SAVE_POINT_WCROCO_SHOP, RadialDirections.SOUTHWEST, 16, 80, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3349_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
