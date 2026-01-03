
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3869_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_3869_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_3869_open_menu_or_run_event_sequence_2',
        "command": 'open_menu_or_run_event_sequence',
        "args": [EventSequences._15_ENTER_GATE_TO_SMITHY_FACTORY]
    },
    {
        "identifier": 'EVENT_3869_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._350_SMITHY_FACTORY_AREA_01, RadialDirections.NORTHEAST, 4, 27, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3869_ret_4',
        "command": 'ret'
    }
]
