from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3159_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3159_jmp_fork_mario_on_object_1',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_3159_enable_controls_until_return_5', 'EVENT_3159_enable_controls_until_return_5']
    },
    {
        "identifier": 'EVENT_3159_run_dialog_2',
        "command": 'run_dialog',
        "args": [1638, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3159_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3159_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3159_enable_controls_until_return_5',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3159_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [59]
    },
    {
        "identifier": 'EVENT_3159_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3159_jmp_if_mario_in_air_8',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3159_clear_bit_12']
    },
    {
        "identifier": 'EVENT_3159_end_loop_9',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3159_enable_controls_until_return_10',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3159_run_dialog_11',
        "command": 'run_dialog',
        "args": [1646, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3159_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3159_ret_13',
        "command": 'ret'
    }
]
