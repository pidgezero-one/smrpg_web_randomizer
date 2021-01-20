from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2446_play_sound_balance_0',
        "command": 'play_sound_balance',
        "args": [Sounds._077_EXOTIC_BIRD_CALLS, 56],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2446_pause_1',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2446_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_2446_play_sound_balance_0'],
        "subscript": []
    },
]
