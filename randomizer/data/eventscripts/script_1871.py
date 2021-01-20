from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1871_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1871_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 4, 'EVENT_1871_fade_in_from_black_async_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1871_remove_from_current_level_2',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1871_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1871_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
