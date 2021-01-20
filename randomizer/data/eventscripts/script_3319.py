from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3319_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_3319_set_7000_to_current_level_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [255],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_set_7000_to_current_level_2',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 367, 'EVENT_3319_start_battle_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 364, 'EVENT_3319_start_battle_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_start_battle_5',
        "command": 'start_battle',
        "args": [0x006c, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_3319_jmp_if_bit_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_start_battle_7',
        "command": 'start_battle',
        "args": [0x006d, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3319_set_temp_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3319_reset_and_choose_game_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_set_temp_action_script_sync_10',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 273],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3319_action_queue_sync_11_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3319_action_queue_sync_11_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3319_action_queue_sync_11_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3319_action_queue_sync_11_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3319_action_queue_sync_11_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3319_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_set_temp_action_script_sync_14',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3319_reset_and_choose_game_17',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
]
