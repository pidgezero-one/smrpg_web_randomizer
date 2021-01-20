from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3286_jmp_fork_mario_on_object_0',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_3286_enable_controls_until_return_6', 'EVENT_3286_enable_controls_until_return_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 0, 'EVENT_3286_run_dialog_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_run_dialog_2',
        "command": 'run_dialog',
        "args": [1778, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_run_dialog_4',
        "command": 'run_dialog',
        "args": [1780, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_enable_controls_until_return_6',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_start_loop_n_times_7',
        "command": 'start_loop_n_times',
        "args": [59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_pause_8',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_jmp_if_mario_in_air_9',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3286_ret_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_end_loop_10',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_enable_controls_until_return_11',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_run_dialog_12',
        "command": 'run_dialog',
        "args": [1781, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3286_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
