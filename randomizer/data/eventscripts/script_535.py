from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_535_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 'EVENT_535_run_dialog_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_535_jmp_if_object_not_in_level_1',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_10, Rooms._084_ROSE_TOWN_OUTSIDE, 'EVENT_535_run_dialog_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_535_run_dialog_2',
        "command": 'run_dialog',
        "args": [808, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_535_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_535_run_dialog_4',
        "command": 'run_dialog',
        "args": [809, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_535_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
