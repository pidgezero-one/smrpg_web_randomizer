from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_459_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6]
    },
    {
        "identifier": 'EVENT_459_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_459_enable_controls_until_return_7']
    },
    {
        "identifier": 'EVENT_459_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [456]
    },
    {
        "identifier": 'EVENT_459_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 3, 'EVENT_459_run_event_as_subroutine_10']
    },
    {
        "identifier": 'EVENT_459_run_dialog_4',
        "command": 'run_dialog',
        "args": [901, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_459_run_background_event_5',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_459_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_459_enable_controls_until_return_7',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_459_pause_8',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_459_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_459_run_event_as_subroutine_10',
        "command": 'run_event_as_subroutine',
        "args": [456]
    },
    {
        "identifier": 'EVENT_459_run_dialog_11',
        "command": 'run_dialog',
        "args": [940, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_459_run_background_event_12',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_459_ret_13',
        "command": 'ret'
    }
]
