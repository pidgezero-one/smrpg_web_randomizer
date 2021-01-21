from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_397_run_dialog_0',
        "command": 'run_dialog',
        "args": [682, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_397_set_short_1',
        "command": 'set_short',
        "args": [0x7022, 0x0008]
    },
    {
        "identifier": 'EVENT_397_run_background_event_with_pause_2',
        "command": 'run_background_event_with_pause',
        "args": [3075, 0x7022, [12, 13]]
    },
    {
        "identifier": 'EVENT_397_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._071_MUSHROOM_CURE, 6]
    },
    {
        "identifier": 'EVENT_397_restore_all_hp_4',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_397_restore_all_fp_5',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_397_ret_6',
        "command": 'ret'
    }
]
