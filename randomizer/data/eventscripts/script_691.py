from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_691_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_691_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65, 'EVENT_691_jmp_if_bit_set_6']
    },
    {
        "identifier": 'EVENT_691_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 7, 'EVENT_691_run_dialog_9']
    },
    {
        "identifier": 'EVENT_691_run_dialog_3',
        "command": 'run_dialog',
        "args": [2116, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_691_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 7, 'EVENT_687_pause_0']
    },
    {
        "identifier": 'EVENT_691_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_691_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 5, 'EVENT_691_run_dialog_11']
    },
    {
        "identifier": 'EVENT_691_run_dialog_7',
        "command": 'run_dialog',
        "args": [2182, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_691_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_691_run_dialog_9',
        "command": 'run_dialog',
        "args": [2117, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_691_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_691_run_dialog_11',
        "command": 'run_dialog',
        "args": [2156, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_691_ret_12',
        "command": 'ret'
    }
]
