from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1148_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1148_action_queue_async_0_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1148_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x704a, 4, 'EVENT_1148_open_shop_19']
    },
    {
        "identifier": 'EVENT_1148_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x704a, 5, 'EVENT_1148_open_shop_19']
    },
    {
        "identifier": 'EVENT_1148_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x704a, 6, 'EVENT_1148_open_shop_19']
    },
    {
        "identifier": 'EVENT_1148_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x704a, 7, 'EVENT_1148_open_shop_19']
    },
    {
        "identifier": 'EVENT_1148_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x704b, 0, 'EVENT_1148_open_shop_19']
    },
    {
        "identifier": 'EVENT_1148_run_dialog_6',
        "command": 'run_dialog',
        "args": [2927, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1148_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1148_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 4, 'EVENT_1148_run_dialog_18']
    },
    {
        "identifier": 'EVENT_1148_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 6, 'EVENT_1148_run_dialog_14']
    },
    {
        "identifier": 'EVENT_1148_run_dialog_10',
        "command": 'run_dialog',
        "args": [2919, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1148_run_dialog_11',
        "command": 'run_dialog',
        "args": [2920, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1148_set_bit_12',
        "command": 'set_bit',
        "args": [0x7088, 4]
    },
    {
        "identifier": 'EVENT_1148_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_1148_open_shop_19']
    },
    {
        "identifier": 'EVENT_1148_run_dialog_14',
        "command": 'run_dialog',
        "args": [2919, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1148_run_dialog_15',
        "command": 'run_dialog',
        "args": [2922, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1148_set_bit_16',
        "command": 'set_bit',
        "args": [0x7088, 4]
    },
    {
        "identifier": 'EVENT_1148_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_1148_open_shop_19']
    },
    {
        "identifier": 'EVENT_1148_run_dialog_18',
        "command": 'run_dialog',
        "args": [2921, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1148_open_shop_19',
        "command": 'open_shop',
        "args": [Shops._03_FROG_DISCIPLE_SHOP]
    },
    {
        "identifier": 'EVENT_1148_fade_in_from_black_async_20',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1148_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1148_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1148_ret_22',
        "command": 'ret'
    }
]
