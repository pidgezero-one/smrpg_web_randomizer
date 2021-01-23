from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1829_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1829_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 6]
    },
    {
        "identifier": 'EVENT_1829_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70cb]
    },
    {
        "identifier": 'EVENT_1829_mem_compare_val_3',
        "command": 'mem_compare_val',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1829_jmp_if_comparison_result_is_greater_or_equal_4',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1829_run_dialog_16']
    },
    {
        "identifier": 'EVENT_1829_mem_compare_val_5',
        "command": 'mem_compare_val',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1829_jmp_if_comparison_result_is_greater_or_equal_6',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1829_run_dialog_14']
    },
    {
        "identifier": 'EVENT_1829_mem_compare_val_7',
        "command": 'mem_compare_val',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1829_jmp_if_comparison_result_is_greater_or_equal_8',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1829_run_dialog_12']
    },
    {
        "identifier": 'EVENT_1829_run_dialog_9',
        "command": 'run_dialog',
        "args": [1319, AreaObjects.NPC_12, [_0x60Flags.BIT_6, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1829_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 6]
    },
    {
        "identifier": 'EVENT_1829_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_1829_load_600f_17']
    },
    {
        "identifier": 'EVENT_1829_run_dialog_12',
        "command": 'run_dialog',
        "args": [1318, AreaObjects.NPC_12, [_0x60Flags.BIT_6, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1829_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_1829_load_600f_17']
    },
    {
        "identifier": 'EVENT_1829_run_dialog_14',
        "command": 'run_dialog',
        "args": [1317, AreaObjects.NPC_12, [_0x60Flags.BIT_6, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1829_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_1829_load_600f_17']
    },
    {
        "identifier": 'EVENT_1829_run_dialog_16',
        "command": 'run_dialog',
        "args": [1316, AreaObjects.NPC_12, [_0x60Flags.BIT_6, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1829_load_600f_17',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1829_ret_18',
        "command": 'ret'
    }
]
