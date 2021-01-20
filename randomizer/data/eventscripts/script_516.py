from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_516_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_unsync_dialog_1',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_516_jmp_if_bit_set_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 0, 'EVENT_516_jmp_if_bit_set_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_run_dialog_6',
        "command": 'run_dialog',
        "args": [781, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_enable_controls_until_return_7',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_resume_action_script_8',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_resume_action_script_9',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_516_run_dialog_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_jmp_if_random_above_128_12',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_516_run_dialog_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_run_dialog_13',
        "command": 'run_dialog',
        "args": [779, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_516_enable_controls_until_return_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_run_dialog_15',
        "command": 'run_dialog',
        "args": [780, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_enable_controls_until_return_16',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_resume_action_script_17',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_516_set_action_script_sync_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_resume_action_script_19',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 625],
        "subscript": []
    },
    {
        "identifier": 'EVENT_516_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
