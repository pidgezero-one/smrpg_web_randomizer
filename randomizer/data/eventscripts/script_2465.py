from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2465_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._096_SWINGING_FIST, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2465_pause_1',
        "command": 'pause',
        "args": [26],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2465_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7045, 0, 'EVENT_2465_play_sound_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2465_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
