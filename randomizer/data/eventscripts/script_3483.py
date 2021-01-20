from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3483_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [2, 96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3483_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._035_RUNNING_WATER, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3483_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 3, 'EVENT_3483_run_event_at_return_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3483_run_event_at_return_3',
        "command": 'run_event_at_return',
        "args": [3492],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3483_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3483_run_event_at_return_5',
        "command": 'run_event_at_return',
        "args": [3493],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3483_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]