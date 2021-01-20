from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1429_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._204_MUSHROOM_WAY_AREA_02, 'EVENT_1429_ret_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1429_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_1429_ret_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1429_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 540],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1429_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1429_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
