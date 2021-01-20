from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_338_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 483, 'EVENT_290_stop_sound_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_set_7010_to_object_xyz_2',
        "command": 'set_7010_to_object_xyz',
        "args": [0x80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_mem_compare_3',
        "command": 'mem_compare',
        "args": [0x7014, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_jmp_if_comparison_result_is_greater_or_equal_4',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_338_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_mem_compare_5',
        "command": 'mem_compare',
        "args": [0x7012, 19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_jmp_if_comparison_result_is_lesser_6',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_338_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_jmp_if_loaded_memory_is_0_7',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_338_mem_compare_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_jmp_to_event_8',
        "command": 'jmp_to_event',
        "args": [560],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_run_dialog_9',
        "command": 'run_dialog',
        "args": [609, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_mem_compare_11',
        "command": 'mem_compare',
        "args": [0x7010, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_jmp_if_comparison_result_is_greater_or_equal_12',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_338_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_338_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [560],
        "subscript": []
    },
]
