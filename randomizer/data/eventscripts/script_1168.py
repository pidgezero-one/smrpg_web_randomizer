from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1168_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 3, 'EVENT_1168_run_dialog_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_run_dialog_1',
        "command": 'run_dialog',
        "args": [2915, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_set_bit_2',
        "command": 'set_bit',
        "args": [0x7088, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_run_dialog_3',
        "command": 'run_dialog',
        "args": [2916, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_jmp_if_dialog_option_b_4',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1168_run_dialog_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_store_coin_amount_7000_5',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_mem_compare_6',
        "command": 'mem_compare',
        "args": [0x7000, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_jmp_if_comparison_result_is_greater_or_equal_7',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1168_set_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_run_dialog_8',
        "command": 'run_dialog',
        "args": [2918, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_store_coin_amount_7000_9',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_dec_coins_10',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_set_bit_11',
        "command": 'set_bit',
        "args": [0x7062, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_273_fade_out_music_to_volume_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_set_13',
        "command": 'set',
        "args": [0x7000, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_dec_coins_14',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_set_bit_15',
        "command": 'set_bit',
        "args": [0x7062, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_273_fade_out_music_to_volume_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_run_dialog_17',
        "command": 'run_dialog',
        "args": [2917, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1168_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
