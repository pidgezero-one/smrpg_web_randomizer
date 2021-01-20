from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1687_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7050, 6, 'EVENT_1687_ret_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_7000_to_tapped_button_1',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_jmp_if_7000_all_bits_clear_2',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_1687_ret_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1687_action_queue_sync_3_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            },
        ]
    },
    {
        "identifier": 'EVENT_1687_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1687_ret_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_pause_5',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1687_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._154_BIG_SQUISH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_pause_8',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_store_02_to_0248_9',
        "command": 'store_02_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_store_00_to_0248_11',
        "command": 'store_00_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_pause_12',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_bit_13',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_jmp_if_var_not_equals_short_14',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 0, 'EVENT_1687_jmp_if_var_not_equals_short_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_short_15',
        "command": 'set_short',
        "args": [0x7024, 0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_add_17',
        "command": 'add',
        "args": [0x7000, 64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x70ac, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_1685_set_short_mem_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_jmp_if_var_not_equals_short_20',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 0, 'EVENT_1687_set_short_mem_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_short_21',
        "command": 'set_short',
        "args": [0x7026, 0x000c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_add_23',
        "command": 'add',
        "args": [0x7000, 64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_short_mem_24',
        "command": 'set_short_mem',
        "args": [0x70ac, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_1685_set_short_mem_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_add_27',
        "command": 'add',
        "args": [0x7000, 64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x70ac, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1685_set_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1687_ret_30',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
