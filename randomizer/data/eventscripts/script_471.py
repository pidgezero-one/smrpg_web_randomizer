from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_471_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._062_BIG_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_471_enable_controls_until_return_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_471_run_event_as_subroutine_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 3, 'EVENT_462_jmp_to_event_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 3, 'EVENT_471_run_event_as_subroutine_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_dialog_6',
        "command": 'run_dialog',
        "args": [906, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_background_event_7',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_dialog_10',
        "command": 'run_dialog',
        "args": [907, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_jmp_to_event_11',
        "command": 'jmp_to_event',
        "args": [476],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_enable_controls_until_return_12',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_pause_13',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_event_as_subroutine_15',
        "command": 'run_event_as_subroutine',
        "args": [456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_dialog_16',
        "command": 'run_dialog',
        "args": [946, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_background_event_17',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_event_as_subroutine_19',
        "command": 'run_event_as_subroutine',
        "args": [456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_dialog_20',
        "command": 'run_dialog',
        "args": [909, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_run_background_event_21',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_471_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
