from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3821_jmp_if_object_trigger_enabled_0',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_0, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3821_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_jmp_if_object_trigger_enabled_1',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_1, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3821_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_jmp_if_object_trigger_enabled_2',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_2, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3821_run_dialog_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_set_3',
        "command": 'set',
        "args": [0x70ae, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_run_dialog_4',
        "command": 'run_dialog',
        "args": [3757, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_jmp_if_dialog_option_b_5',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3821_pause_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_pause_6',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_run_dialog_8',
        "command": 'run_dialog',
        "args": [63, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_run_dialog_10',
        "command": 'run_dialog',
        "args": [3751, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_pause_12',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_set_action_script_async_13',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_run_dialog_14',
        "command": 'run_dialog',
        "args": [3759, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3821_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
