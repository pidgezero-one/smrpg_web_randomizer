from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2575_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x708b, 3, 'EVENT_2575_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2575_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 3, 'EVENT_2575_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2575_set_bit_2',
        "command": 'set_bit',
        "args": [0x708d, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2575_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2575_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2575_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2575_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2575_play_music_default_volume_7',
        "command": 'play_music_default_volume',
        "args": [Music._30_LONG_LONG_AGO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2575_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
