from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_652_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, 6, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_652_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_652_dec_2',
        "command": 'dec',
        "args": [0x70ae],
        "subscript": []
    },
    {
        "identifier": 'EVENT_652_set_short_3',
        "command": 'set_short',
        "args": [0x701c, 0x0078],
        "subscript": []
    },
    {
        "identifier": 'EVENT_652_run_background_event_with_pause_return_on_exit_4',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [653, 0x701c, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_652_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
