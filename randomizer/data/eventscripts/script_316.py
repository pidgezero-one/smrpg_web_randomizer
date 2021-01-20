from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_316_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_316_run_dialog_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_jmp_if_object_in_level_1',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_3, Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 'EVENT_316_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_jmp_if_object_in_level_2',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 'EVENT_316_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_run_dialog_3',
        "command": 'run_dialog',
        "args": [692, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 6, 'EVENT_316_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 7, 'EVENT_316_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_run_dialog_7',
        "command": 'run_dialog',
        "args": [681, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_run_dialog_9',
        "command": 'run_dialog',
        "args": [634, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_316_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
