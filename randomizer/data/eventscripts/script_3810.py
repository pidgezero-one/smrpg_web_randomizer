from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3810_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3810_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3810_remove_from_current_level_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3810_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [3810],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3810_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3810_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
