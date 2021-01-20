from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_445_set_short_0',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_445_enable_controls_1',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_445_run_background_event_2',
        "command": 'run_background_event',
        "args": [447, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_445_set_3',
        "command": 'set',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_445_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_445_play_music_default_volume_5',
        "command": 'play_music_default_volume',
        "args": [Music._47_GRATE_GUYS_CASINO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_445_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_446_set_short_20'],
        "subscript": []
    },
]
