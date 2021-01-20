from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3318_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_3318_set_7000_to_current_level_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [255],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_set_7000_to_current_level_2',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 362, 'EVENT_3318_start_battle_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_start_battle_4',
        "command": 'start_battle',
        "args": [0x0068, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3318_jmp_if_bit_set_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_start_battle_6',
        "command": 'start_battle',
        "args": [0x0069, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3319_set_temp_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3319_reset_and_choose_game_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_pause_action_script_9',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3318_action_queue_async_10_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3318_action_queue_async_10_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3318_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3318_action_queue_async_10_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_3318_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_add_12',
        "command": 'add',
        "args": [0x7000, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_clear_mem_704x_at_7000_bit_13',
        "command": 'clear_mem_704x_at_7000_bit',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3318_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
