from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_317_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_3, Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 'EVENT_317_run_dialog_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 'EVENT_317_run_dialog_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 7, 'EVENT_317_jmp_if_object_not_in_level_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_run_dialog_3',
        "command": 'run_dialog',
        "args": [680, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_jmp_if_object_not_in_level_5',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, 'EVENT_317_run_dialog_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_run_dialog_6',
        "command": 'run_dialog',
        "args": [705, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_run_dialog_8',
        "command": 'run_dialog',
        "args": [729, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_317_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
