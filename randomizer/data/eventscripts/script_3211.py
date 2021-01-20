from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3211_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._168_SUNKEN_SHIP_PUZZLE_ROOM_3, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3211_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3211_run_background_event_2',
        "command": 'run_background_event',
        "args": [3212, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3211_run_dialog_3',
        "command": 'run_dialog',
        "args": [1657, AreaObjects.BOWSER, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3211_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
