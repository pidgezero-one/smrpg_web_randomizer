from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_445_set_short_0',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_445_enable_controls_1',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_445_run_background_event_2',
        "command": 'run_background_event',
        "args": [447, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_445_set_3',
        "command": 'set',
        "args": [0x7000, 30]
    },
    {
        "identifier": 'EVENT_445_set_7000_short_mem_to_7000_4',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_445_play_music_default_volume_5',
        "command": 'play_music_default_volume',
        "args": [Music._47_GRATE_GUYS_CASINO]
    },
    {
        "identifier": 'EVENT_445_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_446_set_short_20']
    }
]
