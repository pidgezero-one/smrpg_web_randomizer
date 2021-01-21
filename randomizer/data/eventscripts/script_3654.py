from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3654_set_0',
        "command": 'set',
        "args": [0x70ae, 16]
    },
    {
        "identifier": 'EVENT_3654_run_dialog_1',
        "command": 'run_dialog',
        "args": [3592, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3654_jmp_if_dialog_option_b_2',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3654_pause_7']
    },
    {
        "identifier": 'EVENT_3654_pause_3',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3654_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3654_run_dialog_5',
        "command": 'run_dialog',
        "args": [3593, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3654_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3654_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3654_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3654_run_dialog_9',
        "command": 'run_dialog',
        "args": [3594, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3654_ret_10',
        "command": 'ret'
    }
]
