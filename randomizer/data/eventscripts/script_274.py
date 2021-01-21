from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_274_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7049, 3]
    },
    {
        "identifier": 'EVENT_274_store_coin_amount_7000_1',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_274_mem_compare_2',
        "command": 'mem_compare',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_274_jmp_if_comparison_result_is_greater_or_equal_3',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_274_ret_8']
    },
    {
        "identifier": 'EVENT_274_set_bit_4',
        "command": 'set_bit',
        "args": [0x7049, 3]
    },
    {
        "identifier": 'EVENT_274_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7049, 4, 'EVENT_274_ret_8']
    },
    {
        "identifier": 'EVENT_274_run_dialog_6',
        "command": 'run_dialog',
        "args": [520, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_274_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7049, 4]
    },
    {
        "identifier": 'EVENT_274_ret_8',
        "command": 'ret'
    }
]
