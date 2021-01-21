from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3297_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 1, 'EVENT_3297_run_dialog_3']
    },
    {
        "identifier": 'EVENT_3297_run_dialog_1',
        "command": 'run_dialog',
        "args": [1680, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3297_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_3297_store_coin_amount_7000_4']
    },
    {
        "identifier": 'EVENT_3297_run_dialog_3',
        "command": 'run_dialog',
        "args": [1681, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3297_store_coin_amount_7000_4',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_3297_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_3297_open_shop_6',
        "command": 'open_shop',
        "args": [Shops._07_SEA_ITEM_SHOP]
    },
    {
        "identifier": 'EVENT_3297_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3297_store_coin_amount_7000_8',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_3297_mem_compare_9',
        "command": 'mem_compare',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3297_jmp_if_loaded_memory_is_0_10',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_3297_run_dialog_15']
    },
    {
        "identifier": 'EVENT_3297_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 1, 'EVENT_3297_run_dialog_15']
    },
    {
        "identifier": 'EVENT_3297_set_bit_12',
        "command": 'set_bit',
        "args": [0x7057, 1]
    },
    {
        "identifier": 'EVENT_3297_run_dialog_13',
        "command": 'run_dialog',
        "args": [1683, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3297_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3297_run_dialog_15',
        "command": 'run_dialog',
        "args": [1682, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3297_ret_16',
        "command": 'ret'
    }
]
