from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2131_pause_0',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_pause_2',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_play_music_default_volume_5',
        "command": 'play_music_default_volume',
        "args": [Music._01_DODOS_COMING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_pause_6',
        "command": 'pause',
        "args": [143],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_pause_7',
        "command": 'pause',
        "args": [235],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_pause_8',
        "command": 'pause',
        "args": [131],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2131_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_2114_action_queue_async_16'],
        "subscript": []
    }
]
