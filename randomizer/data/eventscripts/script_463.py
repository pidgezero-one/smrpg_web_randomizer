from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_463_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6]
    },
    {
        "identifier": 'EVENT_463_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_463_enable_controls_until_return_16']
    },
    {
        "identifier": 'EVENT_463_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [456]
    },
    {
        "identifier": 'EVENT_463_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 3, 'EVENT_463_jmp_if_bit_set_19']
    },
    {
        "identifier": 'EVENT_463_run_dialog_4',
        "command": 'run_dialog',
        "args": [905, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_jmp_if_dialog_option_b_5',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_463_run_dialog_41']
    },
    {
        "identifier": 'EVENT_463_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 3, 'EVENT_463_run_dialog_44']
    },
    {
        "identifier": 'EVENT_463_set_bit_7',
        "command": 'set_bit',
        "args": [0x7099, 3]
    },
    {
        "identifier": 'EVENT_463_run_dialog_8',
        "command": 'run_dialog',
        "args": [938, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_463_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_463_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6]
    },
    {
        "identifier": 'EVENT_463_run_dialog_12',
        "command": 'run_dialog',
        "args": [955, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_run_dialog_13',
        "command": 'run_dialog',
        "args": [956, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_463_run_background_event_14',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_463_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_463_enable_controls_until_return_16',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_463_pause_17',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_463_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_463_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_463_run_dialog_39']
    },
    {
        "identifier": 'EVENT_463_run_dialog_20',
        "command": 'run_dialog',
        "args": [904, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_store_item_amount_7000_21',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_463_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_463_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_463_add_short_mem_24',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_463_jmp_if_7000_equals_short_25',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_463_run_dialog_29']
    },
    {
        "identifier": 'EVENT_463_close_dialog_26',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_463_run_background_event_27',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_463_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_463_run_dialog_29',
        "command": 'run_dialog',
        "args": [941, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_play_sound_30',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_463_set_31',
        "command": 'set',
        "args": [0x7000, 3]
    },
    {
        "identifier": 'EVENT_463_run_dialog_32',
        "command": 'run_dialog',
        "args": [943, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_463_start_loop_n_times_33',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'EVENT_463_put_inventory_34',
        "command": 'put_inventory',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_463_end_loop_35',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_463_run_dialog_36',
        "command": 'run_dialog',
        "args": [945, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_run_background_event_37',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_463_ret_38',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_463_run_dialog_39',
        "command": 'run_dialog',
        "args": [2367, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_463_store_item_amount_7000_21']
    },
    {
        "identifier": 'EVENT_463_run_dialog_41',
        "command": 'run_dialog',
        "args": [939, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_run_background_event_42',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_463_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_463_run_dialog_44',
        "command": 'run_dialog',
        "args": [2368, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_463_run_background_event_45',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_463_ret_46',
        "command": 'ret'
    }
]
