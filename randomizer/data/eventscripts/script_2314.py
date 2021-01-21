from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2314_set_0',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_2314_add_max_FP_7000_1',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_2314_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._101_BOOSTER_PASS_AREA_02]
    },
    {
        "identifier": 'EVENT_2314_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2314_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2314_run_dialog_5',
        "command": 'run_dialog',
        "args": [3175, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2314_ret_6',
        "command": 'ret'
    }
]
