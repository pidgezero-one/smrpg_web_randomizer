from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3311_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_3311_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_3311_run_dialog_1',
        "command": 'run_dialog',
        "args": [1689, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3311_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_3311_open_shop_12']
    },
    {
        "identifier": 'EVENT_3311_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 6, 'EVENT_3311_run_dialog_11']
    },
    {
        "identifier": 'EVENT_3311_set_7000_to_70A0_short_mem_4',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_3311_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_3311_run_dialog_9']
    },
    {
        "identifier": 'EVENT_3311_jmp_if_7000_equals_short_6',
        "command": 'jmp_if_7000_equals_short',
        "args": [6, 'EVENT_3311_run_dialog_11']
    },
    {
        "identifier": 'EVENT_3311_run_dialog_7',
        "command": 'run_dialog',
        "args": [1691, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3311_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3311_open_shop_12']
    },
    {
        "identifier": 'EVENT_3311_run_dialog_9',
        "command": 'run_dialog',
        "args": [1686, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3311_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_3311_open_shop_12']
    },
    {
        "identifier": 'EVENT_3311_run_dialog_11',
        "command": 'run_dialog',
        "args": [1687, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3311_open_shop_12',
        "command": 'open_shop',
        "args": [Shops._07_SEA_ITEM_SHOP]
    },
    {
        "identifier": 'EVENT_3311_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3311_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 6, 'EVENT_3311_ret_16']
    },
    {
        "identifier": 'EVENT_3311_run_dialog_15',
        "command": 'run_dialog',
        "args": [1690, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3311_ret_16',
        "command": 'ret'
    }
]
