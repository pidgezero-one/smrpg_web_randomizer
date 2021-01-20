from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2388_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7091, 0, 'EVENT_2304_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_set_bit_2',
        "command": 'set_bit',
        "args": [0x7091, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_2388_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2388_db_6',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_tile_mod_7',
        "command": 'apply_tile_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_8',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_db_9',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 2, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_11',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_db_12',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 3, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_14',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_db_15',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 4, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_17',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_db_18',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 5, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_20',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_db_21',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_tile_mod_22',
        "command": 'apply_tile_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 6, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_23',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_db_24',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_tile_mod_25',
        "command": 'apply_tile_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 7, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_26',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_db_27',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_tile_mod_28',
        "command": 'apply_tile_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 8, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_pause_29',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_set_action_script_async_30',
        "command": 'set_action_script_async',
        "args": [AreaObjects.SCREEN_FOCUS, 391],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_apply_solidity_mod_31',
        "command": 'apply_solidity_mod',
        "args": [Rooms._221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2388_ret_32',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
