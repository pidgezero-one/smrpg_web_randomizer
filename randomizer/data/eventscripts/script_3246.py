from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3246_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 169, 'EVENT_3246_start_battle_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 182, 'EVENT_3246_start_battle_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_start_battle_3',
        "command": 'start_battle',
        "args": [0x0048, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_3246_jmp_if_bit_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_start_battle_5',
        "command": 'start_battle',
        "args": [0x0049, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3246_set_temp_action_script_sync_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3246_reset_and_choose_game_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_set_temp_action_script_sync_8',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 920],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3246_action_queue_sync_9_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3246_action_queue_sync_9_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3246_action_queue_sync_9_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3246_action_queue_sync_9_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3246_action_queue_sync_9_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3246_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_set_temp_action_script_sync_12',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3246_reset_and_choose_game_15',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
]
