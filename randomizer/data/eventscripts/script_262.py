from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_262_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 5, 'EVENT_262_fade_out_music_to_volume_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_262_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_262_fade_out_music_to_volume_2',
        "command": 'fade_out_music_to_volume',
        "args": [1, 127],
        "subscript": []
    },
    {
        "identifier": 'EVENT_262_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_262_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
