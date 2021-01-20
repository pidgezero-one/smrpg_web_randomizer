from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3848_jmp_if_var_not_equals_byte_0',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70de, 18, 'EVENT_3848_enter_area_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3848_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._055_PIPE_VAULT_ENTRANCE, RadialDirections.NORTHWEST, 20, 30, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3848_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3848_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._055_PIPE_VAULT_ENTRANCE, RadialDirections.SOUTHEAST, 12, 14, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3848_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
