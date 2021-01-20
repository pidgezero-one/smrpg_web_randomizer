from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_740_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_740_pause_1',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_740_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, RadialDirections.NORTHEAST, 1, 35, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_740_play_music_default_volume_3',
        "command": 'play_music_default_volume',
        "args": [Music._61_VALENTINA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_740_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
