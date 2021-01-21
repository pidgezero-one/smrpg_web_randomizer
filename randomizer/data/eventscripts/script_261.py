from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_261_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 5, 'EVENT_261_fade_out_music_to_volume_2']
    },
    {
        "identifier": 'EVENT_261_stop_sound_1',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_261_fade_out_music_to_volume_2',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96]
    },
    {
        "identifier": 'EVENT_261_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_261_ret_4',
        "command": 'ret'
    }
]
